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


class IngestMappingsSchema(object):
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
        'ingest_mapping': 'list[IngestMappingSchema]'
    }

    attribute_map = {
        'ingest_mapping': 'ingest-mapping'
    }

    def __init__(self, ingest_mapping=None):  # noqa: E501
        """IngestMappingsSchema - a model defined in Swagger"""  # noqa: E501

        self._ingest_mapping = None
        self.discriminator = None

        self.ingest_mapping = ingest_mapping

    @property
    def ingest_mapping(self):
        """Gets the ingest_mapping of this IngestMappingsSchema.  # noqa: E501


        :return: The ingest_mapping of this IngestMappingsSchema.  # noqa: E501
        :rtype: list[IngestMappingSchema]
        """
        return self._ingest_mapping

    @ingest_mapping.setter
    def ingest_mapping(self, ingest_mapping):
        """Sets the ingest_mapping of this IngestMappingsSchema.


        :param ingest_mapping: The ingest_mapping of this IngestMappingsSchema.  # noqa: E501
        :type: list[IngestMappingSchema]
        """
        if ingest_mapping is None:
            raise ValueError("Invalid value for `ingest_mapping`, must not be `None`")  # noqa: E501

        self._ingest_mapping = ingest_mapping

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
        if issubclass(IngestMappingsSchema, dict):
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
        if not isinstance(other, IngestMappingsSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
