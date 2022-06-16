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


class RuleSchemaRulepropertiesSupporteddevices(object):
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
        'juniper': 'RuleSchemaRulepropertiesSupporteddevicesJuniper',
        'other_vendor': 'list[RuleSchemaRulepropertiesSupporteddevicesOthervendor]',
        'sensors': 'list[str]'
    }

    attribute_map = {
        'juniper': 'juniper',
        'other_vendor': 'other-vendor',
        'sensors': 'sensors'
    }

    def __init__(self, juniper=None, other_vendor=None, sensors=None):  # noqa: E501
        """RuleSchemaRulepropertiesSupporteddevices - a model defined in Swagger"""  # noqa: E501

        self._juniper = None
        self._other_vendor = None
        self._sensors = None
        self.discriminator = None

        if juniper is not None:
            self.juniper = juniper
        if other_vendor is not None:
            self.other_vendor = other_vendor
        if sensors is not None:
            self.sensors = sensors

    @property
    def juniper(self):
        """Gets the juniper of this RuleSchemaRulepropertiesSupporteddevices.  # noqa: E501


        :return: The juniper of this RuleSchemaRulepropertiesSupporteddevices.  # noqa: E501
        :rtype: RuleSchemaRulepropertiesSupporteddevicesJuniper
        """
        return self._juniper

    @juniper.setter
    def juniper(self, juniper):
        """Sets the juniper of this RuleSchemaRulepropertiesSupporteddevices.


        :param juniper: The juniper of this RuleSchemaRulepropertiesSupporteddevices.  # noqa: E501
        :type: RuleSchemaRulepropertiesSupporteddevicesJuniper
        """

        self._juniper = juniper

    @property
    def other_vendor(self):
        """Gets the other_vendor of this RuleSchemaRulepropertiesSupporteddevices.  # noqa: E501

        Supported other-vendor devices  # noqa: E501

        :return: The other_vendor of this RuleSchemaRulepropertiesSupporteddevices.  # noqa: E501
        :rtype: list[RuleSchemaRulepropertiesSupporteddevicesOthervendor]
        """
        return self._other_vendor

    @other_vendor.setter
    def other_vendor(self, other_vendor):
        """Sets the other_vendor of this RuleSchemaRulepropertiesSupporteddevices.

        Supported other-vendor devices  # noqa: E501

        :param other_vendor: The other_vendor of this RuleSchemaRulepropertiesSupporteddevices.  # noqa: E501
        :type: list[RuleSchemaRulepropertiesSupporteddevicesOthervendor]
        """

        self._other_vendor = other_vendor

    @property
    def sensors(self):
        """Gets the sensors of this RuleSchemaRulepropertiesSupporteddevices.  # noqa: E501


        :return: The sensors of this RuleSchemaRulepropertiesSupporteddevices.  # noqa: E501
        :rtype: list[str]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this RuleSchemaRulepropertiesSupporteddevices.


        :param sensors: The sensors of this RuleSchemaRulepropertiesSupporteddevices.  # noqa: E501
        :type: list[str]
        """

        self._sensors = sensors

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
        if issubclass(RuleSchemaRulepropertiesSupporteddevices, dict):
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
        if not isinstance(other, RuleSchemaRulepropertiesSupporteddevices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
