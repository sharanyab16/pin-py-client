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


class OrganizationSchema(object):
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
        'description': 'str',
        'organization_name': 'str',
        'site': 'list[SiteSchema]'
    }

    attribute_map = {
        'description': 'description',
        'organization_name': 'organization-name',
        'site': 'site'
    }

    def __init__(self, description=None, organization_name=None, site=None):  # noqa: E501
        """OrganizationSchema - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._organization_name = None
        self._site = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.organization_name = organization_name
        if site is not None:
            self.site = site

    @property
    def description(self):
        """Gets the description of this OrganizationSchema.  # noqa: E501

        Description about the organization  # noqa: E501

        :return: The description of this OrganizationSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrganizationSchema.

        Description about the organization  # noqa: E501

        :param description: The description of this OrganizationSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization_name(self):
        """Gets the organization_name of this OrganizationSchema.  # noqa: E501

        Name of the organization. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :return: The organization_name of this OrganizationSchema.  # noqa: E501
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this OrganizationSchema.

        Name of the organization. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]*  # noqa: E501

        :param organization_name: The organization_name of this OrganizationSchema.  # noqa: E501
        :type: str
        """
        if organization_name is None:
            raise ValueError("Invalid value for `organization_name`, must not be `None`")  # noqa: E501
        if organization_name is not None and len(organization_name) > 64:
            raise ValueError("Invalid value for `organization_name`, length must be less than or equal to `64`")  # noqa: E501
        if organization_name is not None and len(organization_name) < 1:
            raise ValueError("Invalid value for `organization_name`, length must be greater than or equal to `1`")  # noqa: E501
        if organization_name is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9_-]*$', organization_name):  # noqa: E501
            raise ValueError(r"Invalid value for `organization_name`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9_-]*$/`")  # noqa: E501

        self._organization_name = organization_name

    @property
    def site(self):
        """Gets the site of this OrganizationSchema.  # noqa: E501


        :return: The site of this OrganizationSchema.  # noqa: E501
        :rtype: list[SiteSchema]
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this OrganizationSchema.


        :param site: The site of this OrganizationSchema.  # noqa: E501
        :type: list[SiteSchema]
        """

        self._site = site

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
        if issubclass(OrganizationSchema, dict):
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
        if not isinstance(other, OrganizationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
