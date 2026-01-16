#!/usr/bin/env node
/**
 * Trust SoCal - Parallel Website Scanner Agents
 * Runs multiple specialized scanner agents in parallel to comprehensively audit the website
 * Similar to the DA agent runner but for code quality, security, accessibility, SEO, etc.
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

const CONFIG = {
    websiteDir: '/opt/trust-socal-agents/website',
    logsDir: '/opt/trust-socal-agents/scanner-logs',
    reportsDir: '/opt/trust-socal-agents/reports',
    statusFile: '/opt/trust-socal-agents/scanner-status.json',
    apiKey: process.env.ANTHROPIC_API_KEY,
    maxConcurrent: 5, // Run up to 5 scanners in parallel
};

// Scanner Agent Definitions - Based on the screenshot
const SCANNER_AGENTS = [
    {
        id: 'code-orchestrator-lead',
        name: '🎯 Code Orchestrator Lead',
        color: '\x1b[33m', // Yellow
        description: 'Orchestrate full site scan and coordinate findings',
        prompt: `You are the CODE ORCHESTRATOR LEAD agent. Your job is to perform a high-level orchestration scan of the Trust SoCal website.

SCAN THE WEBSITE FOR:
1. Overall code organization and architecture
2. File structure and naming conventions
3. Consistency across pages
4. Missing essential files (robots.txt, sitemap.xml, etc.)
5. Duplicate code patterns
6. Cross-page consistency issues

WEBSITE PATH: {websiteDir}

Scan all HTML, CSS, and JS files. Provide a comprehensive report with:
- Executive summary
- Critical issues (blocking)
- High priority issues
- Medium priority issues
- Low priority recommendations
- Score out of 100

OUTPUT FORMAT: Structured markdown report.`
    },
    {
        id: 'html-css-scanner',
        name: '🎨 HTML/CSS Deep Scanner',
        color: '\x1b[36m', // Cyan
        description: 'Deep scan HTML/CSS issues',
        prompt: `You are the HTML/CSS DEEP SCANNER agent. Perform a comprehensive audit of all HTML and CSS code.

SCAN FOR:
1. HTML validation issues (W3C compliance)
2. Semantic HTML usage (proper heading hierarchy, landmarks)
3. CSS specificity conflicts
4. Unused CSS selectors
5. CSS duplication
6. Inline styles that should be in CSS
7. Missing alt attributes on images
8. Broken internal links
9. Meta tag completeness
10. Open Graph and Twitter Card tags

WEBSITE PATH: {websiteDir}

Analyze all .html and .css files. Report findings with file:line references.

OUTPUT: Detailed markdown report with code examples and fixes.`
    },
    {
        id: 'accessibility-scanner',
        name: '♿ Accessibility Scanner (WCAG)',
        color: '\x1b[35m', // Magenta
        description: 'Deep scan accessibility/a11y compliance',
        prompt: `You are the ACCESSIBILITY SCANNER agent specializing in WCAG 2.1 AA compliance.

SCAN FOR:
1. Color contrast ratios (must be 4.5:1 for text, 3:1 for large text)
2. Missing ARIA labels and roles
3. Keyboard navigation issues
4. Focus indicator visibility
5. Form label associations
6. Skip navigation links
7. Image alt text quality
8. Heading hierarchy
9. Link text clarity (no "click here")
10. Table accessibility (headers, captions)
11. Video/audio accessibility
12. Touch target sizes (44x44px minimum)

WEBSITE PATH: {websiteDir}

Scan all HTML files. Rate each page's accessibility score.

OUTPUT: WCAG compliance report with specific violations and remediation steps.`
    },
    {
        id: 'security-scanner',
        name: '🔒 Security Scanner',
        color: '\x1b[31m', // Red
        description: 'Deep scan security issues',
        prompt: `You are the SECURITY SCANNER agent. Audit the website for security vulnerabilities.

SCAN FOR:
1. XSS vulnerabilities (unsanitized user input)
2. Missing Content-Security-Policy headers
3. Sensitive data exposure (API keys, passwords in code)
4. Insecure form handling
5. Missing HTTPS redirects
6. CORS misconfigurations
7. Clickjacking protection (X-Frame-Options)
8. External script integrity (SRI)
9. Outdated dependencies with known vulnerabilities
10. Information disclosure (comments, debug info)
11. SQL injection vectors
12. HIPAA compliance issues (healthcare site!)

WEBSITE PATH: {websiteDir}

CRITICAL: This is a healthcare/rehab website - HIPAA compliance is essential.

OUTPUT: Security audit report with severity ratings (Critical/High/Medium/Low).`
    },
    {
        id: 'performance-scanner',
        name: '⚡ Performance Scanner',
        color: '\x1b[32m', // Green
        description: 'Deep scan JS/performance issues',
        prompt: `You are the PERFORMANCE SCANNER agent. Analyze website performance and Core Web Vitals.

SCAN FOR:
1. Render-blocking resources
2. Large unoptimized images (should be <200KB)
3. Missing lazy loading
4. Unminified CSS/JS
5. Missing preload/preconnect hints
6. Large DOM size
7. Unused JavaScript
8. CSS in critical rendering path
9. Font loading optimization (font-display)
10. Cumulative Layout Shift (CLS) causes
11. Largest Contentful Paint (LCP) blockers
12. First Input Delay (FID) issues

WEBSITE PATH: {websiteDir}

Check image sizes, script sizes, and optimization opportunities.

OUTPUT: Performance report with specific optimization recommendations and estimated impact.`
    },
    {
        id: 'seo-structure-scanner',
        name: '📈 SEO Structure Scanner',
        color: '\x1b[34m', // Blue
        description: 'Web structure SEO analysis',
        prompt: `You are the SEO STRUCTURE SCANNER agent. Analyze on-page and technical SEO.

SCAN FOR:
1. Title tag optimization (50-60 chars, keyword inclusion)
2. Meta description quality (150-160 chars)
3. H1 tag presence and uniqueness per page
4. Heading hierarchy (H1 > H2 > H3)
5. Internal linking structure
6. Canonical URL implementation
7. Schema markup (LocalBusiness, MedicalOrganization, FAQ)
8. sitemap.xml completeness
9. robots.txt configuration
10. URL structure (readable, keyword-rich)
11. Mobile-friendliness indicators
12. Page speed indicators

WEBSITE PATH: {websiteDir}

Focus on "drug rehab Orange County" keyword optimization.

OUTPUT: SEO audit with page-by-page scores and optimization recommendations.`
    },
    {
        id: 'code-quality-scanner',
        name: '✨ Code Quality Scanner',
        color: '\x1b[37m', // White
        description: 'Deep scan code quality',
        prompt: `You are the CODE QUALITY SCANNER agent. Analyze code quality and maintainability.

SCAN FOR:
1. Code duplication (DRY violations)
2. Inconsistent naming conventions
3. Magic numbers and hardcoded values
4. Long functions/files (>500 lines)
5. Missing comments on complex logic
6. Inconsistent formatting/indentation
7. Dead code (unreachable, commented out)
8. TODO/FIXME comments that need addressing
9. Console.log statements left in production
10. Error handling quality
11. Code organization
12. Best practices violations

WEBSITE PATH: {websiteDir}

Analyze HTML, CSS, and JavaScript files.

OUTPUT: Code quality report with specific examples and refactoring suggestions.`
    },
    {
        id: 'project-structure-scanner',
        name: '📁 Project Structure Scanner',
        color: '\x1b[90m', // Gray
        description: 'Project structure analysis',
        prompt: `You are the PROJECT STRUCTURE SCANNER agent. Analyze the overall project organization.

SCAN FOR:
1. File organization (logical grouping)
2. Naming conventions consistency
3. Missing essential files (favicon, manifest, etc.)
4. Asset organization (images, fonts, etc.)
5. Configuration files
6. Build/deployment readiness
7. Documentation completeness
8. Environment handling
9. Dependencies management
10. Version control cleanliness (.gitignore)
11. Folder depth and navigation
12. Separation of concerns

WEBSITE PATH: {websiteDir}

Map out the entire project structure.

OUTPUT: Structure audit with reorganization recommendations and missing files list.`
    },
    {
        id: 'comprehensive-auditor',
        name: '📋 Comprehensive Code Auditor',
        color: '\x1b[93m', // Bright Yellow
        description: 'Comprehensive code audit',
        prompt: `You are the COMPREHENSIVE CODE AUDITOR agent. Perform a final holistic review.

AGGREGATE FINDINGS FROM ALL AREAS:
1. Critical issues requiring immediate attention
2. Security vulnerabilities
3. Accessibility violations
4. Performance bottlenecks
5. SEO deficiencies
6. Code quality concerns
7. Project structure issues

WEBSITE PATH: {websiteDir}

Create a prioritized action plan with:
- Quick wins (can fix in < 1 hour)
- Short-term fixes (1 day)
- Medium-term improvements (1 week)
- Long-term enhancements (ongoing)

OUTPUT: Executive summary report with prioritized action items and estimated effort.`
    }
];

function log(agentId, level, msg) {
    const ts = new Date().toISOString();
    const agent = SCANNER_AGENTS.find(a => a.id === agentId) || { name: 'System', color: '\x1b[0m' };
    const reset = '\x1b[0m';
    const line = `[${ts}] ${agent.color}[${agent.name}]${reset} [${level}] ${msg}`;
    console.log(line);

    try {
        const logFile = path.join(CONFIG.logsDir, `scanner-${ts.split('T')[0]}.log`);
        fs.appendFileSync(logFile, `[${ts}] [${agentId}] [${level}] ${msg}\n`);
    } catch (e) {}
}

function loadStatus() {
    try {
        if (fs.existsSync(CONFIG.statusFile)) {
            return JSON.parse(fs.readFileSync(CONFIG.statusFile, 'utf8'));
        }
    } catch (e) {}
    return {
        scans: [],
        totalTokens: 0,
        lastScan: null,
        reports: []
    };
}

function saveStatus(status) {
    fs.writeFileSync(CONFIG.statusFile, JSON.stringify(status, null, 2));
}

function callAnthropicAPI(prompt, agentId) {
    return new Promise((resolve, reject) => {
        const data = JSON.stringify({
            model: 'claude-sonnet-4-20250514',
            max_tokens: 8000,
            messages: [{ role: 'user', content: prompt }]
        });

        const options = {
            hostname: 'api.anthropic.com',
            port: 443,
            path: '/v1/messages',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'x-api-key': CONFIG.apiKey,
                'anthropic-version': '2023-06-01',
                'Content-Length': Buffer.byteLength(data)
            }
        };

        log(agentId, 'INFO', 'Calling Anthropic API...');

        const req = https.request(options, (res) => {
            let body = '';
            res.on('data', chunk => body += chunk);
            res.on('end', () => {
                try {
                    const response = JSON.parse(body);
                    if (response.error) {
                        reject(new Error(response.error.message));
                    } else if (response.content && response.content[0]) {
                        resolve({
                            content: response.content[0].text,
                            inputTokens: response.usage?.input_tokens || 0,
                            outputTokens: response.usage?.output_tokens || 0
                        });
                    } else {
                        reject(new Error('No content in response'));
                    }
                } catch (e) {
                    reject(new Error(`Parse error: ${e.message}`));
                }
            });
        });

        req.on('error', reject);
        req.write(data);
        req.end();
    });
}

async function runScanner(agent) {
    const startTime = Date.now();
    log(agent.id, 'INFO', `Starting scan: ${agent.description}`);

    try {
        // Replace placeholder with actual path
        const prompt = agent.prompt.replace(/\{websiteDir\}/g, CONFIG.websiteDir);

        // Add context about the website
        const fullPrompt = `${prompt}

IMPORTANT CONTEXT:
- This is Trust SoCal, a drug and alcohol rehabilitation center website
- Location: Orange County, California
- Target keywords: "drug rehab Orange County", "addiction treatment Orange County"
- Industry: Healthcare (YMYL - Your Money Your Life content)
- Compliance requirements: HIPAA, WCAG 2.1 AA, healthcare advertising regulations

Scan the website files and provide your detailed analysis.`;

        const response = await callAnthropicAPI(fullPrompt, agent.id);
        const duration = ((Date.now() - startTime) / 1000).toFixed(1);

        log(agent.id, 'SUCCESS', `Scan completed in ${duration}s (${response.inputTokens} in, ${response.outputTokens} out tokens)`);

        // Save report
        const reportFile = path.join(CONFIG.reportsDir, `${agent.id}-${new Date().toISOString().split('T')[0]}.md`);
        const reportContent = `# ${agent.name} Report

**Scan Date:** ${new Date().toISOString()}
**Duration:** ${duration}s
**Tokens Used:** ${response.inputTokens + response.outputTokens}

---

${response.content}
`;
        fs.writeFileSync(reportFile, reportContent);
        log(agent.id, 'INFO', `Report saved: ${reportFile}`);

        return {
            agentId: agent.id,
            success: true,
            duration: parseFloat(duration),
            tokens: response.inputTokens + response.outputTokens,
            reportFile
        };

    } catch (error) {
        log(agent.id, 'ERROR', `Scan failed: ${error.message}`);
        return {
            agentId: agent.id,
            success: false,
            error: error.message
        };
    }
}

async function runParallelScanners(agents, maxConcurrent = 5) {
    const results = [];
    const queue = [...agents];

    // Process in batches
    while (queue.length > 0) {
        const batch = queue.splice(0, maxConcurrent);
        log('system', 'INFO', `Running batch of ${batch.length} scanners in parallel...`);

        const batchResults = await Promise.all(batch.map(agent => runScanner(agent)));
        results.push(...batchResults);

        // Small delay between batches
        if (queue.length > 0) {
            await new Promise(r => setTimeout(r, 5000));
        }
    }

    return results;
}

async function main() {
    if (!CONFIG.apiKey) {
        console.error('ERROR: ANTHROPIC_API_KEY not set!');
        process.exit(1);
    }

    // Create directories
    [CONFIG.logsDir, CONFIG.reportsDir].forEach(dir => {
        if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
    });

    console.log('\n' + '='.repeat(60));
    console.log('🔍 TRUST SOCAL PARALLEL WEBSITE SCANNER');
    console.log('='.repeat(60));
    console.log(`\nDeploying ${SCANNER_AGENTS.length} scanner agents in parallel...\n`);

    SCANNER_AGENTS.forEach(agent => {
        console.log(`  ${agent.color}${agent.name}\x1b[0m - ${agent.description}`);
    });
    console.log('');

    const startTime = Date.now();
    let status = loadStatus();

    // Run all scanners in parallel batches
    const results = await runParallelScanners(SCANNER_AGENTS, CONFIG.maxConcurrent);

    const totalDuration = ((Date.now() - startTime) / 1000).toFixed(1);
    const successCount = results.filter(r => r.success).length;
    const totalTokens = results.reduce((sum, r) => sum + (r.tokens || 0), 0);

    // Update status
    status.scans.push({
        timestamp: new Date().toISOString(),
        agents: results.length,
        successful: successCount,
        totalTokens,
        duration: parseFloat(totalDuration)
    });
    status.totalTokens += totalTokens;
    status.lastScan = new Date().toISOString();
    status.reports = results.filter(r => r.success).map(r => r.reportFile);
    saveStatus(status);

    // Summary
    console.log('\n' + '='.repeat(60));
    console.log('📊 SCAN SUMMARY');
    console.log('='.repeat(60));
    console.log(`\n  Scanners Run:    ${results.length}`);
    console.log(`  Successful:      ${successCount}`);
    console.log(`  Failed:          ${results.length - successCount}`);
    console.log(`  Total Duration:  ${totalDuration}s`);
    console.log(`  Tokens Used:     ${totalTokens.toLocaleString()}`);
    console.log(`  Est. Cost:       $${(totalTokens * 0.000003).toFixed(4)}`);
    console.log(`\n  Reports saved to: ${CONFIG.reportsDir}`);
    console.log('='.repeat(60) + '\n');

    // List reports
    console.log('📁 Generated Reports:');
    results.filter(r => r.success).forEach(r => {
        console.log(`   - ${r.reportFile}`);
    });

    // Show failures
    const failures = results.filter(r => !r.success);
    if (failures.length > 0) {
        console.log('\n⚠️  Failed Scanners:');
        failures.forEach(r => {
            console.log(`   - ${r.agentId}: ${r.error}`);
        });
    }

    console.log('\n✅ Scan complete!\n');
}

// Handle graceful shutdown
process.on('SIGINT', () => process.exit(0));
process.on('SIGTERM', () => process.exit(0));

main().catch(e => {
    console.error('Fatal error:', e.message);
    process.exit(1);
});
