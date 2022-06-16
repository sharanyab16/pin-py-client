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


class WorkflowStatisticsSchema(object):
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
        'description': 'str',
        'total_run': 'int',
        'total_succeeded': 'int',
        'total_failed': 'int',
        'total_running': 'int',
        'total_suspended': 'int'
    }

    attribute_map = {
        'description': 'description',
        'total_run': 'total_run',
        'total_succeeded': 'total_succeeded',
        'total_failed': 'total_failed',
        'total_running': 'total_running',
        'total_suspended': 'total_suspended'
    }

    def __init__(self, description=None, total_run=None, total_succeeded=None, total_failed=None, total_running=None, total_suspended=None):  # noqa: E501
        """WorkflowStatisticsSchema - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._total_run = None
        self._total_succeeded = None
        self._total_failed = None
        self._total_running = None
        self._total_suspended = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if total_run is not None:
            self.total_run = total_run
        if total_succeeded is not None:
            self.total_succeeded = total_succeeded
        if total_failed is not None:
            self.total_failed = total_failed
        if total_running is not None:
            self.total_running = total_running
        if total_suspended is not None:
            self.total_suspended = total_suspended

    @property
    def description(self):
        """Gets the description of this WorkflowStatisticsSchema.  # noqa: E501

        Description about this workflow statistics  # noqa: E501

        :return: The description of this WorkflowStatisticsSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowStatisticsSchema.

        Description about this workflow statistics  # noqa: E501

        :param description: The description of this WorkflowStatisticsSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def total_run(self):
        """Gets the total_run of this WorkflowStatisticsSchema.  # noqa: E501

        Total workflow instances run  # noqa: E501

        :return: The total_run of this WorkflowStatisticsSchema.  # noqa: E501
        :rtype: int
        """
        return self._total_run

    @total_run.setter
    def total_run(self, total_run):
        """Sets the total_run of this WorkflowStatisticsSchema.

        Total workflow instances run  # noqa: E501

        :param total_run: The total_run of this WorkflowStatisticsSchema.  # noqa: E501
        :type: int
        """
        if total_run is not None and total_run < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_run`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_run = total_run

    @property
    def total_succeeded(self):
        """Gets the total_succeeded of this WorkflowStatisticsSchema.  # noqa: E501

        Total workflow instances succeeded  # noqa: E501

        :return: The total_succeeded of this WorkflowStatisticsSchema.  # noqa: E501
        :rtype: int
        """
        return self._total_succeeded

    @total_succeeded.setter
    def total_succeeded(self, total_succeeded):
        """Sets the total_succeeded of this WorkflowStatisticsSchema.

        Total workflow instances succeeded  # noqa: E501

        :param total_succeeded: The total_succeeded of this WorkflowStatisticsSchema.  # noqa: E501
        :type: int
        """
        if total_succeeded is not None and total_succeeded < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_succeeded`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_succeeded = total_succeeded

    @property
    def total_failed(self):
        """Gets the total_failed of this WorkflowStatisticsSchema.  # noqa: E501

        Total workflow instances failed  # noqa: E501

        :return: The total_failed of this WorkflowStatisticsSchema.  # noqa: E501
        :rtype: int
        """
        return self._total_failed

    @total_failed.setter
    def total_failed(self, total_failed):
        """Sets the total_failed of this WorkflowStatisticsSchema.

        Total workflow instances failed  # noqa: E501

        :param total_failed: The total_failed of this WorkflowStatisticsSchema.  # noqa: E501
        :type: int
        """
        if total_failed is not None and total_failed < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_failed`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_failed = total_failed

    @property
    def total_running(self):
        """Gets the total_running of this WorkflowStatisticsSchema.  # noqa: E501

        Total workflow instances running currently  # noqa: E501

        :return: The total_running of this WorkflowStatisticsSchema.  # noqa: E501
        :rtype: int
        """
        return self._total_running

    @total_running.setter
    def total_running(self, total_running):
        """Sets the total_running of this WorkflowStatisticsSchema.

        Total workflow instances running currently  # noqa: E501

        :param total_running: The total_running of this WorkflowStatisticsSchema.  # noqa: E501
        :type: int
        """
        if total_running is not None and total_running < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_running`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_running = total_running

    @property
    def total_suspended(self):
        """Gets the total_suspended of this WorkflowStatisticsSchema.  # noqa: E501

        Total workflow instances suspended  # noqa: E501

        :return: The total_suspended of this WorkflowStatisticsSchema.  # noqa: E501
        :rtype: int
        """
        return self._total_suspended

    @total_suspended.setter
    def total_suspended(self, total_suspended):
        """Sets the total_suspended of this WorkflowStatisticsSchema.

        Total workflow instances suspended  # noqa: E501

        :param total_suspended: The total_suspended of this WorkflowStatisticsSchema.  # noqa: E501
        :type: int
        """
        if total_suspended is not None and total_suspended < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_suspended`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_suspended = total_suspended

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
        if issubclass(WorkflowStatisticsSchema, dict):
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
        if not isinstance(other, WorkflowStatisticsSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
