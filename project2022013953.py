# write by number int dari 0 - 68
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(68):
	value = randint(0,68)
	print(value)