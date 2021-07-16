from cryptography.fernet import Fernet
import json

def firstEncrypt():
    key = Fernet.generate_key()

    info = input('What would you like to encrypt?:\n')
    data = info.encode()

    f = Fernet(key)
    encrypted = f.encrypt(data)

    s_encrypted = encrypted.decode()

    newEncrypt = {}
    newEncrypt[s_encrypted] = info

    check = str(input('Please confirm Username:\n'))

    with open('src/storage.json', 'r') as s:
        d = json.load(s)
        d['Users'][check] = newEncrypt

    with open('src/storage.json', 'w') as s:
        s.write(json.dumps(d))

    print(f'This is your key: {encrypted}')

def secure():
    key = Fernet.generate_key()

    info = input('What would you like to encrypt?:\n')
    data = info.encode()

    f = Fernet(key)
    encrypted = f.encrypt(data)

    s_encrypted = encrypted.decode()

    newEncrypt = {}
    newEncrypt[s_encrypted] = info

    check = str(input('Please confirm Username:\n'))

    with open('src/storage.json', 'r') as s:
        d = json.load(s)
        d['Users'][check].update(newEncrypt)

    with open('src/storage.json', 'w') as s:
        s.write(json.dumps(d))

    print(f'This is your key: {encrypted}')

def validKey():
    key_input = input('Please enter the key associated with the information you are trying to access:\n')
    key_input = str(key_input)

    check = str(input('Please confirm Username:\n'))

    k = open('src/storage.json')
    k_pass = json.load(k)

    if key_input in k_pass['Users'][check]:
        print(k_pass['Users'][check][key_input])
    else:
        print('Invalid Key.\nPlease Try Again.')

def edit():
    update = str(input('What would you like to change the information to?:\n'))
    reenter = str(input('Please enter your key again:\n'))

    check = str(input('Please confirm Username:\n'))

    with open('src/storage.json', 'r') as s:
        d = json.load(s)
        d['Users'][check][reenter] = update
    
    with open('src/storage.json', 'w') as s:
        s.write(json.dumps(d))
    
    print('Your information has been updated.')

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
        
        print('Your information has been deleted.')
    else:
        return

def newUser():
    user = str(input('Please enter a unique username:\n'))

    if user.isalpha() != True:
        print('That was an invalid username.\nPlease ensure that you use only letters in your username and try again.')
        return

    pass_ = input('Please enter a secure password:\n')
    pass_ = str(pass_)

    acc_u = {}
    acc_u['Username'] = user

    acc_p = {}
    acc_p['Password'] = pass_

    accStor = {}
    accStor[user] = 0

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
        
        with open('src/storage.json', 'r') as s:
            d = json.load(s)
            d['Users'].update(accStor)

        with open('src/storage.json', 'w') as s:
            s.write(json.dumps(d))

        print('Your account has been created.')

def editUser():
    currU = input('Please enter your current Username:\n')
    currU = str(currU)

    userNew = input('What would you like to change your name to?:\n')
    userNew = str(userNew)

    if userNew.isalpha() != True or currU.isalpha() != True:
        print('That was an invalid username.\nPlease ensure that you use only letters in your username and try again.')
        return

    c_acc_u = {}
    c_acc_u['Username'] = currU

    n_acc_u = {}
    n_acc_u['Username'] = userNew

    usr = open('src/users.json')
    usr_new = json.load(usr)

    if usr_new.count(n_acc_u) > 0:
        print('There is already a user with this name.\nPlease try again.')
        return
    else:
        with open('src/users.json', 'r') as u:
            l = json.load(u)
            l = [n_acc_u if i == c_acc_u else i for i in l]
        
        with open('src/users.json', 'w') as u:
            u.write(json.dumps(l))
        
        print('Your Username has been updated.')

def editPass():
    currP = input('Please enter your current Password:\n')
    currP = str(currP)

    newPass = input('What would you like to change your Password to?:\n')
    newPass = str(newPass)

    c_acc_p = {}
    c_acc_p['Password'] = currP

    n_acc_p = {}
    n_acc_p['Password'] = newPass

    with open('src/users.json', 'r') as u:
        l = json.load(u)
        l = [n_acc_p if i == c_acc_p else i for i in l]
    
    with open('src/users.json', 'w') as u:
        u.write(json.dumps(l))
    
    print('Your Password has been updated.')

def deleteAcc():
    user = str(input('Username:\n'))
    pas = str(input('Password:\n'))

    chU = {}
    chU['Username'] = user

    chP = {}
    chP['Password'] = pas

    usr = open('src/users.json')
    usr_new = json.load(usr)

    if usr_new.count(chU) > 0 and usr_new.count(chP) > 0:
        conf = input('Are you sure you want to delete your account.\nYou will lose all saved encryptions. There is no way to recover your account.\nIf you wish to continue, confirm the termination of your account by pressing \'Y\':\n')
        if conf == 'Y':
            with open('src/users.json', 'r') as u:
                l = json.load(u)
                l.pop(l.index(chU))
                l.pop(l.index(chP))

            with open('src/users.json', 'w') as u:
                u.write(json.dumps(l))
            
            print('Your account has been deleted.')
        else:
            return
    else:
        print('This account cannot be deleted as it does not exist.')
        return    

def login():
    user = str(input('Username:\n'))
    pas = str(input('Password:\n'))

    chU = {}
    chU['Username'] = user

    chP = {}
    chP['Password'] = pas

    usr = open('src/users.json')
    usr_new = json.load(usr)

    if usr_new.count(chU) > 0 and usr_new.count(chP) > 0:
        print(f'Welcome User: {user}')
        return

def h():    
    with open('docs/help-documentation.md', 'r') as help_:
        readHelp = help_.read()
        print(readHelp)