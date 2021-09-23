b=[int(c)for c in input("Введите набор чисел: ").split()]
for i in range(1,len(b)):
    for j in range(i+1,len(b)):
        for k in range(j+1, len(b)):
            if b[i]+b[j]>b[k] and b[i]+b[k]>b[j] and b[k]+b[j]>b[i] and b[i]>0 and b[j]>0 and b[k]>0:
                pp=(b[i]+b[j]+b[k])/2
                print("Подходящие числа:",b[i],b[j],b[k])
                print("Площадь треугольника:",((pp*(pp-b[i])*(pp-b[j])*(pp-b[k]))**(1/2)))