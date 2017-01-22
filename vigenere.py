import cs50
import sys

if len(sys.argv) != 2:
    print("use: python caesar.py [key]")
    exit()
key = sys.argv[1]
cipher = []
ciphertext = []

print("plaintext: ", end="")
plaintext = cs50.get_string()

for c in key:
    if not c.isalpha:
        print("Please use only alphabetical characters.")
    if c.isupper():
        cipher.append((ord(c) - 65) % 26)
    if c.islower():
        cipher.append((ord(c) - 97) % 26)

x = 0
for j, c in enumerate(plaintext):        
    if c.isalpha():
        if c.islower():
            newletter = chr((((ord(c) - 97) + cipher[x]) % 26) + 97)
            ciphertext.append(newletter)
        if c.isupper():    
            newletter = chr((((ord(c) - 65) + cipher[x]) % 26) + 65)
            ciphertext.append(newletter)
        if (x == len(cipher) - 1):
            x = 0
        else:
            x += 1
    else:
        newletter = c
        ciphertext.append(newletter)

print("ciphertext: ",end="")
for p in ciphertext: print(p, end="")
print("")
          
