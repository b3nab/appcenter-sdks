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


class LogFlowLogWithProperties(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    event = "event"
    page = "page"
    start_session = "start_session"
    error = "error"
    push_installation = "push_installation"
    start_service = "start_service"
    custom_properties = "custom_properties"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'properties': 'object'
    }

    attribute_map = {
        'properties': 'properties'
    }

    def __init__(self, properties=None):  # noqa: E501
        """LogFlowLogWithProperties - a model defined in Swagger"""  # noqa: E501
        self._properties = None
        self.discriminator = None
        if properties is not None:
            self.properties = properties

    @property
    def properties(self):
        """Gets the properties of this LogFlowLogWithProperties.  # noqa: E501

        Additional key/value pair parameters.
  # noqa: E501

        :return: The properties of this LogFlowLogWithProperties.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this LogFlowLogWithProperties.

        Additional key/value pair parameters.
  # noqa: E501

        :param properties: The properties of this LogFlowLogWithProperties.  # noqa: E501
        :type: object
        """

        self._properties = properties

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
        if not isinstance(other, LogFlowLogWithProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
