def encrypt_message(encrypt):
    encrypt = encrypt.replace('you', 'your+client')
    encrypt = encrypt.replace('youuu', 'your+client')
    encrypt = encrypt.replace('u', 'your+client')
    return encrypt


get_input = input('Enter the input please')
print('This is the Encrypted output: ', encrypt_message(get_input))
