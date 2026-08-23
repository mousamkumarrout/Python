#anagram
# str1="listen"
# str2="silent"

# str1=input("enter first string:")
# str2=input("enter second string:")

# if sorted(str1) == sorted(str2):
#     print("strings are anagram")
# else:
#     print("strings are not anagram")




#pangram
#The quick brown fox jumps over the lazy dog
# sen=input('enter a string:').lower()
# alphabet="abcdefghijklmnopqrstuvwxyz "
# temp=True
# for i in sen:
#     if i not in alphabet:
#         temp=False
#         break
# if temp==True:
#     print("sen is pangram")
    
# else:
#     print("sen is not a pangram")

     



#isogram
#word=machine
#background
#python


# sen=input("Enter a word: ").lower()
# temp = True
# for i in sen:
#     if sen.count(i) > 1:
#         temp = False
#         break
# if temp==True:
#     print(sen, "is an isogram.")
    
    
# else:
#     print(sen, "is not an isogram.")


#find non repating character

# sen=input("enter a string:")
# for i in sen:
#     if sen.count(i)==1:
#         print(i)


# word= "surendra"

# for i in word:
#     if word.count(i) == 1:
#         print(i)



# repeating
# sen=input("enter a string:")
# for i in sen:
#     if sen.count(i)>1:
#         print(i)


# word= "mousam"

# for i in word:
#     if word.count(i) > 1:
#         print(i)



################################################

#find first non repeating charecter
# sen=input("enter a string:")
# for i in sen:
#     if sen.count(i)==1:
#         print(i)
#         break

# word="surendra"

# for i in word:
#     if word.count(i)==1:
#         print(i)
        # break

#find first repeating character
# sen=input('enter a string:')
# for i in sen:
#     if sen.count(i)>1:
#         print(i)
#         break

# word="mousam"
# for i in word:
#     if word.count(i)>1:
#         print(i)
#         break




#highest repeating character













#password validation
#minimum 8 character
#one uppercase
#one lowercase
#one digit
#one special one
# password=input("enter your password:")
# uppercase=0
# lowercase=0
# digit=0
# special=0
# for i in password:
    
#     if i.isupper():
#         uppercase=uppercase+1
#     elif i.islower():
#         lowercase=lowercase+1
#     elif i.isdigit():
#         digit=digit+1
#     elif i in "@#$%":
#         special=special+1
# if len (password) >= 8 and uppercase >= 1 and lowercase >= 1 and digit >= 1 and special >= 1:
#     print("password is valid")
# else:
#     print("password is not valid")


        
# d={}
# a=1
# for i in range(2,11):
#     for a in i:
#         x=i*a
#     d[i]=x
# print(d)




# d={}
# for i in range(2,11):
#     d[i]=[i*j for j in range(11,11)]
# print(d)

# d={}
# a=1
# for i in range(2,11):
#     for a in i:
#         x=a*i
#         a+1
#         d[i]=x 
# print(d)  

        

# d={
    
# }


# for i in range(2,11,1):
#     d[i]=[i*j for j in range(1,11,1)]

# for i in d:
#     print(i,'--->',d[i])




# books={}
# while True:
#     name=input('Enter book name : ')
#     author=input('Enter author name : ')
#     price=int(input('Enter the book price : '))
#     publisher=input('Enter publisher name : ')
#     books[name]={
#         'author':author,
#         'price':price,
#         'publisher':publisher
#     }
        
#     choice=input('Do you want to add more book [yes/no] : ').lower()
#     if choice=='no':
#         break


# for i in books:
#     print('*'*30)
#     print(f'Book Name : {i}')
#     for j in books[i]:
#         print(f'Author Name {books[i]['author']}')
#         print(f'Price is : {books[i]['price']}')
#         print(f'Publisher is {books[i]['publisher']}')
#         print('*'*30)

    
        
# books = {}

