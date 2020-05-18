import simplecrypt
res = ''
with open("C:\\Users\\User\\Downloads\\encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("C:\\Users\\User\\Downloads\\passwords.txt") as pas:
    x = pas.read().splitlines()
    for i in x:
        try:
            print(simplecrypt.decrypt(i, encrypted))
        except  simplecrypt.DecryptionException:
            print(i)
