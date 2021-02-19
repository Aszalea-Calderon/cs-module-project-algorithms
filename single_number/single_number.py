'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# UNDERSTANDING#
# our input will non empty array
# all input in array will be numbers
# all numbers will repeat expept one number

# we want out the non repeating number, there is only one.

# If we have a collections of things we can loop


# Planning #
# loop through the array, .map? .filter?
# if first item is = to second item
# if they do add it to a different array
# if not then you win? Yaassss


def single_number(arr):
    yeahhh_list =[]
    for el in arr:
        if el not in yeahhh_list:
            yeahhh_list.append(el)
        else:
            yeahhh_list.remove(el)

    print("maybe_list", yeahhh_list)
    return yeahhh_list[0]

    #     if el not in nah_list:
    #         nah_list.append(el)
    #     else:
    #         maybe_list.append(el)

        # take the element you want
        # Then loop through checking the next element

    # for i in range(len(arr)):
    #     # if arr[i] == arr[i +1]:
    #     for
    # This is an O(1) space complexity answer,
def single_number2(arr):
    answer = 0
    for el in arr:
        answer ^= el # this is a bitwise opperator, it is an exclusive or. it does binary stuufff. This would not work with negitive numbers.
    return answer





if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number2(arr)}")