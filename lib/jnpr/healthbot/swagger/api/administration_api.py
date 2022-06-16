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


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from jnpr.healthbot.swagger.api_client import ApiClient


class AdministrationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def healthbot_alter_app_settings(self, **kwargs):  # noqa: E501
        """Change runtime app-settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.healthbot_alter_app_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_iam_token: authentication header object
        :param object app_settings: Maintenance endpoint to change app-settings. Not accessible externally.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.healthbot_alter_app_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.healthbot_alter_app_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def healthbot_alter_app_settings_with_http_info(self, **kwargs):  # noqa: E501
        """Change runtime app-settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.healthbot_alter_app_settings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_iam_token: authentication header object
        :param object app_settings: Maintenance endpoint to change app-settings. Not accessible externally.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_iam_token', 'app_settings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method healthbot_alter_app_settings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'app_settings' in params:
            body_params = params['app_settings']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/config/app-settings/', 'POST',
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
