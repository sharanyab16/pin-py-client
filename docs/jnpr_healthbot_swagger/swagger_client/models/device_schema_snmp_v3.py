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


class DeviceSchemaSnmpV3(object):
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
        'source_id': 'DeviceSchemaSnmpV3Sourceid',
        'usm': 'DeviceSchemaSnmpV3Usm'
    }

    attribute_map = {
        'source_id': 'source-id',
        'usm': 'usm'
    }

    def __init__(self, source_id=None, usm=None):  # noqa: E501
        """DeviceSchemaSnmpV3 - a model defined in Swagger"""  # noqa: E501

        self._source_id = None
        self._usm = None
        self.discriminator = None

        if source_id is not None:
            self.source_id = source_id
        if usm is not None:
            self.usm = usm

    @property
    def source_id(self):
        """Gets the source_id of this DeviceSchemaSnmpV3.  # noqa: E501


        :return: The source_id of this DeviceSchemaSnmpV3.  # noqa: E501
        :rtype: DeviceSchemaSnmpV3Sourceid
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this DeviceSchemaSnmpV3.


        :param source_id: The source_id of this DeviceSchemaSnmpV3.  # noqa: E501
        :type: DeviceSchemaSnmpV3Sourceid
        """

        self._source_id = source_id

    @property
    def usm(self):
        """Gets the usm of this DeviceSchemaSnmpV3.  # noqa: E501


        :return: The usm of this DeviceSchemaSnmpV3.  # noqa: E501
        :rtype: DeviceSchemaSnmpV3Usm
        """
        return self._usm

    @usm.setter
    def usm(self, usm):
        """Sets the usm of this DeviceSchemaSnmpV3.


        :param usm: The usm of this DeviceSchemaSnmpV3.  # noqa: E501
        :type: DeviceSchemaSnmpV3Usm
        """

        self._usm = usm

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
        if issubclass(DeviceSchemaSnmpV3, dict):
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
        if not isinstance(other, DeviceSchemaSnmpV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other