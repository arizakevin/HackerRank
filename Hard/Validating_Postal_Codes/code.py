import re


regex_integer_in_range = r"^[1-9][\d]{5}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.

PostalCode = input()
isValid = (
    bool(re.match(regex_integer_in_range, PostalCode))
    and
    len(re.findall(regex_alternating_repetitive_digit_pair, PostalCode)) < 2
)

print(isValid)
