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


class DataSubjectRightResponse(object):
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
        'token': 'string',
        'created_at': 'string'
    }

    attribute_map = {
        'token': 'token',
        'created_at': 'created_at'
    }

    def __init__(self, token=None, created_at=None):  # noqa: E501
        """DataSubjectRightResponse - a model defined in Swagger"""  # noqa: E501
        self._token = None
        self._created_at = None
        self.discriminator = None
        self.token = token
        if created_at is not None:
            self.created_at = created_at

    @property
    def token(self):
        """Gets the token of this DataSubjectRightResponse.  # noqa: E501

        Unique request identifier  # noqa: E501

        :return: The token of this DataSubjectRightResponse.  # noqa: E501
        :rtype: string
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this DataSubjectRightResponse.

        Unique request identifier  # noqa: E501

        :param token: The token of this DataSubjectRightResponse.  # noqa: E501
        :type: string
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def created_at(self):
        """Gets the created_at of this DataSubjectRightResponse.  # noqa: E501

        ISO 8601 format timestamp of when request was created.  # noqa: E501

        :return: The created_at of this DataSubjectRightResponse.  # noqa: E501
        :rtype: string
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DataSubjectRightResponse.

        ISO 8601 format timestamp of when request was created.  # noqa: E501

        :param created_at: The created_at of this DataSubjectRightResponse.  # noqa: E501
        :type: string
        """

        self._created_at = created_at

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
        if not isinstance(other, DataSubjectRightResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
