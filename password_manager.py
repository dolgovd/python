#Cryptography library should be install on your env
#Master password will be used for encryption/decryption of passwords in txt file


from cryptography.fernet import Fernet

#Function for creating a file with encryption key (with construction is used)
def writeKey():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as keyFile:
        keyFile.write(key)

#Function for reading encryption key (open/close construction is used)
def loadKey():
    file = open('key.key', 'rb')
    key = file.read()
    file.close
    return key

masterPassword = input('Please enter master password: ')
key = loadKey() + masterPassword.encode()
fer = Fernet(key)

#!!! 'View' function does not work properly. Additional investigation is needed!!!
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            userName, userPassword = data.split('|')
            print('Login: ', userName, '| Password: ', fer.decrypt(userPassword.encode()).decode())

def add():
    userName = input('Please enter login: ')
    userPassword = input('Please enter password: ')

    with open('password.txt', 'a') as f:
        f.write(userName + '|' + fer.encrypt(userPassword.encode()).decode() + '\n')

while True:
    mode = input('Would you like to add a new password and view existing one (view / add)? Enter Q to exit: ').lower()
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode')
        continue
