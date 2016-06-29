import random
import time

board = [' ',' ',' ', ' ', ' ', ' ',' ',' ',' ',' ']
status = [1,2,3,4,5,6,7,8,9]
def printBoard(board):
		print("\n\n")
		print(board[1]+'  |  '+board[2]+'  |  '+board[3])
		print('-------------')
		print(board[4]+'  |  '+board[5]+'  |  '+board[6])
		print('-------------')
		print(board[7]+'  |  '+board[8]+'  |  '+board[9])
		print("\n\n")

		
chance = random.randint(1, 2)
if(chance==1):
	uch='X'
	print("\n\nyou have been assigned X")
else:
	uch = 'O'
	print("\n\nYou have been assigned O")
count =0
#write a new cturn to make the computer smarter too instead of filling the places randomly

def smart(board):
	cpos = random.choice(status)
	if(uch=='X'):
		cch='O'
	else :
		cch='X'
	if(board[1]==board[2]==cch and board[3]==' '):
		cpos=3
	elif(board[2]==board[3]==cch and board[1]==' '):
		cpos = 1
	elif(board[1]==board[3]==cch and board[2]==' '):
		cpos = 2
	elif(board[4]==board[5]==cch and board[6]==' '):
		cpos = 6
	elif(board[5]==board[6]==cch and board[4]==' '):
		cpos = 4
	elif(board[4]==board[6]==cch and board[5]==' '):
		cpos = 5
	elif(board[7]==board[8]==cch and board[9]==' '):
		cpos = 9
	elif(board[8]==board[9]==cch and board[7]==' '):
		cpos = 7
	elif(board[7]==board[9]==cch and board[8]==' '):
		cpos = 8
	elif(board[1]==board[4]==cch and board[7]==' '):
		cpos = 7
	elif(board[4]==board[7]==cch and board[1]==' '):
		cpos = 1
	elif(board[1]==board[7]==cch and board[4]==' '):
		cpos = 4
	elif(board[2]==board[5]==cch and board[8]==' '):
		cpos = 8
	elif(board[5]==board[8]==cch and board[2]==' '):
		cpos = 2
	elif(board[2]==board[8]==cch and board[5]==' '):
		cpos = 5
	elif(board[3]==board[6]==cch and board[9]==' '):
		cpos = 9
	elif(board[6]==board[9]==cch and board[3]==' '):
		cpos = 3
	elif(board[3]==board[9]==cch and board[6]==' '):
		cpos = 6
	elif(board[1]==board[5]==cch and board[9]==' '):
		cpos = 9
	elif(board[5]==board[9]==cch and board[1]==' '):
		cpos = 1
	elif(board[1]==board[9]==cch and board[5]==' '):
		cpos = 5
	elif(board[3]==board[5]==cch and board[7]==' '):
		cpos = 7
	elif(board[5]==board[7]==cch and board[3]==' '):
		cpos = 3
	elif(board[3]==board[7]==cch and board[5]==' '):
		cpos = 5
	else:
		cpos = random.choice(status)
	
	
	board[cpos]=cch
	status.remove(cpos)
	

def non_smart(board):
	cpos = random.choice(status)
	if(uch=='X'):
		cch='O'
	else :
		cch='X'
	board[cpos]=cch
	status.remove(cpos)

def checkBoard(board):
	if(board[1]==board[2]==board[3]!=' '):
		if(board[1]==uch):
			return 1
		else:
			return 2
	elif(board[4]==board[5]==board[6]!=' '):
		if(board[4]==uch):
			return 1
		else:
			return 2
	elif(board[7]==board[8]==board[9]!=' '):
		if(board[7]==uch):
			return 1
		else:
			return 2
	elif(board[1]==board[4]==board[7]!=' '):
		if(board[1]==uch):
			return 1
		else:
			return 2
	elif(board[2]==board[5]==board[8]!=' '):
		if(board[2]==uch):
			return 1
		else:
			return 2
	elif(board[3]==board[6]==board[9]!=' '):
		if(board[3]==uch):
			return 1
		else:
			return 2
	elif(board[1]==board[5]==board[9]!=' '):
		if(board[1]==uch):
			return 1
		else:
			return 2
	elif(board[3]==board[5]==board[7]!=' '):
		if(board[3]==uch):
			return 1
		else:
			return 2
	else:
		return 3

	
	
while(True):
	print("Enter the position (between 1-9) for your turn")
	pos = int(input())
	if(pos not in status):
		print("invalid position")
		continue
	if board[pos]==' ':
		board[pos]=uch
		count +=1
		status.remove(pos)
		printBoard(board)
		if(checkBoard(board)==1 or checkBoard(board)==2):
			break;
	else:
		print("invalid position")
		continue
	
	if(count==9):
		break;
	print("Computer's turn")
	
	
	
	
	
	smart(board)
	count+=1
	printBoard(board)
	if(checkBoard(board)==1 or checkBoard(board)==2):
			break;
	
	
if(checkBoard(board)==1):
	print("You win!")
elif(checkBoard(board)==2):
	print("You lose :( ")	
else:
	print("Tie !!")
