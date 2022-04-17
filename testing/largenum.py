import random
import math

seed = random.randint(99999, 9999999999999)

f = open("bytes.dat", "a+")


try:

        while True:
                seed = seed / 2
                if seed < 255:
                        hexe = hex(math.trunc(seed))[2:]
                        f.write(hexe + " ")
                        seed = random.randint(99999, 9999999999999)
                        continue

except KeyboardInterrupt:
        f.close()
        exit()
