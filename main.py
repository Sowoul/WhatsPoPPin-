from flask import Flask, render_template, request, redirect, url_for
from Post_Manager import PostManager
from Session_Manager import SessionManager



"""
Initializing the Objects
"""
app = Flask(__name__)
post_manager = PostManager()
session_manager = SessionManager()




"""
This is the homepage, redirects to login if you dont have a proper sessionid
"""
@app.route('/')
def index():
    session_id = request.args.get('sessionid')
    if not session_id:
        return redirect(url_for('login'))
    user_info = session_manager.get_user_by_session(session_id)
    hashtags = ['#BiggBoss17GrandFinale', '#AbhishekKumar', '#MannaraChopra', '#OjaswaSharma']
    posts = post_manager.get_all_posts()
    return render_template('homepage.html', hashtags=hashtags, posts=posts, user_info=user_info)




"""
This handles the login, and assings you a sessionId unique to you so no one else can access your account
"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if session_manager.verify_user(username, password):
            session_id = session_manager.get_session_by_user(username)
            session_manager.create_session(session_id, username)
            return redirect(url_for('index', sessionid=session_id))
        else:
            return render_template('login.html', error_message='Invalid username or password.')
    return render_template('login.html', error_message=None)





"""
This function handles the uploading part of the app, only limited to images for now, also stores the
image info in the posts.json to provide a static storage.
"""
@app.route('/upload', methods=['POST'])
def upload():
    username =request.form['username']
    session_id=session_manager.get_session_by_user(username=username)
    image_url = request.form['image_url']
    post_manager.add_post({'username': username, 'image_url': image_url})
    return redirect(url_for('index', sessionid=session_id))




if __name__ == '__main__':
    app.run(debug=True)
