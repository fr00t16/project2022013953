# write by number int dari 0 - 860
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(860):
	value = randint(0,860)
	print(value)