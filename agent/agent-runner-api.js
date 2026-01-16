#!/usr/bin/env node
/**
 * Trust SoCal - Domain Authority Building Agent Runner
 * Uses Anthropic API directly (no CLI authentication needed)
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

const CONFIG = {
    websiteDir: '/opt/trust-socal-agents/website',
    logsDir: '/opt/trust-socal-agents/logs',
    completedFile: '/opt/trust-socal-agents/completed.json',
    pauseBetweenTasks: 60000, // 1 minute between tasks
    apiKey: process.env.ANTHROPIC_API_KEY,
};

// Task definitions
const DA_TASKS = {
    locationPages: [
        'Los Angeles', 'San Diego', 'Long Beach', 'Pasadena', 'Riverside',
        'San Bernardino', 'Fullerton', 'Costa Mesa', 'Mission Viejo', 'Laguna Beach',
        'Tustin', 'Lake Forest', 'San Clemente', 'Dana Point', 'Yorba Linda',
        'Brea', 'La Habra', 'Rancho Santa Margarita', 'Aliso Viejo', 'Laguna Niguel',
        'Seal Beach', 'Westminster', 'Garden Grove', 'Fountain Valley', 'Cypress',
        'Buena Park', 'La Mirada', 'Placentia', 'Stanton', 'Los Alamitos',
    ].map((city, i) => ({ city, priority: Math.ceil((i + 1) / 10), type: 'location' })),

    pillarContent: [
        'Complete Guide to Drug Rehab in California',
        'Alcohol Addiction Treatment Options Guide',
        'How to Choose the Right Rehab Center',
        'Understanding Addiction Family Guide',
        'Insurance Coverage for Addiction Treatment',
        'Detox Process What to Expect',
        'Outpatient vs Inpatient Treatment',
        'Dual Diagnosis Treatment Guide',
    ].map((topic, i) => ({ topic, priority: Math.ceil((i + 1) / 3), type: 'pillar' })),

    blogPosts: [
        'Signs of Alcohol Addiction',
        'How Long Does Detox Take',
        'Supporting a Loved One in Recovery',
        'Fentanyl Crisis in Orange County',
        'Benefits of Holistic Treatment',
        'Addiction and Mental Health Connection',
        'What Happens in Group Therapy',
        'Rebuilding Relationships After Addiction',
        'Exercise and Recovery',
        'Nutrition in Recovery',
    ].map((topic, i) => ({ topic, priority: Math.ceil((i + 1) / 4), type: 'blog' })),
};

function log(level, msg) {
    const ts = new Date().toISOString();
    const line = `[${ts}] [${level}] ${msg}`;
    console.log(line);
    try {
        const logFile = path.join(CONFIG.logsDir, `agent-${ts.split('T')[0]}.log`);
        fs.appendFileSync(logFile, line + '\n');
    } catch (e) {}
}

function loadState() {
    try {
        if (fs.existsSync(CONFIG.completedFile)) {
            return JSON.parse(fs.readFileSync(CONFIG.completedFile, 'utf8'));
        }
    } catch (e) {}
    return { completed: [], tokensUsed: 0, startTime: Date.now(), pagesCreated: 0 };
}

function saveState(state) {
    fs.writeFileSync(CONFIG.completedFile, JSON.stringify(state, null, 2));
}

function getNextTask(state) {
    const allTasks = [
        ...DA_TASKS.locationPages,
        ...DA_TASKS.pillarContent,
        ...DA_TASKS.blogPosts,
    ].sort((a, b) => a.priority - b.priority);

    for (const task of allTasks) {
        const id = `${task.type}-${(task.city || task.topic).replace(/ /g, '-')}`;
        if (!state.completed.includes(id)) {
            return { ...task, id };
        }
    }
    return null;
}

// Read existing location page as template
function getLocationTemplate() {
    try {
        const templatePath = path.join(CONFIG.websiteDir, 'locations', 'irvine.html');
        if (fs.existsSync(templatePath)) {
            return fs.readFileSync(templatePath, 'utf8');
        }
        const altPath = path.join(CONFIG.websiteDir, 'locations', 'santa-ana.html');
        if (fs.existsSync(altPath)) {
            return fs.readFileSync(altPath, 'utf8');
        }
    } catch (e) {}
    return null;
}

function generatePrompt(task) {
    const template = getLocationTemplate();

    if (task.type === 'location') {
        return `You are creating an SEO-optimized location page for Trust SoCal drug rehab center.

Create a complete HTML page for "${task.city}, California" residents.

REQUIREMENTS:
- Title: "Drug Rehab for ${task.city} Residents | Trust SoCal"
- Use "FOR ${task.city} Residents" NOT "IN ${task.city}" (we serve them, not located there)
- H1: "Drug & Alcohol Rehab for ${task.city} Residents"
- Include local context: demographics, major employers, universities if applicable
- Add travel time from ${task.city} to Orange County (our actual location)
- Include FAQ section with schema markup
- Add nearby locations section linking to 5 related cities
- Target keyword: "drug rehab ${task.city}"

${template ? `Use this existing page as a template for structure and styling:\n\n${template.substring(0, 3000)}...\n\n` : ''}

OUTPUT: Return ONLY the complete HTML file content, nothing else. Start with <!DOCTYPE html>.`;
    }

    if (task.type === 'pillar') {
        return `Create a comprehensive 3000+ word pillar page on "${task.topic}" for Trust SoCal drug rehab.

REQUIREMENTS:
- YMYL compliant with E-E-A-T signals
- Include medical reviewer box with credentials
- H1 with primary keyword
- Clear H2/H3 structure
- FAQ section with schema markup
- Internal links to /services/, /locations/, /insurance.html
- Statistics with sources (SAMHSA, NIDA, CDC)
- Call-to-action with phone number: (555) 123-4567

OUTPUT: Return ONLY the complete HTML file content, nothing else. Start with <!DOCTYPE html>.`;
    }

    if (task.type === 'blog') {
        return `Write a 1500-2000 word SEO-optimized blog post on "${task.topic}" for Trust SoCal.

REQUIREMENTS:
- Engaging H1 title with keyword
- Clear H2/H3 structure for scannability
- Include FAQ section at end
- Internal links to relevant service pages
- Medical accuracy (this is YMYL healthcare content)
- Call-to-action with phone: (555) 123-4567
- Author attribution to Trust SoCal clinical team

OUTPUT: Return ONLY the complete HTML file content, nothing else. Start with <!DOCTYPE html>.`;
    }

    return `Create content for: ${JSON.stringify(task)}`;
}

function callAnthropicAPI(prompt) {
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
                    reject(new Error(`Parse error: ${e.message} - Body: ${body.substring(0, 200)}`));
                }
            });
        });

        req.on('error', reject);
        req.write(data);
        req.end();
    });
}

function getFilePath(task) {
    const name = (task.city || task.topic).toLowerCase().replace(/ /g, '-').replace(/[^a-z0-9-]/g, '');
    if (task.type === 'location') return path.join(CONFIG.websiteDir, 'locations', `${name}.html`);
    if (task.type === 'pillar') return path.join(CONFIG.websiteDir, `${name}.html`);
    if (task.type === 'blog') return path.join(CONFIG.websiteDir, 'blog', `${name}.html`);
    return path.join(CONFIG.websiteDir, `${name}.html`);
}

function extractHTML(content) {
    // Find HTML content in response
    const doctypeMatch = content.match(/<!DOCTYPE html>[\s\S]*/i);
    if (doctypeMatch) return doctypeMatch[0];

    const htmlMatch = content.match(/<html[\s\S]*<\/html>/i);
    if (htmlMatch) return '<!DOCTYPE html>\n' + htmlMatch[0];

    return content;
}

