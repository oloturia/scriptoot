from mastodon import Mastodon
import login

def search_toot(search_tag):
	mastodon = login.login()
	status = mastodon.search(search_tag)['statuses']
	pasrer_cursor = 0
	found_content = []
	toot_id = False



	for toot in status:
		if(len(toot['tags']) > 0):
			parser_cursor = toot['content'].index("#")
			variable = (toot['content'][parser_cursor:parser_cursor+len(search_tag)])
			if variable == search_tag:
				toot_id = toot['id']
				found_content = toot['content'].split("<br/>")[1:]
				break
				
	
	return found_content,toot_id

if __name__ == "__main__":
	print(search_toot("#test"))
	print(search_toot("#nonexistant"))
