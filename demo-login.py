# By Dominic Eggerman
# Login prompt
def userLogin():

    username = input('Enter username: ')
    password = getpass.getpass('Enter password: ')

    print(username)
    print(password)

    return [username, password]

# Main
if __name__ == '__main__':

    # Imports
    import getpass

    # Run
    userpass = userLogin()