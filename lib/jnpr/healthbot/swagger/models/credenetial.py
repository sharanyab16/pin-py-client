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


class Credenetial(object):
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
        'email': 'str',
        'oldpassword': 'str',
        'newpassword': 'str'
    }

    attribute_map = {
        'email': 'email',
        'oldpassword': 'oldpassword',
        'newpassword': 'newpassword'
    }

    def __init__(self, email=None, oldpassword=None, newpassword=None):  # noqa: E501
        """Credenetial - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._oldpassword = None
        self._newpassword = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if oldpassword is not None:
            self.oldpassword = oldpassword
        if newpassword is not None:
            self.newpassword = newpassword

    @property
    def email(self):
        """Gets the email of this Credenetial.  # noqa: E501

        User email address  # noqa: E501

        :return: The email of this Credenetial.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Credenetial.

        User email address  # noqa: E501

        :param email: The email of this Credenetial.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def oldpassword(self):
        """Gets the oldpassword of this Credenetial.  # noqa: E501

        Old password  # noqa: E501

        :return: The oldpassword of this Credenetial.  # noqa: E501
        :rtype: str
        """
        return self._oldpassword

    @oldpassword.setter
    def oldpassword(self, oldpassword):
        """Sets the oldpassword of this Credenetial.

        Old password  # noqa: E501

        :param oldpassword: The oldpassword of this Credenetial.  # noqa: E501
        :type: str
        """

        self._oldpassword = oldpassword

    @property
    def newpassword(self):
        """Gets the newpassword of this Credenetial.  # noqa: E501

        New password  # noqa: E501

        :return: The newpassword of this Credenetial.  # noqa: E501
        :rtype: str
        """
        return self._newpassword

    @newpassword.setter
    def newpassword(self, newpassword):
        """Sets the newpassword of this Credenetial.

        New password  # noqa: E501

        :param newpassword: The newpassword of this Credenetial.  # noqa: E501
        :type: str
        """

        self._newpassword = newpassword

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
        if issubclass(Credenetial, dict):
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
        if not isinstance(other, Credenetial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
