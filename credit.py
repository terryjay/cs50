import cs50

def main():
    print("Number: ", end="")
    card_number = cs50.get_int()
    
    if card_number <= 0:
        print("Please input a valid card number.")
        
    card_string = str(card_number)
    
    valid, cardtype = cardchecker(card_string)
    checksum = numberchecker(card_string)
    
    if checksum % 10 == 0:
        print(cardtype)
    else:
        print("INVALID")
    
    
def cardchecker(card_string):
    if card_string[0] == '3' and (card_string[1] == '4' or card_string[1] == '7'):
        valid = True
        cardtype = "AMEX"
    if card_string[0] == '5' and (card_string[1] == '1' or card_string[1] == '2' or card_string[1] == '3' or card_string[1] == '4' or card_string[1] == '5'):
        valid = True
        cardtype = "MasterCard"
    if card_string[0] == '4':
        valid = True
        cardtype = "Visa"
    
    return valid, cardtype

def numberchecker(card_string):
    checksum = 0
    for i, c in enumerate(card_string):
        if i % 2 == 1: #even number
            c = 2*int(c)
            if c >= 10:
                c = c - 9
            checksum = int(c) + checksum
        elif i % 2 == 0: # odd number
            checksum = int(c) + checksum

    return checksum    

if __name__ == "__main__":
    main()
