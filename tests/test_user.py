from lib.user import User

""" 
User constructs with an id, username, email, password
"""
def test_user_constructs():
    user = User(1, "Test user", "test@email", "password")
    assert user.id == 1
    assert user.username == "Test user"
    assert user.email == "test@email"
    assert user.password == "password"


"""
We can compare two identical users 
and have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Test user", "test@email", "password")
    user2 = User(1, "Test user", "test@email", "password")
    assert user1 == user2

""" 
We can format users to strings nicely
"""
def test_users_formats_nicely():
    user = User(1, "Test user", "test@email", "password")
    assert str(user) == "User(1, Test user, test@email, password)"