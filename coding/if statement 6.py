#2026/11/3
number=input("guess the secret number:")
number=float(number)
if number==2:
    print("bingo!correct answer")
elif number<=2:
    print("close enough to the correct answer")
else:
    print("not close enough")