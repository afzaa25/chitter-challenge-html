from lib.user_repository import UserRepository
from lib.user import User
"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_all(db_connection): 
    db_connection.seed("seeds/chitter.sql") 
    repository = UserRepository(db_connection)
    result = repository.all()
    assert result == [
    User(1, 'afzaa25', 'afzaaatcha25@gmail.com', 'Password123!'),
    User(2, 'atcha25', 'atcha25@gmail.com', 'Password1234!')
    ]


"""
When we call userRepository#find
We get a single user object reflecting the seed data.
"""
def test_find_user(db_connection):
    db_connection.seed("seeds/chitter.sql") 
    repository = UserRepository(db_connection) 
    user = repository.find(1)
    assert user == User(1, 'afzaa25', 'afzaaatcha25@gmail.com', 'Password123!')

"""
When we call userRepository#create
We get a new record in the database.
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/chitter.sql") 
    repository = UserRepository(db_connection)
    repository.create(User(None, "newUser", "new@email", "newPassword"))
    assert repository.all() == [
        User(1, 'afzaa25', 'afzaaatcha25@gmail.com', 'Password123!'),
        User(2, 'atcha25', 'atcha25@gmail.com', 'Password1234!'),
        User(3, "newUser", "new@email", "newPassword")
    ]

"""
When we call UserRepository#delete
We remove a record from the database.
"""
def test_delete_User(db_connection):
    db_connection.seed("seeds/chitter.sql") 
    repository = UserRepository(db_connection)
    repository.delete(2)
    assert repository.all() == [
        User(1, 'afzaa25', 'afzaaatcha25@gmail.com', 'Password123!')
        ]
