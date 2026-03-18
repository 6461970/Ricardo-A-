reminders_db = {}

def add_reminder(user_id, reminder_text):
    if user_id not in reminders_db:
        reminders_db[user_id] = []
    reminders_db[user_id].append(reminder_text)

def get_reminders(user_id):
    return reminders_db.get(user_id, [])
