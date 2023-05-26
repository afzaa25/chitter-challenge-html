from lib.user import User
class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            # print(type(row['date_created']))
            user = User(row['id'], row['username'], row['email'], row['password']) 
            users.append(user)
        return users
    

    def find(self, user_id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row['id'], row['username'], row['email'], row['password']) 

    def create(self, user):
        self._connection.execute('INSERT INTO users(username, email, password) VALUES (%s, %s, %s)', [user.username, user.email, user.password])
        return None
    

    def delete(self, user_id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [user_id])
        return None
