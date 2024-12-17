import bcrypt

# Password input
password = input("Enter your password: ")

# Generate a salt
salt = bcrypt.gensalt()

# Hash the password
hashed_password = bcrypt.hashpw(password.encode(), salt)

print("Original password:", password)
print("Hashed password:", hashed_password)

# Verifying the password
retyped_password = input("Retype your password: ")

if bcrypt.checkpw(retyped_password.encode(), hashed_password):
    print("Passwords match!")
else:
    print("Passwords do not match!")