#imei is 15 digits

#im aware that this code is both messy and not very efficient but it works
#this program validates an imei number using the luhn algorithm which you can read about here https://www.geeksforgeeks.org/luhn-algorithm/

orig = "522857152301042"

if len(orig) != 15:
	print("this number isnt even 15 digits its definitely not a valid imei number")
	quit()

#14s char in (2nd to last)
orig1 = str(int(orig[13]) * 2)
orig2 = str(int(orig[11]) * 2)
orig3 = str(int(orig[9]) * 2)
orig4 = str(int(orig[7]) * 2)
orig5 = str(int(orig[5]) * 2)
orig6 = str(int(orig[3]) * 2)
orig7 = str(int(orig[1]) * 2)

norm1 = int(orig[0])
norm2 = int(orig[2])
norm3 = int(orig[4])
norm4 = int(orig[6])
norm5 = int(orig[8])
norm6 = int(orig[10])
norm7 = int(orig[12])
norm8 = int(orig[14])

if len(orig1) == 2:
	orig1 = int(orig1[0]) + int(orig1[1])

if len(orig2) == 2:
        orig2 = int(orig2[0]) + int(orig2[1])

if len(orig3) == 2:
        orig3 = int(orig3[0]) + int(orig3[1])

if len(orig4) == 2:
        orig4 = int(orig4[0]) + int(orig4[1])

if len(orig5) == 2:
        orig5 = int(orig5[0]) + int(orig5[1])

if len(orig6) == 2:
        orig6 = int(orig6[0]) + int(orig6[1])

if len(orig7) == 2:
        orig7 = int(orig7[0]) + int(orig7[1])

all = int(orig1) + int(orig2) + int(orig3) + int(orig4) + int(orig5) + int(orig6) + int(orig7) + norm1 + norm2 + norm3 + norm4 + norm5 + norm6 + norm7 + norm8

if all % 10 == 0:
	print("the imei number is valid")
