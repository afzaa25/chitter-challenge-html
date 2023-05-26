# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

*In this template, we'll use an example table `students`*

```

```

## 2. Create Test SQL seeds


```bash

```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/peep.py)
class User


# Repository class
# (in lib/peep_repository.py)
class UserRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        # Replace the attributes by your own columns.

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    # Selecting all records
    # No arguments
    def all():

    def find(self, peep_id):


    def create(self, peep)


    def delete(self, peep_id)

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all students

"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_all(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/chitter.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository

    Users = repository.all() # Get all artists
 (1, 'afzaa25', 'afzaaatcha25@gmail.com', 'Password123!');
 (2, 'atcha25', 'atcha25@gmail.com', 'Password1234!');
# 2
# Get a single student
"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""
repository = UserRepository()

User = repository.find(1)
     (1, 'afzaa25', 'afzaaatcha25@gmail.com', 'Password123!');

"""
When we call UserRepository#create
We get a new record in the database.
"""

repository = UserRepository()
User = repository.create(User(None, "This is my third User", '2023-05-25', 2))

result = repository.all()
    => (1, 'afzaa25', 'afzaaatcha25@gmail.com', 'Password123!');
    => (2, 'atcha25', 'atcha25@gmail.com', 'Password1234!');
    => (3, 'atcha25', 'atcha25@gmail.com', 'Password1234!');

"""
When we call UserRepository#delete
We remove a record from the database.
"""
repository = UserRepository()
User = repository.delete(2)
result = repository.all()

    => (1, 'afzaa25', 'afzaaatcha25@gmail.com', 'Password123!');


# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

