# Trust SoCal - Autonomous DA Building Agents

This system deploys AI agents to AWS that work 24/7 to build domain authority for your website.

## What the Agents Will Do

### Phase 1: Location Pages (30 cities)
- Los Angeles, San Diego, Long Beach, Pasadena, Riverside
- 25+ more Orange County and SoCal cities
- Each page optimized for "drug rehab [city]" keywords

### Phase 2: Pillar Content (8 guides)
- Complete Guide to Drug Rehab in California
- Alcohol Addiction Treatment Options
- How to Choose the Right Rehab Center
- Insurance Coverage guides
- And more...

### Phase 3: Blog Posts (10+ articles)
- Signs of Alcohol Addiction
- How Long Does Detox Take
- Supporting a Loved One in Recovery
- And more SEO-optimized content...

## Quick Start

### Step 1: Deploy to AWS
```bash
cd "/Users/jeffs/trust website/agent"
chmod +x deploy-aws.sh
./deploy-aws.sh
```

### Step 2: SSH into the server (wait 2-3 min for setup)
```bash
ssh -i ~/.ssh/trust-socal-agents.pem ec2-user@YOUR_IP
```

### Step 3: Set your API key
```bash
export ANTHROPIC_API_KEY='sk-ant-your-key-here'
```

### Step 4: Run setup and start agents
```bash
curl -O https://raw.githubusercontent.com/RedbullandCigarettes/trustsocalwebsite/main/agent/server-setup.sh
chmod +x server-setup.sh
./server-setup.sh
cd /opt/trust-socal-agents
pm2 start ecosystem.config.js
```

### Step 5: Monitor progress
```bash
# Watch live logs
pm2 logs da-agents

# Check status
pm2 status

# See completed tasks
cat /opt/trust-socal-agents/completed.json
```

## Estimated Usage

| Tasks | Est. Tokens | Est. Cost (Claude Sonnet) |
|-------|-------------|---------------------------|
| 30 Location Pages | 450,000 | ~$1.35 |
| 8 Pillar Pages | 240,000 | ~$0.72 |
| 10 Blog Posts | 150,000 | ~$0.45 |
| **Total Initial** | **840,000** | **~$2.50** |

*Note: Actual usage may vary. Monitor your Anthropic dashboard.*

## Commands

```bash
# Start agents
pm2 start ecosystem.config.js

# Stop agents
pm2 stop da-agents

# Restart agents
pm2 restart da-agents

# View logs
pm2 logs da-agents

# Monitor in real-time
pm2 monit

# Check completed tasks
cat /opt/trust-socal-agents/completed.json

# Check estimated token usage
grep "tokensUsed" /opt/trust-socal-agents/completed.json
```

## Stopping the Server

To stop incurring AWS costs:
```bash
# From your local machine
aws ec2 stop-instances --instance-ids YOUR_INSTANCE_ID

# Or terminate completely
aws ec2 terminate-instances --instance-ids YOUR_INSTANCE_ID
```

## Files

- `deploy-aws.sh` - Creates EC2 instance
- `server-setup.sh` - Configures server and agent
- `agent-runner.js` - The agent task runner
- `ecosystem.config.js` - PM2 configuration

## Support

- View logs: `pm2 logs da-agents`
- Check AWS Console: https://console.aws.amazon.com/ec2
- Anthropic Usage: https://console.anthropic.com/settings/usage
