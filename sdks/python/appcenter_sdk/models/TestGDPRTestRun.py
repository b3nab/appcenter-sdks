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


class TestGDPRTestRun(object):
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
        'id': 'string',
        'app_hash_file_id': 'string',
        'locale': 'string',
        'dsym_hash_file_id': 'string',
        'app_hash_file_url': 'string',
        'dsym_hash_file_url': 'string',
        'app_icon_url': 'string'
    }

    attribute_map = {
        'id': 'id',
        'app_hash_file_id': 'app_hash_file_id',
        'locale': 'locale',
        'dsym_hash_file_id': 'dsym_hash_file_id',
        'app_hash_file_url': 'app_hash_file_url',
        'dsym_hash_file_url': 'dsym_hash_file_url',
        'app_icon_url': 'app_icon_url'
    }

    def __init__(self, id=None, app_hash_file_id=None, locale=None, dsym_hash_file_id=None, app_hash_file_url=None, dsym_hash_file_url=None, app_icon_url=None):  # noqa: E501
        """TestGDPRTestRun - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._app_hash_file_id = None
        self._locale = None
        self._dsym_hash_file_id = None
        self._app_hash_file_url = None
        self._dsym_hash_file_url = None
        self._app_icon_url = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if app_hash_file_id is not None:
            self.app_hash_file_id = app_hash_file_id
        if locale is not None:
            self.locale = locale
        if dsym_hash_file_id is not None:
            self.dsym_hash_file_id = dsym_hash_file_id
        if app_hash_file_url is not None:
            self.app_hash_file_url = app_hash_file_url
        if dsym_hash_file_url is not None:
            self.dsym_hash_file_url = dsym_hash_file_url
        if app_icon_url is not None:
            self.app_icon_url = app_icon_url

    @property
    def id(self):
        """Gets the id of this TestGDPRTestRun.  # noqa: E501


        :return: The id of this TestGDPRTestRun.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestGDPRTestRun.


        :param id: The id of this TestGDPRTestRun.  # noqa: E501
        :type: string
        """

        self._id = id

    @property
    def app_hash_file_id(self):
        """Gets the app_hash_file_id of this TestGDPRTestRun.  # noqa: E501


        :return: The app_hash_file_id of this TestGDPRTestRun.  # noqa: E501
        :rtype: string
        """
        return self._app_hash_file_id

    @app_hash_file_id.setter
    def app_hash_file_id(self, app_hash_file_id):
        """Sets the app_hash_file_id of this TestGDPRTestRun.


        :param app_hash_file_id: The app_hash_file_id of this TestGDPRTestRun.  # noqa: E501
        :type: string
        """

        self._app_hash_file_id = app_hash_file_id

    @property
    def locale(self):
        """Gets the locale of this TestGDPRTestRun.  # noqa: E501


        :return: The locale of this TestGDPRTestRun.  # noqa: E501
        :rtype: string
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this TestGDPRTestRun.


        :param locale: The locale of this TestGDPRTestRun.  # noqa: E501
        :type: string
        """

        self._locale = locale

    @property
    def dsym_hash_file_id(self):
        """Gets the dsym_hash_file_id of this TestGDPRTestRun.  # noqa: E501


        :return: The dsym_hash_file_id of this TestGDPRTestRun.  # noqa: E501
        :rtype: string
        """
        return self._dsym_hash_file_id

    @dsym_hash_file_id.setter
    def dsym_hash_file_id(self, dsym_hash_file_id):
        """Sets the dsym_hash_file_id of this TestGDPRTestRun.


        :param dsym_hash_file_id: The dsym_hash_file_id of this TestGDPRTestRun.  # noqa: E501
        :type: string
        """

        self._dsym_hash_file_id = dsym_hash_file_id

    @property
    def app_hash_file_url(self):
        """Gets the app_hash_file_url of this TestGDPRTestRun.  # noqa: E501


        :return: The app_hash_file_url of this TestGDPRTestRun.  # noqa: E501
        :rtype: string
        """
        return self._app_hash_file_url

    @app_hash_file_url.setter
    def app_hash_file_url(self, app_hash_file_url):
        """Sets the app_hash_file_url of this TestGDPRTestRun.


        :param app_hash_file_url: The app_hash_file_url of this TestGDPRTestRun.  # noqa: E501
        :type: string
        """

        self._app_hash_file_url = app_hash_file_url

    @property
    def dsym_hash_file_url(self):
        """Gets the dsym_hash_file_url of this TestGDPRTestRun.  # noqa: E501


        :return: The dsym_hash_file_url of this TestGDPRTestRun.  # noqa: E501
        :rtype: string
        """
        return self._dsym_hash_file_url

    @dsym_hash_file_url.setter
    def dsym_hash_file_url(self, dsym_hash_file_url):
        """Sets the dsym_hash_file_url of this TestGDPRTestRun.


        :param dsym_hash_file_url: The dsym_hash_file_url of this TestGDPRTestRun.  # noqa: E501
        :type: string
        """

        self._dsym_hash_file_url = dsym_hash_file_url

    @property
    def app_icon_url(self):
        """Gets the app_icon_url of this TestGDPRTestRun.  # noqa: E501


        :return: The app_icon_url of this TestGDPRTestRun.  # noqa: E501
        :rtype: string
        """
        return self._app_icon_url

    @app_icon_url.setter
    def app_icon_url(self, app_icon_url):
        """Sets the app_icon_url of this TestGDPRTestRun.


        :param app_icon_url: The app_icon_url of this TestGDPRTestRun.  # noqa: E501
        :type: string
        """

        self._app_icon_url = app_icon_url

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
        if not isinstance(other, TestGDPRTestRun):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other