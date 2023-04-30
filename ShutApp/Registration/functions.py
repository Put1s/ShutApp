def hash_password(password):
    import os
    import hashlib
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key, salt


def validate_username(username):
    from Messenger.models import User
    if User.objects.filter(Nickname=username).exists():
        return False
    return True


def validate_email(email):
    from Messenger.models import User
    if User.objects.filter(Email=email).exists():
        return False
    return True
