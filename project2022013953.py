# write by number int dari 0 - 962
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(962):
	value = randint(0,962)
	print(value)