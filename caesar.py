import cs50
import sys

if len(sys.argv) != 2:
    print("use: python caesar.py [key]")
    exit()
key = int(sys.argv[1])
ciphertext = []

print("plaintext: ", end="")
plaintext = cs50.get_string()

#change the plaintext to ciphertext letter by letter
for i, c  in enumerate(plaintext):
    if c.isalpha():
        if c.islower():
            newletter = chr((((ord(c) - 97) + key) % 26) + 97)
            ciphertext.append(newletter)
        if c.isupper():    
            newletter = chr((((ord(c) - 65) + key) % 26) + 65)
            ciphertext.append(newletter)
    else:
        newletter = c
        ciphertext.append(newletter)
    
    
# print the new ciphertext
print("ciphertext: ",end="")
for j, c in enumerate(ciphertext):
    print(ciphertext[j],end="")
print("")
