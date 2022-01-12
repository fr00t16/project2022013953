# write by number int dari 0 - 465
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(465):
	value = randint(0,465)
	print(value)