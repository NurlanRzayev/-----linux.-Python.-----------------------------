extensions=['png','jpg','jpeg','gef','svg']

fname=input().split('.')

if len(fname)>=2:
    fname_ext=fname[-1].lower()
    if fname_ext in extensions:
        print('Yes')
    else:
        print('No')
else:
    print('The fname has no extensions')