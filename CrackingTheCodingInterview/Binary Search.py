#

def binary_search(input_array, value):
    """Your code goes here."""
    last_element=len(input_array)-1
    first_element=0
    ret_value=0;
    while first_element <= last_element:
        mid_element =int( (last_element + first_element) / 2)
        #print(mid_element)
        if(value< input_array[mid_element] and value>input_array[first_element]):
            # value is in first half
            last_element=mid_element-1;
        elif(value > input_array[mid_element] and value<input_array[last_element]):
            # value is in second half
            first_element=mid_element+1;

        elif(value == input_array[mid_element]):
            # item found
            ret_value = 1;
            break;
        else:
            ret_value=-1
            break
    return ret_value

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))