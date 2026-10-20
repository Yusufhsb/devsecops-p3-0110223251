class UserModel:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def get_user_info(self):
        return {"username": self.username, "role": self.role}