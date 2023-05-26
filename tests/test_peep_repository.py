from lib.peep_repository import PeepRepository
from lib.peep import Peep
"""
When we call PeepRepository#all
We get a list of Peep objects reflecting the seed data.
"""
def test_all(db_connection): 
    db_connection.seed("seeds/chitter.sql") 
    repository = PeepRepository(db_connection)

    result = repository.all() # Get all artists
    assert result == [
        Peep(1,'Hi, this is my first peep', '2023-05-25', 1),
        Peep(2,'Hi, this is my second peep', '2023-05-26', 1)
]


# Get a single student
"""
When we call PeepRepository#find
We get a single Peep object reflecting the seed data.
"""
def test_find_peep(db_connection):
    db_connection.seed("seeds/chitter.sql") 
    repository = PeepRepository(db_connection) 
    peep = repository.find(1)
    assert peep == Peep(1,'Hi, this is my first peep', '2023-05-25', 1)

"""
When we call PeepRepository#create
We get a new record in the database.
"""
def test_create_peep(db_connection):
    db_connection.seed("seeds/chitter.sql") 
    repository = PeepRepository(db_connection)
    repository.create(Peep(None, "This is my third peep", '2023-05-25', 2))
    assert repository.all() == [
        Peep(1,'Hi, this is my first peep', '2023-05-25', 1),
        Peep(2, 'Hi, this is my second peep', '2023-05-26', 1),
        Peep(3, "This is my third peep", '2023-05-25', 2)]

"""
When we call PeepRepository#delete
We remove a record from the database.
"""
def test_delete_peep(db_connection):
    db_connection.seed("seeds/chitter.sql") 
    repository = PeepRepository(db_connection)
    repository.delete(2)
    assert repository.all() == [
        Peep(1,'Hi, this is my first peep', '2023-05-25', 1)
        ]
