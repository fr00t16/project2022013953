# write by number int dari 0 - 127
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(127):
	value = randint(0,127)
	print(value)