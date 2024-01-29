from collections import deque
import json
"""
For O(1) Time Complexity when Adding a new post, using a deque.
"""
class PostManager:
    def __init__(self, filename="posts.json"):
        self.filename = filename
        self.posts = deque()
        self.load_posts()

    def load_posts(self):
        try:
            with open(self.filename, 'r') as file:
                self.posts.extend(json.load(file))
        except FileNotFoundError:
            pass 
    
    def save_posts(self):
        with open(self.filename, 'w') as file:
            json.dump(list(self.posts), file)

    def add_post(self, post):
        self.posts.appendleft(post)
        self.save_posts()

    def get_all_posts(self):
        return self.posts
