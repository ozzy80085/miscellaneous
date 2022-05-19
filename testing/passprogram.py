import hashlib

password = "b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86"

def protected():
        print(f"Welcome")
        print("this is protected information")

passinput = input("enter your password: ")
passinput = passinput.encode('utf-8')

if hashlib.sha512(passinput).hexdigest() != password:
#       wrong password
        print("Wrong Password!")
        exit()

else:
#       correct password
        print("Correct Password!")
        protected()
