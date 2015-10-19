import nose
from temp_with_doc import above_freezing

def test_above_freezing():
    '''Test function for above_freezing working when above freezing.'''
    assert above_freezing(89.4), 'A temperature above freezing.'

def test_below_freezing():
    '''Test function for above_freezing working when below freezing.'''
    assert not above_freezing(-42), 'A temperature below freezing.'

def test_at_freezing():
    '''Test function for above_freezing working when at freezing.'''
    assert not above_freezing(0), 'A temperature at freezing.'
    
if __name__ == '__main__':
    nose.runmodule()
    