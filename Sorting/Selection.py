def selection_sort(list):
    #i indicates how many items were sorted
    for i in range(len(list)-1):
        #To find the minimum value of the unsorted segement
        #we first assum that the first element is the lowest
        min_index = i 
        #we then use j to loop through the remaining elemeents
        for j in range(i+1, len(list)-1):
            #update the min_index if the element at j is lower than it
            if list[j] < list[min_index]:
                min_index = j
        # after finding the lowest item of the unsorrted regions, swap with
        #the first unsorted item 
        list[i], list[min_index] = list[min_index], list[i]


list = [3, 1, 41, 59, 26, 53, 59]
print(list)
selection_sort(list)

# Let's see the list after we run the Selection Sort
print(list)

