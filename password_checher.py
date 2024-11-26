

master_pwd=input('what is the mastrer password')
def view():
    file = open('password.txt', 'r')

    for line in file.readlines():
        data=line.rstrip()
        user,passw=data.split('|')
        print('user;',user,',password;',passw)
    file.close()


def add():
    name=input('account name: ')
    pwd=input('password: ')
    file= open('password.txt','a')

    file.write(name +'|'+pwd+'\n')
    file.close()

while True:
    mode=input('would you like to add a newpassword or view existing one ( view & add) ? press q to quit ').lower()
    if mode =='q':
        break
    if mode == 'view':
        view()
    elif mode =='add':
        add()
    else:
        print('invalid mode.')
        continue
