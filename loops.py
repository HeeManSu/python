

user_list = ['HImanshu', 'Kinshu', 'Anshu', 'Priyanshu']

for user in user_list:
    print(user);



# With dictionary

marks = {
    'Hindi': 45,
    'Maths': 43,
    'English': 34
}


# Both keys and value
for key, value in marks.items():
    print(f'Subject is: {key}')
    print(f'marks is {value}')
    
# Only keys
for subject in marks.keys():
    print(f'Subject is: {subject}')


# Only values
for marks in marks.values():
    print(f'marks is: {marks}')


for num in range (1, 10): 
    print(num)
    
    
# while loop

user_input = ""
while user_input != 'q':
    user_input = input('Enter a no. or q for quite - ')
    if user_input.isdigit() :
        if int(user_input) % 2 == 0:
            print('Yes the no. is even')
        else : 
            print('No. is odd')    


# break  - to stop the loop
# continue - to stop current iteration of loop and start next iteration

num =[10, 20, 499, 23, 25, 29, 64]

for n in num: 
    if n == 499 :
        continue;
    print(n)    
    
    
    
for n in num: 
    if n == 499 :
        break;
    print(n)    
  