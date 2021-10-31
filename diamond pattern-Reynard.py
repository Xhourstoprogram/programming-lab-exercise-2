def pyramid(rows):
    for i in range(rows):
        print("" * (rows-i*2) + "*"*(i+1))
    for j in range(rows-1, 0, -1):
        print(""*(rows-j) + "*"*j)


pyramid(5)
