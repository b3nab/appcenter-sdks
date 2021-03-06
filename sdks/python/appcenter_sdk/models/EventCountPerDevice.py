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


class EventCountPerDevice(object):
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
        'avg_count_per_device': 'number',
        'previous_avg_count_per_device': 'number',
        'count_per_device': 'array'
    }

    attribute_map = {
        'avg_count_per_device': 'avg_count_per_device',
        'previous_avg_count_per_device': 'previous_avg_count_per_device',
        'count_per_device': 'count_per_device'
    }

    def __init__(self, avg_count_per_device=None, previous_avg_count_per_device=None, count_per_device=None):  # noqa: E501
        """EventCountPerDevice - a model defined in Swagger"""  # noqa: E501
        self._avg_count_per_device = None
        self._previous_avg_count_per_device = None
        self._count_per_device = None
        self.discriminator = None
        if avg_count_per_device is not None:
            self.avg_count_per_device = avg_count_per_device
        if previous_avg_count_per_device is not None:
            self.previous_avg_count_per_device = previous_avg_count_per_device
        if count_per_device is not None:
            self.count_per_device = count_per_device

    @property
    def avg_count_per_device(self):
        """Gets the avg_count_per_device of this EventCountPerDevice.  # noqa: E501


        :return: The avg_count_per_device of this EventCountPerDevice.  # noqa: E501
        :rtype: number
        """
        return self._avg_count_per_device

    @avg_count_per_device.setter
    def avg_count_per_device(self, avg_count_per_device):
        """Sets the avg_count_per_device of this EventCountPerDevice.


        :param avg_count_per_device: The avg_count_per_device of this EventCountPerDevice.  # noqa: E501
        :type: number
        """

        self._avg_count_per_device = avg_count_per_device

    @property
    def previous_avg_count_per_device(self):
        """Gets the previous_avg_count_per_device of this EventCountPerDevice.  # noqa: E501


        :return: The previous_avg_count_per_device of this EventCountPerDevice.  # noqa: E501
        :rtype: number
        """
        return self._previous_avg_count_per_device

    @previous_avg_count_per_device.setter
    def previous_avg_count_per_device(self, previous_avg_count_per_device):
        """Sets the previous_avg_count_per_device of this EventCountPerDevice.


        :param previous_avg_count_per_device: The previous_avg_count_per_device of this EventCountPerDevice.  # noqa: E501
        :type: number
        """

        self._previous_avg_count_per_device = previous_avg_count_per_device

    @property
    def count_per_device(self):
        """Gets the count_per_device of this EventCountPerDevice.  # noqa: E501


        :return: The count_per_device of this EventCountPerDevice.  # noqa: E501
        :rtype: array
        """
        return self._count_per_device

    @count_per_device.setter
    def count_per_device(self, count_per_device):
        """Sets the count_per_device of this EventCountPerDevice.


        :param count_per_device: The count_per_device of this EventCountPerDevice.  # noqa: E501
        :type: array
        """

        self._count_per_device = count_per_device

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
        if not isinstance(other, EventCountPerDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
