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


class DistributionGroupPatchRequest(object):
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
        'name': 'string',
        'is_public': 'boolean'
    }

    attribute_map = {
        'name': 'name',
        'is_public': 'is_public'
    }

    def __init__(self, name=None, is_public=None):  # noqa: E501
        """DistributionGroupPatchRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._is_public = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if is_public is not None:
            self.is_public = is_public

    @property
    def name(self):
        """Gets the name of this DistributionGroupPatchRequest.  # noqa: E501

        The name of the distribution group  # noqa: E501

        :return: The name of this DistributionGroupPatchRequest.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DistributionGroupPatchRequest.

        The name of the distribution group  # noqa: E501

        :param name: The name of this DistributionGroupPatchRequest.  # noqa: E501
        :type: string
        """

        self._name = name

    @property
    def is_public(self):
        """Gets the is_public of this DistributionGroupPatchRequest.  # noqa: E501

        Whether the distribution group is public  # noqa: E501

        :return: The is_public of this DistributionGroupPatchRequest.  # noqa: E501
        :rtype: boolean
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this DistributionGroupPatchRequest.

        Whether the distribution group is public  # noqa: E501

        :param is_public: The is_public of this DistributionGroupPatchRequest.  # noqa: E501
        :type: boolean
        """

        self._is_public = is_public

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
        if not isinstance(other, DistributionGroupPatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other