from random import seed, randint

index_range = int(5e8)
n = int(1e6)

sampled_indexes = []


seed(12345)

for i in range(n):
    sampled_indexes.append(randint(0, index_range))

for index in sampled_indexes:
    print(index)