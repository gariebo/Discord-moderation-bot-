class XP:
    def __init__(self):
        self.data = {}

    def add_xp(self, user, points):
        if user in self.data:
            self.data[user] += points
        else:
            self.data[user] = points

    def subtract_xp(self, user, points):
        if user in self.data:
            self.data[user] -= points
        else:
            raise ValueError("User does not exist in the XP system.")

    def get_xp(self, user):
        if user in self.data:
            return self.data[user]
        else:
            raise ValueError("User does not exist in the XP system.")
