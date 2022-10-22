import random
f = open("WriteNumRandom.txt","w")

for i in range(1,51):
       n = random.randint(500,1000)
       f.write(str(n))
       f.write("\n")

f.close()
