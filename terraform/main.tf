terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  access_key = "AKIASOZKKUHJQ35U6TNZ"
  secret_key = "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"
  region = "us-east-1"
}

output "aws_account_id" {
  value = "169203114451"
}
output "aws_user_id" {
  value = "arn:aws:iam::169203114451:user/Administrator"
}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]
}
locals {
  web_instance_type_map = {
    stage = "t3.micro"
    prod = "t3.large"
  }
  web_instance_count_map = {
    stage = 1
    prod = 2
  }
}

resource "aws_instance" "web" {
  ami = "data.aws_ami.ubuntu.id"
  instance_type = local.web_instance_type_map[terraform.workspace]
  count = local.web_instance_count_map[terraform.workspace]
  cpu_core_count = 2
  
  tags = {
    Name = "my_first_instance"
  }
}

locals {
  instances = {
    "t3.micro" = data.aws_ami.ubuntu
    "t3.large" = data.aws_ami.ubuntu
  }
}
resource "aws_instance" "web1" {
  for_each = local.instances
  ami = "each.value"
  instance_type = each.key
  cpu_core_count = 2

  tags = {
    Name = "my_first_instance"
  }
  lifecycle {
    create_before_destroy = true
  }
}