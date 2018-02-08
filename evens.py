from byotest import *

def even_number_of_evens(l):
    
    count = 0
    for int in l:
        if int % 2 == 0:
            count+= 1
    if count % 2 == 0:
        return True
    else:
        return False
        
test_are_equal(even_number_of_evens([]), True)
test_are_equal(even_number_of_evens([2, 5]), False)
test_are_equal(even_number_of_evens([4, 8, 1]), True)
test_are_equal(even_number_of_evens([12, 8, 14,2]), True)
test_are_equal(even_number_of_evens([12, 8, 14]), False)
test_are_equal(even_number_of_evens([1, 13, 5, 9]), True)
test_are_equal(even_number_of_evens([1, 13, 5]), True)
test_are_equal(even_number_of_evens([-2, -4]), True)
test_are_equal(even_number_of_evens([2, 0]), True)

# assert even_number_of_evens([]) == True, "Empty list"
# assert even_number_of_evens([2]) == False, "Odd number of even numbers"
# assert even_number_of_evens([4, 8, 1]) == True, "Even number of even numbers odd number of odd numbers"
# assert even_number_of_evens([12, 8, 14, 2]) == True, "Even number of even numbers"
# assert even_number_of_evens([12, 8, 14]) == False, "Odd number of even numbers"
# assert even_number_of_evens([1, 13, 5, 9]) == True, "Zero numbers of even numbers"
# assert even_number_of_evens([1, 13,5]) == True, "Zero numbers of even numbers"
# assert even_number_of_evens([-2,-4]) == True, "Even numbers"
# assert even_number_of_evens([2, 0]) == True, "Even numbers"

print("All tests pass")