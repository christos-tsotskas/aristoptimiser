import time
from flask import Flask, request, jsonify

app = Flask(__name__)
users_seen = {}

@app.route('/')
def hello():
    user_agent = request.headers.get('User-Agent')
    return 'Hello! I see you are using %s' % user_agent

@app.route('/checkin/<user>', methods=['POST'])
def check_in(user):
    users_seen[user] = time.strftime('%Y-%m-%d')
    return jsonify(success=True, user=user)

@app.route('/last-seen/<user>')
def last_seen(user):
    if user in users_seen:
        return jsonify(user=user, date=users_seen[user])
    else:
        return jsonify(error='Who dis?', user=user), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)