import msvcrt as ms

while True:
    if ms.kbhit():
        key = ms.getch()
        print(key)
        print(str(key)[2])
