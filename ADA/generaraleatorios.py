import random
from random import randint

def random_seed_list(n):
    
    list = []
    for i in range(0,n):
        random.seed(i)
        list.append(random.randrange(5))
    return list

print(random_seed_list(5))
#print(random_seed_list(10))
#print(random_seed_list(20))
#print(random_seed_list(50))
#print(random_seed_list(100))
#print(random_seed_list(200))
#print(random_seed_list(300))
#print(random_seed_list(400))
#print(random_seed_list(500))
#print(random_seed_list(600))
#print(random_seed_list(700))
#print(random_seed_list(800))
#print(random_seed_list(900))
#print(random_seed_list(1000))


