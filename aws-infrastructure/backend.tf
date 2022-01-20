terraform {
  backend "s3" {
    bucket = "annoying-bot-state-bucket"
    key    = "terraform.tfstate"
    region = "sa-east-1"
  }
}
