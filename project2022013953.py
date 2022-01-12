# write by number int dari 0 - 256
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(256):
	value = randint(0,256)
	print(value)