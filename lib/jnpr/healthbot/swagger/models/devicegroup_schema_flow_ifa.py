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


class DevicegroupSchemaFlowIfa(object):
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
        'ports': 'list[int]',
        'deploy_nodes': 'list[str]'
    }

    attribute_map = {
        'ports': 'ports',
        'deploy_nodes': 'deploy-nodes'
    }

    def __init__(self, ports=None, deploy_nodes=None):  # noqa: E501
        """DevicegroupSchemaFlowIfa - a model defined in Swagger"""  # noqa: E501

        self._ports = None
        self._deploy_nodes = None
        self.discriminator = None

        if ports is not None:
            self.ports = ports
        if deploy_nodes is not None:
            self.deploy_nodes = deploy_nodes

    @property
    def ports(self):
        """Gets the ports of this DevicegroupSchemaFlowIfa.  # noqa: E501


        :return: The ports of this DevicegroupSchemaFlowIfa.  # noqa: E501
        :rtype: list[int]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this DevicegroupSchemaFlowIfa.


        :param ports: The ports of this DevicegroupSchemaFlowIfa.  # noqa: E501
        :type: list[int]
        """

        self._ports = ports

    @property
    def deploy_nodes(self):
        """Gets the deploy_nodes of this DevicegroupSchemaFlowIfa.  # noqa: E501


        :return: The deploy_nodes of this DevicegroupSchemaFlowIfa.  # noqa: E501
        :rtype: list[str]
        """
        return self._deploy_nodes

    @deploy_nodes.setter
    def deploy_nodes(self, deploy_nodes):
        """Sets the deploy_nodes of this DevicegroupSchemaFlowIfa.


        :param deploy_nodes: The deploy_nodes of this DevicegroupSchemaFlowIfa.  # noqa: E501
        :type: list[str]
        """

        self._deploy_nodes = deploy_nodes

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
        if issubclass(DevicegroupSchemaFlowIfa, dict):
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
        if not isinstance(other, DevicegroupSchemaFlowIfa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
