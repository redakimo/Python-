#coding:utf-8
def permuter(arg1,arg2):
    arg1,arg2=arg2,arg1
    return arg1,arg2

x=int(input("Enter x: "))
y=int(input("Enter y: "))
x,y=permuter(x,y)
print("la valeur x=",x)
print("la valeur y=",y)
