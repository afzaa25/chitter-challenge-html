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
class Peep


# Repository class
# (in lib/peep_repository.py)
class PeepRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class Peep:
    def __init__(self, id, message, date_created):
        self.id = id
        self.message = message
        self.date_created = date_created

        # Replace the attributes by your own columns.

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python

class PeepRepository():
    def __init__(self, connection):
        self._connection = connection
    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT * from peeps;

        # Returns an array of peeps objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(self, peep_id):
        # Executes the SQL query:
        # SELECT * from peeps where id = %, [peep_id];

        # Returns a single Peep object.

        # Add more methods below for each operation you'd like to implement.

    def create(self, peep)
    # Executes the SQL Query:
    # "INSERT INTO peeps(message, date_created, peep_id) VALUES (%s,%s,%s)", [peep.message, peep.date_created]

    def delete(self, peep_id)
    # Executes the SQL query
    # 'DELETE FROM peeps WHERE id = %s', [peep_id])

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all students

"""
When we call PeepRepository#all
We get a list of Peep objects reflecting the seed data.
"""
def test_all(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/chitter.sql") # Seed our database with some test data
    repository = PeepRepository(db_connection) # Create a new ArtistRepository

    peeps = repository.all() # Get all artists
    => Peep(1,'Hi, this is my first peep', '2023-05-25', 1),
    => Peep(2, 'Hi, this is my second peep', '2023-05-26', 1)
# 2
# Get a single student
"""
When we call PeepRepository#find
We get a single Peep object reflecting the seed data.
"""
repository = PeepRepository()

peep = repository.find(1)
    Peep(1,'Hi, this is my first peep', '2023-05-25', 1)

"""
When we call PeepRepository#create
We get a new record in the database.
"""

repository = PeepRepository()
peep = repository.create(Peep(None, "This is my third peep", '2023-05-25', 2))

result = repository.all()
    => Peep(1,'Hi, this is my first peep', '2023-05-25', 1),
    => Peep(2, 'Hi, this is my second peep', '2023-05-26', 1)
    => Peep(3, "This is my third peep", '2023-05-25', 2)

"""
When we call PeepRepository#delete
We remove a record from the database.
"""
repository = PeepRepository()
peep = repository.delete(2)
result = repository.all()

    => Peep(1,'Hi, this is my first peep', '2023-05-25', 1)

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

