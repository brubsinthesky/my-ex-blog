print('Hello, Django girls!')
print(2 > 4)
name = 'Bruna'
print (name * 3)
if 3 > 2:
	print ('It works')
if 5 > 2:
	print('5 is indeed greater than 2')
else:
	print('5 is not greater than 2')
name = 'Gisele'
if name == 'Bruna':
	print('Hey Bruna!')
elif name == 'Clara':
	print('Hey Clara!')
else:
	print('Hey anonymous')
volume = 57
if volume < 20:
	print("Its's kinda quiet.")
elif 20 <= volume < 40:
	print("It's nice for background music")
elif 40 <= volume < 60:
	print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
	print("Nice for parties")
elif 80 <= volume < 100:
	print("A bit loud!")
else:
	print("My ears are hurting! :(")
def hi():
	print('Hi there!')
	print('How are you?')
hi()
def hi(name):
	if name == 'Bruna':
		print('Hi Bruna!')
	elif name == 'Clara':
		print('Hi Clara!')
	else:
		print('Hi anonymous')
hi('Gisele')
def hi(name):
	print('Hi ' + name + '!')
hi("Rachel")
girls = ['Hannah', 'Kariza', 'Beatriz', 'Jessica', 'You']
for name in girls:
	hi(name)
	print('Next girl')
for i in range(1, 6):
	print(i)
	





