import random as r, string as s

elements = s.ascii_letters + s.ascii_uppercase + s.digits + s.punctuation
lenght = int(input("cuantos caracteres tendra la contrasena? "))

passwword = ""

for i in range (lenght):
    passwword += r.choice(elements)
print (f" 🔐 Su contraseña ha sido generada 😎 : {passwword}")
