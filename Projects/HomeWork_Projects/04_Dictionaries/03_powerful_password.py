"""
You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!

This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.

For example, using a hash function called SHA256(...) something as simple as

hello

can be hashed into a much more complex

2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.

(Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)
"""

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


stored_logins = {
    "user@example.com": hash_password("user@12345"),
    "admin@example.com": hash_password("admin@12345"),
}

def login(email, password_to_check):
    if email in stored_logins:
        
        if stored_logins[email] == hash_password(password_to_check):
            return True
        else:
            return False
    else:
        return False


email = input("Enter your email: ")
password = input("Enter your password: ")

if login(email, password):
    print("Login successful!")
else:
    print("Login failed!")
