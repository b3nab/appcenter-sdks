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


class EventCountPerSession(object):
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
        'avg_count_per_session': 'number',
        'previous_avg_count_per_session': 'number',
        'count_per_session': 'array'
    }

    attribute_map = {
        'avg_count_per_session': 'avg_count_per_session',
        'previous_avg_count_per_session': 'previous_avg_count_per_session',
        'count_per_session': 'count_per_session'
    }

    def __init__(self, avg_count_per_session=None, previous_avg_count_per_session=None, count_per_session=None):  # noqa: E501
        """EventCountPerSession - a model defined in Swagger"""  # noqa: E501
        self._avg_count_per_session = None
        self._previous_avg_count_per_session = None
        self._count_per_session = None
        self.discriminator = None
        if avg_count_per_session is not None:
            self.avg_count_per_session = avg_count_per_session
        if previous_avg_count_per_session is not None:
            self.previous_avg_count_per_session = previous_avg_count_per_session
        if count_per_session is not None:
            self.count_per_session = count_per_session

    @property
    def avg_count_per_session(self):
        """Gets the avg_count_per_session of this EventCountPerSession.  # noqa: E501


        :return: The avg_count_per_session of this EventCountPerSession.  # noqa: E501
        :rtype: number
        """
        return self._avg_count_per_session

    @avg_count_per_session.setter
    def avg_count_per_session(self, avg_count_per_session):
        """Sets the avg_count_per_session of this EventCountPerSession.


        :param avg_count_per_session: The avg_count_per_session of this EventCountPerSession.  # noqa: E501
        :type: number
        """

        self._avg_count_per_session = avg_count_per_session

    @property
    def previous_avg_count_per_session(self):
        """Gets the previous_avg_count_per_session of this EventCountPerSession.  # noqa: E501


        :return: The previous_avg_count_per_session of this EventCountPerSession.  # noqa: E501
        :rtype: number
        """
        return self._previous_avg_count_per_session

    @previous_avg_count_per_session.setter
    def previous_avg_count_per_session(self, previous_avg_count_per_session):
        """Sets the previous_avg_count_per_session of this EventCountPerSession.


        :param previous_avg_count_per_session: The previous_avg_count_per_session of this EventCountPerSession.  # noqa: E501
        :type: number
        """

        self._previous_avg_count_per_session = previous_avg_count_per_session

    @property
    def count_per_session(self):
        """Gets the count_per_session of this EventCountPerSession.  # noqa: E501


        :return: The count_per_session of this EventCountPerSession.  # noqa: E501
        :rtype: array
        """
        return self._count_per_session

    @count_per_session.setter
    def count_per_session(self, count_per_session):
        """Sets the count_per_session of this EventCountPerSession.


        :param count_per_session: The count_per_session of this EventCountPerSession.  # noqa: E501
        :type: array
        """

        self._count_per_session = count_per_session

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
        if not isinstance(other, EventCountPerSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
