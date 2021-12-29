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


class DeviceSchemaVendor(object):
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
        'arista': 'DeviceSchemaVendorArista',
        'cisco': 'DeviceSchemaVendorCisco',
        'juniper': 'DeviceSchemaVendorJuniper',
        'linux': 'DeviceSchemaVendorLinux',
        'other_vendor': 'DeviceSchemaVendorOthervendor',
        'paloalto': 'DeviceSchemaVendorPaloalto'
    }

    attribute_map = {
        'arista': 'arista',
        'cisco': 'cisco',
        'juniper': 'juniper',
        'linux': 'linux',
        'other_vendor': 'other-vendor',
        'paloalto': 'paloalto'
    }

    def __init__(self, arista=None, cisco=None, juniper=None, linux=None, other_vendor=None, paloalto=None):  # noqa: E501
        """DeviceSchemaVendor - a model defined in Swagger"""  # noqa: E501

        self._arista = None
        self._cisco = None
        self._juniper = None
        self._linux = None
        self._other_vendor = None
        self._paloalto = None
        self.discriminator = None

        if arista is not None:
            self.arista = arista
        if cisco is not None:
            self.cisco = cisco
        if juniper is not None:
            self.juniper = juniper
        if linux is not None:
            self.linux = linux
        if other_vendor is not None:
            self.other_vendor = other_vendor
        if paloalto is not None:
            self.paloalto = paloalto

    @property
    def arista(self):
        """Gets the arista of this DeviceSchemaVendor.  # noqa: E501


        :return: The arista of this DeviceSchemaVendor.  # noqa: E501
        :rtype: DeviceSchemaVendorArista
        """
        return self._arista

    @arista.setter
    def arista(self, arista):
        """Sets the arista of this DeviceSchemaVendor.


        :param arista: The arista of this DeviceSchemaVendor.  # noqa: E501
        :type: DeviceSchemaVendorArista
        """

        self._arista = arista

    @property
    def cisco(self):
        """Gets the cisco of this DeviceSchemaVendor.  # noqa: E501


        :return: The cisco of this DeviceSchemaVendor.  # noqa: E501
        :rtype: DeviceSchemaVendorCisco
        """
        return self._cisco

    @cisco.setter
    def cisco(self, cisco):
        """Sets the cisco of this DeviceSchemaVendor.


        :param cisco: The cisco of this DeviceSchemaVendor.  # noqa: E501
        :type: DeviceSchemaVendorCisco
        """

        self._cisco = cisco

    @property
    def juniper(self):
        """Gets the juniper of this DeviceSchemaVendor.  # noqa: E501


        :return: The juniper of this DeviceSchemaVendor.  # noqa: E501
        :rtype: DeviceSchemaVendorJuniper
        """
        return self._juniper

    @juniper.setter
    def juniper(self, juniper):
        """Sets the juniper of this DeviceSchemaVendor.


        :param juniper: The juniper of this DeviceSchemaVendor.  # noqa: E501
        :type: DeviceSchemaVendorJuniper
        """

        self._juniper = juniper

    @property
    def linux(self):
        """Gets the linux of this DeviceSchemaVendor.  # noqa: E501


        :return: The linux of this DeviceSchemaVendor.  # noqa: E501
        :rtype: DeviceSchemaVendorLinux
        """
        return self._linux

    @linux.setter
    def linux(self, linux):
        """Sets the linux of this DeviceSchemaVendor.


        :param linux: The linux of this DeviceSchemaVendor.  # noqa: E501
        :type: DeviceSchemaVendorLinux
        """

        self._linux = linux

    @property
    def other_vendor(self):
        """Gets the other_vendor of this DeviceSchemaVendor.  # noqa: E501


        :return: The other_vendor of this DeviceSchemaVendor.  # noqa: E501
        :rtype: DeviceSchemaVendorOthervendor
        """
        return self._other_vendor

    @other_vendor.setter
    def other_vendor(self, other_vendor):
        """Sets the other_vendor of this DeviceSchemaVendor.


        :param other_vendor: The other_vendor of this DeviceSchemaVendor.  # noqa: E501
        :type: DeviceSchemaVendorOthervendor
        """

        self._other_vendor = other_vendor

    @property
    def paloalto(self):
        """Gets the paloalto of this DeviceSchemaVendor.  # noqa: E501


        :return: The paloalto of this DeviceSchemaVendor.  # noqa: E501
        :rtype: DeviceSchemaVendorPaloalto
        """
        return self._paloalto

    @paloalto.setter
    def paloalto(self, paloalto):
        """Sets the paloalto of this DeviceSchemaVendor.


        :param paloalto: The paloalto of this DeviceSchemaVendor.  # noqa: E501
        :type: DeviceSchemaVendorPaloalto
        """

        self._paloalto = paloalto

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
        if issubclass(DeviceSchemaVendor, dict):
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
        if not isinstance(other, DeviceSchemaVendor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other