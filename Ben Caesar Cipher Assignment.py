"""
PROGRAM CaesarCipher:
Begin by defining alphabet;
Ask wheter the user would like to encrypt, decypt or quit;
If (user enters encrypt)
 Then ask user what they would like to encrypt;
 Ask user how much of a shift they want;
 Repeat the shifted phrase back to them;
ENDIF;

If (user enters decrypt)
 Then ask user what they would like to decrypt;
 Ask user how much of a shift they want;
 Repeat the shifted phrase back to them;
ENDIF;
 
If (user enters quit)
 End the loop;
ENDIF;

END.

"""

print ("Caesar Cipher Assignment Ben Lemoine")
print ("---------------------------------------")
print ()

alphabet = "abcdefghijklmnopqrstuvwxyz"

done = False

def encrypt():
    encryption = ""
    enc = input("What phrase would you like to encrypt?: ")
    key = int(input("What shift would you like to use?: "))
    enc = enc.lower()
    for char in enc:
        x = ord(char)
        if x >= 97:
            x += key
            while x > 122:
                x = (x - 122 + 96)
        x = chr (x)
        encryption += x
    print ("")
    print ("Encrypted Phrase:", encryption)
    print ("--------------------------------")
    print ("")

def decrypt():
    decryption = ""
    dec = input("What phrase would you like to decrypt?: ")
    key = int(input("What shift would you like to use?: "))
    dec = dec.lower()
    for char in dec:
        x = ord(char)
        if x >= 97:
            x -= key
            while x > 122:
                x = (x - 122 + 96)
        x = chr (x)
        decryption += x
    print ("")
    print ("Decrypted Phrase:", decryption)
    print ("--------------------------------")
    print ("")    
    
while not done:
    print ("Welcome to the Encryption and Decryption Machine.")
    print ("Please select an option from the list below.")
    print ("A. Encrypt, (A)")
    print ("B. Decrypt, (B)")
    print ("Q. Quit,    (Q)")
    user = input(": ")
        
    if user.lower() == "a":
        encrypt() 
            
    elif user.lower() == "b":
        decrypt()   
        
    elif user.lower() == "q":
        done = True
        print ("//Quitting Caesar Cipher//")