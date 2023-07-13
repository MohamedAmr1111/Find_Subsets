# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:50:26 2023

@author: MG Magic
"""

def FindAllSubsets(unique_elements):
    subsets = [[]]

    for i in unique_elements:
        new_subsets = []  
        for j in subsets:  
            new_subset = j + [i]
            new_subsets.append(new_subset) 
        subsets.extend(new_subsets)   

    return subsets


n = int(input("Enter the number of elements: "))
elements = []

print("Enter the elements:")
for i in range(n):
    num = int(input())
    elements.append(num)
    
def remove_duplicates(elements):
    return list(set(elements))


unique_elements = remove_duplicates(elements)
print("Elements After Removing duplicate = {}".format(unique_elements))
  

subsets = FindAllSubsets(unique_elements)


print("All subsets:")
for i in subsets:
    print(i)
    
print("The number of subsets = {}".format(len(subsets)))




















