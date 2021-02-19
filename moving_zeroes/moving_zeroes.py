'''
Input: a List of integers
Returns: a List of integers
'''
#KNOLLEEDDGGGEE#
# we need to move each non-zero to the left
# if there are no zeros nothing happens. Oh noes
# needs to return the altered array. Period. End oh story

## Pseudo knowledge#
# Search for that zero in a for loop d loop
# push the zeros to a new array
# once dat loop finished
# append the zero list to the end of the origin list
# return the Origin array.


def moving_zeroes(arr):
    # Your code here
    zero_array =[]
    for el in arr:
        if el == 0:
            zero_array.append(el)
            arr.remove(el)
    arr.extend(zero_array)
    return arr

def moving_zeros2(arr): # o(n),
    zer0_array= [0]*len(arr)
    counter = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            zer0_array[counter]= arr[i]
            counter +=1
    return zer0_array

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeros2(arr)}")