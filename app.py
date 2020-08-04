#!/usr/bin/env python3

from aws_cdk import core

from cdkgoat.cdkgoat_stack import CdkGoatStack


app = core.App()
CdkGoatStack(app, "cdkgoat")

app.synth()
