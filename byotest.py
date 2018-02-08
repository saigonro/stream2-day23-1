def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, but got {1}".format(expected,actual)
    
def test_not_equal(a, b):
    assert a != b, "{0} should not equal {1} but did".format(a, b)
    
def test_in_collection(collection, item):
    assert item in collection, "{0} should be in {1} but isn't".format(item, collection)