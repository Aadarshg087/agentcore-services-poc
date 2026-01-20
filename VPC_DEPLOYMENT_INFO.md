# VPC Deployment Information for AgentCore Services POC

## Summary

**The Terraform code in this repository does NOT deploy to a specific VPC. Instead, it uses PUBLIC network mode, which means the AgentCore Runtime is deployed without VPC integration.**

## Network Configuration Details

### AgentCore Runtime Network Configuration

In the file `terraform/bedrock_agentcore.tf` (lines 384-386), the AgentCore Runtime is configured as follows:

```hcl
network_configuration {
  network_mode = "PUBLIC"
}
```

### What This Means

1. **No VPC Required**: The `network_mode = "PUBLIC"` setting means that the AgentCore Runtime does not require or use a VPC for deployment.

2. **Public Internet Access**: The runtime will have public internet access and does not need to be placed within a private VPC subnet.

3. **No VPC Dependencies**: There are no VPC-related resources defined in the Terraform configuration, such as:
   - No `aws_vpc` resource
   - No subnet configurations
   - No security groups
   - No NAT gateways
   - No VPC endpoints

### Resources Deployed

The Terraform code deploys the following AWS resources **without VPC integration**:

1. **ECR Repository**: For storing the Docker container image
2. **Lambda Function**: MCP Lambda function (deployed in AWS-managed VPC)
3. **Cognito User Pool**: For authentication
4. **Bedrock AgentCore Gateway**: Gateway for MCP protocol
5. **Bedrock AgentCore Runtime**: The main agent runtime (PUBLIC mode)
6. **IAM Roles and Policies**: For permissions management

### Lambda Function Note

The MCP Lambda function (`aws_lambda_function.mcp_lambda`) is deployed without explicit VPC configuration in the Terraform code. This means it runs in the default AWS-managed Lambda execution environment, which has internet access but is not connected to a customer VPC.

## If You Need VPC Integration

If you want to deploy the AgentCore Runtime within a specific VPC, you would need to:

1. Change the `network_mode` from `"PUBLIC"` to `"VPC"` in the runtime configuration
2. Add VPC configuration block with:
   - `vpc_id`: The ID of your VPC
   - `subnet_ids`: List of subnet IDs where the runtime should be deployed
   - `security_group_ids`: List of security group IDs for network access control

Example modification:

```hcl
network_configuration {
  network_mode = "VPC"
  vpc_id       = "vpc-xxxxxxxxx"
  subnet_ids   = ["subnet-xxxxxxxx", "subnet-yyyyyyyy"]
  security_group_ids = ["sg-xxxxxxxxx"]
}
```

## Current Deployment Region

The deployment region is determined by your AWS CLI or Terraform provider configuration. The Terraform code uses:

```hcl
data "aws_region" "current" {}
```

This dynamically detects the current AWS region from your AWS configuration.

## References

- Terraform files: `terraform/bedrock_agentcore.tf`, `terraform/main.tf`, `terraform/variables.tf`
- Application configuration: `terraform/terraform.tfvars`
