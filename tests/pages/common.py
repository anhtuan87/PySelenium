from heapq import merge
import random
import string
import time
import uuid


def wait(seconds):
    time.sleep(seconds)


def generate_random_string(prefix=""):
    return prefix + uuid.uuid4().hex


def generate_random_number(length=4, prefix=""):
    return prefix + ''.join(random.choice(string.digits) for x in range(length))

    
def is_list_sorted(list, ascending=True):
    return list == sorted(list, key=str.lower, reverse=not ascending)


def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

        
def is_list_contained(list, items, match_order=True):
    if items == []: return list == []
    subset = intersection(items, list) == items
    if match_order: return subset and intersection(list, items) == intersection(items, list)
    return subset


def merge_linked_lists(*lists):
    "Merge multiple sorted linked lists."
    return merge(lists)
