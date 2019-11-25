import json
from unittest import TestCase

from db import db
from app import create_app

app = create_app('TEST')


class TestSchool(TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_post(self):
        data = json.dumps({"name": "school_1"})
        resp = app.test_client().post('/school', data=data, content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json, {"id": 1, "name": "school_1"})
