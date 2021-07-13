from cryptography.fernet import Fernet
import json

def secure():
    key = Fernet.generate_key()

    info = input('What would you like to encrypt?:\n')
    data = info.encode()

    f = Fernet(key)
    encrypted = f.encrypt(data)

    s_encrypted = encrypted.decode()

    with open('src/storage.json', 'r') as s:
        d = json.load(s)
        d[s_encrypted] = info

    with open('src/storage.json', 'w') as s:
        s.write(json.dumps(d))

    print(encrypted)

def validKey():
    key_input = input('Please enter the key associated with the information you are trying to access:\n')
    key_input = str(key_input)

    k = open('src/storage.json')

    k_pass = json.load(k)

    if key_input in k_pass:
        print(k_pass[key_input])
    else:
        print('Invalid Key.\nPlease Try Again.')

def edit():
    update = input('What would you like to change the information to?:\n')
    reenter = input('Please enter your key again:\n')
    update = str(update)
    reenter = str(reenter)

    with open('src/storage.json', 'r') as s:
        d = json.load(s)
        d[reenter] = update
    
    with open('src/storage.json', 'w') as s:
        s.write(json.dumps(d))

def delete():
    objDel = input('Which key would you like to delete:\n')
    objDel = str(objDel)

    with open('src/storage.json', 'r') as s:
        d = json.load(s)
        d.pop(objDel)
    
    with open('src/storage.json', 'w') as s:
        s.write(json.dumps(d))
