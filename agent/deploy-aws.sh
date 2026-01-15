#!/bin/bash
# Trust SoCal - AWS Agent Deployment Script
# Deploys autonomous agents to build domain authority 24/7

set -e

# Configuration
INSTANCE_TYPE="t3.medium"  # 2 vCPU, 4GB RAM - good for agents
AMI_ID="ami-0c55b159cbfafe1f0"  # Amazon Linux 2023 (will auto-detect region)
KEY_NAME="trust-socal-agents"
SECURITY_GROUP="trust-socal-agent-sg"
INSTANCE_NAME="TrustSoCal-DA-Agents"

echo "🚀 Trust SoCal Agent Deployment"
echo "================================"

# Get region
REGION=$(aws configure get region || echo "us-west-2")
echo "📍 Region: $REGION"

# Get latest Amazon Linux 2023 AMI for the region
echo "🔍 Finding latest Amazon Linux 2023 AMI..."
AMI_ID=$(aws ec2 describe-images \
    --owners amazon \
    --filters "Name=name,Values=al2023-ami-2023*-x86_64" "Name=state,Values=available" \
    --query 'sort_by(Images, &CreationDate)[-1].ImageId' \
    --output text \
    --region $REGION)
echo "✅ AMI: $AMI_ID"

# Create key pair if doesn't exist
if ! aws ec2 describe-key-pairs --key-names $KEY_NAME --region $REGION 2>/dev/null; then
    echo "🔑 Creating SSH key pair..."
    aws ec2 create-key-pair \
        --key-name $KEY_NAME \
        --query 'KeyMaterial' \
        --output text \
        --region $REGION > ~/.ssh/${KEY_NAME}.pem
    chmod 400 ~/.ssh/${KEY_NAME}.pem
    echo "✅ Key saved to ~/.ssh/${KEY_NAME}.pem"
else
    echo "✅ Key pair exists"
fi

# Create security group if doesn't exist
SG_ID=$(aws ec2 describe-security-groups \
    --group-names $SECURITY_GROUP \
    --query 'SecurityGroups[0].GroupId' \
    --output text \
    --region $REGION 2>/dev/null || echo "")

if [ -z "$SG_ID" ] || [ "$SG_ID" == "None" ]; then
    echo "🔒 Creating security group..."
    SG_ID=$(aws ec2 create-security-group \
        --group-name $SECURITY_GROUP \
        --description "Trust SoCal Agent Security Group" \
        --query 'GroupId' \
        --output text \
        --region $REGION)

    # Allow SSH
    aws ec2 authorize-security-group-ingress \
        --group-id $SG_ID \
        --protocol tcp \
        --port 22 \
        --cidr 0.0.0.0/0 \
        --region $REGION

    echo "✅ Security group created: $SG_ID"
else
    echo "✅ Security group exists: $SG_ID"
fi

# User data script to set up the instance
USER_DATA=$(cat << 'USERDATA'
#!/bin/bash
set -e

# Update system
yum update -y

# Install Node.js 20
curl -fsSL https://rpm.nodesource.com/setup_20.x | bash -
yum install -y nodejs git

# Install PM2 for process management
npm install -g pm2

# Create agent directory
mkdir -p /opt/trust-socal-agents
cd /opt/trust-socal-agents

# Install Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Install Claude-Flow
npm install -g claude-flow@alpha

# Create marker file for setup completion
touch /opt/trust-socal-agents/.setup-complete

echo "Setup complete at $(date)" >> /var/log/agent-setup.log
USERDATA
)

# Launch instance
echo "🖥️  Launching EC2 instance..."
INSTANCE_ID=$(aws ec2 run-instances \
    --image-id $AMI_ID \
    --instance-type $INSTANCE_TYPE \
    --key-name $KEY_NAME \
    --security-group-ids $SG_ID \
    --user-data "$USER_DATA" \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$INSTANCE_NAME}]" \
    --query 'Instances[0].InstanceId' \
    --output text \
    --region $REGION)

echo "✅ Instance launched: $INSTANCE_ID"

# Wait for instance to be running
echo "⏳ Waiting for instance to start..."
aws ec2 wait instance-running --instance-ids $INSTANCE_ID --region $REGION

# Get public IP
PUBLIC_IP=$(aws ec2 describe-instances \
    --instance-ids $INSTANCE_ID \
    --query 'Reservations[0].Instances[0].PublicIpAddress' \
    --output text \
    --region $REGION)

echo ""
echo "=========================================="
echo "✅ DEPLOYMENT COMPLETE"
echo "=========================================="
echo "Instance ID: $INSTANCE_ID"
echo "Public IP:   $PUBLIC_IP"
echo "SSH Key:     ~/.ssh/${KEY_NAME}.pem"
echo ""
echo "📋 Next Steps:"
echo "1. Wait 2-3 minutes for setup to complete"
echo "2. SSH into the server:"
echo "   ssh -i ~/.ssh/${KEY_NAME}.pem ec2-user@$PUBLIC_IP"
echo ""
echo "3. Set your Anthropic API key:"
echo "   export ANTHROPIC_API_KEY='your-key-here'"
echo ""
echo "4. Start the agents:"
echo "   cd /opt/trust-socal-agents"
echo "   pm2 start agent-runner.js --name da-agents"
echo ""
echo "5. Monitor progress:"
echo "   pm2 logs da-agents"
echo "=========================================="

# Save connection info
cat > ~/trust-socal-agent-connection.txt << EOF
Trust SoCal Agent Server
========================
Instance ID: $INSTANCE_ID
Public IP: $PUBLIC_IP
SSH Command: ssh -i ~/.ssh/${KEY_NAME}.pem ec2-user@$PUBLIC_IP
Region: $REGION
EOF

echo "📄 Connection info saved to ~/trust-socal-agent-connection.txt"
