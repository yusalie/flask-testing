from test_base import BaseTest
import json

class TestApp(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {'message':'hello world'})