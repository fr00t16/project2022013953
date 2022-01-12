# write by number int dari 0 - 70
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(70):
	value = randint(0,70)
	print(value)