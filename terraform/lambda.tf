module "bindicator_lambda" {
  source                    = "./lambda"
  project_name              = var.project_name
  environment_name          = var.environment_name
  fn_name                   = var.fn_name
  fn_handler                = var.fn_handler
  lambda_source_bucket_name = "domweldon-bindicator-lambda-source-01"

  environment_variables = [{
    # project
    ENV              = var.environment_name
    PROJECT_NAME     = var.project_name
    ENVIRONMENT_NAME = var.environment_name
    # sentry
    SENTRY_DSN = sentry_key.asgi.dsn_public
  }]
}
