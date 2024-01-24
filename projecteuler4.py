a=[]
for i in range(100,1000):
    for x in range(100,1000):
       b=str(i*x)
       if b[::-1]==str(i*x):
          a.append(i*x)
print(max(a))        

        