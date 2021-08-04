variable "project" {
    description = "project name"
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
}