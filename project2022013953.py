# write by number int dari 0 - 629
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(629):
	value = randint(0,629)
	print(value)