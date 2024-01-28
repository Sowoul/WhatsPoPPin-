from collections import deque
class PostManager:
    def __init__(self):
        self.posts=deque()
        self.posts.appendleft({
        'username': 'Shreetama',
        'image_url': 'https://media.licdn.com/dms/image/D5603AQEwOcsB83GsxQ/profile-displayphoto-shrink_800_800/0/1701112592806?e=1712188800&v=beta&t=FUsQoVMSNW2GGmc9iCvisJx6Q_cp48w7CXAOrJfM_o8'
    })
        self.posts.appendleft({
        'username': 'Ojaswa',
        'image_url': 'https://media.licdn.com/dms/image/D4D03AQGBWNHjbio17w/profile-displayphoto-shrink_800_800/0/1689695616193?e=1712188800&v=beta&t=IuJ0YkGDXsX00YvMOFtIZfrPLJlhZV6lRqUOqdfDNdY'
    })

    def add_post(self, post):
        self.posts.appendleft(post)

    def get_all_posts(self):
        return self.posts
