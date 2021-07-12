# Implementation Plan

<br>

## Login Menu

The login menu will consist of multiple options that take the user to the login screen, the create new user screen, the help documentation and exit the application. The login menu is low in priority as the encryption generator, library and profile are more necessary to the main function of the application.

The login screen should allow the user to input a valid Username and Password, and confirm the existence of the user by checking if the login details are in the local database. A valid login will give them access to their profile page. A function that tests the validity of the login will be necessary, as well as a function that verifies the existence of the login details within the database.

The create new user screen should allow the user to input a valid Username, assign it a Password and check that the Username does not already exist in the database. A function that tests the validity of the Username is required, alongside a function to verify the singularity of the Username.

The help option will require the application to display the help documentation to the user inside the terminal instance. A function that displays the content of a text file to the user via the terminal will be necessary.

The user should also be able to exit the application. A function to exit the application upon input will be required.

To view the deadlines for this feature please refer to the screenshot at the end of the document.

<!-- - Login:
    - Input valid Username and Password:
        - Function to test validity
        - Check if Login in database
- New User:
    - Create valid Username and Password:
        - Check if Username exists in database
        - Function to test valid username
- Help:
    - Access help documentation:
        - Display text from file
- Exit the application -->
<br>

## C.R.U.D Profile

The profile page in the application should allow the user to access the encryption features of the application (the generator and library) and also allow the user to edit their profile. The user should be able to edit their Username, Password and also delete their account if desired. The profile is average in priority, it is important in that it houses the encryption features but is less important than the features themselves. However, it is still more of a priority than the login menu.

The user should have the ability to edit their profile, specifically their Username and Password. A function to test the validity of a Username is required, alongside the ability to check for singularity to avoid two users having the same Username. A function to receive confirmation of a Password change via input of valid, existing Password, and entry of a new password in it's place is needed as well.

The termination of an account should require the user to confirm the termination alongside requiring the user to enter valid login details. The termination of the account should also trigger the termination of the application. Thus requiring the user to return to the login menu and create a new account before accessing the encryption features. A function to validate confirmation of termination and a function that will verify the login details, terminate the account and exit the application will be necessary.

To view the deadlines for this feature please refer to the screenshot at the end of the document.

<!-- - Created from Login Menu
- Profile page contains access to encryption features
- Edit Profile:
    - Edit Username:
        - Input new, valid Username:
            - Function to test validity
    - Edit Password:
        - Input existing Password:
            - Test for validity
        - Input new Password:
            - User input
    - Delete Account:
        - Confirm Termination (Y/N):
            - Confirm valid input
        - Input valid login details and terminate account, exit application:
            - Test for validity -->
<br>

## Encryption Generator

The encryption generator is the highest priority feature and should allow the user to input any data, convert that data into a string and store that data inside a file that will act as a database. The generator will provide the user with an encryption key as soon they input any data into the generator.

The generator will not need a function that checks for validity but will require that any data that is input by the user is converted into a string before being stored in the database (accessible through the encryptions library). A function, preferably acquired from an existing Python encryption module, to create an encryption key for the user will be required.

To view the deadlines for this feature please refer to the screenshot at the end of the document.

<!-- - Input by User:
    - No check for validity, accept any data as string
- Return encryption key:
    - Function from external encryption library
- Store information in Encryptions Library -->

<br>

## C.R.U.D Encryptions

The encryptions library accessible from the profile page will allow the user to input an encryption key and receive access to the associated information stored in the database. After displaying the information the user will be able to choose to edit or delete the information, and return to the library.

The validity of the encryption key will have to be confirmed, a function that accomplishes this will be required.

If the user chooses to edit the data there will be no need to check for validity, only a conversion of the information into string will be required. The app should return to the displayed information after changes are made.

If the user chooses to delete the data, they should be asked to confirm the deletion, alongside this the entry must also be removed from the database and the encryption key must be removed as well. After the deletion of the entry the user will be returned to the library.

To view the deadlines for this feature please refer to the screenshot at the end of the document.

<!-- - User input:
    - Check for validity of encryption key
- Display the encrypted information:
    - Edit Data:
        - User input:
            - No check for validity, accept any data as string
        - Display new, edited data
    - Delete Entry:
        - confirm deletion
        - Remove entry from stored information, remove key
        - Return to Library
    - Return to Library -->
<br>

### Project Management Platform (Deadlines for Features)

![Project-Management-Platform](/Pranav-RatishShankar-T1A3-13-project-mgmt-checklist1.jpg)