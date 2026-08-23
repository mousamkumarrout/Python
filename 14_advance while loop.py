#write a program to count the total number of digit
#input=12345
# num=int(input("enter a number"))

# count=0

# while num>0:
#     num=num//10
#     count=count+1
# print("Total digit=",count)


# num=int(input("enter a number"))
# count=0

# while num>0:
#     num=num//10
#     count=count+1
# print("total digit="count)



# num=int(input("enter a number"))
# count=0

# while num>0:
#     num=num//10
#     count=count+1
# print("Total digit=",count)



#write a program to sum the all numbers
# num=int(input("enter a num:"))
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum+digit
#     num=num//10
# print("sum of digit=",sum)


#write a program to reverse the num
# num=int(input("enter a number:"))
# reverse=0

# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10

# print("reverse number=",reverse)


#check palindrome number
#input=1234
#output=4321

# num=int(input("enter number"))
# original=num
# reverse=0

# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10

# if original==reverse:
#     print("palindrome number")
# else:
#     print("not a palindrome number")
     

#check armstrong number
#example=153=(1**1+5**5+3**3)
# num=int(input("enter a number"))
# original=num
# sum=0

# while num>0:
#     digit=num%10
#     sum=sum+(digit**3)
#     num=num//10

# if original==sum:
#     print("armstrong number")
# else:
#     print("not a armstrong num")


#print individual digits of a number
# num=int(input("enter a number:"))
# while num>0:
#     digit=num%10
#     print(digit)
#     num=num//10

#find the largest digit of a number
# num=int(input("enter a number:"))
# largest=0

# while num>0:
#     digit=num%10
#     if digit>largest:
#         largest=digit
#     num=num//10

# print("largest number=",largest)

########################################
#input-58219
# num=int(input("enter a number:"))
# smallest=9

# while num>0:
#     digit=num%10
#     if digit<smallest:
#         smallest=digit
#     num=num//10
# print("Smallest number=",smallest)

#write a program to calculate Xn using while loop
# x=int(input("enter a num:"))
# n=int(input("enter a num:"))

# result=1
# i=1

# while i<=n:
#     result=result*x
#     i=i+1
# print("answer=",result)

#print fibonnaci series
#each number is sum of the perious two numbers
#logic
#--------
# first num=0
# second number=1
# nxt number=first number+second number

n=int(input("enter number of trems:"))
a=0
b=1
count=1

while count<=n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count=count+1








