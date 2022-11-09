import tkinter as tk
import hashlib


def hash_value():
    hash_input = input.get()
    hash_text = hashlib.md5(hash_input)
    hashentry.insert(0, hash_text)

def ce():
    output.delete(0, "end")
def encrypt():
    tegn = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ0123456789 .,-!?=+_"
    crypt_tegn = "dejst?=YZGHIJKLM+uÆØÅABCDEFvwxqrPQRSTUVWfghiy23_4abc567zæøåkl.,-!mnopXNO0189 "
    encrypted_text = ""
    text = input.get()
    for i in text:
        for n, j in enumerate(tegn):
            if i == j:
                encrypted_text += crypt_tegn[n]
    ce()
    output.insert(0, encrypted_text)
    return encrypted_text


def decrypt():
    crypted_tegn = "dejst?=YZGHIJKLM+uÆØÅABCDEFvwxqrPQRSTUVWfghiy234abc567zæøåkl.,-!mnopXNO0189 "
    decrypt_tegn = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ0123456789 .,-!?=+"
    decrypted_text = ""
    tekst = input.get()
    for i in tekst:
        for n , j in enumerate(crypted_tegn):
            if i == j:
                decrypted_text += decrypt_tegn[n]
    ce()
    output.insert(0, decrypted_text)
    return decrypted_text




root = tk.Tk()

input = tk.Entry(root, font = ("ARIAL", 20))
input.pack()
output = tk.Entry(root, font = ("ARIAL", 20))
output.pack()
encryptB = tk.Button(root,font = ("ARIAL", 20),text = "encrypt", command = encrypt)
encryptB.pack()
decryptB = tk.Button(root,font = ("ARIAL", 20),text = "decrypt", command = decrypt)
decryptB.pack()
hashentry = tk.Entry(root, font = ("ARIAL", 20))
hashentry.pack()




root.mainloop()