#1
def count_occurrences(lst, element):
    return lst.count(element)

my_list = [1, 2, 3, 4, 2, 2, 5, 2]
element_to_count = 2
result = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {result} times in the list.")

#2
def calculate_total(lst):
    return sum(lst)

my_list = [10, 20, 30, 40, 50]
total = calculate_total(my_list)
print(f"The total of all elements in the list is: {total}")

#3
def find_largest_element(lst):
    return max(lst)

my_list = [10, 20, 30, 40, 50]
largest_element = find_largest_element(my_list)
print(f"The largest element in the list is: {largest_element}")

#4
def find_smallest_element(lst):
    return min(lst)

my_list = [10, 20, 30, 40, 5]
smallest_element = find_smallest_element(my_list)
print(f"The smallest element in the list is: {smallest_element}")

#5
def is_element_present(lst, element):
    return element in lst

my_list = [10, 20, 30, 40, 50]
element_to_check = 30
if is_element_present(my_list, element_to_check):
    print(f"The element {element_to_check} is present in the list.")
else:
    print(f"The element {element_to_check} is not present in the list.")

#6
def get_first_element(lst):
    return lst[0] if lst else None


my_list = [10, 20, 30, 40, 50]
first_element = get_first_element(my_list)

if first_element is not None:
    print(f"The first element in the list is: {first_element}")
else:
    print("The list is empty.")

#7
def get_last_element(lst):
    return lst[-1] if lst else None

my_list = [10, 20, 30, 40, 50]
last_element = get_last_element(my_list)

if last_element is not None:
    print(f"The last element in the list is: {last_element}")
else:
    print("The list is empty.")

#8
def get_first_three_elements(lst):
    return lst[:3]

my_list = [10, 20, 30, 40, 50]
first_three_elements = get_first_three_elements(my_list)
print(f"The first three elements of the list are: {first_three_elements}")

#9
def reverse_list(lst):
    return lst[::-1]

my_list = [10, 20, 30, 40, 50]
reversed_list = reverse_list(my_list)
print(f"The reversed list is: {reversed_list}")

#10
def sort_list(lst):
    return sorted(lst)

my_list = [50, 20, 40, 10, 30]
sorted_list = sort_list(my_list)
print(f"The sorted list is: {sorted_list}")

#11
def get_unique_elements(lst):
    return list(set(lst))

my_list = [10, 20, 30, 20, 40, 10, 50]
unique_elements = get_unique_elements(my_list)
print(f"The list with unique elements is: {unique_elements}")

#12
def insert_element(lst, element, index):
    lst.insert(index, element)
    return lst

my_list = [10, 20, 30, 40, 50]
element_to_insert = 25
index_to_insert = 2
new_list = insert_element(my_list, element_to_insert, index_to_insert)
print(f"The list after inserting {element_to_insert} at index {index_to_insert} is: {new_list}")

#13
def find_first_index(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1  # Return -1 if the element is not found

my_list = [10, 20, 30, 20, 40, 50]
element_to_find = 20
index = find_first_index(my_list, element_to_find)

if index != -1:
    print(f"The first occurrence of {element_to_find} is at index: {index}")
else:
    print(f"The element {element_to_find} is not found in the list.")

#14
def is_list_empty(lst):
    return not lst

my_list = []
if is_list_empty(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")

#15
def count_even_numbers(lst):
    return sum(1 for num in lst if num % 2 == 0)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = count_even_numbers(my_list)
print(f"The number of even numbers in the list is: {even_count}")

#16
def count_odd_numbers(lst):
    return sum(1 for num in lst if num % 2 != 0)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_count = count_odd_numbers(my_list)
print(f"The number of odd numbers in the list is: {odd_count}")

#17
def concatenate_lists(list1, list2):
    return list1 + list2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = concatenate_lists(list1, list2)
print(f"The combined list is: {combined_list}")

#18
def is_sublist(main_list, sublist):
    # Convert both lists to strings and check for substring
    return str(sublist)[1:-1] in str(main_list)[1:-1]

main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist = [3, 4, 5]
if is_sublist(main_list, sublist):
    print("The sublist exists within the main list.")
else:
    print("The sublist does not exist within the main list.")

#19
def replace_first_occurrence(lst, old_element, new_element):
    if old_element in lst:
        index = lst.index(old_element)
        lst[index] = new_element
    return lst

my_list = [10, 20, 30, 20, 40, 50]
old_element = 20
new_element = 99
updated_list = replace_first_occurrence(my_list, old_element, new_element)
print(f"The updated list is: {updated_list}")

#20
def find_second_largest(lst):
    if len(lst) < 2:
        return None  # Return None if the list has fewer than 2 elements

    sorted_list = sorted(lst, reverse=True)
    return sorted_list[1]

my_list = [10, 20, 30, 40, 50]
second_largest = find_second_largest(my_list)
if second_largest is not None:
    print(f"The second largest element in the list is: {second_largest}")
else:
    print("The list does not have enough elements to find the second largest.")

#21
def find_second_smallest(lst):
    if len(lst) < 2:
        return None  # Return None if the list has fewer than 2 elements

    sorted_list = sorted(lst)
    return sorted_list[1]

my_list = [50, 40, 30, 20, 10]
second_smallest = find_second_smallest(my_list)
if second_smallest is not None:
    print(f"The second smallest element in the list is: {second_smallest}")
else:
    print("The list does not have enough elements to find the second smallest.")

#22
even_lst = [x for x in lst if x % 2 == 0]
print(even_lst)

#23
odd_lst = [x for x in lst if x % 2 != 0]
print(odd_lst)

#24
print(len(lst))

#25
copy_lst = lst.copy()
print(copy_lst)

#26
n = len(lst)
middle = lst[n//2] if n % 2 == 1 else lst[n//2 - 1:n//2 + 1]
print(middle)

#27
subsection = lst[1:5]
max_value = max(subsection)
print(max_value)

#28
print(min(subsection))

#29
def find_second_smallest(lst):
    if len(lst) < 2:
        return None  # Return None if the list has fewer than 2 elements

    sorted_list = sorted(lst)
    return sorted_list[1]

my_list = [50, 40, 30, 20, 10]
second_smallest = find_second_smallest(my_list)
if second_smallest is not None:
    print(f"The second smallest element in the list is: {second_smallest}")
else:
    print("The list does not have enough elements to find the second smallest.")

#30
print(lst == sorted(lst))

#31
repeat_number = 3
repeated_lst = [x for x in lst for _ in range(repeat_number)]
print(repeated_lst)

#32
merged_sorted = sorted(lst + lst2)
print(merged_sorted)

#33
all_indices = [i for i, x in enumerate(lst) if x == 2]
print(all_indices)

#34
def rotate_list_right(lst, positions):
    positions = positions % len(lst)
    return lst[-positions:] + lst[:-positions]

my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list_right(my_list, 2)
print(f"The rotated list is: {rotated_list}")

#35
range_lst = list(range(1, 11))
print(range_lst)

#36
print(sum(x for x in lst if x > 0))

#37
print(sum(x for x in mixed_lst if x < 0))

#38
print(lst == lst[::-1])

#39

#40
def get_unique_elements_ordered(lst):
    seen = set()
    unique_elements = []
    for item in lst:
        if item not in seen:
            unique_elements.append(item)
            seen.add(item)
    return unique_elements


my_list = [3, 5, 2, 5, 3, 8, 1, 2]
unique_list = get_unique_elements_ordered(my_list)
print(f"The list with unique elements (order preserved) is: {unique_list}")
























