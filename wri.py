from mastodon import Mastodon
import login
from search_toot import search_toot

def wri(variable,index,new_text):
	mastodon = login.login()
	
	status = mastodon.search(variable)['statuses']
	parser_cursor = 0
	found_content = ""
	found_content,toot_id = search_toot(variable)
	# for toot in status:
		# if(len(toot['tags']) > 0):
			# parser_cursor = toot['content'].index("</a>")
			# found_content = toot['content'][parser_cursor+5:]
			# break

	mastodon.status_delete(toot_id)

	if index > len(found_content):
		for x in range(0,index-len(found_content)):
			found_content += " "
			
	found_content = variable+" "+found_content[:index]+new_text+found_content[index+len(new_text):]
	mastodon.status_post(found_content)

	# example
	# variable = "#test"
	# new_text = 'abcde'
	# index = 7

if __name__ == "__main__":
	wri("#test",5,"123")
