from mastodon import Mastodon
import login
from search_toot import search_toot

def wri(variable,index,new_text):
	mastodon = login.login()
	
	status = mastodon.search(variable)['statuses']

	
	parser_cursor = 0
	found_content = ""
	found_content,toot_id = search_toot(variable)

	if index == -1:
		mastodon.status_delete(toot_id)
		return
	
	if len(found_content) < index +1:
		found_content.extend(['']*((index +1) - len(found_content)))
	
	found_content[index] = new_text
	
	new_toot = variable

	for row in found_content:
		new_toot += "\n"+row
	
	if toot_id:
		mastodon.status_delete(toot_id)
	mastodon.status_post(new_toot)

	return

if __name__ == "__main__":
	wri("#test",5,"ABC")

	# example
	# variable = "#test"
	# index = 7
	# new_text = 'abcde'
