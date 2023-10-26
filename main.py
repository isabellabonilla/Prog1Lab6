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

if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print('2. Decode')
        print("3. Quit")
        option = input("Please enter an option: ")
        if option == 1:
            password = encoder(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        if option == 2:
            pass
        if option == 3:
            break

