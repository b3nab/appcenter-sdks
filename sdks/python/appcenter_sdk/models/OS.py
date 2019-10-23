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


class OS(object):
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
        'os_name': 'string',
        'count': 'integer',
        'previous_count': 'integer'
    }

    attribute_map = {
        'os_name': 'os_name',
        'count': 'count',
        'previous_count': 'previous_count'
    }

    def __init__(self, os_name=None, count=None, previous_count=None):  # noqa: E501
        """OS - a model defined in Swagger"""  # noqa: E501
        self._os_name = None
        self._count = None
        self._previous_count = None
        self.discriminator = None
        if os_name is not None:
            self.os_name = os_name
        if count is not None:
            self.count = count
        if previous_count is not None:
            self.previous_count = previous_count

    @property
    def os_name(self):
        """Gets the os_name of this OS.  # noqa: E501

        OS name  # noqa: E501

        :return: The os_name of this OS.  # noqa: E501
        :rtype: string
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this OS.

        OS name  # noqa: E501

        :param os_name: The os_name of this OS.  # noqa: E501
        :type: string
        """

        self._os_name = os_name

    @property
    def count(self):
        """Gets the count of this OS.  # noqa: E501

        count current of OS  # noqa: E501

        :return: The count of this OS.  # noqa: E501
        :rtype: integer
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this OS.

        count current of OS  # noqa: E501

        :param count: The count of this OS.  # noqa: E501
        :type: integer
        """

        self._count = count

    @property
    def previous_count(self):
        """Gets the previous_count of this OS.  # noqa: E501

        count of previous OS  # noqa: E501

        :return: The previous_count of this OS.  # noqa: E501
        :rtype: integer
        """
        return self._previous_count

    @previous_count.setter
    def previous_count(self, previous_count):
        """Sets the previous_count of this OS.

        count of previous OS  # noqa: E501

        :param previous_count: The previous_count of this OS.  # noqa: E501
        :type: integer
        """

        self._previous_count = previous_count

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
        if not isinstance(other, OS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other