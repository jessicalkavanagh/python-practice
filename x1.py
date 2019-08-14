# Task 2 EX 1:
# def pick_largest_num(x, y):
#     if x == y: 
#         print('The numbers you entered are the same.')

#     elif x > y: 
#         print(x)

#     else: 
#         print(y)

# pick_largest_num(6, 3)
# pick_largest_num(34, 48)
# pick_largest_num(123, 123)


# Task 2 EX 2:
# def parameter(x):
#     if x == 5:
#         print('The integer is exactly 5.')

#     elif x < 5: 
#         print('False')

#     else: 
#         print('True')

# parameter(10)
# parameter(1)
# parameter(5)


# Task 2 EX 3:
# def message(y):
#     if y == ('hayley is awesome!'):
#         print('True')

#     else: 
#         print('false')

# message(hayley is awesome!)
# message(hayley is awesome)


# Task 2 EX 4:
# def user(name,age):
#     if age < 30:
#         print (name, 'is', age, 'years old')
#     elif age > 30:
#         print (name, 'is at level', age)
#     else:
#         print (name, 'is', age, '!!!')

# user('Hayley',22)
# user('Sally',52)
# user('Josh',30)

# Task 3 EX 1:
# name = 'Hayley'
# age = '22'

# message='{name} is {age} years old.' .format(name=name, age=age)
# print(message)

# # Task 3 EX 2:
# def capital(x,y):
#     if x.lower() == y.lower():
#         print("They are the same.")
#     else:
#          print(":(")

# capital('Marc LOVES hanging off the side of buildings','marc loves hanging off the side of buildings')
# capital('James is writing his FIRST react app','james is writing a react app')


# Task 4 ex 1:
# try:
#     num1 = int(input('Please enter a number: '))
#     print(num1*10)

# except: 
#     print('Woops! That\'s not an integer, try again!')


# Task 4 ex 2:
def input(x):
    if isinstance(x, str):
        print (x)
        
    elif isinstance(x, int):
        print ('Woops! That\'s an integer, try again!')

    elif isinstance(x, float):
        print ('Woops! That\'s a float, try again!')

input(12)
input('cats')
input(3.4)

def check():
    while True:
        x=input('give me a word? ')
        try:
            int(x)
            print('Woops! That\'s an integer, try again!') 
        except ValueError:
            try:
                float(x)
                print('Woops! That\'s an float, try again!') 
            except ValueError:
                print(x)
                break
check()
