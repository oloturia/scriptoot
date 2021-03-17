from mastodon import Mastodon

fileDir = os.path.dirname(os.path.abspath(__file__))
try:
	with open(fileDir+"/config.json") as f:
		config = json.load(f)
except IOError:
	print("config.json not found")
	quit()

'''
Mastodon.create_app(
	'scriptoot',
	api_base_url = config["api_base_url"],
	to_file = 'scriptoot.secret'
)
'''

mastodon = Mastodon(
	client_id = 'scriptoot.secret',
    api_base_url = config["api_base_url"]
)

mastodon.log_in(
	config["user"]ls,
	config["password_user"],
	to_file = 'scriptoot.cred.secret'
)
