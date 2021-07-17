# Software Development Plan

<br>

## Statement of Purpose and Scope

Black-Box is a terminal application that encrypts any information that the user gives it. It is designed as to store this information securely within a profile you create in the application. The app provides the user with an encryption key they can use to access the information stored within their account.

The purpose behind Black-Box is to provide a safe space to store information locally on the users device. In todays world, as we integrate ourselves into the global society that exists on the internet, we tend to share more and more of our personal details, knowingly and unknowingly, with complete strangers. Although this application will not solve all the users safety needs, it does provide them with a storage space for information that they consider particularly sensitive, acting almost like a 'little black book' or a diary... with a little more security.

The primary demographic that this application is catered towards, is the average technologically competent user. Anyone that wishes to protect certain information that they feel they may forget if not written down, or they feel that they must keep a virtual copy of incase of misplacement.

As stated previously the app will be launched within the users local terminal. The users will then log in or create an account inside the application. Within their profile, the user will be able to access the encryption key generator and a library of their previously encrypted information. Within the generator they can feed any information they would like to encrypt and be returned an encryption key that they must remember in order to access the information again. Within the library, they will be able to enter in the encryption key pertaining to a specific set of information that they had previously encrypted which will allow them to access said information. They will also be able to exit the application in the login menu.

<br>

## Features

### Login Menu

This feature allows the user to enter into their profile. This feature also allows the user to access the help document if needed, as well as allow the user to exit the application. In the event that the user does not have an account, they will also be able to create a profile from this menu.

### C.R.U.D Profile

This feature allows the user to Create, Read, Update, and Delete their profile within the application, editing their username and/or password. 

### Encryption Generator

The main feature of the application, the encryption generator allows the user to receive an encryption key after submitting data that they wish to keep safe. This information can later be accessed in a pseudo-library 'encryptions' database.

### C.R.U.D Encryptions

This feature allows the user to Create, Read, Update, and Delete previously saved data within the application. Deleting an entry will remove the associated encryption key.

<br>

## User Interaction and Experience

The help documentation supplied with the app that can be accessed through the '-help' argument provided with the bash shell will provide all the necessary information to the user regarding how to interact and use each feature available within the application.

### Feature 1: Login Menu

This feature allows the user to login, create a new profile and exit the application. If the user inputs an invalid username or password they will be unable to enter the profile menu, be notified that the user does not exist and the application will quit automatically, this quite inconvenient to the user but is to allow the utmost safety and privacy. If the user inputs a correct username and incorrect username or vice-versa the application will once again let the user know that either the password or username was incorrect and exit the app. When creating a new user if the user already exists within the local database of the client's application the application will let the user know this and once again exit the application. Passwords can be the same between users the app will not raise an issue. The sys.exit function is used to exit the application alongside the termination of the simple_term_menu modules TerminalMenu function.

### Feature 2: C.R.U.D Profile

This feature acts as a central hub from which the user can access other crucial features of the application, such as the encryption generator and their previously save encryptions. They can also update, delete and read their profile through this feature. If the user attempts to change their username they will require a username that is valid and does not exist in the database already. The app ensures this. The user cannot delete their account without confirmation and in the event that the user does not confirm the termination of their account the app will send the user back to the edit profile menu. The application can handle any invalid inputs from the user.

### Feature 3: Encryption Generator

The encryption generator is the major feature within the application and allows the user to input information into it, and in turn receive an encryption key that they can use to later access that same information. The new user function also creates a json object with the same key and appends it to the storage json file, effectively linking the user's account to their library of encryptions, the encryption generator ensures that the user will have their encryptions saved to the json object specific to their username. You can enter any data type and receive a key.

### Feature 4: C.R.U.D Encryptions

This feature acts as a pseudo-library that is accessible from the profile and stores all the users previously documented encryptions. Within this the feature the user can utilise their received encryption keys to access the above-mentioned encryptions. Accessing the saved information will require the exact key given by the application, the app will not accept invalid keys, or any other invalid user input. The application will handle any invalid inputs from the user regarding the updating and deleting of any existing key: value pairs.

<br>

## Control Flow Diagram

![Control-Flow-Diagram](/Pranav-RatishShankar-T1A3-5-control-flow-diagram.jpg)
