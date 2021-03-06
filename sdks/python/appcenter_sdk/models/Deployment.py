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


class Deployment(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    Upload = "Upload"
    Promote = "Promote"
    Rollback = "Rollback"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'key': 'string',
        'name': 'string',
        'latest_release': ''
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'latest_release': 'latest_release'
    }

    def __init__(self, key=None, name=None, latest_release=None):  # noqa: E501
        """Deployment - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._name = None
        self._latest_release = None
        self.discriminator = None
        if key is not None:
            self.key = key
        self.name = name
        if latest_release is not None:
            self.latest_release = latest_release

    @property
    def key(self):
        """Gets the key of this Deployment.  # noqa: E501


        :return: The key of this Deployment.  # noqa: E501
        :rtype: string
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Deployment.


        :param key: The key of this Deployment.  # noqa: E501
        :type: string
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this Deployment.  # noqa: E501


        :return: The name of this Deployment.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Deployment.


        :param name: The name of this Deployment.  # noqa: E501
        :type: string
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def latest_release(self):
        """Gets the latest_release of this Deployment.  # noqa: E501


        :return: The latest_release of this Deployment.  # noqa: E501
        :rtype: 
        """
        return self._latest_release

    @latest_release.setter
    def latest_release(self, latest_release):
        """Sets the latest_release of this Deployment.


        :param latest_release: The latest_release of this Deployment.  # noqa: E501
        :type: 
        """

        self._latest_release = latest_release

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
        if not isinstance(other, Deployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
