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


class PanelDataSchema(object):
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
        'add_group_by_tag': 'PanelDataSchemaAddGroupByTag',
        'add_where_condition': 'PanelDataSchemaAddWhereCondition',
        'change_where_key_field': 'PanelDataSchemaChangeWhereKeyField',
        'group_by_fill': 'PanelDataSchemaGroupByFill',
        'group_by_time': 'PanelDataSchemaGroupByTime',
        'group_type': 'str',
        'selected_aggregation': 'PanelDataSchemaSelectedAggregation',
        'selected_device': 'PanelDataSchemaSelectedDevice',
        'selected_dropdown': 'PanelDataSchemaSelectedDropdown',
        'selected_field': 'PanelDataSchemaSelectedField',
        'selected_group': 'PanelDataSchemaSelectedGroup',
        'selected_logical_operator': 'PanelDataSchemaSelectedLogicalOperator',
        'selected_topic': 'PanelDataSchemaSelectedTopic',
        'selected_transformation': 'PanelDataSchemaSelectedTransformation'
    }

    attribute_map = {
        'add_group_by_tag': 'addGroupByTag',
        'add_where_condition': 'addWhereCondition',
        'change_where_key_field': 'changeWhereKeyField',
        'group_by_fill': 'groupByFill',
        'group_by_time': 'groupByTime',
        'group_type': 'groupType',
        'selected_aggregation': 'selectedAggregation',
        'selected_device': 'selectedDevice',
        'selected_dropdown': 'selectedDropdown',
        'selected_field': 'selectedField',
        'selected_group': 'selectedGroup',
        'selected_logical_operator': 'selectedLogicalOperator',
        'selected_topic': 'selectedTopic',
        'selected_transformation': 'selectedTransformation'
    }

    def __init__(self, add_group_by_tag=None, add_where_condition=None, change_where_key_field=None, group_by_fill=None, group_by_time=None, group_type=None, selected_aggregation=None, selected_device=None, selected_dropdown=None, selected_field=None, selected_group=None, selected_logical_operator=None, selected_topic=None, selected_transformation=None):  # noqa: E501
        """PanelDataSchema - a model defined in Swagger"""  # noqa: E501

        self._add_group_by_tag = None
        self._add_where_condition = None
        self._change_where_key_field = None
        self._group_by_fill = None
        self._group_by_time = None
        self._group_type = None
        self._selected_aggregation = None
        self._selected_device = None
        self._selected_dropdown = None
        self._selected_field = None
        self._selected_group = None
        self._selected_logical_operator = None
        self._selected_topic = None
        self._selected_transformation = None
        self.discriminator = None

        if add_group_by_tag is not None:
            self.add_group_by_tag = add_group_by_tag
        if add_where_condition is not None:
            self.add_where_condition = add_where_condition
        if change_where_key_field is not None:
            self.change_where_key_field = change_where_key_field
        if group_by_fill is not None:
            self.group_by_fill = group_by_fill
        if group_by_time is not None:
            self.group_by_time = group_by_time
        if group_type is not None:
            self.group_type = group_type
        if selected_aggregation is not None:
            self.selected_aggregation = selected_aggregation
        if selected_device is not None:
            self.selected_device = selected_device
        if selected_dropdown is not None:
            self.selected_dropdown = selected_dropdown
        if selected_field is not None:
            self.selected_field = selected_field
        if selected_group is not None:
            self.selected_group = selected_group
        if selected_logical_operator is not None:
            self.selected_logical_operator = selected_logical_operator
        if selected_topic is not None:
            self.selected_topic = selected_topic
        if selected_transformation is not None:
            self.selected_transformation = selected_transformation

    @property
    def add_group_by_tag(self):
        """Gets the add_group_by_tag of this PanelDataSchema.  # noqa: E501


        :return: The add_group_by_tag of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaAddGroupByTag
        """
        return self._add_group_by_tag

    @add_group_by_tag.setter
    def add_group_by_tag(self, add_group_by_tag):
        """Sets the add_group_by_tag of this PanelDataSchema.


        :param add_group_by_tag: The add_group_by_tag of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaAddGroupByTag
        """

        self._add_group_by_tag = add_group_by_tag

    @property
    def add_where_condition(self):
        """Gets the add_where_condition of this PanelDataSchema.  # noqa: E501


        :return: The add_where_condition of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaAddWhereCondition
        """
        return self._add_where_condition

    @add_where_condition.setter
    def add_where_condition(self, add_where_condition):
        """Sets the add_where_condition of this PanelDataSchema.


        :param add_where_condition: The add_where_condition of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaAddWhereCondition
        """

        self._add_where_condition = add_where_condition

    @property
    def change_where_key_field(self):
        """Gets the change_where_key_field of this PanelDataSchema.  # noqa: E501


        :return: The change_where_key_field of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaChangeWhereKeyField
        """
        return self._change_where_key_field

    @change_where_key_field.setter
    def change_where_key_field(self, change_where_key_field):
        """Sets the change_where_key_field of this PanelDataSchema.


        :param change_where_key_field: The change_where_key_field of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaChangeWhereKeyField
        """

        self._change_where_key_field = change_where_key_field

    @property
    def group_by_fill(self):
        """Gets the group_by_fill of this PanelDataSchema.  # noqa: E501


        :return: The group_by_fill of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaGroupByFill
        """
        return self._group_by_fill

    @group_by_fill.setter
    def group_by_fill(self, group_by_fill):
        """Sets the group_by_fill of this PanelDataSchema.


        :param group_by_fill: The group_by_fill of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaGroupByFill
        """

        self._group_by_fill = group_by_fill

    @property
    def group_by_time(self):
        """Gets the group_by_time of this PanelDataSchema.  # noqa: E501


        :return: The group_by_time of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaGroupByTime
        """
        return self._group_by_time

    @group_by_time.setter
    def group_by_time(self, group_by_time):
        """Sets the group_by_time of this PanelDataSchema.


        :param group_by_time: The group_by_time of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaGroupByTime
        """

        self._group_by_time = group_by_time

    @property
    def group_type(self):
        """Gets the group_type of this PanelDataSchema.  # noqa: E501

        Group type(device/network)  # noqa: E501

        :return: The group_type of this PanelDataSchema.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this PanelDataSchema.

        Group type(device/network)  # noqa: E501

        :param group_type: The group_type of this PanelDataSchema.  # noqa: E501
        :type: str
        """

        self._group_type = group_type

    @property
    def selected_aggregation(self):
        """Gets the selected_aggregation of this PanelDataSchema.  # noqa: E501


        :return: The selected_aggregation of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaSelectedAggregation
        """
        return self._selected_aggregation

    @selected_aggregation.setter
    def selected_aggregation(self, selected_aggregation):
        """Sets the selected_aggregation of this PanelDataSchema.


        :param selected_aggregation: The selected_aggregation of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaSelectedAggregation
        """

        self._selected_aggregation = selected_aggregation

    @property
    def selected_device(self):
        """Gets the selected_device of this PanelDataSchema.  # noqa: E501


        :return: The selected_device of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaSelectedDevice
        """
        return self._selected_device

    @selected_device.setter
    def selected_device(self, selected_device):
        """Sets the selected_device of this PanelDataSchema.


        :param selected_device: The selected_device of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaSelectedDevice
        """

        self._selected_device = selected_device

    @property
    def selected_dropdown(self):
        """Gets the selected_dropdown of this PanelDataSchema.  # noqa: E501


        :return: The selected_dropdown of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaSelectedDropdown
        """
        return self._selected_dropdown

    @selected_dropdown.setter
    def selected_dropdown(self, selected_dropdown):
        """Sets the selected_dropdown of this PanelDataSchema.


        :param selected_dropdown: The selected_dropdown of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaSelectedDropdown
        """

        self._selected_dropdown = selected_dropdown

    @property
    def selected_field(self):
        """Gets the selected_field of this PanelDataSchema.  # noqa: E501


        :return: The selected_field of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaSelectedField
        """
        return self._selected_field

    @selected_field.setter
    def selected_field(self, selected_field):
        """Sets the selected_field of this PanelDataSchema.


        :param selected_field: The selected_field of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaSelectedField
        """

        self._selected_field = selected_field

    @property
    def selected_group(self):
        """Gets the selected_group of this PanelDataSchema.  # noqa: E501


        :return: The selected_group of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaSelectedGroup
        """
        return self._selected_group

    @selected_group.setter
    def selected_group(self, selected_group):
        """Sets the selected_group of this PanelDataSchema.


        :param selected_group: The selected_group of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaSelectedGroup
        """

        self._selected_group = selected_group

    @property
    def selected_logical_operator(self):
        """Gets the selected_logical_operator of this PanelDataSchema.  # noqa: E501


        :return: The selected_logical_operator of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaSelectedLogicalOperator
        """
        return self._selected_logical_operator

    @selected_logical_operator.setter
    def selected_logical_operator(self, selected_logical_operator):
        """Sets the selected_logical_operator of this PanelDataSchema.


        :param selected_logical_operator: The selected_logical_operator of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaSelectedLogicalOperator
        """

        self._selected_logical_operator = selected_logical_operator

    @property
    def selected_topic(self):
        """Gets the selected_topic of this PanelDataSchema.  # noqa: E501


        :return: The selected_topic of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaSelectedTopic
        """
        return self._selected_topic

    @selected_topic.setter
    def selected_topic(self, selected_topic):
        """Sets the selected_topic of this PanelDataSchema.


        :param selected_topic: The selected_topic of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaSelectedTopic
        """

        self._selected_topic = selected_topic

    @property
    def selected_transformation(self):
        """Gets the selected_transformation of this PanelDataSchema.  # noqa: E501


        :return: The selected_transformation of this PanelDataSchema.  # noqa: E501
        :rtype: PanelDataSchemaSelectedTransformation
        """
        return self._selected_transformation

    @selected_transformation.setter
    def selected_transformation(self, selected_transformation):
        """Sets the selected_transformation of this PanelDataSchema.


        :param selected_transformation: The selected_transformation of this PanelDataSchema.  # noqa: E501
        :type: PanelDataSchemaSelectedTransformation
        """

        self._selected_transformation = selected_transformation

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
        if issubclass(PanelDataSchema, dict):
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
        if not isinstance(other, PanelDataSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