# while True:
#     name = input("Enter book name : ")
#     author = input("Enter author name : ")
#     price = int(input("Enter the book price : "))
#     publisher = input("Enter publisher name : ")

#     books[name] = {
#         "author": author,
#         "price": price,
#         "publisher": publisher
#     }

#     choice = input("Do you want to add more book [yes/no] : ").lower()

#     if choice == "no":
#         break

# Display Book Details
# for book in books:
#     print("*" * 30)
#     print(f"Book Name : {book}")
#     print(f"Author Name : {books[book]['author']}")
#     print(f"Price : {books[book]['price']}")
#     print(f"Publisher : {books[book]['publisher']}")
#     print("*" * 30)





students = {}

while True:
    print("Press")
    print("1. Add Student")
    print("2. Display all Student")
    print("3. Search Student")
    print("4. Get Student Total Mark")
    print("5. Display Total Number of Students")
    


    choice = int(input("Select any option : "))

    if choice == 1:
        name = input("Enter Name : ")
        redg_no = input("Enter Regd No : ")
        course = input("Enter Course : ")

        phy = int(input("Enter Physics Mark : "))
        chem = int(input("Enter Chemistry Mark : "))
        math = int(input("Enter Math Mark : "))
        bio = int(input("Enter Biology Mark : "))
        eng = int(input("Enter English Mark : "))
        odia = int(input("Enter Odia Mark : "))

        at = input("Enter At : ")
        post = input("Enter Post : ")
        district = input("Enter District : ")

        students[redg_no] = {
            "name": name,
            "course": course,
            "mark": {
                "phy": phy,
                "chem": chem,
                "math": math,
                "bio": bio,
                "eng": eng,
                "odia": odia
            },
            "address": {
                "at": at,
                "post": post,
                "district": district
            }
        }

        print(name, "Inserted Successfully")

    elif choice == 2:
        print(students)

    elif choice == 3:
        redg_no = input("Enter Regd No : ")
        print(students.get(redg_no))

    elif choice == 4:
        redg_no = input("Enter Regd No : ")

        total = 0
        for mark in students[redg_no]["mark"].values():
            total = total + mark

        print("Total Marks =", total)

    
    elif choice == 5:
        print("Total Number of Students :", len(students))
        break

    



# students = {}

# while True:
#     print("\n========== STUDENT MENU ==========")
#     print("1. Add Student")
#     print("2. Display All Student")
#     print("3. Search Student")
#     print("4. Get Student Total Mark")
#     print("5. Display Topper Student")
#     print("6. Exit")

#     choice = int(input("Select any option : "))

#     if choice == 1:
#         name = input("Enter Name : ")
#         redg_no = input("Enter Regd No : ")
#         course = input("Enter Course : ")

#         phy = int(input("Enter Physics Mark : "))
#         chem = int(input("Enter Chemistry Mark : "))
#         math = int(input("Enter Math Mark : "))
#         bio = int(input("Enter Biology Mark : "))
#         eng = int(input("Enter English Mark : "))
#         odia = int(input("Enter Odia Mark : "))

#         at = input("Enter At : ")
#         post = input("Enter Post : ")
#         district = input("Enter District : ")

#         students[redg_no] = {
#             "name": name,
#             "course": course,
#             "mark": {
#                 "phy": phy,
#                 "chem": chem,
#                 "math": math,
#                 "bio": bio,
#                 "eng": eng,
#                 "odia": odia
#             },
#             "address": {
#                 "at": at,
#                 "post": post,
#                 "district": district
#             }
#         }

#         print(f"\n{name} inserted successfully.")

#     elif choice == 2:
#         if len(students) == 0:
#             print("No Student Record Found.")
#         else:
#             for regd_no, details in students.items():
#                 print("\n------------------------------")
#                 print("Registration No :", regd_no)
#                 print("Name            :", details["name"])
#                 print("Course          :", details["course"])

#                 print("\nMarks")
#                 for subject, mark in details["mark"].items():
#                     print(subject, ":", mark)

