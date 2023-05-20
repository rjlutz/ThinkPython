# https://learn.zybooks.com/zybook/LutzPython3May2023/chapter/8/section/3

# Write a loop to print all elements in hourly_temperature. Separate elements with a -> surrounded by spaces.
#
# Sample output for the given program with input: '90 92 94 95'
# 90 -> 92 -> 94 -> 95
# Note: 95 is followed by a space, then a newline.

# user_input = input()
# hourly_temperature = user_input.split()
#
# ''' Your solution goes here '''

# user_input = input()
# or
user_input = "90 92 94 95"

hourly_temperature = user_input.split()


''' Your solution goes here '''
for index, temp in enumerate(hourly_temperature):
    if index > 0:
        print(f'->', end=" ")
    print(f'{temp}', end=" ")
print()
