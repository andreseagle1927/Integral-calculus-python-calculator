# Function decimal to binary

def decimal_to_binary(decimal):
    integer = int(decimal)
    fraction = decimal - integer
    binary = bin(integer).split("b")[-1]
    if fraction == 0:
        return binary
    else:
        binary_fraction = ""
        while fraction != 0 and len(binary_fraction) < 32:
            fraction = fraction * 2
            if fraction >= 1:
                binary_fraction += "1"
                fraction -= 1
            else:
                binary_fraction += "0"
        return binary + "." + binary_fraction

# Function decimal to octal
def decimal_to_octal(decimal):
    integer = int(decimal)
    fraction = decimal - integer
    octal = oct(integer).split("o")[-1]
    if fraction == 0:
        return octal
    else:
        octal_fraction = ""
        while fraction != 0 and len(octal_fraction) < 32:
            fraction = fraction * 8
            octal_fraction += str(int(fraction))
            fraction = fraction - int(fraction)
        return octal + "." + octal_fraction

# Function decimal to hexadecimal
def decimal_to_hexadecimal(decimal):
    integer = int(decimal)
    fraction = decimal - integer
    hexadecimal = hex(integer).split("x")[-1]
    if fraction == 0:
        return hexadecimal
    else:
        hexadecimal_fraction = ""
        while fraction != 0 and len(hexadecimal_fraction) < 32:
            fraction = fraction * 16
            hexadecimal_fraction += hex(int(fraction))[2:]
            fraction = fraction - int(fraction)
        return hexadecimal + "." + hexadecimal_fraction

# Function binary to decimal
def binary_to_decimal(binary):
    if "." in binary:
        integer, fraction = binary.split(".")
        decimal = int(
            integer, 2) + sum([int(fraction[i]) * 2**(-i-1) for i in range(len(fraction))])
    else:
        decimal = int(binary, 2)
    return round(decimal, 5)

# Function binary to octal
def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_octal(decimal)

# Function binary to hexadecimal
def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_hexadecimal(decimal)

# Function octal to decimal
def octal_to_decimal(octal):
    if "." in octal:
        integer, fraction = octal.split(".")
        decimal = sum([int(integer[i]) * 8**(len(integer)-i-1)
                      for i in range(len(integer))])
        decimal += sum([int(fraction[i]) * 8**(-i-1)
                       for i in range(len(fraction))])
    else:
        decimal = int(octal, 8)
    return round(decimal, 5)

# Function octal to binary
def octal_to_binary(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_binary(decimal)

# Function octal to hexadecimal
def octal_to_hexadecimal(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_hexadecimal(decimal)

# Function hexadecimal to decimal
def hexadecimal_to_decimal(hexadecimal):
    if "." in hexadecimal:
        integer, fraction = hexadecimal.split(".")
        decimal = int(
            integer, 16) + sum([int(fraction[i], 16) * 16**(-i-1) for i in range(len(fraction))])
    else:
        decimal = int(hexadecimal, 16)
    return round(decimal, 5)

# Function hexadecimal to binary
def hexadecimal_to_binary(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_binary(decimal)

# Function hexadecimal to octal
def hexadecimal_to_octal(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_octal(decimal)

# Function convert
def convert(number, from_base, to_base):
    if from_base == "decimal":
        if to_base == "binary":
            return decimal_to_binary(number)
        elif to_base == "octal":
            return decimal_to_octal(number)
        elif to_base == "hexadecimal":
            return decimal_to_hexadecimal(number)
    elif from_base == "binary":
        if to_base == "decimal":
            return binary_to_decimal(number)
        elif to_base == "octal":
            return binary_to_octal(number)
        elif to_base == "hexadecimal":
            return binary_to_hexadecimal(number)
    elif from_base == "octal":
        if to_base == "decimal":
            return octal_to_decimal(number)
        elif to_base == "binary":
            return octal_to_binary(number)
        elif to_base == "hexadecimal":
            return octal_to_hexadecimal(number)
    elif from_base == "hexadecimal":
        if to_base == "decimal":
            return hexadecimal_to_decimal(number)
        elif to_base == "binary":
            return hexadecimal_to_binary(number)
        elif to_base == "octal":
            return hexadecimal_to_octal(number)

