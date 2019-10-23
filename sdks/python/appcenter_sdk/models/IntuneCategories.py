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


class IntuneCategories(object):
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
        'odata_context': 'string',
        'value': 'array'
    }

    attribute_map = {
        'odata_context': 'odata_context',
        'value': 'value'
    }

    def __init__(self, odata_context=None, value=None):  # noqa: E501
        """IntuneCategories - a model defined in Swagger"""  # noqa: E501
        self._odata_context = None
        self._value = None
        self.discriminator = None
        if odata_context is not None:
            self.odata_context = odata_context
        if value is not None:
            self.value = value

    @property
    def odata_context(self):
        """Gets the odata_context of this IntuneCategories.  # noqa: E501

        context  # noqa: E501

        :return: The odata_context of this IntuneCategories.  # noqa: E501
        :rtype: string
        """
        return self._odata_context

    @odata_context.setter
    def odata_context(self, odata_context):
        """Sets the odata_context of this IntuneCategories.

        context  # noqa: E501

        :param odata_context: The odata_context of this IntuneCategories.  # noqa: E501
        :type: string
        """

        self._odata_context = odata_context

    @property
    def value(self):
        """Gets the value of this IntuneCategories.  # noqa: E501

        categories for intune app  # noqa: E501

        :return: The value of this IntuneCategories.  # noqa: E501
        :rtype: array
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IntuneCategories.

        categories for intune app  # noqa: E501

        :param value: The value of this IntuneCategories.  # noqa: E501
        :type: array
        """

        self._value = value

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
        if not isinstance(other, IntuneCategories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other