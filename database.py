import sqlite3
import json

json_string = '{"user1": 100}'

try:
    data = json.loads(json_string)
except json.JSONDecodeError as e:
    print("An error occurred while decoding the JSON data:", e)

def save_to_file(data, file_path):
    with open(file_path, 'w') as f:
        f.write(json.dumps(data))

def add_user(data, user_id, username, level, xp):
    data[user_id] = {
        'username': username,
        'level': level,
        'xp': xp
    }
    save_to_file(data, 'data.json')
    return data

def get_user(data, user_id):
    return data.get(user_id)

def update_xp(data, user_id, xp):
    user = get_user(data, user_id)
    if user:
        user['xp'] = xp
        save_to_file(data, 'data.json')
    return data

def update_level(data, user_id, level):
    user = get_user(data, user_id)
    if user:
        user['level'] = level
        save_to_file(data, 'data.json')
    return data

class XP:
    def __init__(self):
        self.conn = sqlite3.connect('xp.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                discord_id TEXT,
                username TEXT,
                xp INTEGER,
                level INTEGER
            )
        ''')
        self.conn.commit()

    def add_xp(self, discord_id, username, points):
        self.cursor.execute('''
            INSERT OR IGNORE INTO users (discord_id, username, xp, level)
            VALUES (?, ?, 0, 1)
        ''', (discord_id, username))
        self.cursor.execute('''
            UPDATE users
            SET xp = xp + ?
            WHERE discord_id = ?
        ''', (points, discord_id))
        self.conn.commit()

    def subtract_xp(self, discord_id, points):
        self.cursor.execute('''
            UPDATE users
            SET xp = xp - ?
            WHERE discord_id = ?
        ''', (points, discord_id))
        self.conn.commit()
