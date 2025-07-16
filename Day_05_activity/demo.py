# #print() activity
# print("sum is:",2+3)
# print("greater is:",2>3)
# print("greater is:",int(2>3))
# #newline(\n)
# print("Hello, \nWorld")

# #custom separators:(sep) 
# print("2025","07","16",sep="-")

# # custom ending:(end)
# print("sathya",end="...")
# print("rangaraj")

# # f-String:
# name="sathya"
# marks=90
# print(f"name:{name} \nmarks:{marks}")

# #ascii
# print(ord('A')) 
# print(chr(97)) 

# #list
# mixed_sathya=[10,False,20,"sathya",40.0,None]

#list()
# letters=list("hello")
# result=""
# result+=letters[0].upper()
# result+=letters[1].upper()
# result+=letters[2].upper()
# result+=letters[3].upper()
# result+=letters[4].upper()
# print(result)

# print(*list('hello'.upper()))


# a=[1,2,3,4]
# print(a)
# print(*a)


# print(*list('hello'.upper()))

# a=list("hello")
# for char in a:
#     print(chr(ord(char)-32),end="")
    

# words=["geeks","for","geeks"]
# for val in words:
#     str=""
#     for char in val:
#         str+=chr(ord(char)-32)
#     print(" ".join(str))

# words=["geeks","for","geeks"]
# num=[123,287,9001]
# print(str(num[2])[2])

# try :
# num=[123,287,9001]
# print(str(num[2])[2])
# # print(str(num[2])[2])


#concatenation
# a=[1,2,3]
# b=[5,6]
# c=a+b
# print(c)
# print(type(c))

#
# a=["hi","hello"]*3
# print(a)

#membership operators (in,not in)
# a=["hi","hello"]
# print("yellow" in a)


# methods
# try :
# num=[123,287,9001]
# num.append(30)

# #shallow copy
# a=[1,2,3]
# b=a
# b[0]=100
# print(a)
# print(b)

# a=[1,2,3]
# b=a.copy()
# b[0]=100
# print(a)
# print(b)


# a=[1,2,3]
# b=[4,5]

name=["alice","bob"]
# print(name[name.index("alice")].index('i'))

print(name.pop(3))

