provider "aws" {
  region = "us-east-1"
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