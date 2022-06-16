# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.

# coding: utf-8

"""
    Healthbot APIs

    API interface for Healthbot application  # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GroupgroupidRoles(object):
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
        'role_id': 'str',
        'role_name': 'str'
    }

    attribute_map = {
        'role_id': 'roleId',
        'role_name': 'roleName'
    }

    def __init__(self, role_id=None, role_name=None):  # noqa: E501
        """GroupgroupidRoles - a model defined in Swagger"""  # noqa: E501

        self._role_id = None
        self._role_name = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        if role_name is not None:
            self.role_name = role_name

    @property
    def role_id(self):
        """Gets the role_id of this GroupgroupidRoles.  # noqa: E501


        :return: The role_id of this GroupgroupidRoles.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this GroupgroupidRoles.


        :param role_id: The role_id of this GroupgroupidRoles.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

    @property
    def role_name(self):
        """Gets the role_name of this GroupgroupidRoles.  # noqa: E501


        :return: The role_name of this GroupgroupidRoles.  # noqa: E501
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this GroupgroupidRoles.


        :param role_name: The role_name of this GroupgroupidRoles.  # noqa: E501
        :type: str
        """

        self._role_name = role_name

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
        if issubclass(GroupgroupidRoles, dict):
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
        if not isinstance(other, GroupgroupidRoles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
