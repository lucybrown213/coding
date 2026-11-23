number=input("Enter an integer number:")
number=int(number)
if number > 0:
    if number%2 ==0:
        print(number,'is a postive even number.')
    else:
         print(number,'is postive odd number.')
elif number < 0:
    if number%2 ==0:
        print(f'{number}is a negative even.')
    else:
        print(f'{number}is a negative odd number.')
else:
    if number == 0:
        print(number,'is an even number.')
        
print('program finished.')