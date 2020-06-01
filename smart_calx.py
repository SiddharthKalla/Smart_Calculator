response=['My name is CALX a smart calculator', 'Thanks for using me '
          ,'Sorry ,this is beyond my ability'] 

# get tokens
def extract_from_text(text): 
	l=[] 
	for t in text.split(' '): 
		try: 
			l.append(float(t)) 
		except ValueError: 
			pass
	return l 
#Different functions for the calculator
#LCM 
def lcm(a,b): 
	L=a if a>b else b 
	while L<=a*b: 
		if L%a==0 and L%b==0: 
			return L 
		L+=1

#HCF 
def hcf(a,b): 
	H=a if a<b else b 
	while H>=1: 
		if a%H==0 and b%H==0: 
			return H 
		H-=1

#Addition 
def add(a,b): 
	return a+b 

#Subtraction 
def sub(a,b): 
	return a-b 

#Multiplication 
def mul(a,b): 
	return a*b 

#Division 
def div(a,b): 
	return a/b 

#Remainder 
def mod(a,b): 
	return a%b 

def end(): 
	print(response[1]) 
	input('press enter key to exit') 
	exit() 

def myname(): 
	print(response[0]) 
def sorry(): 
	print(response[2]) 

#Operations used
operations={'+':add,'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add, 
	    '-':sub,'SUB':sub,'SUBTRACT':sub, 'MINUS':sub, 
	    'DIFFERENCE':sub,'LCM':lcm,'HCF':hcf, 
	    '*':mul,'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul, 
	    '/':div,'DIVISION':div,'MOD':mod,'REMANDER':mod,'MODULAS':mod} 

#commands 
commands={'NAME':myname,'BYE':end,'EXIT':end,'END':end,'CLOSE':end} 
		
print('      '+response[0]+'      ')
print('                Hi,there!!!!        ')

while True: 
	print() 
	text=input('enter your queries: ') 
	for word in text.split(' '): 
		if word.upper() in operations.keys(): 
			try: 
				l = extract_from_text(text) 
				r = operations[word.upper()] (l[0],l[1]) 
				print(r) 
			except: 
				print('something went wrong going plz enter again !!') 
			finally: 
					break
		elif word.upper() in commands.keys(): 
					commands[word.upper()]() 
					break
	else:		 
		sorry() 
