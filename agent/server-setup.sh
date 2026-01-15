#!/bin/bash
# Trust SoCal - Server Setup Script
# Run this on the EC2 instance after SSH'ing in

set -e

echo "🚀 Trust SoCal Agent Server Setup"
echo "=================================="

# Check for API key
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "❌ ERROR: ANTHROPIC_API_KEY not set!"
    echo "Please run: export ANTHROPIC_API_KEY='your-key-here'"
    exit 1
fi

AGENT_DIR="/opt/trust-socal-agents"
WEBSITE_DIR="$AGENT_DIR/website"
LOGS_DIR="$AGENT_DIR/logs"

# Create directories
echo "📁 Creating directories..."
sudo mkdir -p $AGENT_DIR $WEBSITE_DIR $LOGS_DIR
sudo chown -R ec2-user:ec2-user $AGENT_DIR

# Clone the website repository
echo "📥 Cloning website repository..."
cd $AGENT_DIR
if [ ! -d "$WEBSITE_DIR/.git" ]; then
    git clone https://github.com/RedbullandCigarettes/trustsocalwebsite.git website
else
    cd website && git pull origin main
fi

# Copy agent files
echo "📋 Setting up agent runner..."
cd $AGENT_DIR

# Create the agent runner (copy from local or download)
cat > agent-runner.js << 'AGENT_SCRIPT'
#!/usr/bin/env node
/**
 * Trust SoCal - Domain Authority Building Agent Runner
 * Runs continuously to build domain authority through content and SEO
 */

const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const CONFIG = {
    websiteDir: '/opt/trust-socal-agents/website',
    logsDir: '/opt/trust-socal-agents/logs',
    completedFile: '/opt/trust-socal-agents/completed.json',
    pauseBetweenTasks: 30000,
    estimatedTokensPerTask: 15000,
};

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
        'Understanding Addiction: A Family Guide',
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
        'Addiction and Mental Health',
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
    const logFile = path.join(CONFIG.logsDir, `agent-${ts.split('T')[0]}.log`);
    fs.appendFileSync(logFile, line + '\n');
}

function loadState() {
    try {
        if (fs.existsSync(CONFIG.completedFile)) {
            return JSON.parse(fs.readFileSync(CONFIG.completedFile, 'utf8'));
        }
    } catch (e) {}
    return { completed: [], tokensUsed: 0, startTime: Date.now() };
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

function generatePrompt(task) {
    if (task.type === 'location') {
        return `Create an SEO-optimized location page for "${task.city}, California" for Trust SoCal drug rehab.
Title: "Drug Rehab for ${task.city} Residents | Trust SoCal"
Use "FOR ${task.city} Residents" not "IN ${task.city}"
Include: local stats, demographics, travel info, FAQ schema, nearby locations
Target: "drug rehab ${task.city}"
Save to: locations/${task.city.toLowerCase().replace(/ /g, '-')}.html
Use the existing location page template from the website.`;
    }
    if (task.type === 'pillar') {
        return `Create a 3000+ word pillar page on "${task.topic}" for Trust SoCal.
YMYL compliant with E-E-A-T signals, medical reviewer box, FAQ schema, internal links.
Save to appropriate location.`;
    }
    if (task.type === 'blog') {
        return `Write a 1500 word SEO blog post on "${task.topic}" for Trust SoCal.
Include: clear H2/H3 structure, FAQ section, internal links, CTA.
Save to: blog/${task.topic.toLowerCase().replace(/ /g, '-')}.html`;
    }
    return `Execute: ${JSON.stringify(task)}`;
}

async function runTask(task) {
    return new Promise((resolve, reject) => {
        log('INFO', `Starting: ${task.id}`);
        const claude = spawn('claude', [
            '--print', '--dangerously-skip-permissions',
            '-p', generatePrompt(task)
        ], { cwd: CONFIG.websiteDir, env: process.env });

        claude.stdout.pipe(process.stdout);
        claude.stderr.pipe(process.stderr);

        claude.on('close', code => {
            if (code === 0) {
                log('SUCCESS', `Completed: ${task.id}`);
                resolve({ success: true, task });
            } else {
                log('ERROR', `Failed: ${task.id}`);
                reject(new Error(`Exit code ${code}`));
            }
        });
    });
}

async function main() {
    if (!fs.existsSync(CONFIG.logsDir)) fs.mkdirSync(CONFIG.logsDir, { recursive: true });

    log('INFO', '=== Trust SoCal DA Agent Started ===');
    let state = loadState();
    log('INFO', `Completed: ${state.completed.length}, Tokens: ${state.tokensUsed}`);

    while (true) {
        const task = getNextTask(state);
        if (!task) {
            log('INFO', 'All tasks done! Waiting 1 hour before checking again...');
            await new Promise(r => setTimeout(r, 3600000));
            continue;
        }

        try {
            await runTask(task);
            state.completed.push(task.id);
            state.tokensUsed += CONFIG.estimatedTokensPerTask;
            saveState(state);

            // Git commit and push after each task
            const { execSync } = require('child_process');
            try {
                execSync('git add -A && git commit -m "Auto: Added ' + task.id + '" && git push', {
                    cwd: CONFIG.websiteDir,
                    stdio: 'inherit'
                });
                log('INFO', 'Changes pushed to GitHub');
            } catch (e) {
                log('WARN', 'Git push failed (may be no changes)');
            }

        } catch (e) {
            log('ERROR', e.message);
        }

        log('INFO', `Pausing 30s... Progress: ${state.completed.length} tasks`);
        await new Promise(r => setTimeout(r, CONFIG.pauseBetweenTasks));
    }
}

process.on('SIGINT', () => process.exit(0));
process.on('SIGTERM', () => process.exit(0));
main().catch(e => { log('ERROR', e.message); process.exit(1); });
AGENT_SCRIPT

chmod +x agent-runner.js

# Create PM2 ecosystem file
cat > ecosystem.config.js << 'PM2CONFIG'
module.exports = {
  apps: [{
    name: 'da-agents',
    script: './agent-runner.js',
    cwd: '/opt/trust-socal-agents',
    env: {
      NODE_ENV: 'production',
    },
    log_date_format: 'YYYY-MM-DD HH:mm:ss',
    error_file: '/opt/trust-socal-agents/logs/error.log',
    out_file: '/opt/trust-socal-agents/logs/output.log',
    merge_logs: true,
    max_restarts: 10,
    restart_delay: 60000,
  }]
};
PM2CONFIG

# Configure git for auto-commits
cd $WEBSITE_DIR
git config user.email "agent@trustsocal.com"
git config user.name "Trust SoCal DA Agent"

echo ""
echo "=========================================="
echo "✅ SETUP COMPLETE!"
echo "=========================================="
echo ""
echo "To start the agents:"
echo "  cd /opt/trust-socal-agents"
echo "  export ANTHROPIC_API_KEY='your-key'"
echo "  pm2 start ecosystem.config.js"
echo ""
echo "To monitor:"
echo "  pm2 logs da-agents"
echo "  pm2 monit"
echo ""
echo "To stop:"
echo "  pm2 stop da-agents"
echo ""
echo "To check status:"
echo "  pm2 status"
echo "  cat /opt/trust-socal-agents/completed.json"
echo ""
