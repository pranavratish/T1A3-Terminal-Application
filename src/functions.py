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

    confirm = input('Are you sure about this? You won\'t be able to get this information back once deleted.\nIf you are sure please press \'Y\':\n')    

    if confirm == 'Y':
        with open('src/storage.json', 'r') as s:
            d = json.load(s)
            d.pop(objDel)
        
        with open('src/storage.json', 'w') as s:
            s.write(json.dumps(d))
    else:
        return

def newUser():
    user = input('Please enter a unique username:\n')
    user = str(user)

    if user.isalpha() != True:
        print('That was an invalid username.\nPlease ensure that you use only letters in your username and try again.')
        return

    pass_ = input('Please enter a secure password:\n')
    pass_ = str(pass_)

    acc_u = {}
    acc_u['Username'] = user

    acc_p = {}
    acc_p['Password'] = pass_

    usr = open('src/users.json')
    usr_pass = json.load(usr)

    if usr_pass.count(acc_u) > 0:
        print('There is already a user with this name.\nPlease try again.')
        return
    else:
        with open('src/users.json', 'r') as u:
            l = json.load(u)
            l.append(acc_u)
            l.append(acc_p)

        with open('src/users.json', 'w') as u:
            u.write(json.dumps(l))


