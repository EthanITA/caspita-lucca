import bcrypt as bcrypt


def get_hashed(plain_text):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text, bcrypt.gensalt())


def check_password(plain_text, hashed_text):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text, hashed_text)
