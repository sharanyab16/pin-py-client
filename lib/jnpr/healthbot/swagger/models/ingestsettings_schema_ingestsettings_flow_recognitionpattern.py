# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.

# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: healthbot-hackers@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IngestsettingsSchemaIngestsettingsFlowRecognitionpattern(object):
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
        'exclude_fields': 'list[str]',
        'include_fields': 'list[str]'
    }

    attribute_map = {
        'exclude_fields': 'exclude-fields',
        'include_fields': 'include-fields'
    }

    def __init__(self, exclude_fields=None, include_fields=None):  # noqa: E501
        """IngestsettingsSchemaIngestsettingsFlowRecognitionpattern - a model defined in Swagger"""  # noqa: E501

        self._exclude_fields = None
        self._include_fields = None
        self.discriminator = None

        if exclude_fields is not None:
            self.exclude_fields = exclude_fields
        if include_fields is not None:
            self.include_fields = include_fields

    @property
    def exclude_fields(self):
        """Gets the exclude_fields of this IngestsettingsSchemaIngestsettingsFlowRecognitionpattern.  # noqa: E501


        :return: The exclude_fields of this IngestsettingsSchemaIngestsettingsFlowRecognitionpattern.  # noqa: E501
        :rtype: list[str]
        """
        return self._exclude_fields

    @exclude_fields.setter
    def exclude_fields(self, exclude_fields):
        """Sets the exclude_fields of this IngestsettingsSchemaIngestsettingsFlowRecognitionpattern.


        :param exclude_fields: The exclude_fields of this IngestsettingsSchemaIngestsettingsFlowRecognitionpattern.  # noqa: E501
        :type: list[str]
        """

        self._exclude_fields = exclude_fields

    @property
    def include_fields(self):
        """Gets the include_fields of this IngestsettingsSchemaIngestsettingsFlowRecognitionpattern.  # noqa: E501


        :return: The include_fields of this IngestsettingsSchemaIngestsettingsFlowRecognitionpattern.  # noqa: E501
        :rtype: list[str]
        """
        return self._include_fields

    @include_fields.setter
    def include_fields(self, include_fields):
        """Sets the include_fields of this IngestsettingsSchemaIngestsettingsFlowRecognitionpattern.


        :param include_fields: The include_fields of this IngestsettingsSchemaIngestsettingsFlowRecognitionpattern.  # noqa: E501
        :type: list[str]
        """

        self._include_fields = include_fields

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
        if issubclass(IngestsettingsSchemaIngestsettingsFlowRecognitionpattern, dict):
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
        if not isinstance(other, IngestsettingsSchemaIngestsettingsFlowRecognitionpattern):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
