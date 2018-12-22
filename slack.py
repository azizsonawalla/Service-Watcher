import requests
import json
from host import Host

SERVICE_UP_MSG = " is live again!"
SERVICE_DOWN_MSG = " is unreachable.\nI'll update you when it's up again."
SLACK_URL = ""

def send_message(self, host):
	print("Sending Slack notification")
	sys.stdout.flush()

	if host.get_last_status():
		message = host.get_name() + SERVICE_UP_MSG
	else:
		message = host.get_name() + SERVICE_DOWN_MSG

	headers = {
	    "Accept": "application/json"
	}

	query = {
	    "username": self.slack["username"],
	    "channel": self.slack["channel"],
	    "icon_emoji": self.slack["icon"],
	    "text": message,
	}

	try:
	    requests.request("POST", SLACK_URL, headers=headers, data=json.dumps(query), verify=True)
	except Exception as e:
	    print("** Failed to send Slack notification {}".format(str(e)))
	    sys.stdout.flush()

	print("** Successfully sent Slack notification")
	