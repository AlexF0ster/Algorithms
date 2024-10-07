data=[4,56,72,34,900002,274,15]


for i in range (1,len(data)):
    position=i
    print(data[position-1])
    while data[position]<data[position-1] and position>0:
        temp=data[position-1]
        data[position-1]=data[position]
        data[position]=temp
        position=position-1

print(data)