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


class RuleSchemaRulepropertiesSupporteddevicesOthervendor(object):
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
        'apply_macro': 'list[ApplyMacroSchema]',
        'operating_system': 'str',
        'operating_systems': 'list[RuleSchemaRulepropertiesSupporteddevicesOperatingsystems]',
        'sensors': 'list[str]',
        'vendor_identifier': 'str',
        'vendor_name': 'str'
    }

    attribute_map = {
        'apply_macro': 'apply-macro',
        'operating_system': 'operating-system',
        'operating_systems': 'operating-systems',
        'sensors': 'sensors',
        'vendor_identifier': 'vendor-identifier',
        'vendor_name': 'vendor-name'
    }

    def __init__(self, apply_macro=None, operating_system=None, operating_systems=None, sensors=None, vendor_identifier=None, vendor_name=None):  # noqa: E501
        """RuleSchemaRulepropertiesSupporteddevicesOthervendor - a model defined in Swagger"""  # noqa: E501

        self._apply_macro = None
        self._operating_system = None
        self._operating_systems = None
        self._sensors = None
        self._vendor_identifier = None
        self._vendor_name = None
        self.discriminator = None

        if apply_macro is not None:
            self.apply_macro = apply_macro
        if operating_system is not None:
            self.operating_system = operating_system
        if operating_systems is not None:
            self.operating_systems = operating_systems
        if sensors is not None:
            self.sensors = sensors
        self.vendor_identifier = vendor_identifier
        self.vendor_name = vendor_name

    @property
    def apply_macro(self):
        """Gets the apply_macro of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501


        :return: The apply_macro of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :rtype: list[ApplyMacroSchema]
        """
        return self._apply_macro

    @apply_macro.setter
    def apply_macro(self, apply_macro):
        """Sets the apply_macro of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.


        :param apply_macro: The apply_macro of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :type: list[ApplyMacroSchema]
        """

        self._apply_macro = apply_macro

    @property
    def operating_system(self):
        """Gets the operating_system of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501

        [Deprecated] Vendor operating system, Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The operating_system of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.

        [Deprecated] Vendor operating system, Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param operating_system: The operating_system of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :type: str
        """
        if operating_system is not None and len(operating_system) > 64:
            raise ValueError("Invalid value for `operating_system`, length must be less than or equal to `64`")  # noqa: E501
        if operating_system is not None and len(operating_system) < 1:
            raise ValueError("Invalid value for `operating_system`, length must be greater than or equal to `1`")  # noqa: E501
        if operating_system is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', operating_system):  # noqa: E501
            raise ValueError(r"Invalid value for `operating_system`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._operating_system = operating_system

    @property
    def operating_systems(self):
        """Gets the operating_systems of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501

        Operating system of the device  # noqa: E501

        :return: The operating_systems of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :rtype: list[RuleSchemaRulepropertiesSupporteddevicesOperatingsystems]
        """
        return self._operating_systems

    @operating_systems.setter
    def operating_systems(self, operating_systems):
        """Sets the operating_systems of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.

        Operating system of the device  # noqa: E501

        :param operating_systems: The operating_systems of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :type: list[RuleSchemaRulepropertiesSupporteddevicesOperatingsystems]
        """

        self._operating_systems = operating_systems

    @property
    def sensors(self):
        """Gets the sensors of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501


        :return: The sensors of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :rtype: list[str]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.


        :param sensors: The sensors of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :type: list[str]
        """

        self._sensors = sensors

    @property
    def vendor_identifier(self):
        """Gets the vendor_identifier of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501

        Unique key to identify the other vendor specific products  # noqa: E501

        :return: The vendor_identifier of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :rtype: str
        """
        return self._vendor_identifier

    @vendor_identifier.setter
    def vendor_identifier(self, vendor_identifier):
        """Sets the vendor_identifier of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.

        Unique key to identify the other vendor specific products  # noqa: E501

        :param vendor_identifier: The vendor_identifier of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :type: str
        """
        if vendor_identifier is None:
            raise ValueError("Invalid value for `vendor_identifier`, must not be `None`")  # noqa: E501
        if vendor_identifier is not None and len(vendor_identifier) > 64:
            raise ValueError("Invalid value for `vendor_identifier`, length must be less than or equal to `64`")  # noqa: E501
        if vendor_identifier is not None and len(vendor_identifier) < 1:
            raise ValueError("Invalid value for `vendor_identifier`, length must be greater than or equal to `1`")  # noqa: E501

        self._vendor_identifier = vendor_identifier

    @property
    def vendor_name(self):
        """Gets the vendor_name of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501

        Vendor name  # noqa: E501

        :return: The vendor_name of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        """Sets the vendor_name of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.

        Vendor name  # noqa: E501

        :param vendor_name: The vendor_name of this RuleSchemaRulepropertiesSupporteddevicesOthervendor.  # noqa: E501
        :type: str
        """
        if vendor_name is None:
            raise ValueError("Invalid value for `vendor_name`, must not be `None`")  # noqa: E501
        if vendor_name is not None and len(vendor_name) > 64:
            raise ValueError("Invalid value for `vendor_name`, length must be less than or equal to `64`")  # noqa: E501
        if vendor_name is not None and len(vendor_name) < 1:
            raise ValueError("Invalid value for `vendor_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._vendor_name = vendor_name

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
        if issubclass(RuleSchemaRulepropertiesSupporteddevicesOthervendor, dict):
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
        if not isinstance(other, RuleSchemaRulepropertiesSupporteddevicesOthervendor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other