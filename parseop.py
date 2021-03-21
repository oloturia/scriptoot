from wri import wri
from search_toot import search_toot

import logging

def parseop(textop):
	logging.getLogger().setLevel(logging.INFO)

	sp = ','
	
	command_list = textop.split("<br/>")[1:]
	index = 0

	while index < len(command_list):
		command = command_list[index]
		command,value = command[0:3],command[4:]
		logging.log(logging.INFO,"COMMAND=%s VALUE=%s",command,value)
		
		try:
			if command == "WRI":
				wri("#"+value.split(sp)[0],int(value.split(sp)[1]),sp.join(value.split(sp)[2:]))
				
			elif command == "DEL":
				wri("#"+value.split(sp)[0],-1,"")
				
			elif command == "ADD":
				vale_1 = "#"+value.split(sp)[0]
				offset = len(search_toot(vale_1)[0])
				vale_2 = search_toot( "#"+value.split(sp)[1] )[0][int(value.split(sp)[2])]
				wri(vale_1,offset,vale_2)
								
			elif command == "JMP":
				jmp_to = "#"+value.split(sp)[0]
				offset = int(value.split(sp)[1])
				command_list = search_toot(jmp_to)[0] 
				index = offset-1
									
			elif command == "JEQ" or command == "JNQ" or command == "JGT" or command == "JLT" or command == "SUM" or command == "MUL" or command == "CON" or command == "CPY":
				vale_1 = "#"+value.split(sp)[0]
				strt_1 = int(value.split(sp)[1])
				vale_2 = "#"+value.split(sp)[2]
				strt_2 = int(value.split(sp)[3])
				
				if command != "CPY":
					jmp_to = "#"+value.split(sp)[4]
					offset = int(value.split(sp)[5])
				
				
				toot1 = search_toot(vale_1)[0][strt_1]
				
				if command == "CPY":
					wri(vale_2,strt_2,toot1)
				
				toot2 = search_toot(vale_2)[0][strt_2]
				
				
				try:
					toot1 = int(toot1)
					toot2 = int(toot2)
					if command == "SUM":
						wri(jmp_to,offset,str(toot1+toot2))
					elif command == "MUL":
						wri(jmp_to,offset,str(toot1*toot2))
				except ValueError:	
					if command == "CON":
						wri(jmp_to,offset,str(toot1)+str(toot2))
				
				if (command == "JEQ" and (toot1 == toot2)) or (command == "JNQ" and (toot1 != toot2)) or (command == "JGT" and (toot1 > toot2)) or (command == "JLT" and (toot1 < toot2)):
					command_list = search_toot(jmp_to)[0]
					index = offset -1
		except Exception as err:
			logging.log(logging.INFO,"Error: %s",err)

		index +=1
	
	
				


