import pytest
import json

from source.run import app

def test_basic():
    assert 1 == 1


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = {'hello': 'DevOps'}
    assert expected == json.loads(res.get_data(as_text=True))