tuple1 = (3,5,16,35,75)
tuple2 = (1,19,28,44,64)
t=[i for j in zip(tuple1, tuple2) for i in j]
print(tuple(t))