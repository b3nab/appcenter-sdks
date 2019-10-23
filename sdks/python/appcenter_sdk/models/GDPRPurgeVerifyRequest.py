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


class GDPRPurgeVerifyRequest(object):
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
        'key': 'string'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key'
    }

    def __init__(self, id=None, key=None):  # noqa: E501
        """GDPRPurgeVerifyRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._key = None
        self.discriminator = None
        self.id = id
        self.key = key

    @property
    def id(self):
        """Gets the id of this GDPRPurgeVerifyRequest.  # noqa: E501

        deployment id  # noqa: E501

        :return: The id of this GDPRPurgeVerifyRequest.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GDPRPurgeVerifyRequest.

        deployment id  # noqa: E501

        :param id: The id of this GDPRPurgeVerifyRequest.  # noqa: E501
        :type: string
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def key(self):
        """Gets the key of this GDPRPurgeVerifyRequest.  # noqa: E501

        deployment key  # noqa: E501

        :return: The key of this GDPRPurgeVerifyRequest.  # noqa: E501
        :rtype: string
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this GDPRPurgeVerifyRequest.

        deployment key  # noqa: E501

        :param key: The key of this GDPRPurgeVerifyRequest.  # noqa: E501
        :type: string
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

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
        if not isinstance(other, GDPRPurgeVerifyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other