def valid_decimal(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        try:
            if int(item) > 255 or int(item) < 0:
                return False
        except:
            return False
    return True

def valid_binary(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        try:
            # int(item,2) is used to convert the binary to integer form 2 shows the base of the string which is binary
            # so all the parts of IP address must be between 0 to 255
            if int(item, 2) > 255 or int(item, 2) < 0:
                return False
        except:
            return False
    return True

def convert_to_binary(address):
    parts = address.split(".")
    binary_parts = []
    for item in parts:
        decimal = int(item)
        binary = ''
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2
        binary = '0' * (8 - len(binary)) + binary
        binary_parts.append(binary)
    return ".".join(binary_parts)

def convert_to_decimal(address):
    parts = address.split(".")
    decimal_parts = []
    for item in parts:
        binary = item
        decimal = 0
        for i in range(len(binary)):
            decimal += int(binary[i]) * 2**(len(binary)-i-1)
        decimal_parts.append(str(decimal))
    return ".".join(decimal_parts)

def get_class(address):
    first_part = int(address.split(".")[0])
    if first_part >= 0 and first_part <= 126:
        return "Class A"
    elif first_part >= 128 and first_part <= 191:
        return "Class B"
    elif first_part >= 192 and first_part <= 223:
        return "Class C"
    elif first_part >= 224 and first_part <= 239:
        return "Class D"
    elif first_part >= 240 and first_part <= 255:
        return "Class E"
    else:
        return "Invalid address"

def main():
    address = input("Enter an IPv4 address (Decimal or binary): ")
    if valid_binary(address):
        print("Valid binary representation")
        decimal_representation = convert_to_decimal(address)
        print("Decimal representation:", decimal_representation)
        Class = get_class(decimal_representation)
        print("Class:", Class)
    elif valid_decimal(address):
        print("Valid Decimal representation")
        binary_representation = convert_to_binary(address)
        print("Binary representation:", binary_representation)
        Class = get_class(address)
        print("Class:", Class)
    else:
        print("Invalid representation")

main()