import time
import sys

length = 0
max_length = int(sys.argv[1]) - 1
while True:
    text = ''
    if length <= max_length:
        length += 1
        for i in range(length):
            text += 'a'
        time.sleep(0.00001)
        print(text)
    else:
        for i in range(max_length):
            text = ''
            length -= 1
            for i in range(length):
                text += 'a'
            time.sleep(0.00001)
            print(text)
