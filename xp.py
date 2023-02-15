class XP:
    def __init__(self):
        self.xp = {}
        self.levels = [0, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]

    def add_xp(self, user, points):
        if user in self.xp:
            self.xp[user] += points
        else:
            self.xp[user] = points
        print(f"{user} has gained {points} XP and now has a total of {self.xp[user]} XP.")

    def subtract_xp(self, user, points):
        if user in self.xp:
            self.xp[user] -= points

    def get_xp(self, user):
        if user in self.xp:
            return self.xp[user]
        else:
            return 0

    def get_level(self, user):
        xp = self.get_xp(user)
        for i, level_xp in enumerate(self.levels):
            if xp < level_xp:
                return i
        return len(self.levels)
