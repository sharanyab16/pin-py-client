# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.instance_schedule_state_api import InstanceScheduleStateApi  # noqa: E501
from swagger_client.rest import ApiException


class TestInstanceScheduleStateApi(unittest.TestCase):
    """InstanceScheduleStateApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.instance_schedule_state_api.InstanceScheduleStateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_instances_schedule_state(self):
        """Test case for retrieve_instances_schedule_state

        Get scheduled state of playbook instances with schedule.  # noqa: E501
        """
        pass

    def test_update_instances_schedule_state(self):
        """Test case for update_instances_schedule_state

        Update scheduled state of playbook instances with schedule.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
