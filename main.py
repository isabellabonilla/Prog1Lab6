def encoder(password):
    int_password = int(password)
    encoded_password = ""
    for x in int_password:
        if 0 <= x < 7:
            encoded_password += str(x + 3)
        elif x == 7:
            encoded_password += "0"
        elif x == 8:
            encoded_password += "1"
        elif x == 9:
            encoded_password += "2"
    return encoded_password

