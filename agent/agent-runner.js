#!/usr/bin/env node
/**
 * Trust SoCal - Domain Authority Building Agent Runner
 * Runs continuously to build domain authority through content and SEO
 *
 * Tasks the agents will perform:
 * 1. Generate location pages (50+ cities)
 * 2. Create pillar content (guides, resources)
 * 3. Write blog posts (SEO optimized)
 * 4. Create linkable assets (infographics data, statistics)
 * 5. Optimize existing pages continuously
 * 6. Monitor and fix technical SEO issues
 */

const { spawn, execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

// Configuration
const CONFIG = {
    websiteDir: '/opt/trust-socal-agents/website',
    logsDir: '/opt/trust-socal-agents/logs',
    tasksFile: '/opt/trust-socal-agents/tasks.json',
    completedFile: '/opt/trust-socal-agents/completed.json',
    pauseBetweenTasks: 30000, // 30 seconds between tasks
    maxConcurrentAgents: 3,
    estimatedTokensPerTask: 15000, // For credit tracking
};

// Task definitions for building domain authority
const DA_TASKS = {
    // Phase 1: Location Pages (High Priority - Local SEO)
    locationPages: [
        { city: 'Los Angeles', priority: 1, type: 'location' },
        { city: 'San Diego', priority: 1, type: 'location' },
        { city: 'Long Beach', priority: 1, type: 'location' },
        { city: 'Pasadena', priority: 1, type: 'location' },
        { city: 'Riverside', priority: 1, type: 'location' },
        { city: 'San Bernardino', priority: 2, type: 'location' },
        { city: 'Fullerton', priority: 2, type: 'location' },
        { city: 'Costa Mesa', priority: 2, type: 'location' },
        { city: 'Mission Viejo', priority: 2, type: 'location' },
        { city: 'Laguna Beach', priority: 2, type: 'location' },
        { city: 'Tustin', priority: 3, type: 'location' },
        { city: 'Lake Forest', priority: 3, type: 'location' },
        { city: 'San Clemente', priority: 3, type: 'location' },
        { city: 'Dana Point', priority: 3, type: 'location' },
        { city: 'Yorba Linda', priority: 3, type: 'location' },
        { city: 'Brea', priority: 3, type: 'location' },
        { city: 'La Habra', priority: 3, type: 'location' },
        { city: 'Rancho Santa Margarita', priority: 3, type: 'location' },
        { city: 'Aliso Viejo', priority: 3, type: 'location' },
        { city: 'Laguna Niguel', priority: 3, type: 'location' },
        { city: 'Seal Beach', priority: 3, type: 'location' },
        { city: 'Westminster', priority: 3, type: 'location' },
        { city: 'Garden Grove', priority: 3, type: 'location' },
        { city: 'Fountain Valley', priority: 3, type: 'location' },
        { city: 'Cypress', priority: 3, type: 'location' },
        { city: 'Buena Park', priority: 3, type: 'location' },
        { city: 'La Mirada', priority: 3, type: 'location' },
        { city: 'Placentia', priority: 3, type: 'location' },
        { city: 'Stanton', priority: 4, type: 'location' },
        { city: 'Los Alamitos', priority: 4, type: 'location' },
    ],

    // Phase 2: Pillar Content (Authority Building)
    pillarContent: [
        { topic: 'Complete Guide to Drug Rehab in California', priority: 1, type: 'pillar' },
        { topic: 'Alcohol Addiction Treatment Options Guide', priority: 1, type: 'pillar' },
        { topic: 'How to Choose the Right Rehab Center', priority: 1, type: 'pillar' },
        { topic: 'Understanding Addiction: A Family Guide', priority: 2, type: 'pillar' },
        { topic: 'Insurance Coverage for Addiction Treatment', priority: 2, type: 'pillar' },
        { topic: 'Detox Process: What to Expect', priority: 2, type: 'pillar' },
        { topic: 'Outpatient vs Inpatient Treatment Comparison', priority: 2, type: 'pillar' },
        { topic: 'Dual Diagnosis Treatment Guide', priority: 2, type: 'pillar' },
        { topic: 'Medication-Assisted Treatment (MAT) Guide', priority: 3, type: 'pillar' },
        { topic: 'Aftercare and Relapse Prevention', priority: 3, type: 'pillar' },
    ],

    // Phase 3: Blog Content (Ongoing SEO)
    blogPosts: [
        { topic: 'Signs of Alcohol Addiction', priority: 1, type: 'blog' },
        { topic: 'How Long Does Detox Take', priority: 1, type: 'blog' },
        { topic: 'Supporting a Loved One in Recovery', priority: 1, type: 'blog' },
        { topic: 'Fentanyl Crisis in Orange County', priority: 2, type: 'blog' },
        { topic: 'Benefits of Holistic Addiction Treatment', priority: 2, type: 'blog' },
        { topic: 'Addiction and Mental Health Connection', priority: 2, type: 'blog' },
        { topic: 'What Happens in Group Therapy', priority: 2, type: 'blog' },
        { topic: 'Rebuilding Relationships After Addiction', priority: 3, type: 'blog' },
        { topic: 'Exercise and Recovery', priority: 3, type: 'blog' },
        { topic: 'Nutrition in Addiction Recovery', priority: 3, type: 'blog' },
        { topic: 'Mindfulness and Sobriety', priority: 3, type: 'blog' },
        { topic: 'PTSD and Substance Abuse', priority: 3, type: 'blog' },
        { topic: 'Prescription Drug Addiction Signs', priority: 3, type: 'blog' },
        { topic: 'Intervention Tips for Families', priority: 3, type: 'blog' },
        { topic: 'Sober Living Benefits', priority: 3, type: 'blog' },
    ],

    // Phase 4: Linkable Assets (Backlink Magnets)
    linkableAssets: [
        { topic: 'Orange County Addiction Statistics 2025', priority: 1, type: 'stats' },
        { topic: 'California Rehab Center Comparison Chart', priority: 2, type: 'comparison' },
        { topic: 'Addiction Treatment Cost Calculator', priority: 2, type: 'tool' },
        { topic: 'Recovery Timeline Infographic', priority: 2, type: 'infographic' },
        { topic: 'Insurance Coverage Checker Guide', priority: 3, type: 'tool' },
    ],

    // Phase 5: Technical SEO Maintenance
    technicalSEO: [
        { task: 'Audit and fix broken links', priority: 1, type: 'technical' },
        { task: 'Update sitemap.xml', priority: 1, type: 'technical' },
        { task: 'Optimize meta descriptions', priority: 2, type: 'technical' },
        { task: 'Add schema markup to new pages', priority: 2, type: 'technical' },
        { task: 'Improve internal linking', priority: 2, type: 'technical' },
        { task: 'Compress and optimize images', priority: 3, type: 'technical' },
    ],
};

// Logger
function log(level, message) {
    const timestamp = new Date().toISOString();
    const logMessage = `[${timestamp}] [${level}] ${message}`;
    console.log(logMessage);

    // Append to log file
    const logFile = path.join(CONFIG.logsDir, `agent-${new Date().toISOString().split('T')[0]}.log`);
    fs.appendFileSync(logFile, logMessage + '\n');
}

// Load or initialize task state
function loadTaskState() {
    try {
        if (fs.existsSync(CONFIG.completedFile)) {
            return JSON.parse(fs.readFileSync(CONFIG.completedFile, 'utf8'));
        }
    } catch (e) {
        log('WARN', `Could not load completed tasks: ${e.message}`);
    }
    return { completed: [], inProgress: [], tokensUsed: 0, startTime: Date.now() };
}

// Save task state
function saveTaskState(state) {
    fs.writeFileSync(CONFIG.completedFile, JSON.stringify(state, null, 2));
}

// Get next task to run
function getNextTask(state) {
    const allTasks = [
        ...DA_TASKS.locationPages,
        ...DA_TASKS.pillarContent,
        ...DA_TASKS.blogPosts,
        ...DA_TASKS.linkableAssets,
        ...DA_TASKS.technicalSEO,
    ].sort((a, b) => a.priority - b.priority);

    for (const task of allTasks) {
        const taskId = `${task.type}-${task.city || task.topic || task.task}`;
        if (!state.completed.includes(taskId) && !state.inProgress.includes(taskId)) {
            return { ...task, id: taskId };
        }
    }
    return null;
}

// Generate prompt for task
function generatePrompt(task) {
    switch (task.type) {
        case 'location':
            return `Create a comprehensive SEO-optimized location page for "${task.city}, California" for Trust SoCal drug rehab center.

Use the rehab-location-pages skill guidelines:
- Title: "Drug Rehab for ${task.city} Residents | Trust SoCal"
- Use "FOR ${task.city} Residents" not "IN ${task.city}"
- Include local statistics, demographics, travel info
- Add FAQ schema markup
- Include nearby locations section
- Target keyword: "drug rehab ${task.city}"

Save to: locations/${task.city.toLowerCase().replace(/ /g, '-')}.html`;

        case 'pillar':
            return `Create a comprehensive 3000+ word pillar page on "${task.topic}" for Trust SoCal.

Use the seo-content-creator skill guidelines:
- YMYL compliant with E-E-A-T signals
- Include medical reviewer box
- Add FAQ section with schema
- Internal links to services and locations
- Target long-tail keywords
- Include statistics with sources

Save to appropriate location based on topic.`;

        case 'blog':
            return `Write a 1500-2000 word SEO-optimized blog post on "${task.topic}" for Trust SoCal.

Use seo-content-creator guidelines:
- Engaging introduction with keyword
- Clear H2/H3 structure
- Include FAQ section
- Internal links to services
- Call-to-action at end
- Medical accuracy (YMYL)

Save to: blog/${task.topic.toLowerCase().replace(/ /g, '-')}.html`;

        case 'stats':
        case 'comparison':
        case 'tool':
        case 'infographic':
            return `Create a linkable asset: "${task.topic}" for Trust SoCal.

This should be:
- Data-rich and shareable
- Well-designed with proper HTML/CSS
- Include sources and citations
- Easy to reference/link to
- Schema markup for rich snippets

Save to: resources/${task.topic.toLowerCase().replace(/ /g, '-')}.html`;

        case 'technical':
            return `Perform technical SEO task: "${task.task}" for Trust SoCal website.

Audit the current website and:
- Identify issues
- Fix problems found
- Document changes made
- Update sitemap if needed`;

        default:
            return `Execute task: ${JSON.stringify(task)}`;
    }
}

// Run a single task with Claude
async function runTask(task) {
    return new Promise((resolve, reject) => {
        const prompt = generatePrompt(task);

        log('INFO', `Starting task: ${task.id}`);
        log('INFO', `Type: ${task.type}, Priority: ${task.priority}`);

        // Use Claude Code CLI to execute the task
        const claude = spawn('claude', [
            '--print',
            '--dangerously-skip-permissions',
            '-p', prompt
        ], {
            cwd: CONFIG.websiteDir,
            env: { ...process.env },
        });

        let output = '';
        let errorOutput = '';

        claude.stdout.on('data', (data) => {
            output += data.toString();
            process.stdout.write(data);
        });

        claude.stderr.on('data', (data) => {
            errorOutput += data.toString();
            process.stderr.write(data);
        });

        claude.on('close', (code) => {
            if (code === 0) {
                log('SUCCESS', `Task completed: ${task.id}`);
                resolve({ success: true, output, task });
            } else {
                log('ERROR', `Task failed: ${task.id} - ${errorOutput}`);
                reject(new Error(`Task failed with code ${code}: ${errorOutput}`));
            }
        });

        claude.on('error', (err) => {
            log('ERROR', `Failed to start task: ${err.message}`);
            reject(err);
        });
    });
}

// Main loop
async function main() {
    // Ensure directories exist
    if (!fs.existsSync(CONFIG.logsDir)) {
        fs.mkdirSync(CONFIG.logsDir, { recursive: true });
    }

    log('INFO', '========================================');
    log('INFO', 'Trust SoCal DA Agent Runner Started');
    log('INFO', '========================================');

    let state = loadTaskState();
    log('INFO', `Completed tasks: ${state.completed.length}`);
    log('INFO', `Estimated tokens used: ${state.tokensUsed}`);

    while (true) {
        const task = getNextTask(state);

        if (!task) {
            log('INFO', 'All tasks completed! Restarting from technical SEO...');
            // Reset technical SEO tasks for continuous maintenance
            state.completed = state.completed.filter(id => !id.startsWith('technical-'));
            saveTaskState(state);
            continue;
        }

        // Mark task as in progress
        state.inProgress.push(task.id);
        saveTaskState(state);

        try {
            await runTask(task);

            // Mark as completed
            state.inProgress = state.inProgress.filter(id => id !== task.id);
            state.completed.push(task.id);
            state.tokensUsed += CONFIG.estimatedTokensPerTask;
            saveTaskState(state);

            log('INFO', `Progress: ${state.completed.length} tasks completed`);
            log('INFO', `Estimated tokens used: ${state.tokensUsed.toLocaleString()}`);

        } catch (error) {
            log('ERROR', `Task ${task.id} failed: ${error.message}`);
            state.inProgress = state.inProgress.filter(id => id !== task.id);
            saveTaskState(state);
        }

        // Pause between tasks
        log('INFO', `Pausing ${CONFIG.pauseBetweenTasks / 1000}s before next task...`);
        await new Promise(resolve => setTimeout(resolve, CONFIG.pauseBetweenTasks));
    }
}

// Handle graceful shutdown
process.on('SIGINT', () => {
    log('INFO', 'Received SIGINT, shutting down gracefully...');
    process.exit(0);
});

process.on('SIGTERM', () => {
    log('INFO', 'Received SIGTERM, shutting down gracefully...');
    process.exit(0);
});

// Start
main().catch(err => {
    log('ERROR', `Fatal error: ${err.message}`);
    process.exit(1);
});
