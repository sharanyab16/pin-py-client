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


class RuleSchemaThenWorkflow(object):
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
        'argument': 'WorkflowArgumentGroupSchema',
        'batch': 'int',
        'retry': 'RuleSchemaThenRetry',
        'timeout': 'str',
        'workflow_name': 'str'
    }

    attribute_map = {
        'argument': 'argument',
        'batch': 'batch',
        'retry': 'retry',
        'timeout': 'timeout',
        'workflow_name': 'workflow-name'
    }

    def __init__(self, argument=None, batch=None, retry=None, timeout=None, workflow_name=None):  # noqa: E501
        """RuleSchemaThenWorkflow - a model defined in Swagger"""  # noqa: E501

        self._argument = None
        self._batch = None
        self._retry = None
        self._timeout = None
        self._workflow_name = None
        self.discriminator = None

        if argument is not None:
            self.argument = argument
        if batch is not None:
            self.batch = batch
        if retry is not None:
            self.retry = retry
        if timeout is not None:
            self.timeout = timeout
        self.workflow_name = workflow_name

    @property
    def argument(self):
        """Gets the argument of this RuleSchemaThenWorkflow.  # noqa: E501


        :return: The argument of this RuleSchemaThenWorkflow.  # noqa: E501
        :rtype: WorkflowArgumentGroupSchema
        """
        return self._argument

    @argument.setter
    def argument(self, argument):
        """Sets the argument of this RuleSchemaThenWorkflow.


        :param argument: The argument of this RuleSchemaThenWorkflow.  # noqa: E501
        :type: WorkflowArgumentGroupSchema
        """

        self._argument = argument

    @property
    def batch(self):
        """Gets the batch of this RuleSchemaThenWorkflow.  # noqa: E501

        Maximum parallel steps launched  # noqa: E501

        :return: The batch of this RuleSchemaThenWorkflow.  # noqa: E501
        :rtype: int
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this RuleSchemaThenWorkflow.

        Maximum parallel steps launched  # noqa: E501

        :param batch: The batch of this RuleSchemaThenWorkflow.  # noqa: E501
        :type: int
        """

        self._batch = batch

    @property
    def retry(self):
        """Gets the retry of this RuleSchemaThenWorkflow.  # noqa: E501


        :return: The retry of this RuleSchemaThenWorkflow.  # noqa: E501
        :rtype: RuleSchemaThenRetry
        """
        return self._retry

    @retry.setter
    def retry(self, retry):
        """Sets the retry of this RuleSchemaThenWorkflow.


        :param retry: The retry of this RuleSchemaThenWorkflow.  # noqa: E501
        :type: RuleSchemaThenRetry
        """

        self._retry = retry

    @property
    def timeout(self):
        """Gets the timeout of this RuleSchemaThenWorkflow.  # noqa: E501

        Maximum time to wait for the step completion before bailing out (default 60 seconds)  # noqa: E501

        :return: The timeout of this RuleSchemaThenWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this RuleSchemaThenWorkflow.

        Maximum time to wait for the step completion before bailing out (default 60 seconds)  # noqa: E501

        :param timeout: The timeout of this RuleSchemaThenWorkflow.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def workflow_name(self):
        """Gets the workflow_name of this RuleSchemaThenWorkflow.  # noqa: E501

        Name of the workflow to trigger  # noqa: E501

        :return: The workflow_name of this RuleSchemaThenWorkflow.  # noqa: E501
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this RuleSchemaThenWorkflow.

        Name of the workflow to trigger  # noqa: E501

        :param workflow_name: The workflow_name of this RuleSchemaThenWorkflow.  # noqa: E501
        :type: str
        """
        if workflow_name is None:
            raise ValueError("Invalid value for `workflow_name`, must not be `None`")  # noqa: E501

        self._workflow_name = workflow_name

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
        if issubclass(RuleSchemaThenWorkflow, dict):
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
        if not isinstance(other, RuleSchemaThenWorkflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
