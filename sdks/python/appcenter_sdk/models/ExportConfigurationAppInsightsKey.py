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


class ExportConfigurationAppInsightsKey(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    crashes = "crashes"
    errors = "errors"
    attachments = "attachments"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'instrumentation_key': 'string'
    }

    attribute_map = {
        'instrumentation_key': 'instrumentation_key'
    }

    def __init__(self, instrumentation_key=None):  # noqa: E501
        """ExportConfigurationAppInsightsKey - a model defined in Swagger"""  # noqa: E501
        self._instrumentation_key = None
        self.discriminator = None
        self.instrumentation_key = instrumentation_key

    @property
    def instrumentation_key(self):
        """Gets the instrumentation_key of this ExportConfigurationAppInsightsKey.  # noqa: E501

        Instrumentation key for Application Insights resource  # noqa: E501

        :return: The instrumentation_key of this ExportConfigurationAppInsightsKey.  # noqa: E501
        :rtype: string
        """
        return self._instrumentation_key

    @instrumentation_key.setter
    def instrumentation_key(self, instrumentation_key):
        """Sets the instrumentation_key of this ExportConfigurationAppInsightsKey.

        Instrumentation key for Application Insights resource  # noqa: E501

        :param instrumentation_key: The instrumentation_key of this ExportConfigurationAppInsightsKey.  # noqa: E501
        :type: string
        """
        if instrumentation_key is None:
            raise ValueError("Invalid value for `instrumentation_key`, must not be `None`")  # noqa: E501

        self._instrumentation_key = instrumentation_key

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
        if not isinstance(other, ExportConfigurationAppInsightsKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
