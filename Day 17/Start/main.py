#PascalCase class
'''
has attributes
does methods
'''
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0


user_1 = User(9, "ayush")

print(user_1.username)
