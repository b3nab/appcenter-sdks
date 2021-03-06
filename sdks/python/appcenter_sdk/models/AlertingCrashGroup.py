# coding: utf-8

"""
    App Center Client

    Microsoft Visual Studio App Center API  # noqa: E501

    OpenAPI spec version: preview
    Contact: benedetto.abbenanti@gmail.com
    Project Repository: https://github.com/b3nab/appcenter-sdks
"""

import pprint
import re  # noqa: F401

import six


class AlertingCrashGroup(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ios = "ios"
    android = "android"
    xamarin = "xamarin"
    react-native = "react-native"
    ndk = "ndk"
    unity = "unity"
    other = "other"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'string',
        'app_display_name': 'string',
        'app_platform': 'string',
        'app_version': 'string',
        'id': 'string',
        'name': 'string',
        'reason': 'string',
        'stack_trace': 'array'
    }

    attribute_map = {
        'url': 'url',
        'app_display_name': 'app_display_name',
        'app_platform': 'app_platform',
        'app_version': 'app_version',
        'id': 'id',
        'name': 'name',
        'reason': 'reason',
        'stack_trace': 'stack_trace'
    }

    def __init__(self, url=None, app_display_name=None, app_platform=None, app_version=None, id=None, name=None, reason=None, stack_trace=None):  # noqa: E501
        """AlertingCrashGroup - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._app_display_name = None
        self._app_platform = None
        self._app_version = None
        self._id = None
        self._name = None
        self._reason = None
        self._stack_trace = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if app_display_name is not None:
            self.app_display_name = app_display_name
        if app_platform is not None:
            self.app_platform = app_platform
        if app_version is not None:
            self.app_version = app_version
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if reason is not None:
            self.reason = reason
        if stack_trace is not None:
            self.stack_trace = stack_trace

    @property
    def url(self):
        """Gets the url of this AlertingCrashGroup.  # noqa: E501


        :return: The url of this AlertingCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AlertingCrashGroup.


        :param url: The url of this AlertingCrashGroup.  # noqa: E501
        :type: string
        """

        self._url = url

    @property
    def app_display_name(self):
        """Gets the app_display_name of this AlertingCrashGroup.  # noqa: E501


        :return: The app_display_name of this AlertingCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._app_display_name

    @app_display_name.setter
    def app_display_name(self, app_display_name):
        """Sets the app_display_name of this AlertingCrashGroup.


        :param app_display_name: The app_display_name of this AlertingCrashGroup.  # noqa: E501
        :type: string
        """

        self._app_display_name = app_display_name

    @property
    def app_platform(self):
        """Gets the app_platform of this AlertingCrashGroup.  # noqa: E501

        SDK/Platform this thread is beeing generated from  # noqa: E501

        :return: The app_platform of this AlertingCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._app_platform

    @app_platform.setter
    def app_platform(self, app_platform):
        """Sets the app_platform of this AlertingCrashGroup.

        SDK/Platform this thread is beeing generated from  # noqa: E501

        :param app_platform: The app_platform of this AlertingCrashGroup.  # noqa: E501
        :type: string
        """
        allowed_values = [undefined, undefined, undefined, undefined, undefined, undefined, undefined, ]  # noqa: E501

        self._app_platform = app_platform

    @property
    def app_version(self):
        """Gets the app_version of this AlertingCrashGroup.  # noqa: E501


        :return: The app_version of this AlertingCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this AlertingCrashGroup.


        :param app_version: The app_version of this AlertingCrashGroup.  # noqa: E501
        :type: string
        """

        self._app_version = app_version

    @property
    def id(self):
        """Gets the id of this AlertingCrashGroup.  # noqa: E501


        :return: The id of this AlertingCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertingCrashGroup.


        :param id: The id of this AlertingCrashGroup.  # noqa: E501
        :type: string
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AlertingCrashGroup.  # noqa: E501


        :return: The name of this AlertingCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlertingCrashGroup.


        :param name: The name of this AlertingCrashGroup.  # noqa: E501
        :type: string
        """

        self._name = name

    @property
    def reason(self):
        """Gets the reason of this AlertingCrashGroup.  # noqa: E501


        :return: The reason of this AlertingCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this AlertingCrashGroup.


        :param reason: The reason of this AlertingCrashGroup.  # noqa: E501
        :type: string
        """

        self._reason = reason

    @property
    def stack_trace(self):
        """Gets the stack_trace of this AlertingCrashGroup.  # noqa: E501


        :return: The stack_trace of this AlertingCrashGroup.  # noqa: E501
        :rtype: array
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """Sets the stack_trace of this AlertingCrashGroup.


        :param stack_trace: The stack_trace of this AlertingCrashGroup.  # noqa: E501
        :type: array
        """

        self._stack_trace = stack_trace

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlertingCrashGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
