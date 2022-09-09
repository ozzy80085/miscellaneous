from sys import argv as arg

try:

        if arg[1] == "-1":
                print("Hello, World!")

        if arg[1] != "-1":
                exit()

except:
        quit()
