from random import randint
secret_num=randint(1,100)
user_num=-1
try_count=1

while user_num!=secret_num:
    print('%d try: '%try_count,end='')
    user_num=int(input())
    if user_num<secret_num:
        print('Too less')
    elif user_num>secret_num:
        print('Too much')
    else:
        print('You guessed it!')
    try_count+=1