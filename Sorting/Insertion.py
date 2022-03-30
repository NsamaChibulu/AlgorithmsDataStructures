def insertion_sort(list):
    #First we start a loop that begins at index 1 and runs through entire array
    for index in range(1, len(list)):
        #within each pass through, we we save the value we're "removing"
        # in a variable called temp_value
        temp_value = list[index]
        #Next, we create a variable called "position", which will start immediately to the left of the index
        #temp_value       
        #As we move through the pass-through, this position will keep moving 
        #leftward as we compare each value to temp_value
        position = index - 1
        # We then begin an inner "while" loop, which runs as long as position is greater or equal to zero 
        while position >= 0:
            #we then perform our comparison. That is, we check whether the value at position is greater than the temp_value
            if list[position] > temp_value:
                #if it is, we then shift that left value to the right. 
                list[position+1] = list[position]
                #we then decrement position by 1 to compare the next left value against the 
                #temp_value in the next round of the loop.
                position = position - 1
            #if at any point we encounter a value at position that is greater or equal to the temp_value,
            # we can get ready to end our pass through, since its them to move the temp_value into the gap
            else: 
                break
        #final step of each pass-through is moving the temp_value into the gap
        list[position + 1] = temp_value
    #after all pass-throughs have been completed, we return the sorted array.
    return list


list = [3, 1, 41, 59, 26, 53, 59]
print(list)
insertion_sort(list)

# Let's see the list after we run the Selection Sort
print(list)
