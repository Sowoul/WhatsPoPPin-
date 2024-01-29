import json
import uuid


"""
Creates and stores sessions while active to keep track of user activity, and to give the user info to 
the frontend of the webpage.
"""

class SessionManager:
    def __init__(self, filename='users.json'):
        self.filename = filename
        self.users = {}
        self.sessions = {} 
        self.load_users()

    def load_users(self):
        try:
            with open(self.filename, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            pass

    def save_users(self):
        with open(self.filename, 'w') as file:
            json.dump(self.users, file)

    def verify_user(self, username, password):
        user = self.users.get(username)
        return user and user['password'] == password

    def add_user(self, username, password, user_img_url):
        user_id = str(uuid.uuid4())
        self.users[username] = {'id': user_id, 'user_img': user_img_url, 'password': password, 'username': username}
        self.save_users()

    def create_session(self, user_id, username):
        self.sessions[user_id] = username

    def get_user_by_session(self, user_id):
        username = self.sessions.get(user_id)
        if username:
            return self.users.get(username)
        return None

    def get_session_by_user(self, username):
        return self.users[username]['id']
    
if __name__ == '__main__':
    session=SessionManager()
    session.add_user('username','password','img_url')
