import cs50

print("Height: ", end="")
height = cs50.get_int()
    
while height <= 0 or height >= 24:
    print("Please use a positive number less than 23.")
    print("Height: ", end="")
    height = cs50.get_int()

for i in range(height):
    row = i
    hashes = row + 2
    spaces = (height - i) - 1
    
    #print(row, hashes, spaces)

    for j in range(spaces):
        print(" ",end="")  
    
    for k in range(hashes):
        print("#",end="")
    
    print("")
