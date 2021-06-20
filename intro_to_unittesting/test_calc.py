from simple_calc import SimpleCalc

calc = SimpleCalc()

def test_add():
    assert calc.add(2, 2) == 3

def test_subtract():
    assert calc.subtract(4, 2) == 2