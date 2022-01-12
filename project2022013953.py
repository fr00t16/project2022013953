# write by number int dari 0 - 20
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(20):
	value = randint(0,20)
	print(value)