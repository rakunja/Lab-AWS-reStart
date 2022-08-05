age=int(input("input your age = "))
if age>18:
	print("Adult")
elif age in range(13,19): #you can use 'elif age >=13 and <=18:'
	print("Teen")
else:
	print("Child")