async function runTask(task) {
    log('INFO', `Starting: ${task.id}`);

    const prompt = generatePrompt(task);
    log('INFO', `Calling Anthropic API...`);

    const response = await callAnthropicAPI(prompt);
    log('INFO', `Got response: ${response.inputTokens} in, ${response.outputTokens} out tokens`);

    const html = extractHTML(response.content);
    const filePath = getFilePath(task);

    // Ensure directory exists
    const dir = path.dirname(filePath);
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }

    fs.writeFileSync(filePath, html);
    log('SUCCESS', `Created: ${filePath}`);

    return {
        tokens: response.inputTokens + response.outputTokens,
        file: filePath
    };
}

async function gitPush(message) {
    const { execSync } = require('child_process');
    try {
        execSync(`cd ${CONFIG.websiteDir} && git add -A && git commit -m "${message}" && git push`, {
            stdio: 'pipe'
        });
        log('INFO', 'Pushed to GitHub');
        return true;
    } catch (e) {
        log('WARN', 'Git push skipped (may be no changes)');
        return false;
    }
}

async function main() {
    if (!CONFIG.apiKey) {
        log('ERROR', 'ANTHROPIC_API_KEY not set!');
        process.exit(1);
    }

    if (!fs.existsSync(CONFIG.logsDir)) {
        fs.mkdirSync(CONFIG.logsDir, { recursive: true });
    }

    log('INFO', '==========================================');
    log('INFO', 'Trust SoCal DA Agent Runner v2 (API Mode)');
    log('INFO', '==========================================');

    let state = loadState();
    log('INFO', `Completed: ${state.completed.length} | Tokens: ${state.tokensUsed} | Pages: ${state.pagesCreated || 0}`);

    while (true) {
        const task = getNextTask(state);

        if (!task) {
            log('INFO', '🎉 All tasks completed! Waiting 1 hour...');
            await new Promise(r => setTimeout(r, 3600000));
            continue;
        }

        try {
            const result = await runTask(task);

            state.completed.push(task.id);
            state.tokensUsed += result.tokens;
            state.pagesCreated = (state.pagesCreated || 0) + 1;
            saveState(state);

            // Push every 5 pages
            if (state.pagesCreated % 5 === 0) {
                await gitPush(`Auto: Added ${state.pagesCreated} pages (latest: ${task.id})`);
            }

            log('INFO', `✅ Progress: ${state.completed.length}/${DA_TASKS.locationPages.length + DA_TASKS.pillarContent.length + DA_TASKS.blogPosts.length} tasks`);
            log('INFO', `📊 Tokens used: ${state.tokensUsed.toLocaleString()}`);

        } catch (e) {
            log('ERROR', `Task ${task.id} failed: ${e.message}`);
            // Don't mark as complete, will retry
        }

        log('INFO', `⏳ Pausing ${CONFIG.pauseBetweenTasks / 1000}s...`);
        await new Promise(r => setTimeout(r, CONFIG.pauseBetweenTasks));
    }
}

process.on('SIGINT', () => process.exit(0));
process.on('SIGTERM', () => process.exit(0));

main().catch(e => {
    log('ERROR', `Fatal: ${e.message}`);
    process.exit(1);
});
