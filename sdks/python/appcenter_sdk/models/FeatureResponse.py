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


class FeatureResponse(object):
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
        'description': 'string',
        'display_name': 'string',
        'name': 'string',
        'state': 'integer'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'name': 'name',
        'state': 'state'
    }

    def __init__(self, description=None, display_name=None, name=None, state=None):  # noqa: E501
        """FeatureResponse - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._display_name = None
        self._name = None
        self._state = None
        self.discriminator = None
        if description is not None:
            self.description = description
        self.display_name = display_name
        self.name = name
        self.state = state

    @property
    def description(self):
        """Gets the description of this FeatureResponse.  # noqa: E501

        The description of the feature  # noqa: E501

        :return: The description of this FeatureResponse.  # noqa: E501
        :rtype: string
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeatureResponse.

        The description of the feature  # noqa: E501

        :param description: The description of this FeatureResponse.  # noqa: E501
        :type: string
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this FeatureResponse.  # noqa: E501

        The friendly name of the feature  # noqa: E501

        :return: The display_name of this FeatureResponse.  # noqa: E501
        :rtype: string
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this FeatureResponse.

        The friendly name of the feature  # noqa: E501

        :param display_name: The display_name of this FeatureResponse.  # noqa: E501
        :type: string
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def name(self):
        """Gets the name of this FeatureResponse.  # noqa: E501

        The unique name of the feature  # noqa: E501

        :return: The name of this FeatureResponse.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeatureResponse.

        The unique name of the feature  # noqa: E501

        :param name: The name of this FeatureResponse.  # noqa: E501
        :type: string
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def state(self):
        """Gets the state of this FeatureResponse.  # noqa: E501

        The state (unset, enabled, disabled) of the feature  # noqa: E501

        :return: The state of this FeatureResponse.  # noqa: E501
        :rtype: integer
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FeatureResponse.

        The state (unset, enabled, disabled) of the feature  # noqa: E501

        :param state: The state of this FeatureResponse.  # noqa: E501
        :type: integer
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

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
        if not isinstance(other, FeatureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
