""" aspects_eample1.py
CMD : pip install aspectlib

"""
import aspectlib

@aspectlib.Aspect
def strip_return_value(*args, **kwargs):
    result = yield aspectlib.Proceed
    print(result)
    yield aspectlib.Return(result.strip())

@strip_return_value
def read(name):
    return open(name).read()

if __name__ == '__main__':
    read('testFile.txt')