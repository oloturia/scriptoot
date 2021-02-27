from mastodon import Mastodon
import json,os

fileDir = os.path.dirname(os.path.abspath(__file__))

def login():
	try:
		with open(fileDir+"/config.json") as f:
			config = json.load(f)
	except IOError:
		print("config.json not found")
		quit()
	mastodon = Mastodon(
		access_token = "scriptoot.cred.secret",
		api_base_url = config["api_base_url"]
	)	
	return mastodon
