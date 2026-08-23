# for i in range(1,6):
#     print(i)

# for i in range(1,6):
#     print(i)


# for i in range(5):
#     print(i)


# for i in range(5):
#     print(i,end='')

# for i in range(1,11,2):
#     print(i)

# for i in range(1,11,2):
#     print(i,end='')

#print your name 5 times
# for i in range(5):
#     print("mousam",end='')

#print numbers from 1 to 10
# for i in range(1,10):
#     print(i)

#print all even numbers between 2 to 21
# for i in range(2,21,2):
#     print(i)

# l=[23,33,4,11,16,75,42]
# for i in l:
#     print(i)


#print all the even numbers
# l=[23,33,4,11,16,75,42]
# for i in l:
#     if i%2==0:
        # print(i)

#print sum of the element from the list

# l=[23,33,4,11,16,75,42]
# sum=0
# for i in l:
#     sum=sum+i
#     print(sum)

#print all the str from the list
# l=['surendra',12,13,14.56,'mousam']
# for i in l:
#     if type(i)==str:
#         print(i)


#print all  int from the str
# l=['surendra',12,13,14.56,'mousam']
# for i in l:
#     if type(i)==int:
#         print(i)

#print all float from the str
# l=['surendra',12,13,14.56,'mousam']
# for i in l:
#     if type(i)==float:
#         print(i)

#print lenght of name
# name='surendra kumar panda'
# i=0
# l=len(name)
# while i<l:
#     print(name[i])
#     i=i+1

# name='mousam kumar rout'
# i=0
# l=len(name)
# while i<l:
#     print(name[i])
#     i=i+1


#print the name must end with 'a'
# l=['surendra','rahul','priaynka','zini','jack','scoot']

# for i in l:
#     if i[-1]=='a':
#         print(i)

# l=['surendra','mousam','chinmaya','priyanka','zini']

# for i in l:
#     if i[-1]=='a':
#         print(i)


# l=['surendra','mousam','chinmaya','priyanka','zini']

# for i in l:
#     if i[-1]=='m':
#         print(i)




l=['surendra','mousam','chinmaya','priyanka','zini']
for i in l:
    if i[-1]==i:
        print(i)


#print odd numbers from 1 to 20
# for i in range(1,21,2):
#     print(i)



#print numbers from 10 to 1 in reverse number
# for i in range(10,0,-1):
#     print(i)


#print multipication of given number
# num=int(input("enter a number:"))

# for i in range(1,11):
#     print(f'{num}x{i}={num*i}')


#find the sum of the n natiral number
# n=int(input("enter a number:"))
# sum=0

# for i in range(1,n+1):
#     sum=sum+1

# print("sum=",sum)

#find sum of the all numbers between m to n
m=int(input("enter m value:"))
n=int(input("enter n value:"))

sum=0

for i in range(m,n+1):
    sum=sum+1

print("sum=",sum)
    







