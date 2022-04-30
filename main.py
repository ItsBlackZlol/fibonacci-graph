import matplotlib.pyplot as plt

fibolist = [1,1]
def fibo(numbers):
    number = 0
    while number <= numbers:
        fibolist.append(fibolist[-1] + fibolist[-2])
        number += 1

fibonum = int(input("How much fibonnaci numbers? > "))
fibo(fibonum)

plt.plot(fibolist)
plt.show()
