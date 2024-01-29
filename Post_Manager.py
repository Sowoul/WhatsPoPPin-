from collections import deque
import json
"""
Simple PostManager Object that used a queue to store the image, to keep O(1) time complexity, 
while returning in time based order.
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
    def delete_posts(self):
        self.posts.popleft()
        self.save_posts()
    def save_posts(self):
        with open(self.filename, 'w') as file:
            json.dump(list(self.posts), file)

    def add_post(self, post):
        self.posts.appendleft(post)
        self.save_posts()

    def get_all_posts(self):
        return self.posts
if __name__ == '__main__':
    postmanager = PostManager()
    postmanager.delete_posts()
