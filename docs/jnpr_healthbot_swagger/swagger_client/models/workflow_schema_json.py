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


class WorkflowSchemaJson(object):
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
        'jqpath': 'str'
    }

    attribute_map = {
        'jqpath': 'jqpath'
    }

    def __init__(self, jqpath=None):  # noqa: E501
        """WorkflowSchemaJson - a model defined in Swagger"""  # noqa: E501

        self._jqpath = None
        self.discriminator = None

        if jqpath is not None:
            self.jqpath = jqpath

    @property
    def jqpath(self):
        """Gets the jqpath of this WorkflowSchemaJson.  # noqa: E501

        Export output using jqpath  # noqa: E501

        :return: The jqpath of this WorkflowSchemaJson.  # noqa: E501
        :rtype: str
        """
        return self._jqpath

    @jqpath.setter
    def jqpath(self, jqpath):
        """Sets the jqpath of this WorkflowSchemaJson.

        Export output using jqpath  # noqa: E501

        :param jqpath: The jqpath of this WorkflowSchemaJson.  # noqa: E501
        :type: str
        """

        self._jqpath = jqpath

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
        if issubclass(WorkflowSchemaJson, dict):
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
        if not isinstance(other, WorkflowSchemaJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
