ls = ["A",'B','C','D','E','F','G','L','Q','U']
n = int(input("son kiriting: "))
uzunlik = len(ls)
list1 = []
for i in range(0, uzunlik, n):
    bolak = ls[i:i+n]
    list1.append(bolak)
print(list1)
