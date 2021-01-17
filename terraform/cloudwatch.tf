# resource "aws_cloudwatch_event_rule" "every-binday-eve" {
#   name                = "every-binday-eve"
#   description         = "Fires every Sunday night"
#   schedule_expression = "cron(0 17 ? * SUN *)"
# }

resource "aws_cloudwatch_event_rule" "every-binday-eve" {
  name                = "every-binday-eve"
  description         = "Fires every ${var.bin_day_eve} night"
  schedule_expression = "cron(0 18 ? * ${var.bin_day_eve} *)"
}

resource "aws_cloudwatch_event_target" "bindicator" {
  rule      = aws_cloudwatch_event_rule.every-binday-eve.name
  target_id = "lambda"
  arn       = module.bindicator_lambda.lambda_arn
}

resource "aws_lambda_permission" "bindicator" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = module.bindicator_lambda.lambda_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.every-binday-eve.arn
}
