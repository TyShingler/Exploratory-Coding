""" main.py
CMD : pip install aspectlib

"""
import aspectlib
import Dance_Utility
from Dance import Dance

@aspectlib.Aspect
def mock_dance(name):
    yield aspectlib.Return(f'||Mocking {name} dancing||')

print('=' * 10)
print('How the code runs normally . . .')
print('-' * 10)
Dance().perform()
print('-' * 10)
print('How the code runs after applying the aspect . . .')
print('-' * 10)
aspectlib.weave(Dance_Utility.perform_dance, mock_dance)
Dance().perform()
print('=' * 10)