# nested function
def outer_fun(): 
    print('inside outer fun')
    def inner_fun():
        print('inside inner fun')
        def inner_inner_fun():
            print('Inside inner inner fun')

inner_fun()
outer_fun()
inner_inner_fun()





def outer_fun():
    print('inside outer fun')
    
    def inner_fun():
        print('inside inner fun')
        def inner_inner_fun():
            print('Inside inner inner fun')
    inner_fun()
    inner_inner_fun()

outer_fun()




def outer_fun():
    print('inside outer fun')
    def inner_fun():
        print('inside inner fun')
        def inner_inner_fun():
            print('Inside inner inner fun')
        inner_inner_fun()
    inner_fun()
outer_fun()





def outer_fun():
    print('inside outer fun')
    inner_fun()
    def inner_fun():
        inner_inner_fun()
        print('inside inner fun')
        def inner_inner_fun():
            print('inside inner inner fun')
outer_fun()




# def fun(a, b, c):
#     print(a+b+c)


# fun(10, 20, 30)
# fun(10, 20)  # fun() missing 1 required positional argument: 'c'

# fun(30)  # fun() missing 2 required positional arguments: 'b' and 'c

# fun()  # TypeError: fun() missing 3 required positional arguments: 'a', 'b', and 'c'

# fun([22, 23, 999])  

# TypeError: fun() missing 2 required positional arguments: 'b' and 'c'


# def fun(a, b, c):
#     print(a+b+c)

# fun([10, 20, 30], [10, 20], [90])

















# def fun(a, b, c):
#     print(a+b+c)
# fun((), [], {})






# def fun():
#     print('hello python ! how r u ?')


# fun()
# fun(10)  # TypeError: fun() takes 0 positional arguments but 1 was given

# fun(10, 20)  # TypeError: fun() takes 0 positional arguments but 2 were given

# fun(None)

# fun(0)  # TypeError: fun() takes 0 positional arguments but 1 was given

# fun(False)  # TypeError: fun() takes 0 positional arguments but 1 was given












# def cal(a, b, c):
#     print(a+b*c)

# cal(a=5, b=6, c=7)  # 47
# cal(5,c=7,b=6) 
# cal(5,6,c=7)
# cal(5, b=6, c=7)
# cal(5, c=6, b=7)

# cal(5, a=6, b=7)  # TypeError: cal() got multiple values for argument 'a'