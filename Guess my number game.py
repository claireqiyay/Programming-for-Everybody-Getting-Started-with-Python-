import random
secret_number = random.randint(1,100)
while True:
    n = input('Guess the secret number between 1 and 100: ')
    n = int(n)
    if n == secret_number:
        break
    if n - 2 == secret_number or n + 2 == secret_number or n + 1 == secret_number or n -1 == secret_number:
        print('So close!')
    elif n > secret_number:
        print('That is too high')
    else:
        print('That is too low')

print('That is correct! Good job and thanks for playing!')
