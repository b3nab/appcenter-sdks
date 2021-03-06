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


class HandledErrorDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    JavaScript = "JavaScript"
    CSharp = "CSharp"
    Objective-C = "Objective-C"
    Objective-Cpp = "Objective-Cpp"
    Cpp = "Cpp"
    C = "C"
    Swift = "Swift"
    Java = "Java"
    Unknown = "Unknown"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'string',
        'reason_frames': 'array',
        'app_launch_timestamp': 'string',
        'carrier_name': 'string',
        'jailbreak': 'boolean',
        'properties': 'object'
    }

    attribute_map = {
        'name': 'name',
        'reason_frames': 'reason_frames',
        'app_launch_timestamp': 'app_launch_timestamp',
        'carrier_name': 'carrier_name',
        'jailbreak': 'jailbreak',
        'properties': 'properties'
    }

    def __init__(self, name=None, reason_frames=None, app_launch_timestamp=None, carrier_name=None, jailbreak=None, properties=None):  # noqa: E501
        """HandledErrorDetails - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._reason_frames = None
        self._app_launch_timestamp = None
        self._carrier_name = None
        self._jailbreak = None
        self._properties = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if reason_frames is not None:
            self.reason_frames = reason_frames
        if app_launch_timestamp is not None:
            self.app_launch_timestamp = app_launch_timestamp
        if carrier_name is not None:
            self.carrier_name = carrier_name
        if jailbreak is not None:
            self.jailbreak = jailbreak
        if properties is not None:
            self.properties = properties

    @property
    def name(self):
        """Gets the name of this HandledErrorDetails.  # noqa: E501


        :return: The name of this HandledErrorDetails.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HandledErrorDetails.


        :param name: The name of this HandledErrorDetails.  # noqa: E501
        :type: string
        """

        self._name = name

    @property
    def reason_frames(self):
        """Gets the reason_frames of this HandledErrorDetails.  # noqa: E501


        :return: The reason_frames of this HandledErrorDetails.  # noqa: E501
        :rtype: array
        """
        return self._reason_frames

    @reason_frames.setter
    def reason_frames(self, reason_frames):
        """Sets the reason_frames of this HandledErrorDetails.


        :param reason_frames: The reason_frames of this HandledErrorDetails.  # noqa: E501
        :type: array
        """

        self._reason_frames = reason_frames

    @property
    def app_launch_timestamp(self):
        """Gets the app_launch_timestamp of this HandledErrorDetails.  # noqa: E501

        Timestamp when the app was launched, example: '2017-03-13T18:05:42Z'.
  # noqa: E501

        :return: The app_launch_timestamp of this HandledErrorDetails.  # noqa: E501
        :rtype: string
        """
        return self._app_launch_timestamp

    @app_launch_timestamp.setter
    def app_launch_timestamp(self, app_launch_timestamp):
        """Sets the app_launch_timestamp of this HandledErrorDetails.

        Timestamp when the app was launched, example: '2017-03-13T18:05:42Z'.
  # noqa: E501

        :param app_launch_timestamp: The app_launch_timestamp of this HandledErrorDetails.  # noqa: E501
        :type: string
        """

        self._app_launch_timestamp = app_launch_timestamp

    @property
    def carrier_name(self):
        """Gets the carrier_name of this HandledErrorDetails.  # noqa: E501

        Carrier name (for mobile devices).
  # noqa: E501

        :return: The carrier_name of this HandledErrorDetails.  # noqa: E501
        :rtype: string
        """
        return self._carrier_name

    @carrier_name.setter
    def carrier_name(self, carrier_name):
        """Sets the carrier_name of this HandledErrorDetails.

        Carrier name (for mobile devices).
  # noqa: E501

        :param carrier_name: The carrier_name of this HandledErrorDetails.  # noqa: E501
        :type: string
        """

        self._carrier_name = carrier_name

    @property
    def jailbreak(self):
        """Gets the jailbreak of this HandledErrorDetails.  # noqa: E501

        Flag indicating if device is jailbroken
  # noqa: E501

        :return: The jailbreak of this HandledErrorDetails.  # noqa: E501
        :rtype: boolean
        """
        return self._jailbreak

    @jailbreak.setter
    def jailbreak(self, jailbreak):
        """Sets the jailbreak of this HandledErrorDetails.

        Flag indicating if device is jailbroken
  # noqa: E501

        :param jailbreak: The jailbreak of this HandledErrorDetails.  # noqa: E501
        :type: boolean
        """

        self._jailbreak = jailbreak

    @property
    def properties(self):
        """Gets the properties of this HandledErrorDetails.  # noqa: E501


        :return: The properties of this HandledErrorDetails.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this HandledErrorDetails.


        :param properties: The properties of this HandledErrorDetails.  # noqa: E501
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
        if not isinstance(other, HandledErrorDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
