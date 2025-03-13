#1
def get_value(dictionary, key, default=None):
    return dictionary.get(key, default)

my_dict = {"a": 1, "b": 2}
print(get_value(my_dict, "a"))  
print(get_value(my_dict, "c", "Not Found"))  

#2
def check_key(dictionary, key):
    return key in dictionary

my_dict = {"a": 1, "b": 2}
print(check_key(my_dict, "a"))  
print(check_key(my_dict, "c"))  

#3
def count_keys(dictionary):
    return len(dictionary)

my_dict = {"a": 1, "b": 2, "c": 3}
print(count_keys(my_dict))  

#4
def get_all_keys(dictionary):
    return list(dictionary.keys())

my_dict = {"a": 1, "b": 2, "c": 3}
print(get_all_keys(my_dict)) 

#5
def get_all_values(dictionary):
    return list(dictionary.values())

my_dict = {"a": 1, "b": 2, "c": 3}
print(get_all_values(my_dict)) 

#6

#7
def remove_key(dictionary, key):
    dictionary.pop(key, None)

my_dict = {"a": 1, "b": 2}
remove_key(my_dict, "a")
print(my_dict) 

#8
def clear_dict():
    return {}

print(clear_dict()) 

#9
def is_dict_empty(dictionary):
    return not bool(dictionary)

print(is_dict_empty({})) 
print(is_dict_empty({"a": 1}))  

#10
def get_key_value(dictionary, key):
    return (key, dictionary[key]) if key in dictionary else None

my_dict = {"a": 1, "b": 2}
print(get_key_value(my_dict, "a")) 
print(get_key_value(my_dict, "c"))  

#11
def update_value(dictionary, key, value):
    dictionary[key] = value

my_dict = {"a": 1, "b": 2}
update_value(my_dict, "a", 10)
print(my_dict)  

#12
from collections import Counter

def count_value_occurrences(dictionary):
    return Counter(dictionary.values())

my_dict = {"a": 1, "b": 2, "c": 1, "d": 2, "e": 3}
print(count_value_occurrences(my_dict)) 

#13
def invert_dict(dictionary):
    return {v: k for k, v in dictionary.items()}

my_dict = {"a": 1, "b": 2, "c": 3}
print(invert_dict(my_dict)) 

#14
def find_keys_with_value(dictionary, value):
    return [k for k, v in dictionary.items() if v == value]

my_dict = {"a": 1, "b": 2, "c": 1}
print(find_keys_with_value(my_dict, 1))  

#15
def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

keys = ["a", "b", "c"]
values = [1, 2, 3]
print(create_dict_from_lists(keys, values)) 

#16
def has_nested_dict(dictionary):
    return any(isinstance(v, dict) for v in dictionary.values())

my_dict = {"a": 1, "b": {"c": 2}, "d": 3}
print(has_nested_dict(my_dict))  

#17
def get_nested_value(dictionary, key1, key2):
    return dictionary.get(key1, {}).get(key2)

my_dict = {"a": {"b": 10}, "c": 5}
print(get_nested_value(my_dict, "a", "b")) 
print(get_nested_value(my_dict, "a", "c"))  

#18
from collections import defaultdict

def create_default_dict(default_value):
    return defaultdict(lambda: default_value)

my_dict = create_default_dict(0)
print(my_dict["a"])  

#19
def count_unique_values(dictionary):
    return len(set(dictionary.values()))

my_dict = {"a": 1, "b": 2, "c": 1}
print(count_unique_values(my_dict)) 

#20
def sort_dict_by_key(dictionary):
    return dict(sorted(dictionary.items()))

my_dict = {"b": 2, "a": 1, "c": 3}
print(sort_dict_by_key(my_dict))  

#21
def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1]))

my_dict = {"a": 3, "b": 1, "c": 2}
print(sort_dict_by_value(my_dict))  

#22
def filter_by_value(dictionary, condition):
    return {k: v for k, v in dictionary.items() if condition(v)}

my_dict = {"a": 1, "b": 2, "c": 3}
print(filter_by_value(my_dict, lambda x: x > 1))  

#23
def check_common_keys(dict1, dict2):
    return bool(set(dict1.keys()) & set(dict2.keys()))

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(check_common_keys(dict1, dict2))  

#24
def create_dict_from_tuple(tuple_pairs):
    return dict(tuple_pairs)

tuple_pairs = [("a", 1), ("b", 2)]
print(create_dict_from_tuple(tuple_pairs))  

#25
def get_first_key_value(dictionary):
    return next(iter(dictionary.items()), None)

my_dict = {"a": 1, "b": 2}
print(get_first_key_value(my_dict))  




















