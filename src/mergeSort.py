#/****************************************************************/ 
# Program:  mergeSort
# Version:  1.0
# Date:     05/25/2014
# Website:  http://www.HumairAhmed.com
#
# Lead Developer:   Humair Ahmed 
#
# Written for educational purposes. Program takes a list of numbers as arguments
# and sorts the list. Displays the final sorted list at end and how long it took to 
# sort in seconds.
#
#  
# License:
# 
# Open source software being distributed under GPL license. For more information see here:
# http://www.gnu.org/copyleft/gpl.html. 
# 
# Can edit and redistribute code as long as above reference of authorship is kept within the code.
#/****************************************************************/

import sys, time


#divides list and makes recursive calls
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
 
    middle = len(unsorted_list) // 2
    left = unsorted_list[:middle]
    right = unsorted_list[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    
    return list(merge(left, right))


#main sort function
def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        #make comparisons between left and right arrays and add smallest value to sorted array
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
 
    if left:
        sorted_list.extend(left[left_index:])
    if right:
        sorted_list.extend(right[right_index:])

    return sorted_list


#main program
def main():
    unsorted_list = list(map(int, sys.argv[1:]))
    
    start_time = time.time()
    sorted_list = merge_sort(unsorted_list)
    stop_time = time.time()
    
    print("\nSorted: ", sorted_list)
    print("Time to sort: ", start_time - stop_time, "\n")
    
    
    
if __name__ == "__main__":
    main()    
    
    