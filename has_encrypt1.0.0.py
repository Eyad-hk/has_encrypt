#!/usr/bin/python
# -*- coding: utf-8 -*- 
#Script Encryption

print('''
        +=======================================+
        |.*..*.Prince Cham.......hashlib..*..*. |
        +---------------------------------------+
        |.*...*.......Grey Hat Hackers....*..*..|
        +---------------------------------------+
''')

import hashlib
while True:
    print('\n1)md5\n2)has1\n3)has512\n4)sha224\n5)sha256\n6)sha384\n99)exit')
    user=input('Enter the type of Hash :')
    user1=input('Enter the pass to encrypt :')
    if user=='1':
        print(hashlib.md5(user1.encode()).hexdigest())
    elif user=='2':
        print(hashlib.sha1(user1.encode()).hexdigest())
    elif user=='3':
        print(hashlib.sha512(user1.encode()).hexdigest())
    elif user=='4':
        print(hashlib.sha224(user1.encode()).hexdigest())
    elif user=='5':
        print(hashlib.sha256(user1.encode()).hexdigest())
    elif user=='6':
        print(hashlib.sha384(user1.encode()).hexdigest())
    elif user or user1=='99':
        break
    else:
        print('There is no')




