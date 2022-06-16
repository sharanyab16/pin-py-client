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


class NetworkgroupSchemaPublish(object):
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
        'destination': 'list[str]',
        'field': 'list[str]'
    }

    attribute_map = {
        'destination': 'destination',
        'field': 'field'
    }

    def __init__(self, destination=None, field=None):  # noqa: E501
        """NetworkgroupSchemaPublish - a model defined in Swagger"""  # noqa: E501

        self._destination = None
        self._field = None
        self.discriminator = None

        self.destination = destination
        if field is not None:
            self.field = field

    @property
    def destination(self):
        """Gets the destination of this NetworkgroupSchemaPublish.  # noqa: E501


        :return: The destination of this NetworkgroupSchemaPublish.  # noqa: E501
        :rtype: list[str]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this NetworkgroupSchemaPublish.


        :param destination: The destination of this NetworkgroupSchemaPublish.  # noqa: E501
        :type: list[str]
        """
        if destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def field(self):
        """Gets the field of this NetworkgroupSchemaPublish.  # noqa: E501


        :return: The field of this NetworkgroupSchemaPublish.  # noqa: E501
        :rtype: list[str]
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this NetworkgroupSchemaPublish.


        :param field: The field of this NetworkgroupSchemaPublish.  # noqa: E501
        :type: list[str]
        """

        self._field = field

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
        if issubclass(NetworkgroupSchemaPublish, dict):
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
        if not isinstance(other, NetworkgroupSchemaPublish):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
