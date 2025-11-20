
#project-8b

#Gabriel Venegas
#GitHub username: GVenegas1
#Date: 11/19/2025
"""This function changes the order of the list in reverse.
It mutates the list and doesn't return anything """

def reverse_list(list):

    #Two pointers: one at the start and one at the end
    start = 0

    #last index in the list
    end = len(list) - 1

#Keep swapping elements until the two pointers meet in the middle
    while start < end:

        #Swap the element at the start and end
        list[start], list[end] = list[end], list[start]

        #Move the pointers towards the middle
        #pointer moves forward to the next element
        start += 1

        #pointer moves backwards to the previous element
        end -= 1

#example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#reverse_list(example)
#print(example)