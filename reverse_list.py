
#project-8b

#Gabriel Venegas
#GitHub username: GVenegas1
#Date: 11/19/2025

def reverse_list(list):
    start = 0
    end = len(list) - 1

    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1

example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_list(example)
print(example)