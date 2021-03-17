from wri import wri
from search_toot import search_toot

def parseop(textop):
	
	sp = ','
	
	command_list = textop.split("<br/>")[1:]
	index = 0

	while index < len(command_list):
		command = command_list[index]
		command,value = command[0:3],command[4:]
		print("COMMAND="+command)
		
		if command == "WRI":
			#wri("#"+value.split(sp)[0],int(value.split(sp)[1]),value.split(sp)[2])
			wri("#"+value.split(sp)[0],int(value.split(sp)[1]),sp.join(value.split(sp)[2:]))
		elif command == "CON": #TEST COMMAND ONLY AT THE MOMENT
			print("addressA="+value.split(',')[0])
			print("start  A="+value.split(',')[1])
			print("stop   A="+value.split(',')[2])
			print("addressB="+value.split(',')[3])
			print("start  B="+value.split(',')[4])
			print("stop   B="+value.split(',')[5])
			print("addressC="+value.split(',')[6])
			print("start  C="+value.split(',')[7])
		elif command == "JMP":
			try:
				jmp_to = "#"+value.split(sp)[0]
				offset = int(value.split(sp)[1])
				command_list = search_toot(jmp_to)[0] 
				index = offset-1
			except:
				pass
				
		elif command == "JEQ":
			try:
				vale_1 = value.split(sp)[0]
				strt_1 = int(value.split(sp)[1])
				
				vale_2 = value.split(sp)[3]
				strt_2 = int(value.split(sp)[4])
				
				jmp_to = value.split(sp)[6]
				offset = int(value.split(sp)[7])
			except:
				pass

			toot = search_toot(vale_1)[0]
			toot1 = toot.split("\n")[strt1]
			# print(toot1)
			toot = search_toot(vale_2)[0]
			toot2 = toot.split("\n")[strt2]
			# print(toot2)
			try:
				toot1 = int(toot1)
				toot2 = int(toot2)
			except ValueError:	
				pass
			if toot1 == toot2:
				command_list = search_toot(jmp_to.split(";")) #TEST THIS
				index = offset -1
			

		index +=1
	
	
				


