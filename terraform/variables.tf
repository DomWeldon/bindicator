variable "project_name" {
  type        = string
  description = "Name of the project"
}

variable "environment_name" {
  type        = string
  description = "Name of the environment"
}

variable "fn_handler" {
  type        = string
  description = "Handler for the bindicator lambda function"
}

variable "fn_name" {
  type        = string
  description = "Name for the bindicator lambda function"
}

variable "tags" {
  default = {}
}

variable "aws_region" {
  default = "eu-west-1"
}


# circleci
variable "circleci_project_name" {
  type        = string
  description = "Repository name in CircleCI"
}

variable "circleci_vcs_type" {
  type        = string
  default     = "github"
  description = "e.g. GitHub"
}

variable "circleci_organization" {
  type        = string
  description = "For VCS Type"
}


# sentry
variable "sentry_organization" {
  type        = string
  description = "Sentry org name"
}

variable "sentry_organization_slug" {
  type        = string
  description = "Sentry org slug"
}

variable "sentry_team" {
  type        = string
  description = "Sentry team name"
}

variable "sentry_team_slug" {
  type        = string
  description = "Sentry team slug"
}

# meross
variable "meross_password" {
  type = string
}

variable "meross_email" {
  type = string
}
