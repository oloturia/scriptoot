#!/usr/bin/python3
from mastodon import Mastodon
import threading
import login,parseop
import datetime,time
import signal,sys,os
import psycopg2
import json

mastodon = login.login()
fileDir = os.path.dirname(os.path.abspath(__file__))

def signal_handler(sig, frame):
		print('exiting...',end=' ')
		conn.close()
		print('done!')
		sys.exit(0)


if __name__ == "__main__":
	try:
		with open(fileDir+"/config.json") as f:
			config = json.load(f)
	except IOError:
		print("config.json not found")
		quit()
	try:
		conn = psycopg2.connect(host=config["host"],database=config["database"],user=config["user_database"],password=config["password_database"])
		print("CONNECTION OK")
	except:
		print("ERROR CONNECTING TO DATABASE")
		quit()	

	signal.signal(signal.SIGINT, signal_handler)

	cur = conn.cursor()


	while True:
		time.sleep(2)
		for x in mastodon.conversations():
			
			cur.execute("SELECT eval FROM ListEval WHERE node =1;")
			last = cur.fetchall()[0][0]
			
			delta = x['last_status']['created_at'].replace(tzinfo=None)
			
			if delta.timestamp() > last.timestamp():
				cur.execute("UPDATE ListEval SET eval = '"+str(delta)+"' WHERE node =1;")
				conn.commit()
				
				parseop.parseop(x['last_status']['content'])
			else:
				pass