#                 print("\nAddress")
#                 print("At       :", details["address"]["at"])
#                 print("Post     :", details["address"]["post"])
#                 print("District :", details["address"]["district"])

#     elif choice == 3:
#         regd_no = input("Enter Regd No : ")

#         if regd_no in students:
#             details = students[regd_no]

#             print("\nStudent Details")
#             print("------------------------------")
#             print("Name :", details["name"])
#             print("Course :", details["course"])

#             print("\nMarks")
#             for subject, mark in details["mark"].items():
#                 print(subject, ":", mark)

#             print("\nAddress")
#             print("At :", details["address"]["at"])
#             print("Post :", details["address"]["post"])
#             print("District :", details["address"]["district"])

#         else:
#             print("Student Not Found.")

#     elif choice == 4:
#         regd_no = input("Enter Regd No : ")

#         if regd_no in students:
#             total = 0

#             for mark in students[regd_no]["mark"].values():
#                 total = total + mark

#             print("Total Marks :", total)
#             print("Percentage :", total / 6)
#         else:
#             print("Student Not Found.")

#     elif choice == 5:
#         if len(students) == 0:
#             print("No Student Record Found.")
#         else:
#             topper_regd = ""
#             highest_total = 0

#             for regd_no, details in students.items():
#                 total = 0

#                 for mark in details["mark"].values():
#                     total = total + mark

#                 if total > highest_total:
#                     highest_total = total
#                     topper_regd = regd_no

#             topper = students[topper_regd]

#             print("\n========== TOPPER STUDENT ==========")
#             print("Registration No :", topper_regd)
#             print("Name            :", topper["name"])
#             print("Course          :", topper["course"])

#             print("\nMarks")
#             for subject, mark in topper["mark"].items():
#                 print(subject, ":", mark)

#             print("\nAddress")
#             print("At       :", topper["address"]["at"])
#             print("Post     :", topper["address"]["post"])
#             print("District :", topper["address"]["district"])

#             print("\nTotal Marks :", highest_total)
#             print("Percentage :", highest_total / 6)

#     elif choice == 6:
#         print("Thank You...")
#         break

#     else:
#         print("Invalid Choice.")

        
    


tudents = {}

while True:
    print("Press")
    print("1. Add Student")
    print("2. Display all Student")
    print("3. Search Student")
    print("4. Get Student Total Mark")
    print("5. Display Total Number of Students")
    print("6. check pass/fail students")
    


    choice = int(input("Select any option : "))

    if choice == 1:
        name = input("Enter Name : ")
        redg_no = input("Enter Regd No : ")
        course = input("Enter Course : ")

        phy = int(input("Enter Physics Mark : "))
        chem = int(input("Enter Chemistry Mark : "))
        math = int(input("Enter Math Mark : "))
        bio = int(input("Enter Biology Mark : "))
        eng = int(input("Enter English Mark : "))
        odia = int(input("Enter Odia Mark : "))

        at = input("Enter At : ")
        post = input("Enter Post : ")
        district = input("Enter District : ")

        students[redg_no] = {
            "name": name,
            "course": course,
            "mark": {
                "phy": phy,
                "chem": chem,
                "math": math,
                "bio": bio,
                "eng": eng,
                "odia": odia
            },
            "address": {
                "at": at,
                "post": post,
                "district": district
            }
        }

        print(name, "Inserted Successfully")

    elif choice == 2:
        print(students)

    elif choice == 3:
        redg_no = input("Enter Regd No : ")
        print(students.get(redg_no))

    elif choice == 4:
        redg_no = input("Enter Regd No : ")

        total = 0
        for mark in students[redg_no]["mark"].values():
            total = total + mark

        print("Total Marks =", total)

    
    elif choice == 5:
        print("Total Number of Students :", len(students))

    elif choice == 6:
        redg_no = input("enter redg no :")
        
        break

    
        
    
    
