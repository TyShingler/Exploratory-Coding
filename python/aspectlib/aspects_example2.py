""" aspects_eample2.py
CMD : pip install aspectlib

"""
import aspectlib

def test(name):
    return name + ' more stuff'

@aspectlib.Aspect
def mock(name):
    print('Start timer')
    result = yield aspectlib.Proceed
    print('End timer - take the difference')
    print(f'Acctual result  : {result}')
    print(f'My result       : mystuff')
    yield aspectlib.Return('mystuff')

with aspectlib.weave(test, mock):
    print(test('Testing---'))
    assert test('/doesnt/exist.txt') == 'mystuff'

print(test('--- Last test ---'))