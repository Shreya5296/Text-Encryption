import hashlib

# initializing string
text = "hi whitehatters"

# encoding string using encode()
# then sending to SHA256()
result = hashlib.sha3_256(text.encode())

# printing the SHA256 value.
print("The SHA256 is : ",result.hexdigest())
