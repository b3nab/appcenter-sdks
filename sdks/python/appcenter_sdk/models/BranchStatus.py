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


class BranchStatus(object):
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
        'configured': 'boolean',
        'last_build': ''
    }

    attribute_map = {
        'configured': 'configured',
        'last_build': 'last_build'
    }

    def __init__(self, configured=None, last_build=None):  # noqa: E501
        """BranchStatus - a model defined in Swagger"""  # noqa: E501
        self._configured = None
        self._last_build = None
        self.discriminator = None
        self.configured = configured
        if last_build is not None:
            self.last_build = last_build

    @property
    def configured(self):
        """Gets the configured of this BranchStatus.  # noqa: E501


        :return: The configured of this BranchStatus.  # noqa: E501
        :rtype: boolean
        """
        return self._configured

    @configured.setter
    def configured(self, configured):
        """Sets the configured of this BranchStatus.


        :param configured: The configured of this BranchStatus.  # noqa: E501
        :type: boolean
        """
        if configured is None:
            raise ValueError("Invalid value for `configured`, must not be `None`")  # noqa: E501

        self._configured = configured

    @property
    def last_build(self):
        """Gets the last_build of this BranchStatus.  # noqa: E501


        :return: The last_build of this BranchStatus.  # noqa: E501
        :rtype: 
        """
        return self._last_build

    @last_build.setter
    def last_build(self, last_build):
        """Sets the last_build of this BranchStatus.


        :param last_build: The last_build of this BranchStatus.  # noqa: E501
        :type: 
        """

        self._last_build = last_build

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
        if not isinstance(other, BranchStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
