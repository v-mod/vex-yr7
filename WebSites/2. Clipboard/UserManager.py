import os.path
import os
class User:
    def __init__(self, userName, password, email, fname, lname, dob):
        self.userName = userName
        self.password = password
        self.email = email
        self.fname = fname
        self.lname = lname
        self.dob = dob

class UserManager:

    def Auth(self,userName,password):
        path = '/home/site/wwwroot/ClipBoard/User-Info/'
        if os.path.isfile(path + userName + '/'  + 'Me.txt'):
            f = open(path + userName + '/'+ 'Me.txt', 'r')
            data = f.read()
            userData = data.split(',')
            f.close()
            cpassword = userData[1]
            if cpassword == password:
                user = User(userData[0], '', userData[2], userData[3],userData[4],userData[5])
                return { 'user': user, 'message': 'User found' }
            else:
                return{'user': None, 'message': 'Incorrect Username or Password'}
        else:
            return { 'user': None, 'message': 'Incorrect Username or Password' }
    def Signup(self, userName, password, email, fname, lname, dob):
        userInfo=userName + ',' + password + ',' + email + ',' + fname + ',' + lname+ ','+ dob
        os.mkdir('User-Info/'+userName)
        me = open('User-Info/'+userName+'/Me.txt', 'w')
        me.write(userInfo)
        me.close()

