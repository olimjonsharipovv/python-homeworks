#1
def count_occurrences(tup, element):
    return tup.count(element)

my_tuple = (1, 2, 3, 4, 2, 2, 5, 2, 4, 6)
element_to_count = 2
result = count_occurrences(my_tuple, element_to_count)
print(f"The element {element_to_count} appears {result} times in the tuple.")

#2
def find_largest_element(tup):
    return max(tup)

my_tuple = (10, 20, 30, 40, 50)
largest_element = find_largest_element(my_tuple)
print(f"The largest element in the tuple is: {largest_element}")

#3
def find_smallest_element(tup):
    return min(tup)

# Example usage:
my_tuple = (10, 20, 30, 40, 50)
smallest_element = find_smallest_element(my_tuple)
print(f"The smallest element in the tuple is: {smallest_element}")

#4
def is_element_present(tup, element):
    return element in tup

my_tuple = (10, 20, 30, 40, 50)
element_to_check = 30
if is_element_present(my_tuple, element_to_check):
    print(f"The element {element_to_check} is present in the tuple.")
else:
    print(f"The element {element_to_check} is not present in the tuple.")

#5
def get_first_element(tup):
    return tup[0] if tup else None

my_tuple = (10, 20, 30, 40, 50)
first_element = get_first_element(my_tuple)

if first_element is not None:
    print(f"The first element in the tuple is: {first_element}")
else:
    print("The tuple is empty.")

#6
def get_last_element(tup):
    return tup[-1] if tup else None

my_tuple = (10, 20, 30, 40, 50)
last_element = get_last_element(my_tuple)

if last_element is not None:
    print(f"The last element in the tuple is: {last_element}")
else:
    print("The tuple is empty.")

#7
def count_elements(tup):
    return len(tup)

my_tuple = (10, 20, 30, 40, 50)
num_elements = count_elements(my_tuple)
print(f"The number of elements in the tuple is: {num_elements}")

#8
def get_first_three_elements(tup):
    return tup[:3]

my_tuple = (10, 20, 30, 40, 50)
first_three_elements = get_first_three_elements(my_tuple)
print(f"The first three elements of the tuple are: {first_three_elements}")

#9
def combine_tuples(tup1, tup2):
    return tup1 + tup2

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = combine_tuples(tuple1, tuple2)
print(f"The combined tuple is: {combined_tuple}")

#10
def is_tuple_empty(tup):
    return not tup

my_tuple = ()
if is_tuple_empty(my_tuple):
    print("The tuple is empty.")
else:
    print("The tuple is not empty.")

#11
def find_all_indices(tup, element):
    return [index for index, value in enumerate(tup) if value == element]

my_tuple = (10, 20, 30, 20, 40, 20)
element_to_find = 20
indices = find_all_indices(my_tuple, element_to_find)
print(f"The indices of {element_to_find} in the tuple are: {indices}")

#12
def second_largest(tup):
    unique_elements = list(set(tup))  
    if len(unique_elements) < 2:
        return None  
    unique_elements.sort(reverse=True)  
    return unique_elements[1]  

my_tuple = (10, 20, 4, 45, 99, 99, 20)
print(second_largest(my_tuple))  


#13
second_smallest = unique_tup[1] if len(unique_tup) >= 2 else None
print(second_smallest)

#14
single_element_tup = (99,)
print(single_element_tup)

#15
def list_to_tuple(lst):
    return tuple(lst)

my_list = [1, 2, 3, 4, 5]
my_tuple = list_to_tuple(my_list)
print(f"The tuple created from the list is: {my_tuple}")

#16
def is_sorted_ascending(t):
    return t == tuple(sorted(t))

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (5, 3, 1, 4, 2)

print(is_sorted_ascending(tuple1))  
print(is_sorted_ascending(tuple2))  

#17
subtup = tup[1:5]
print(max(subtup))

#18
print(min(subtup))

#19
def remove_element_by_value(tup, element):
    # Convert the tuple to a list for easier manipulation
    lst = list(tup)
    if element in lst:
        lst.remove(element)  # Remove the first occurrence of the element
    return tuple(lst)  # Convert the list back to a tuple

my_tuple = (10, 20, 30, 20, 40, 50)
element_to_remove = 20
new_tuple = remove_element_by_value(my_tuple, element_to_remove)
print(f"The new tuple after removing the first occurrence of {element_to_remove} is: {new_tuple}")

#20
def create_nested_tuple(tup, subtuple_size):
    return tuple(tup[i:i + subtuple_size] for i in range(0, len(tup), subtuple_size))

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
subtuple_size = 3
nested_tuple = create_nested_tuple(my_tuple, subtuple_size)
print(f"The nested tuple is: {nested_tuple}")

#21
tup = (1, 2, 3)
repeat = 3
result1 = []
for x in tup:
    for i in range(repeat):
        result1.append(x)
repeated_tup = tuple(result1)
print(repeated_tup)

#22
range_tup = tuple(range(1, 11))
print(range_tup)

#23
print(tup[::-1])

#24
print(tup == tup[::-1])

#25
unique_in_order = []
for x in tup:
    if x not in unique_in_order:
        unique_in_order.append(x)
print(tuple(unique_in_order))


















