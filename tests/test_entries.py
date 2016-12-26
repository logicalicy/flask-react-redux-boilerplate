import json
from .base import BaseTestCase


class EntriesTestCase(BaseTestCase):
    def test_empty_db(self):
        rv = self.app.get('/api/entries/')
        assert [] == json.loads(rv.data)

    def test_add_entry(self):
        rv = self.app.post('/api/entries/add/',
            data=dict(title='Hello World', text='My first entry'))
        result = json.loads(rv.data)
        assert result.get('title') == 'Hello World'
        assert result.get('text') == 'My first entry'
