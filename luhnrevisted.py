num = "378282246310005"

numarr = []

for i in num[::-1]:
        numarr.append(int(i))

count = 1

newarr = []

for i in numarr:
        if count % 2 == 0:
                i = i * 2
        newarr.append(i)
        count += 1

anothernewarr = []

for i in newarr:
        if int(len(str(i))) == 2:
                i = int(str(i)[0]) + int(str(i)[1])
        anothernewarr.append(i)
total = 0

for i in anothernewarr:
        total = total + i

if total % 10 == 0:
        print("the number is valid")

else:
        print("the number is INVALID")
