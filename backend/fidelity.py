points_db = {}

def add_points(user_id, action):
    if user_id not in points_db:
        points_db[user_id] = 0
    if action == "chat":
        points_db[user_id] += 1
    elif action == "purchase":
        points_db[user_id] += 10

def get_points(user_id):
    return points_db.get(user_id, 0)
