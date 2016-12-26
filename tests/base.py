import os
import app
import unittest
import tempfile


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        tmp_db = tempfile.mkstemp()
        app.app.config['DATABASE'] = tmp_db[1]
        self.db_fd, app.app.config['SQLALCHEMY_DATABASE_URI'] = (
            tmp_db[0], 'sqlite:///' + tmp_db[1])
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        with app.app.app_context():
            app.db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])


if __name__ == '__main__':
    unittest.main()