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


class TopicSchema(object):
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
        'resource': 'list[ResourceSchema]',
        'rule': 'list[RuleSchema]',
        'sub_topics': 'list[str]',
        'synopsis': 'str',
        'topic_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'resource': 'resource',
        'rule': 'rule',
        'sub_topics': 'sub-topics',
        'synopsis': 'synopsis',
        'topic_name': 'topic-name'
    }

    def __init__(self, description=None, resource=None, rule=None, sub_topics=None, synopsis=None, topic_name=None):  # noqa: E501
        """TopicSchema - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._resource = None
        self._rule = None
        self._sub_topics = None
        self._synopsis = None
        self._topic_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if resource is not None:
            self.resource = resource
        if rule is not None:
            self.rule = rule
        if sub_topics is not None:
            self.sub_topics = sub_topics
        if synopsis is not None:
            self.synopsis = synopsis
        self.topic_name = topic_name

    @property
    def description(self):
        """Gets the description of this TopicSchema.  # noqa: E501

        Description about this topic  # noqa: E501

        :return: The description of this TopicSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TopicSchema.

        Description about this topic  # noqa: E501

        :param description: The description of this TopicSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def resource(self):
        """Gets the resource of this TopicSchema.  # noqa: E501


        :return: The resource of this TopicSchema.  # noqa: E501
        :rtype: list[ResourceSchema]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this TopicSchema.


        :param resource: The resource of this TopicSchema.  # noqa: E501
        :type: list[ResourceSchema]
        """

        self._resource = resource

    @property
    def rule(self):
        """Gets the rule of this TopicSchema.  # noqa: E501


        :return: The rule of this TopicSchema.  # noqa: E501
        :rtype: list[RuleSchema]
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this TopicSchema.


        :param rule: The rule of this TopicSchema.  # noqa: E501
        :type: list[RuleSchema]
        """

        self._rule = rule

    @property
    def sub_topics(self):
        """Gets the sub_topics of this TopicSchema.  # noqa: E501


        :return: The sub_topics of this TopicSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_topics

    @sub_topics.setter
    def sub_topics(self, sub_topics):
        """Sets the sub_topics of this TopicSchema.


        :param sub_topics: The sub_topics of this TopicSchema.  # noqa: E501
        :type: list[str]
        """

        self._sub_topics = sub_topics

    @property
    def synopsis(self):
        """Gets the synopsis of this TopicSchema.  # noqa: E501

        Short description about this topic  # noqa: E501

        :return: The synopsis of this TopicSchema.  # noqa: E501
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """Sets the synopsis of this TopicSchema.

        Short description about this topic  # noqa: E501

        :param synopsis: The synopsis of this TopicSchema.  # noqa: E501
        :type: str
        """

        self._synopsis = synopsis

    @property
    def topic_name(self):
        """Gets the topic_name of this TopicSchema.  # noqa: E501

        Name of the topic. Should be of pattern [a-z][a-z-]*(\\.{1}[a-z0-9-]+)*  # noqa: E501

        :return: The topic_name of this TopicSchema.  # noqa: E501
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this TopicSchema.

        Name of the topic. Should be of pattern [a-z][a-z-]*(\\.{1}[a-z0-9-]+)*  # noqa: E501

        :param topic_name: The topic_name of this TopicSchema.  # noqa: E501
        :type: str
        """
        if topic_name is None:
            raise ValueError("Invalid value for `topic_name`, must not be `None`")  # noqa: E501
        if topic_name is not None and len(topic_name) > 64:
            raise ValueError("Invalid value for `topic_name`, length must be less than or equal to `64`")  # noqa: E501
        if topic_name is not None and not re.search(r'^[a-z][a-z-]*(\\.{1}[a-z0-9-]+)*$', topic_name):  # noqa: E501
            raise ValueError(r"Invalid value for `topic_name`, must be a follow pattern or equal to `/^[a-z][a-z-]*(\\.{1}[a-z0-9-]+)*$/`")  # noqa: E501

        self._topic_name = topic_name

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
        if issubclass(TopicSchema, dict):
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
        if not isinstance(other, TopicSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
