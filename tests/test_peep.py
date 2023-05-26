from lib.peep import Peep

""" 
Peep constructs with an id, message, date created
"""
def test_peep_constructs():
    peep = Peep(1, "Test Peep", "2023-05-25", 1)
    assert peep.id == 1
    assert peep.message== "Test Peep"
    assert peep.date_created == "2023-05-25"
    assert peep.user_id == 1


"""
We can compare two identical peeps 
and have them be equal
"""
def test_peeps_are_equal():
    peep1 = Peep(1, "Test Peep", "2023-05-25", 1)
    peep2 = Peep(1, "Test Peep", "2023-05-25", 1)
    assert peep1 == peep2

""" 
We can format peeps to strings nicely
"""
def test_peeps_formats_nicely():
    peep = Peep(1, "Test Peep", "2023-05-25",1)
    assert str(peep) == "Peep(1, Test Peep, 2023-05-25, 1)"