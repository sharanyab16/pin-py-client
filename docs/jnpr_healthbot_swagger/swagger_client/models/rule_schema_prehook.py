# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.

# coding: utf-8

"""
    Paragon Insights APIs

    API interface for PI application  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RuleSchemaPrehook(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'argument': 'WorkflowArgumentGroupSchema',
        'workflow_name': 'str',
        'execute_once': 'bool'
    }

    attribute_map = {
        'argument': 'argument',
        'workflow_name': 'workflow-name',
        'execute_once': 'execute-once'
    }

    def __init__(self, argument=None, workflow_name=None, execute_once=None):  # noqa: E501
        """RuleSchemaPrehook - a model defined in Swagger"""  # noqa: E501

        self._argument = None
        self._workflow_name = None
        self._execute_once = None
        self.discriminator = None

        if argument is not None:
            self.argument = argument
        self.workflow_name = workflow_name
        if execute_once is not None:
            self.execute_once = execute_once

    @property
    def argument(self):
        """Gets the argument of this RuleSchemaPrehook.  # noqa: E501


        :return: The argument of this RuleSchemaPrehook.  # noqa: E501
        :rtype: WorkflowArgumentGroupSchema
        """
        return self._argument

    @argument.setter
    def argument(self, argument):
        """Sets the argument of this RuleSchemaPrehook.


        :param argument: The argument of this RuleSchemaPrehook.  # noqa: E501
        :type: WorkflowArgumentGroupSchema
        """

        self._argument = argument

    @property
    def workflow_name(self):
        """Gets the workflow_name of this RuleSchemaPrehook.  # noqa: E501

        Name of the workflow to trigger  # noqa: E501

        :return: The workflow_name of this RuleSchemaPrehook.  # noqa: E501
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this RuleSchemaPrehook.

        Name of the workflow to trigger  # noqa: E501

        :param workflow_name: The workflow_name of this RuleSchemaPrehook.  # noqa: E501
        :type: str
        """
        if workflow_name is None:
            raise ValueError("Invalid value for `workflow_name`, must not be `None`")  # noqa: E501

        self._workflow_name = workflow_name

    @property
    def execute_once(self):
        """Gets the execute_once of this RuleSchemaPrehook.  # noqa: E501

        Execute workflow once with in a device group  # noqa: E501

        :return: The execute_once of this RuleSchemaPrehook.  # noqa: E501
        :rtype: bool
        """
        return self._execute_once

    @execute_once.setter
    def execute_once(self, execute_once):
        """Sets the execute_once of this RuleSchemaPrehook.

        Execute workflow once with in a device group  # noqa: E501

        :param execute_once: The execute_once of this RuleSchemaPrehook.  # noqa: E501
        :type: bool
        """

        self._execute_once = execute_once

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RuleSchemaPrehook, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RuleSchemaPrehook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
