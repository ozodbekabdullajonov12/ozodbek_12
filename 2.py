import random as ran
st = str(input("Satrni kiriting "))
ls = []
ls = st.split("*")
list1 = []
list1 = ls[-1].split("=")
ls.pop(-1)
ls.append(list1[0])
list1.pop(0)
natija = list1[0]
list1.clear()
ishora = []
sum = 0
i = 0
while int(natija) != sum :
	a = ran.randint(1,2)
	i = i % len(ls)-1
	if i == -1:
		i = 0
	if a == 1 :
		sum = sum + int(ls[i]) + int(ls[i+1])
		ishora.append("+")
	else :
		sum = sum + int(ls[i]) + int(ls[i+1])
		ishora.append("-")
	i = i + 1
print(sum)
print(ishora)
