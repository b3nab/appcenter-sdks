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


class ReleasePublishErrorResponse(object):
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
        'message': 'string',
        'is_logs_available': 'boolean'
    }

    attribute_map = {
        'message': 'message',
        'is_logs_available': 'is_logs_available'
    }

    def __init__(self, message=None, is_logs_available=None):  # noqa: E501
        """ReleasePublishErrorResponse - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._is_logs_available = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if is_logs_available is not None:
            self.is_logs_available = is_logs_available

    @property
    def message(self):
        """Gets the message of this ReleasePublishErrorResponse.  # noqa: E501

        error Details  # noqa: E501

        :return: The message of this ReleasePublishErrorResponse.  # noqa: E501
        :rtype: string
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ReleasePublishErrorResponse.

        error Details  # noqa: E501

        :param message: The message of this ReleasePublishErrorResponse.  # noqa: E501
        :type: string
        """

        self._message = message

    @property
    def is_logs_available(self):
        """Gets the is_logs_available of this ReleasePublishErrorResponse.  # noqa: E501

        boolean property to tell if logs are available for download  # noqa: E501

        :return: The is_logs_available of this ReleasePublishErrorResponse.  # noqa: E501
        :rtype: boolean
        """
        return self._is_logs_available

    @is_logs_available.setter
    def is_logs_available(self, is_logs_available):
        """Sets the is_logs_available of this ReleasePublishErrorResponse.

        boolean property to tell if logs are available for download  # noqa: E501

        :param is_logs_available: The is_logs_available of this ReleasePublishErrorResponse.  # noqa: E501
        :type: boolean
        """

        self._is_logs_available = is_logs_available

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
        if not isinstance(other, ReleasePublishErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
