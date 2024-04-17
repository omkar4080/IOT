

n=int(input("enter the 4 digit number:"))
a = int(n/10)
b = int(n/10%10)
c = int(n/100%10)
d = int(n/1000)
print(d,c,b,a,'\n')
print(f"{n} = {d*1000} + {c*100} + {b*10} + {a} \n")
print(a ,b,c,d,'\n')