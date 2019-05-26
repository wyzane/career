"""使用Client测试
"""

import json

from django.test import TestCase
from django.test import Client

from resume.skill.models import Skill


class SkillTestCase(TestCase):

    def setUp(self):
        print("-- test start --")

        self.client = Client()
        self.url = {
            "url_skill_create": "/api/v1/resume/create/skill",
            "url_skill_list": "/api/v1/resume/list/skill",
            "url_skill_detail": "/api/v1/resume/detail/skill"
        }

        Skill.objects.create(desc="熟悉java")
        Skill.objects.create(desc="熟悉python")
        self.content_type = 'multipart/form-data'

    def tearDown(self):
        print("-- test finish --")

    def test_skill_create(self):
        """skill create
        """

        data = {
            "desc": "linux",
        }
        response = (self.client
                    .post(self.url["url_skill_create"],
                          data))
        res = json.loads(response.content, encoding="utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res["data"]["desc"], "linux")

    def test_skill_list(self):
        """skill list
        """

        response = (self.client
                    .post(self.url["url_skill_list"]))
        res = json.loads(response.content, encoding="utf-8")
        self.assertEqual(response.status_code, 200)

    def test_skill_detail(self):
        """skill detail
        """

        data = {
            "skillId": 1,
        }
        response = (self.client
                    .post(self.url["url_skill_detail"],
                          data))
        res = json.loads(response.content, encoding="utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res["data"]["id"], data.get("skillId"))

