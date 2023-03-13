#(1)

def roman_to_arabic(s):
    translations = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
            number += translations[char]
    print("Roman numeral: MCMXCIV", "Arabic numeral:", number)
		
roman_to_arabic('MCMXCIV')

#(2)

def roman_to_arabic(roman_numeral):
    roman_symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabic_symbols = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    arabic_numeral = 0
    i = 0
    for idx, r in enumerate(roman_symbols):
        while roman_numeral[i:i + len(r)] == r:
            arabic_numeral += arabic_symbols[idx]
            i += len(r)
    return arabic_numeral
roman_numeral = 'MCMXCIV'
arabic_numeral = roman_to_arabic(roman_numeral)
print("Roman numeral:", roman_numeral, "Arabic numeral:", arabic_numeral)
