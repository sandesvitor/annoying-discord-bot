#-------------------------------------------------------------------------------------------
# Security Group
#-------------------------------------------------------------------------------------------

resource "aws_security_group" "security_group" {
  name                   = "bot-security-group"
  description            = "Security group for annoying bot"
  vpc_id                 = var.vpc_id
  revoke_rules_on_delete = true
}

resource "aws_security_group_rule" "egress" {
  security_group_id = aws_security_group.security_group.id
  description       = "Egress rule"
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
}

resource "aws_security_group_rule" "ingres_ssh" {
  security_group_id = aws_security_group.security_group.id
  description       = "Ingress rule for SSH"
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
}

#-------------------------------------------------------------------------------------------
# EC2
#-------------------------------------------------------------------------------------------

resource "aws_instance" "this" {
  ami                    = "ami-06078a297452ba5aa"
  instance_type          = "t2.micro"
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.security_group.id]
  subnet_id              = var.subnet_id
  monitoring             = true
  source_dest_check      = true
}
