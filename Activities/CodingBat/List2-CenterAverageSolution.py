# https://codingbat.com/prob/p126968 centered average


# Return the "centered" average of an array of ints, which we'll
# say is the mean average of the values, except ignoring the largest
# and smallest values in the array. If there are multiple copies of
# the smallest value, ignore just one copy, and likewise for the
# largest value. Use int division to produce the final average.
# You may assume that the array is length 3 or more.
#
#
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
    # nums.sort() careful -- introduces side effects!
    nums_copy = sorted(nums)
    trunc_copy = nums_copy[1:len(nums) - 1]
    return sum(trunc_copy) // len(trunc_copy)


print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))

nums = [2, 1, -32000, 3, 4000]
print(nums)
print(centered_average(nums))  # careful, watch for side effects!
print(nums)                    # will be different if nums.sort() was used
