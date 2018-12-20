import requests
import json

class Slack:

	def __init__(self, webhook):
		self.webhook = webhook

