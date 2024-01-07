
def gretting() :
    print("Hello Himanshu")
    

gretting();


def gretting(user_name, age):
    print(f'Hello {user_name} and age {age}')

gretting('Himanshu', 23);


# All the values are considered as a list. 

def greeting(user_name, *hobbies):
    print(f'{user_name} hobbies are - ')
    for i in hobbies :
        print(i)


greeting('Himanshu', 'singing', 'dancing', 'playing')


# When we use two star ** input is given as dictionary.
 
def greeting(user_name, **user_info) : 
    print(f'Hello {user_name}')
    
    for key, value in user_info.items():
        print(f'{key} is {value}')


greeting('Himanshu', age = 18, city = 'Delhi', email = "ragjusdfa")


# return result

def add(num1, num2) :
    return num1 + num2

result  = add(10, 29)
print(result)