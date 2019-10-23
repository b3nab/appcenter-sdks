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


class v2MissingSymbolCrashGroup(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    active = "active"
    pending = "pending"
    closed = "closed"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'symbol_group_id': 'string',
        'crash_count': 'integer',
        'app_id': 'string',
        'app_ver': 'string',
        'app_build': 'string',
        'last_modified': 'string',
        'missing_symbols': 'array',
        'status': 'string'
    }

    attribute_map = {
        'symbol_group_id': 'symbol_group_id',
        'crash_count': 'crash_count',
        'app_id': 'app_id',
        'app_ver': 'app_ver',
        'app_build': 'app_build',
        'last_modified': 'last_modified',
        'missing_symbols': 'missing_symbols',
        'status': 'status'
    }

    def __init__(self, symbol_group_id=None, crash_count=None, app_id=None, app_ver=None, app_build=None, last_modified=None, missing_symbols=None, status=None):  # noqa: E501
        """v2MissingSymbolCrashGroup - a model defined in Swagger"""  # noqa: E501
        self._symbol_group_id = None
        self._crash_count = None
        self._app_id = None
        self._app_ver = None
        self._app_build = None
        self._last_modified = None
        self._missing_symbols = None
        self._status = None
        self.discriminator = None
        self.symbol_group_id = symbol_group_id
        if crash_count is not None:
            self.crash_count = crash_count
        self.app_id = app_id
        self.app_ver = app_ver
        self.app_build = app_build
        self.last_modified = last_modified
        self.missing_symbols = missing_symbols
        self.status = status

    @property
    def symbol_group_id(self):
        """Gets the symbol_group_id of this v2MissingSymbolCrashGroup.  # noqa: E501

        id of the symbol group  # noqa: E501

        :return: The symbol_group_id of this v2MissingSymbolCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._symbol_group_id

    @symbol_group_id.setter
    def symbol_group_id(self, symbol_group_id):
        """Sets the symbol_group_id of this v2MissingSymbolCrashGroup.

        id of the symbol group  # noqa: E501

        :param symbol_group_id: The symbol_group_id of this v2MissingSymbolCrashGroup.  # noqa: E501
        :type: string
        """
        if symbol_group_id is None:
            raise ValueError("Invalid value for `symbol_group_id`, must not be `None`")  # noqa: E501

        self._symbol_group_id = symbol_group_id

    @property
    def crash_count(self):
        """Gets the crash_count of this v2MissingSymbolCrashGroup.  # noqa: E501

        number of crashes that belong to this group  # noqa: E501

        :return: The crash_count of this v2MissingSymbolCrashGroup.  # noqa: E501
        :rtype: integer
        """
        return self._crash_count

    @crash_count.setter
    def crash_count(self, crash_count):
        """Sets the crash_count of this v2MissingSymbolCrashGroup.

        number of crashes that belong to this group  # noqa: E501

        :param crash_count: The crash_count of this v2MissingSymbolCrashGroup.  # noqa: E501
        :type: integer
        """

        self._crash_count = crash_count

    @property
    def app_id(self):
        """Gets the app_id of this v2MissingSymbolCrashGroup.  # noqa: E501

        application id  # noqa: E501

        :return: The app_id of this v2MissingSymbolCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this v2MissingSymbolCrashGroup.

        application id  # noqa: E501

        :param app_id: The app_id of this v2MissingSymbolCrashGroup.  # noqa: E501
        :type: string
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def app_ver(self):
        """Gets the app_ver of this v2MissingSymbolCrashGroup.  # noqa: E501

        application version  # noqa: E501

        :return: The app_ver of this v2MissingSymbolCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._app_ver

    @app_ver.setter
    def app_ver(self, app_ver):
        """Sets the app_ver of this v2MissingSymbolCrashGroup.

        application version  # noqa: E501

        :param app_ver: The app_ver of this v2MissingSymbolCrashGroup.  # noqa: E501
        :type: string
        """
        if app_ver is None:
            raise ValueError("Invalid value for `app_ver`, must not be `None`")  # noqa: E501

        self._app_ver = app_ver

    @property
    def app_build(self):
        """Gets the app_build of this v2MissingSymbolCrashGroup.  # noqa: E501

        application build  # noqa: E501

        :return: The app_build of this v2MissingSymbolCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._app_build

    @app_build.setter
    def app_build(self, app_build):
        """Sets the app_build of this v2MissingSymbolCrashGroup.

        application build  # noqa: E501

        :param app_build: The app_build of this v2MissingSymbolCrashGroup.  # noqa: E501
        :type: string
        """
        if app_build is None:
            raise ValueError("Invalid value for `app_build`, must not be `None`")  # noqa: E501

        self._app_build = app_build

    @property
    def last_modified(self):
        """Gets the last_modified of this v2MissingSymbolCrashGroup.  # noqa: E501

        last update date for the group  # noqa: E501

        :return: The last_modified of this v2MissingSymbolCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this v2MissingSymbolCrashGroup.

        last update date for the group  # noqa: E501

        :param last_modified: The last_modified of this v2MissingSymbolCrashGroup.  # noqa: E501
        :type: string
        """
        if last_modified is None:
            raise ValueError("Invalid value for `last_modified`, must not be `None`")  # noqa: E501

        self._last_modified = last_modified

    @property
    def missing_symbols(self):
        """Gets the missing_symbols of this v2MissingSymbolCrashGroup.  # noqa: E501

        A list of missing symbols  # noqa: E501

        :return: The missing_symbols of this v2MissingSymbolCrashGroup.  # noqa: E501
        :rtype: array
        """
        return self._missing_symbols

    @missing_symbols.setter
    def missing_symbols(self, missing_symbols):
        """Sets the missing_symbols of this v2MissingSymbolCrashGroup.

        A list of missing symbols  # noqa: E501

        :param missing_symbols: The missing_symbols of this v2MissingSymbolCrashGroup.  # noqa: E501
        :type: array
        """
        if missing_symbols is None:
            raise ValueError("Invalid value for `missing_symbols`, must not be `None`")  # noqa: E501

        self._missing_symbols = missing_symbols

    @property
    def status(self):
        """Gets the status of this v2MissingSymbolCrashGroup.  # noqa: E501

        group status  # noqa: E501

        :return: The status of this v2MissingSymbolCrashGroup.  # noqa: E501
        :rtype: string
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this v2MissingSymbolCrashGroup.

        group status  # noqa: E501

        :param status: The status of this v2MissingSymbolCrashGroup.  # noqa: E501
        :type: string
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = [undefinedundefinedundefined]  # noqa: E501

        self._status = status

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
        if not isinstance(other, v2MissingSymbolCrashGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other