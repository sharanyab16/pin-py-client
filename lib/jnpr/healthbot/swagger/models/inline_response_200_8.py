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


class InlineResponse2008(object):
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
        'group_id': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'group_id': 'groupId',
        'group_name': 'groupName'
    }

    def __init__(self, group_id=None, group_name=None):  # noqa: E501
        """InlineResponse2008 - a model defined in Swagger"""  # noqa: E501

        self._group_id = None
        self._group_name = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name

    @property
    def group_id(self):
        """Gets the group_id of this InlineResponse2008.  # noqa: E501

        ID generated by system  # noqa: E501

        :return: The group_id of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this InlineResponse2008.

        ID generated by system  # noqa: E501

        :param group_id: The group_id of this InlineResponse2008.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this InlineResponse2008.  # noqa: E501

        Name of the group  # noqa: E501

        :return: The group_name of this InlineResponse2008.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this InlineResponse2008.

        Name of the group  # noqa: E501

        :param group_name: The group_name of this InlineResponse2008.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2008):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
