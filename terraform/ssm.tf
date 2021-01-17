// app lambda
resource "aws_ssm_parameter" "bindicator_lambda_arn" {
  name      = "/${var.project_name}/${var.environment_name}/bindicator/lambda/arn"
  type      = "String"
  value     = module.bindicator_lambda.lambda_arn
  overwrite = true
  tags      = local.tags
}

resource "aws_ssm_parameter" "bindicator_source_bucket_id" {
  name      = "/${var.project_name}/${var.environment_name}/bindicator/source/bucket_id"
  type      = "String"
  value     = module.bindicator_lambda.source_bucket_id
  overwrite = true
  tags      = local.tags
}

resource "aws_ssm_parameter" "bindicator_source_key" {
  name      = "/${var.project_name}/${var.environment_name}/bindicator/source/key"
  type      = "String"
  value     = module.bindicator_lambda.source_key
  overwrite = true
  tags      = local.tags
}
