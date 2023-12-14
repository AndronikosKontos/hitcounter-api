#!/usr/bin/env python3

import aws_cdk as cdk

from hitcounter_api.hitcounter_api_stack import HitcounterApiStack


app = cdk.App()
HitcounterApiStack(app, "HitcounterApiStack")

app.synth()
