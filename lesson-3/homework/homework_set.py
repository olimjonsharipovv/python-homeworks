def union_of_sets(set1, set2):
    return set1.union(set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = union_of_sets(set1, set2)
print(f"The union of the two sets is: {union_set}")

#2
def intersection_of_sets(set1, set2):
    return set1.intersection(set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = intersection_of_sets(set1, set2)
print(f"The intersection of the two sets is: {intersection_set}")

#3
def difference_of_sets(set1, set2):
    return set1.difference(set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference_set = difference_of_sets(set1, set2)
print(f"The difference of the two sets is: {difference_set}")

#4
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 <= union_set)

#5
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(5 in set2)

#6
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(len(set1))

#7
set1 = {1, 2, 3, 4}
list1 = {3, 4, 5, 6}

converted_set = set(list1)
print(converted_set)

#8
my_set = {1, 2, 3, 4, 5}
element_to_remove = 3
my_set.discard(element_to_remove)

print(my_set)  


#9
set4 = set1.copy()
set4.clear()
print(set4)

#10
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(len(set1) == 0)

#11
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result_set = set1 ^ set2 

print(result_set) 

#12
my_set = {1, 2, 3, 4}
element_to_add = 5

my_set.add(element_to_add)  
print(my_set) 

#13
my_set = {1, 2, 3, 4, 5}

removed_element = my_set.pop() 

print("Removed element:", removed_element)
print("Updated set:", my_set)

#14

max_element = max(set4)
print(max_element)

#15
min_element = min(set4)
print(min_element)

#16
my_set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_set = {num for num in my_set if num % 2 == 0}

print(even_set)  

#17
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
odd_set = {num for num in my_set if num % 2 != 0}

print(odd_set)  

#18
num_set = set(range(1, 11)) 

print(num_set) 

#19
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

merged_set = set(list1) | set(list2)  
print(merged_set) 

#20
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}

if set1.isdisjoint(set2):
    print("The sets have no elements in common.")
else:
    print("The sets share some elements.")

#21
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

unique_list = list(set(my_list))

print(unique_list)  

#22
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

unique_count = len(set(my_list))

print("Count of unique elements:", unique_count)  


#23



























