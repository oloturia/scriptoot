from wri import wri
from search_toot import search_toot
from search_toot import strip_html

def parseop(testop):
	testop = strip_html(testop)
	testop = testop[15:]
	sp = ','
	command_list = testop.split(";")
	index = 0
	
	while index < len(command_list):
		command = command_list[index]
		command,value = command[0:3],command[3:]
		print("COMMAND="+command)
		
		if command == "WRI":
			wri(value.split(sp)[0],int(value.split(sp)[1]),value.split(sp)[2])
		elif command == "CON":
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
				jmp_to = value.split(sp)[0]
				offset = value.split(sp)[1]
				command_list = search_toot(jmp_to.split(";"))
				index = offset-1
			except:
				pass

		index +=1
	
	
				


