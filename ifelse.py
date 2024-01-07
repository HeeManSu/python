

print('Enter a number to check it is even or not')

num = int(input('Enter a no - '))

if num % 2 == 0: 
    print('Yes, the given number is even')
else :
    print("NO the number is odd") 
    
    
    
    
users = ['Kinshu', 'Anshu', 'Himanshu', 'Priyanshu']

if 'Kinshu' in users: 
    print('User Exist')
else : 
    print('Not exist')     



  # elif
marks = int(input('Enter the marks - '))

if marks < 50 : 
    print('Marks is smaller than 50')
elif marks > 50 : 
    print('Marks is greater than 50')
else : 
    print('Marks is 50')
    
    
# Nested IF Else

age = 19
voter_id = True

if age >= 18 : 
    if voter_id : 
        print('Yes you can vote')
    else:
        print('PLease apply for voter id first')
else: 
    print('HImanshu sharma')        
    
    
    
    # and 
    # or