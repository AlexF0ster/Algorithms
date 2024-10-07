data=[4,56,72,34,900002,274,15]

sorted=False
while sorted==False:
    sorted=True
    for i in range (len(data)-1):
        if data[i]>data[i+1]:
            temp=data[i+1]
            data[i+1]=data[i]
            data[i]=temp
            sorted=False

print(data)