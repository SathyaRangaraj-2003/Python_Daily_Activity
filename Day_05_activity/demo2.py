#split()
x,y=input("enter 2 num: ").split(' ')
print(x,y)


#int,float
#soln 1
v1,v2=5,5.0
print(f"int v1:{v1} \nfloat v2:{v2}")
#soln 2
v1,v2=input("enter int num:"),input("enter float num")
print(f"int v1:{v1} \nfloat v2:{v2}")
#soln 3
v1,v2=input("enter 2 num: ").split(',')
print(f"int v1:{v1} \nfloat v2:{v2}")

#comma()
x,y,z=input("enter 3 num: ").split(',')
print(f'x:{x}\ny:{y}\nz:{z}')

# type casting to integer using map:
v1,v2,v3,v4,v5 = map(int,input("enter five nums: ").split(','))
print(f'v1:{v1}\nv2:{v2}\nv3:{v3}\nv4:{v4}\nv5:{v5}')