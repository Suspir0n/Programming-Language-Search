import pytest
from flask import Flask

@pytest.fixture
def sum():
    test_sum

def test_sum():
    '''Starting the test with pytest'''
    _sum = 2 + 5
    result = False
    if _sum == 4:
        print('2 + 2 = {}'.format(_sum))
        result = True
    else:
        print('Algo de errado não está certo hehe')
        result = False