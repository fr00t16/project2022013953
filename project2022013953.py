# write by number int dari 0 - 398
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(398):
	value = randint(0,398)
	print(value)