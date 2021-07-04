import hashlib
string1="SHAPEAI"
result=hashlib.md5(string1.encode())
print("The Hexadecimal equivalent of hash is:-",end=" ")
print(result.hexdigest())
string2=input("Enter your STRING DATA:-")
result=hashlib.md5(string2.encode())
print("The Hexadecimal equivalent of hash is:-",end=" ")
print(result.hexdigest())
input()
