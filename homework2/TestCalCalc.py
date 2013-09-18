#Test functions

from CalCalc import Calculate

def test_1():
    assert abs(4. - Calculate('2**2')) < .001

def test_2():
    assert abs(8. - Calculate('2*3*4*5/3/5')) < .001

def test_3():
    assert abs(100. - Calculate('100+2-3')) > .9

def test_4():
    assert abs(1.5 - Calculate('2**.5')) <.5
               
def test_5():
    assert abs(3.14 - Calculate('22./7')) <.003
