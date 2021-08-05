variable "project" {
    description = "project name"
    default = "frontstep-iac"
}

variable "namespace" {
  type        = string
  description = "Name to be used on all the resources as identifier"
  default = "frontstep-dev"
}


#====================================
#           Networking
#====================================

variable "cidr" {
    description = "VPC CIDR"
    default = "10.0.0.0/16"
}

variable "available_azs" {
  type        = list
  description = "The available AZ's in the region."
  default = ["us-east-2a", "us-east-2b"]

}

variable "private_subnets" {
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}


variable "public_subnets" {
  default = ["10.0.101.0/24", "10.0.102.0/24"]
}


variable "enable_nat_gateway" {
  type        = string
  description = "Should be true if you want to provision NAT Gateways for each of your private networks"
  default = "true"
  
}