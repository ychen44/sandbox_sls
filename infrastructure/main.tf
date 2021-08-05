terraform {
    required_version = ">= 1.0.2 "

}

provider "aws" {
    region = "us-east-1"
}

module "vpc" {
    source = "terraform-aws-modules/vpc/aws"

    name = join("", [var.project, "-", terraform.workspace,"-", "vpc"])
    cidr = var.cidr
    azs  = var.available_azs
    private_subnets = var.private_subnets
    public_subnets = var.public_subnets

    enable_nat_gateway = var.enable_nat_gateway

    tags = {
        name = var.namespace

    }


}