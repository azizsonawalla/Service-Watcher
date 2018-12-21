import requests
import json

class Slack:

	def __init__(self, webhook):
		self.webhook = webhook

	def send_message(self, msg):
		print("Sending Slack notification")
		sys.stdout.flush()

		headers = {
		    "Accept": "application/json"
		}

		query = {
		    "username": self.slack["username"],
		    "channel": self.slack["channel"],
		    "icon_emoji": self.slack["icon"],
		    "text": msg,
		}

		try:
		    requests.request("POST", self.slack["url"], headers=headers, data=json.dumps(query), verify=True)
		except Exception as e:
		    print("** Failed to send Slack notification {}".format(str(e)))
		    sys.stdout.flush()

		print("** Successfully sent Slack notification")
		
