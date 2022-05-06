import numpy

f = open("code.bf", "w")

text = input("text> ")
text = text + "\n"
text = list(text)
arr = numpy.array(text)

for i in arr:
        num = ord(i)
        f.write("+" * num)
        f.write(".\n")
        f.write("-" * num)
        f.write("\n")


f.close()
