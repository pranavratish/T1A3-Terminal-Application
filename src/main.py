import os
import sys
from time import sleep
import json
from cryptography.fernet import Fernet
from simple_term_menu import TerminalMenu
import methods

def start():
    main_menu_title = ' Welcome to Black-Box\n'
    main_menu_options = [
        'Login',
        'New User',
        'Help',
        'Exit']
    main_menu_cursor = '> '
    main_menu_c_style = ('fg_cyan', 'bold')
    main_menu_theme = ('bg_black', 'fg_yellow')
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_options,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_c_style,
        menu_highlight_style=main_menu_theme,
        clear_screen=True
    )

    profile_menu_title = ' Profile\n'
    profile_menu_options = [
        'Encryption',
        'Encryption Library',
        'Edit Profile',
        'Exit to Home'
    ]
    profile_menu_cursor = '> '
    profile_menu_c_style = ('fg_cyan', 'bold')
    profile_menu_theme = ('bg_black', 'fg_yellow')
    profile_menu_exit = False

    profile_menu = TerminalMenu(
        menu_entries=profile_menu_options,
        title=profile_menu_title,
        menu_cursor=profile_menu_cursor,
        menu_cursor_style=profile_menu_c_style,
        menu_highlight_style=profile_menu_theme,
        clear_screen=True
    )

    encLib_menu_title = ' Encryption Library\n'
    encLib_menu_options = [
        'Edit',
        'Delete',
        'Exit to Profile'
    ]
    encLib_menu_cursor = '> '
    encLib_menu_c_style = ('fg_cyan', 'bold')
    encLib_menu_theme = ('bg_black', 'fg_yellow')
    encLib_menu_exit = False

    encLib_menu = TerminalMenu(
        menu_entries=encLib_menu_options,
        title=encLib_menu_title,
        menu_cursor=encLib_menu_cursor,
        menu_cursor_style=encLib_menu_c_style,
        menu_highlight_style=encLib_menu_theme,
        clear_screen=True
    )

    eProfile_menu_title = ' Edit Profile\n'
    eProfile_menu_options = [
        'Edit Username',
        'Edit Password',
        'Delete Account (In case of successful termination, the application will close)',
        'Return to Profile'
    ]
    eProfile_menu_cursor = '> '
    eProfile_menu_c_style = ('fg_cyan', 'bold')
    eProfile_menu_theme = ('bg_black', 'fg_yellow')
    eProfile_menu_exit = False

    eProfile_menu = TerminalMenu(
        menu_entries=eProfile_menu_options,
        title=eProfile_menu_title,
        menu_cursor=eProfile_menu_cursor,
        menu_cursor_style=eProfile_menu_c_style,
        menu_highlight_style=eProfile_menu_theme,
        clear_screen=True
    )

    quickExit = False

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            user = str(input('Confirm Username:\n'))
            pas = str(input('Password:\n'))

            chU = {}
            chU['Username'] = user

            chP = {}
            chP['Password'] = pas

            usr = open('./users.json')
            usr_new = json.load(usr)

            if usr_new.count(chU) > 0 and usr_new.count(chP) > 0:
                print(f'Welcome User: {user}')
                print('Loading...')
                sleep(4)
                while not profile_menu_exit:
                    prof_sel = profile_menu.show()

                    if prof_sel == 0:
                        while not quickExit:
                            c = open('./storage.json')
                            cDict = json.load(c)
                            if cDict['Users'][user] == 0:
                                methods.firstEncrypt()
                                sleep(30)
                                quickExit = True
                            else:
                                methods.secure()
                                sleep(30)
                                quickExit = True
                        quickExit = False
                        
                    elif prof_sel == 1:
                        methods.validKey()
                        sleep(30)
                        while not encLib_menu_exit:
                            encLib_sel = encLib_menu.show()

                            if encLib_sel == 0:
                                methods.edit()
                                sleep(5)
                                encLib_menu_exit = True
                                
                            elif encLib_sel == 1:
                                methods.delete()
                                sleep(5)
                                encLib_menu_exit = True
                                
                            elif encLib_sel == 2:
                                encLib_menu_exit = True
                        encLib_menu_exit = False
                        
                    elif prof_sel == 2:
                        while not eProfile_menu_exit:
                            eProf_sel = eProfile_menu.show()

                            if eProf_sel == 0:
                                methods.editUser()
                                sleep(3)
                                eProfile_menu_exit = True
                                
                            elif eProf_sel == 1:
                                methods.editPass()
                                sleep(3)
                                eProfile_menu_exit = True
                            
                            elif eProf_sel == 2:
                                methods.deleteAcc()
                                
                            elif eProf_sel == 3:
                                eProfile_menu_exit = True
                        eProfile_menu_exit = False
                        
                    elif prof_sel == 3:
                        profile_menu_exit = True
                profile_menu_exit = False
            else:
                print('I am sorry but that user does not exist.')
        
        elif main_sel == 1:
            methods.newUser()
            sleep(3)
        
        elif main_sel == 2:
            methods.h()
            sleep(120)
        
        elif main_sel == 3:
            main_menu_exit = True

start()