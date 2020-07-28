#!/usr/bin/env python3

from aws_cdk import core

from cdkgoat.cdkgoat_stack import CdkgoatStack


app = core.App()
CdkgoatStack(app, "cdkgoat")

app.synth()
