provider "aws" {
  region  = "eu-west-1"
  profile = "default"
}

provider "circleci" {
  organization = var.circleci_organization
  vcs_type     = var.circleci_vcs_type
}

provider "sentry" {}
