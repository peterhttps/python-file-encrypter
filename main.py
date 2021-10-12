import pyAesCrypt
password = "batatinha"

def encrypt():
  print()
  fileName = input("Type the file name to encrypt\n> ")
  encryptPass = input("Type the password to encrypt\n> ")
  pyAesCrypt.encryptFile(f"{fileName}", f"{fileName}.aes", encryptPass)
  print("Encrypted!")

def decrypt():
  print()
  fileName = input("Type the file name to decrypt\n> ")
  encryptPass = input("Type the password to decrypt\n> ")
  pyAesCrypt.decryptFile(f"{fileName}", "dataout.txt", encryptPass)
  print("Decrypted!")

print("Do you wanna:\n1 - Encrypt\n2 - Decrypt")
choice = input("> ")

if (choice == '1'):
  encrypt()
else:
  decrypt()