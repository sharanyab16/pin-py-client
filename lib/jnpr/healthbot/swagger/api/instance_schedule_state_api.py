# coding: utf-8

"""
    Paragon Insights APIs

    API interface for PI application  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jnpr.healthbot.swagger.api_client import ApiClient


class InstanceScheduleStateApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def retrieve_instances_schedule_state(self, group_name, group_type, **kwargs):  # noqa: E501
        """Get scheduled state of playbook instances with schedule.  # noqa: E501

        Retrieve the scheduled state of instances with an active scheduler attached to it and present under the group with name passed in the path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_instances_schedule_state(group_name, group_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Group name (required)
        :param str group_type: Group type (required)
        :param str x_iam_token: authentication header object
        :return: InstancesScheduleStateSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_instances_schedule_state_with_http_info(group_name, group_type, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_instances_schedule_state_with_http_info(group_name, group_type, **kwargs)  # noqa: E501
            return data

    def retrieve_instances_schedule_state_with_http_info(self, group_name, group_type, **kwargs):  # noqa: E501
        """Get scheduled state of playbook instances with schedule.  # noqa: E501

        Retrieve the scheduled state of instances with an active scheduler attached to it and present under the group with name passed in the path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_instances_schedule_state_with_http_info(group_name, group_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Group name (required)
        :param str group_type: Group type (required)
        :param str x_iam_token: authentication header object
        :return: InstancesScheduleStateSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name', 'group_type', 'x_iam_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_instances_schedule_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `retrieve_instances_schedule_state`")  # noqa: E501
        # verify the required parameter 'group_type' is set
        if ('group_type' not in params or
                params['group_type'] is None):
            raise ValueError("Missing the required parameter `group_type` when calling `retrieve_instances_schedule_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['group_name'] = params['group_name']  # noqa: E501
        if 'group_type' in params:
            path_params['group_type'] = params['group_type']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/instances-schedule-state/{group_type}/{group_name}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InstancesScheduleStateSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_instances_schedule_state(self, group_name, group_type, instances_schedule_state, **kwargs):  # noqa: E501
        """Update scheduled state of playbook instances with schedule.  # noqa: E501

        Update the scheduled state of instances with active scheduler attached to it and present under the group with name passed in the path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_instances_schedule_state(group_name, group_type, instances_schedule_state, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Group name (required)
        :param str group_type: Group type (required)
        :param InstancesScheduleStateSchema instances_schedule_state: List of instances and their scheduled state (required)
        :param str x_iam_token: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_instances_schedule_state_with_http_info(group_name, group_type, instances_schedule_state, **kwargs)  # noqa: E501
        else:
            (data) = self.update_instances_schedule_state_with_http_info(group_name, group_type, instances_schedule_state, **kwargs)  # noqa: E501
            return data

    def update_instances_schedule_state_with_http_info(self, group_name, group_type, instances_schedule_state, **kwargs):  # noqa: E501
        """Update scheduled state of playbook instances with schedule.  # noqa: E501

        Update the scheduled state of instances with active scheduler attached to it and present under the group with name passed in the path parameter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_instances_schedule_state_with_http_info(group_name, group_type, instances_schedule_state, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group_name: Group name (required)
        :param str group_type: Group type (required)
        :param InstancesScheduleStateSchema instances_schedule_state: List of instances and their scheduled state (required)
        :param str x_iam_token: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_name', 'group_type', 'instances_schedule_state', 'x_iam_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_instances_schedule_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_name' is set
        if ('group_name' not in params or
                params['group_name'] is None):
            raise ValueError("Missing the required parameter `group_name` when calling `update_instances_schedule_state`")  # noqa: E501
        # verify the required parameter 'group_type' is set
        if ('group_type' not in params or
                params['group_type'] is None):
            raise ValueError("Missing the required parameter `group_type` when calling `update_instances_schedule_state`")  # noqa: E501
        # verify the required parameter 'instances_schedule_state' is set
        if ('instances_schedule_state' not in params or
                params['instances_schedule_state'] is None):
            raise ValueError("Missing the required parameter `instances_schedule_state` when calling `update_instances_schedule_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group_name' in params:
            path_params['group_name'] = params['group_name']  # noqa: E501
        if 'group_type' in params:
            path_params['group_type'] = params['group_type']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'instances_schedule_state' in params:
            body_params = params['instances_schedule_state']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/instances-schedule-state/{group_type}/{group_name}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
