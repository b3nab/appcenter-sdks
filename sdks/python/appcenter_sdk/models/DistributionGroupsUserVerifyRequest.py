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


class DistributionGroupsUserVerifyRequest(object):
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
        'distribution_group_ids': 'array'
    }

    attribute_map = {
        'distribution_group_ids': 'distribution_group_ids'
    }

    def __init__(self, distribution_group_ids=None):  # noqa: E501
        """DistributionGroupsUserVerifyRequest - a model defined in Swagger"""  # noqa: E501
        self._distribution_group_ids = None
        self.discriminator = None
        self.distribution_group_ids = distribution_group_ids

    @property
    def distribution_group_ids(self):
        """Gets the distribution_group_ids of this DistributionGroupsUserVerifyRequest.  # noqa: E501

        An array of distribution group ids  # noqa: E501

        :return: The distribution_group_ids of this DistributionGroupsUserVerifyRequest.  # noqa: E501
        :rtype: array
        """
        return self._distribution_group_ids

    @distribution_group_ids.setter
    def distribution_group_ids(self, distribution_group_ids):
        """Sets the distribution_group_ids of this DistributionGroupsUserVerifyRequest.

        An array of distribution group ids  # noqa: E501

        :param distribution_group_ids: The distribution_group_ids of this DistributionGroupsUserVerifyRequest.  # noqa: E501
        :type: array
        """
        if distribution_group_ids is None:
            raise ValueError("Invalid value for `distribution_group_ids`, must not be `None`")  # noqa: E501

        self._distribution_group_ids = distribution_group_ids

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
        if not isinstance(other, DistributionGroupsUserVerifyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
