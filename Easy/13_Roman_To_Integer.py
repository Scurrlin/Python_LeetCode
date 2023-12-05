# 13 Pseudocode

# 1. Create a dictionary to map Roman numerals to their corresponding integer values.
# 2. Initialize a variable to store the total value.
# 3. Iterate over the Roman numeral string from right to left.
# 4. If the current Roman numeral is greater or equal to the previous one, add its value to the total.
# 5. If the current Roman numeral is less than the previous one, subtract its value from the total.

def roman_to_int(s):
    roman_to_int_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for c in reversed(s):
        current_value = roman_to_int_mapping[c]
        if current_value >= prev_value:
            total += current_value
        else:
            total -= current_value
        prev_value = current_value
    return total

print(roman_to_int('MCMXCIV'))  # Output: 1994

# This function works by iterating over the Roman numeral string from right to left.
# It then adds or subtracts the integer value of the current Roman numeral.
# This acition is dependent on whether it is greater or less than the previous Roman numeral.