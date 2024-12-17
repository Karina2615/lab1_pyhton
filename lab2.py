# -*- coding: utf-8 -*-
import csv

#task 1
'''
file_path = "/mnt/c/Users/karin/OneDrive/Desktop/studying/python/Lab2/netflix_list.csv"

name = []
list = []
with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    csv_reader = csv.reader(f, delimiter=',')
    name = next(csv_reader)  
    for row in csv_reader:
        list.append(row)
'''

'''
rating = name.index("rating")
above_7_5_list = [x for x in list if x[rating] != "" and float(x[rating]) > 7.5]

for i in above_7_5_list:  
    print(f"{i[1]}, {i[rating]}")
'''

'''
first_5_column = [x[:5] for x in list]

for i in first_5_column:
    print(i)

'''

'''
def eng(lst):
    lang_index = name.index('language')
    for i in lst:
        if i[lang_index] == 'English':
            yield i

for row in eng(list):
    print(f"{row[1]} - {row[10]}")

'''

'''
def ended_2015(lst):
    end_index = name.index('endYear')
    for i in lst:
        if i[end_index] != '' and int(i[end_index]) >= 2015:
            yield i

for row in ended_2015(list):
    print(f"{row[1]} - {row[5]}")

'''
'''
class CastIterator:
    def __init__(self, dataset, field_name):
        self.dataset = dataset
        self.cast_index = name.index(field_name)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_index < len(self.dataset):
            row = self.dataset[self.current_index]
            self.current_index += 1
            if len(row[self.cast_index]) > 50:
                return row[self.cast_index]
        raise StopIteration

    print("\nFirst 10 entries with 'cast' length > 50:")
cast_iterator = CastIterator(list, "cast")
for i, cast in enumerate(cast_iterator):
    if i >= 10:
        break
    print(f"{i + 1}: {cast}")
    '''

'''
def analyze_dataset(dataset, headers):
    is_adult_index = headers.index("isAdult")
    rating_index = headers.index("rating")
    num_votes_index = headers.index("numVotes")
    
    adult_count = sum(1 for row in dataset if row[is_adult_index] == "1")
    
    ratings = []
    for row in dataset:
        try:
            num_votes = float(row[num_votes_index])  
            if num_votes > 1000:
                rating = float(row[rating_index])  
                ratings.append(rating)
        except ValueError:
            pass  

    average_rating = sum(ratings) / len(ratings) if ratings else 0
    return adult_count, average_rating

adult_count, average_rating = analyze_dataset(list, name)

print(f"Number of adult shows/movies (isAdult == 1): {adult_count}")
print(f"Average rating of shows/movies with more than 1000 votes: {average_rating:.2f}")

def filter_shows_by_episodes_and_rating(dataset, headers, avg_rating):
    title_index = headers.index("title")
    episodes_index = headers.index("episodes")
    rating_index = headers.index("rating")
    
    for row in dataset:
        try:
            episodes = int(row[episodes_index]) 
            rating = float(row[rating_index])  
            if episodes > 10 and rating > avg_rating:
                yield row[title_index]
        except ValueError:
            pass  

filtered_shows = filter_shows_by_episodes_and_rating(list, name, average_rating)

filtered_show_titles = [title for title in filtered_shows]

print("\nTitles of shows with more than 10 episodes and rating above average:")
for title in filtered_show_titles:
    print(title)

    '''

    #task 2

class Node:
    def __init__(self, key):
        self.key = key  
        self.left = None  
        self.right = None  
        self.height = 1  


class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def pre_order(self, root):
        if not root:
            return
        print(f"{root.key} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

if __name__ == "__main__":
    tree = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]

    for key in keys:
        root = tree.insert(root, key)

    print("Pre-order traversal of the AVL tree is:")
    tree.pre_order(root)
    print()
