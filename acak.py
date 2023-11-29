def input():
    import random
    file = open('random.txt','w')
    for a in range(1,101):
        value = random.randint(0,400)
        if a != 100:
            file.write(f"{value}\n")
        else:
            file.write(f"{value}")
    file.close()

def output():
    file2 = open('random.txt','r')
    nums = file2.read()
    gan = 0
    gen = 0
    nol = 0
    numbers = [int(x) for x in nums.split()]
    for x in numbers:
        if x % 2:
            gan += 1
        elif x == 0:
            nol += 1
    gen = 100 - gan - nol
    file2.close()

    file3 = open('outputrandom.txt','w')
    file3.write(f"ganjil : {gan}\n")
    file3.write(f"genap  : {gen}\n")
    file3.write(f"nol    : {nol}")
input()
output()