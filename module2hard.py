import random

n = int(input("Введите значение первой плитки(от 3 до 20): "))

#def first_plite():
#    list_ = range(3, 20)
#    n = random.choice(list_)
#    return n
#n = first_plite()
#print ("Значение первой плитки =", n)


for i in range(1, 20):
    if i != n:
        for j in range(1, 20):
            if j != n and j != i:
                if n % (i + j) == 0:
                    if i < j:
                        print("Значения второй плитки: ", i, j)