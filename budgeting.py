import time

total = 0
while True:
    time.sleep(3)
    print('Slept')
    file = open('./example.txt', 'r+')
    fileO = open('./exampleO.txt', 'r+')
    total = sum(int(line.strip()) for line in file)
    print(total)
    fileO.write(str(total) + " Dollars ")
        