a=[]
print("Введите число. чтобы закончить нажмите 0")
k=int(input())
while k!=0:
    a.append(k)
    k=int(input())
print("максимальное число: ", max(a))
