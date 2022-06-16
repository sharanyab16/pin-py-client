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


class TaggingprofileSchemaWhenMatcheswithscheduler(object):
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
        'scheduler': 'str',
        'time': 'str',
        'in_memory': 'bool'
    }

    attribute_map = {
        'scheduler': 'scheduler',
        'time': 'time',
        'in_memory': 'in-memory'
    }

    def __init__(self, scheduler=None, time=None, in_memory=None):  # noqa: E501
        """TaggingprofileSchemaWhenMatcheswithscheduler - a model defined in Swagger"""  # noqa: E501

        self._scheduler = None
        self._time = None
        self._in_memory = None
        self.discriminator = None

        self.scheduler = scheduler
        if time is not None:
            self.time = time
        if in_memory is not None:
            self.in_memory = in_memory

    @property
    def scheduler(self):
        """Gets the scheduler of this TaggingprofileSchemaWhenMatcheswithscheduler.  # noqa: E501

        Name of the scheduler defined within system/scheduler hierarchy  # noqa: E501

        :return: The scheduler of this TaggingprofileSchemaWhenMatcheswithscheduler.  # noqa: E501
        :rtype: str
        """
        return self._scheduler

    @scheduler.setter
    def scheduler(self, scheduler):
        """Sets the scheduler of this TaggingprofileSchemaWhenMatcheswithscheduler.

        Name of the scheduler defined within system/scheduler hierarchy  # noqa: E501

        :param scheduler: The scheduler of this TaggingprofileSchemaWhenMatcheswithscheduler.  # noqa: E501
        :type: str
        """
        if scheduler is None:
            raise ValueError("Invalid value for `scheduler`, must not be `None`")  # noqa: E501

        self._scheduler = scheduler

    @property
    def time(self):
        """Gets the time of this TaggingprofileSchemaWhenMatcheswithscheduler.  # noqa: E501

        Field holding time in UNIX time format. Optional default is point time  # noqa: E501

        :return: The time of this TaggingprofileSchemaWhenMatcheswithscheduler.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TaggingprofileSchemaWhenMatcheswithscheduler.

        Field holding time in UNIX time format. Optional default is point time  # noqa: E501

        :param time: The time of this TaggingprofileSchemaWhenMatcheswithscheduler.  # noqa: E501
        :type: str
        """
        if time is not None and not re.search(r'^[$][a-z][a-zA-Z0-9_-]*$', time):  # noqa: E501
            raise ValueError(r"Invalid value for `time`, must be a follow pattern or equal to `/^[$][a-z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._time = time

    @property
    def in_memory(self):
        """Gets the in_memory of this TaggingprofileSchemaWhenMatcheswithscheduler.  # noqa: E501

        Look for time in internal cache  # noqa: E501

        :return: The in_memory of this TaggingprofileSchemaWhenMatcheswithscheduler.  # noqa: E501
        :rtype: bool
        """
        return self._in_memory

    @in_memory.setter
    def in_memory(self, in_memory):
        """Sets the in_memory of this TaggingprofileSchemaWhenMatcheswithscheduler.

        Look for time in internal cache  # noqa: E501

        :param in_memory: The in_memory of this TaggingprofileSchemaWhenMatcheswithscheduler.  # noqa: E501
        :type: bool
        """

        self._in_memory = in_memory

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
        if issubclass(TaggingprofileSchemaWhenMatcheswithscheduler, dict):
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
        if not isinstance(other, TaggingprofileSchemaWhenMatcheswithscheduler):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
