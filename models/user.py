class User:
    def __init__(self, user_id, username, email, password_hash, date_created):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.date_created = date_created