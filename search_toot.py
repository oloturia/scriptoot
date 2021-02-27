from mastodon import Mastodon
import login

def strip_html(htmltoot):
	striptoot = ""
	writing = True
	for l in htmltoot:
		if l == "<":
			writing = False
		if writing:
			striptoot += l
		if l == ">":
			writing = True
	return striptoot


def search_toot(search_tag):
	mastodon = login.login()
	status = mastodon.search(search_tag)['statuses']
	pasrer_cursor = 0
	found_content = ""
	toot_id = ""

	for toot in status:
		if(len(toot['tags']) > 0):
			parser_cursor = toot['content'].index("#")
			variable = (toot['content'][parser_cursor:parser_cursor+len(search_tag)])
			if variable == search_tag:
				toot_id = toot['id']
				found_content = strip_html(toot['content'])
				found_content = found_content[len(search_tag)+1:]
				break


	return found_content,toot_id

if __name__ == "__main__":
	print(search_toot("#test"))
