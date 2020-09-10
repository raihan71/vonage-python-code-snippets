#!/usr/bin/env python3
import os
from vonage import Voice, Client
from pprint import pprint

APPLICATION_ID = os.environ.get("APPLICATION_ID")
APPLICATION_PRIVATE_KEY_PATH = os.environ.get("APPLICATION_PRIVATE_KEY_PATH")

voice = Voice(
    Client(application_id=APPLICATION_ID, private_key=APPLICATION_PRIVATE_KEY_PATH,)
)

# Note call can be made to current call or a completed call
response = voice.get_call("VONAGE_CALL_UUID")
pprint(response)
