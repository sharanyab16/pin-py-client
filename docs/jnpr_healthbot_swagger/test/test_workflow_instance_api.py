# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.workflow_instance_api import WorkflowInstanceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWorkflowInstanceApi(unittest.TestCase):
    """WorkflowInstanceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.workflow_instance_api.WorkflowInstanceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_healthbot_workflow_instance_by_id(self):
        """Test case for create_healthbot_workflow_instance_by_id

        Create workflow by ID  # noqa: E501
        """
        pass

    def test_delete_healthbot_workflow_instance_by_id(self):
        """Test case for delete_healthbot_workflow_instance_by_id

        Delete workflow instance by ID  # noqa: E501
        """
        pass

    def test_delete_healthbot_workflow_instances(self):
        """Test case for delete_healthbot_workflow_instances

        Delete workflow by ID  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_workflow_instance_by_id(self):
        """Test case for retrieve_healthbot_workflow_instance_by_id

        Retrieve workflow by ID  # noqa: E501
        """
        pass

    def test_retrieve_healthbot_workflow_instances(self):
        """Test case for retrieve_healthbot_workflow_instances

        Retrieve workflow instances  # noqa: E501
        """
        pass

    def test_update_healthbot_workflow_instance_by_id(self):
        """Test case for update_healthbot_workflow_instance_by_id

        Retrieve workflow by ID  # noqa: E501
        """
        pass

    def test_update_healthbot_workflow_instances(self):
        """Test case for update_healthbot_workflow_instances

        Update workflow instances  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
