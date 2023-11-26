import struct # Import struct library 
from backend.conversor_bases import convert # Import the convert function from the conversor_bases.py file

# Function to convert decimal to binary
def decimal_to_bin(num, precision):
    if precision == "simple":
        bin_num = format(struct.unpack('!I', struct.pack('!f', num))[0], 'b').zfill(32)
        sign = bin_num[0]
        exponent = bin_num[1:9]
        mantissa = bin_num[9:]
        decimal_exponent = int(exponent, 2) - 127
        decimal_mantissa = int(mantissa, 2) / 2**23
        decimal_mantissa_str = str(decimal_mantissa)[2:18]
        decimal_equivalent = (-1)**int(sign) * (1 + decimal_mantissa) * 2**decimal_exponent
        return (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent)
    elif precision == "doble":
        bin_num = format(struct.unpack('!Q', struct.pack('!d', num))[0], 'b').zfill(64)
        sign = bin_num[0]
        exponent = bin_num[1:12]
        mantissa = bin_num[12:]
        decimal_exponent = int(exponent, 2) - 1023
        decimal_mantissa = int(mantissa, 2) / 2**52
        decimal_mantissa_str = str(decimal_mantissa)[2:18]
        decimal_equivalent = (-1)**int(sign) * (1 + decimal_mantissa) * 2**decimal_exponent
        return (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent)

# Function to convert decimal to hexadecimal
def decimal_to_hex(num, precision):
    if precision == "simple":
        return convert(num,"decimal", "hexadecimal")
    elif precision == "doble":
        return convert(num,"decimal", "hexadecimal")

# Function to convert binary to decimal
def bin_to_decimal(bin_num, precision):
    if precision == "simple":
        sign = int(bin_num[0])
        exponent = int(bin_num[1:9], 2)
        mantissa = int(bin_num[9:], 2) / 2**23
        decimal_exponent = exponent - 127
        decimal_mantissa = 1 + mantissa
        decimal_mantissa_str = str(decimal_mantissa)[2:18]
        decimal_equivalent = (-1)**sign * decimal_mantissa * 2**decimal_exponent
        #print(sign, exponent, bin_num[1:], decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent)
        return (sign, exponent, bin_num[1:], decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent)
    elif precision == "doble":
        sign = int(bin_num[0])
        exponent = int(bin_num[1:12], 2)
        mantissa = int(bin_num[12:], 2) / 2**52
        decimal_exponent = exponent - 1023
        decimal_mantissa = 1 + mantissa
        decimal_mantissa_str = str(decimal_mantissa)[2:18]
        decimal_equivalent = (-1)**sign * decimal_mantissa * 2**decimal_exponent
        (sign, exponent, bin_num[1:], decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent)
        return (sign, exponent, bin_num[1:], decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent)
    else:     
        return "Error: precision no reconocida"

# Function to main
def main():
    num = float(input("Introduce un número decimal: "))

    print("Simple Precision:")
    (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent) = decimal_to_bin(num, "simple")
    hex_simple = decimal_to_hex(num, "simple")
    print(f"Signo: {sign}")
    print(f"Exponente: {exponent} (decimal: {decimal_exponent})")
    print(f"Mantissa: {mantissa} (decimal: {decimal_mantissa_str})")
    print(f"Valor decimal equivalente: {decimal_equivalent}")
    print(f"Binario: {sign}{exponent}{mantissa}")
    print(f"Hexadecimal: {hex_simple}")

    print("Doble Precision:")
    (sign, exponent, mantissa, decimal_exponent, decimal_mantissa, decimal_mantissa_str, decimal_equivalent) = decimal_to_bin(num, "doble")
    hex_doble = decimal_to_hex(num, "doble")
    print(f"Signo: {sign}")
    print(f"Exponente: {exponent} (decimal: {decimal_exponent})")
    print(f"Mantissa: {mantissa} (decimal: {decimal_mantissa_str})")
    print(f"Valor decimal equivalente: {decimal_equivalent}")
    print(f"Binario: {sign}{exponent}{mantissa}")
    print(f"Hexadecimal: {hex_doble}")


    #print binary to presicion simple 
    print("Binario a presición simple:")
    bin_num = input("Introduce un número binario: ")
    (sign, exponent, bin_num, decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent) = bin_to_decimal(bin_num, "simple")
    print(f"Signo: {sign}")
    print(f"Exponente: {exponent} (decimal: {decimal_exponent})")
    print(f"Mantissa: {bin_num} (decimal: {decimal_mantissa_str})")
    print(f"Valor decimal equivalente: {round(decimal_equivalent,5)}")
    print(f"Hexadecimal: {decimal_to_hex(decimal_equivalent, 'simple')}")

    #print binary to presicion doble
    print("Binario a presición doble:")
    bin_num = input("Introduce un número binario: ")
    (sign, exponent, bin_num, decimal_exponent, mantissa, decimal_mantissa_str, decimal_equivalent) = bin_to_decimal(bin_num, "doble")
    print(f"Signo: {sign}")
    print(f"Exponente: {exponent} (decimal: {decimal_exponent})")
    print(f"Mantissa: {bin_num} (decimal: {decimal_mantissa_str})")
    print(f"Valor decimal equivalente: {decimal_equivalent}")
    print(f"Hexadecimal: {decimal_to_hex(decimal_equivalent, 'doble')}")


if __name__ == "__main__":
    main()
