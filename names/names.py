import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

with open('names_1.txt', 'r') as f:
    names_1 = f.read().split("\n")  # List containing 10000 names

with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names

duplicates = []
# Initialize BST w/ first name in names_1
bst = BinarySearchTree(names_1[0])
# Insert the rest of the names from names_1
for name_1 in names_1[1:]:
    bst.insert(name_1)
# Search BST for each name in name_2
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time() # First run in 0.1 seconds
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

