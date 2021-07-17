from cryptography.fernet import Fernet
import json
import sys
from time import sleep

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

    with open('./storage.json', 'r') as s:
        d = json.load(s)
        d['Users'][check] = newEncrypt

    with open('./storage.json', 'w') as s:
        s.write(json.dumps(d))

    print(f'This is your key: {encrypted}\nIn 30 seconds you will return to the Profile menu.')

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

    with open('./storage.json', 'r') as s:
        d = json.load(s)
        d['Users'][check].update(newEncrypt)

    with open('./storage.json', 'w') as s:
        s.write(json.dumps(d))

    print(f'This is your key: {encrypted}\nIn 30 seconds you will return to the Profile menu.')

def validKey():
    key_input = input('Please enter the key associated with the information you are trying to access:\n')
    key_input = str(key_input)

    check = str(input('Please confirm Username:\n'))

    k = open('./storage.json')
    k_pass = json.load(k)

    if key_input in k_pass['Users'][check]:
        print(k_pass['Users'][check][key_input])
        print('You have 30 seconds to view this information. If you wish to see this information after the 30 seconds, access the Library again.')
    else:
        print('Invalid Key.\nPlease try again after 30 seconds.')

def edit():
    update = str(input('What would you like to change the information to?:\n'))
    reenter = str(input('Please enter your key again:\n'))

    check = str(input('Please confirm Username:\n'))

    with open('./storage.json', 'r') as s:
        d = json.load(s)
        if reenter in d['Users'][check]:
            d['Users'][check][reenter] = update
            print('Your information has been updated.')
        else:
            print('That key does not exist.')
    with open('./storage.json', 'w') as s:
        s.write(json.dumps(d))
    

def delete():
    objDel = input('Which key would you like to delete:\n')
    objDel = str(objDel)

    confirm = input('Are you sure about this? You won\'t be able to get this information back once deleted.\nIf you are sure please press \'Y\':\n')    

    check = input('Confirm Username:\n')

    if confirm == 'Y':
        with open('./storage.json', 'r') as s:
            d = json.load(s)
            if objDel in d['Users'][check]:
                d['Users'][check].pop(objDel)
            else:
                print('That key does not exist.')
        
        with open('./storage.json', 'w') as s:
            s.write(json.dumps(d))

        print('Your information has been deleted.')
    else:
        return

def newUser():
    user = str(input('Please enter a unique username (only letters of the alphabet are allowed):\n'))

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

    usr = open('./users.json')
    usr_pass = json.load(usr)

    if usr_pass.count(acc_u) > 0:
        print('There is already a user with this name.\nPlease try again.')
        return
    else:
        with open('./users.json', 'r') as u:
            l = json.load(u)
            l.append(acc_u)
            l.append(acc_p)

        with open('./users.json', 'w') as u:
            u.write(json.dumps(l))
        
        with open('./storage.json', 'r') as s:
            d = json.load(s)
            d['Users'].update(accStor)

        with open('./storage.json', 'w') as s:
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

    usr = open('./users.json')
    usr_new = json.load(usr)

    if usr_new.count(n_acc_u) > 0:
        print('There is already a user with this name.\nPlease try again.')
        return
    else:
        with open('./users.json', 'r') as u:
            l = json.load(u)
            l = [n_acc_u if i == c_acc_u else i for i in l]
        
        with open('./users.json', 'w') as u:
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

    with open('./users.json', 'r') as u:
        l = json.load(u)
        l = [n_acc_p if i == c_acc_p else i for i in l]
    
    with open('./users.json', 'w') as u:
        u.write(json.dumps(l))
    
    print('Your Password has been updated.')

def deleteAcc():
    user = str(input('Username:\n'))
    pas = str(input('Password:\n'))

    chU = {}
    chU['Username'] = user

    chP = {}
    chP['Password'] = pas

    usr = open('./users.json')
    usr_new = json.load(usr)

    if usr_new.count(chU) > 0 and usr_new.count(chP) > 0:
        conf = input('Are you sure you want to delete your account.\nYou will lose all saved encryptions. There is no way to recover your account.\nIf you wish to continue, confirm the termination of your account by pressing \'Y\':\n')
        if conf == 'Y':
            with open('./users.json', 'r') as u:
                l = json.load(u)
                l.pop(l.index(chU))
                l.pop(l.index(chP))

            with open('./users.json', 'w') as u:
                u.write(json.dumps(l))
            
            with open('./storage.json', 'r') as s:
                d = json.load(s)
                if user in d['Users']:
                    d['Users'].pop(user)
            
            with open('./storage.json', 'w') as s:
                s.write(json.dumps(d))
            
            print('Your account has been deleted.\nThe application will close in 5 seconds.')
            sleep(5)
            sys.exit()
        else:
            return
    else:
        print('This account cannot be deleted as it does not exist.')
        sleep(3)
        return

def h():    
    with open('../docs/help-documentation.txt', 'r') as help_:
        readHelp = help_.read()
        print(readHelp)
        print('In 2 minutes you will return to the Home screen.')