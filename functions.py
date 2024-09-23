dc={"Salim":[74,86,63],"avaz":[65,74,80],"sarvinoz":[80,90,95]}
for x in dc:
        sum=0
        k=len(dc[x])
        for i in dc[x]:
                sum+=i
        print(f"{x}      {sum/k}")
    