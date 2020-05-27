"""
This program is developed for conversion of Arabic numbers to Roman Numerals.
DATE : 27-05-2020
DEVELOPER : SURIYA KRISHNAN
"""


def subtractive_notation(arabic_number):
    """
     Subtractive Notation method is useful for converting Arabic numbers into corresponding Roman Numerals
     1. Range of Roman Numerals from 1 to 3999
     2. There is no negative Roman Numerals and there is no roman numeral for Zero
     3. The Roman numerals never repeat a symbol more than three times
    """

    # Tuples are immutable, so using it in the indirect mapping of arabic_numerals
    # Arabic_Roman Mappings are initialized only for certain subtracting pairs (IV,IX,XL,XC,CD,CM)
    # Rest all are addition anyway but to make the code easier we are initializing certain other values

    arabic_numerals = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    roman_numerals = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    max_roman = 3999
    i = 0
    list_output = []

    # Validations for the input
    try:
        arabic_number = int(arabic_number)
    except ValueError:
        raise ValueError("Wrong Input...Input value must be an Integer without float")

    if arabic_number <= 0 or arabic_number > max_roman:
        raise ValueError("The value should start from 1 to %d because there are no negative Roman "
                         "Numerals nor there is a Roman Numeral for Zero" % max_roman)
    else:
        while arabic_number > 0:
            if arabic_number - arabic_numerals[i] >= 0:
                list_output.append(roman_numerals[i])
                arabic_number -= arabic_numerals[i]
            else:
                i += 1
        return "".join(list_output)


if __name__ == "__main__":
    # Input for the conversion
    number = input("Please enter a value to be converted to Roman Numerals: \n")  # Float numbers are not allowed
    print("The input value is converted into %s" % subtractive_notation(number))

