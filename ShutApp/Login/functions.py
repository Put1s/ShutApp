import hashlib
salt = b''  # Получение соли, сохраненной для *этого* пользователя
key = b''  # Получение рассчитанного ключа пользователя

password_to_check = 'password246'  # Пароль, предоставленный пользователем, проверяется

# Используется та же настройка для генерации ключа, только на этот раз вставляется для проверки настоящий пароль
new_key = hashlib.pbkdf2_hmac(
    'sha256',
    password_to_check.encode('utf-8'),  # Конвертирование пароля в байты
    salt,
    100000
)

if new_key == key:
    print('Пароль правильный')
else:
    print('Пароль неправильный')