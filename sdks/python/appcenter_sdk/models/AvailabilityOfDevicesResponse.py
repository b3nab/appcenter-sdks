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


class AvailabilityOfDevicesResponse(object):
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
        'iphones': '',
        'ipads': '',
        'ipods': '',
        'watches': ''
    }

    attribute_map = {
        'iphones': 'iphones',
        'ipads': 'ipads',
        'ipods': 'ipods',
        'watches': 'watches'
    }

    def __init__(self, iphones=None, ipads=None, ipods=None, watches=None):  # noqa: E501
        """AvailabilityOfDevicesResponse - a model defined in Swagger"""  # noqa: E501
        self._iphones = None
        self._ipads = None
        self._ipods = None
        self._watches = None
        self.discriminator = None
        self.iphones = iphones
        self.ipads = ipads
        self.ipods = ipods
        self.watches = watches

    @property
    def iphones(self):
        """Gets the iphones of this AvailabilityOfDevicesResponse.  # noqa: E501

        ...  # noqa: E501

        :return: The iphones of this AvailabilityOfDevicesResponse.  # noqa: E501
        :rtype: 
        """
        return self._iphones

    @iphones.setter
    def iphones(self, iphones):
        """Sets the iphones of this AvailabilityOfDevicesResponse.

        ...  # noqa: E501

        :param iphones: The iphones of this AvailabilityOfDevicesResponse.  # noqa: E501
        :type: 
        """
        if iphones is None:
            raise ValueError("Invalid value for `iphones`, must not be `None`")  # noqa: E501

        self._iphones = iphones

    @property
    def ipads(self):
        """Gets the ipads of this AvailabilityOfDevicesResponse.  # noqa: E501

        ...  # noqa: E501

        :return: The ipads of this AvailabilityOfDevicesResponse.  # noqa: E501
        :rtype: 
        """
        return self._ipads

    @ipads.setter
    def ipads(self, ipads):
        """Sets the ipads of this AvailabilityOfDevicesResponse.

        ...  # noqa: E501

        :param ipads: The ipads of this AvailabilityOfDevicesResponse.  # noqa: E501
        :type: 
        """
        if ipads is None:
            raise ValueError("Invalid value for `ipads`, must not be `None`")  # noqa: E501

        self._ipads = ipads

    @property
    def ipods(self):
        """Gets the ipods of this AvailabilityOfDevicesResponse.  # noqa: E501

        ...  # noqa: E501

        :return: The ipods of this AvailabilityOfDevicesResponse.  # noqa: E501
        :rtype: 
        """
        return self._ipods

    @ipods.setter
    def ipods(self, ipods):
        """Sets the ipods of this AvailabilityOfDevicesResponse.

        ...  # noqa: E501

        :param ipods: The ipods of this AvailabilityOfDevicesResponse.  # noqa: E501
        :type: 
        """
        if ipods is None:
            raise ValueError("Invalid value for `ipods`, must not be `None`")  # noqa: E501

        self._ipods = ipods

    @property
    def watches(self):
        """Gets the watches of this AvailabilityOfDevicesResponse.  # noqa: E501

        ...  # noqa: E501

        :return: The watches of this AvailabilityOfDevicesResponse.  # noqa: E501
        :rtype: 
        """
        return self._watches

    @watches.setter
    def watches(self, watches):
        """Sets the watches of this AvailabilityOfDevicesResponse.

        ...  # noqa: E501

        :param watches: The watches of this AvailabilityOfDevicesResponse.  # noqa: E501
        :type: 
        """
        if watches is None:
            raise ValueError("Invalid value for `watches`, must not be `None`")  # noqa: E501

        self._watches = watches

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
        if not isinstance(other, AvailabilityOfDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
