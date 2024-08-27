from mod import std

def test_std1():
    obs = std([0.0, 2.0])
    exp = 1.0
    assert_equal(obs, exp)

def test_std2():
    obs = std([])
    exp = 0.0
    assert_equal(obs, exp)

def test_std3():
    obs = std([0.0, 4.0])
    exp = 2.0
    assert_equal(obs, exp)

def test_std4():
    # The first value is not zero.
    obs = std([1.0, 3.0])
    exp = 1.0
    assert_equal(obs, exp)

def test_std5():
    # Here, we have more than two values, but all of the values are the same.
    obs = std([1.0, 1.0, 1.0])
    exp = 0.0
    assert_equal(obs, exp)