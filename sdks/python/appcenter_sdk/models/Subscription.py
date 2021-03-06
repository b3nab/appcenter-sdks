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


class Subscription(object):
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
        'subscription': 'object',
        'starts_at': 'string',
        'ends_at': 'string',
        'days_left': 'number',
        'subscription_tier': 'object',
        'active': 'boolean',
        'id': 'string'
    }

    attribute_map = {
        'subscription': 'subscription',
        'starts_at': 'starts_at',
        'ends_at': 'ends_at',
        'days_left': 'days_left',
        'subscription_tier': 'subscription_tier',
        'active': 'active',
        'id': 'id'
    }

    def __init__(self, subscription=None, starts_at=None, ends_at=None, days_left=None, subscription_tier=None, active=None, id=None):  # noqa: E501
        """Subscription - a model defined in Swagger"""  # noqa: E501
        self._subscription = None
        self._starts_at = None
        self._ends_at = None
        self._days_left = None
        self._subscription_tier = None
        self._active = None
        self._id = None
        self.discriminator = None
        if subscription is not None:
            self.subscription = subscription
        if starts_at is not None:
            self.starts_at = starts_at
        if ends_at is not None:
            self.ends_at = ends_at
        if days_left is not None:
            self.days_left = days_left
        if subscription_tier is not None:
            self.subscription_tier = subscription_tier
        if active is not None:
            self.active = active
        if id is not None:
            self.id = id

    @property
    def subscription(self):
        """Gets the subscription of this Subscription.  # noqa: E501

        Subscription information  # noqa: E501

        :return: The subscription of this Subscription.  # noqa: E501
        :rtype: object
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this Subscription.

        Subscription information  # noqa: E501

        :param subscription: The subscription of this Subscription.  # noqa: E501
        :type: object
        """

        self._subscription = subscription

    @property
    def starts_at(self):
        """Gets the starts_at of this Subscription.  # noqa: E501

        The date the subscription began  # noqa: E501

        :return: The starts_at of this Subscription.  # noqa: E501
        :rtype: string
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this Subscription.

        The date the subscription began  # noqa: E501

        :param starts_at: The starts_at of this Subscription.  # noqa: E501
        :type: string
        """

        self._starts_at = starts_at

    @property
    def ends_at(self):
        """Gets the ends_at of this Subscription.  # noqa: E501

        The date the subscription will end or ended  # noqa: E501

        :return: The ends_at of this Subscription.  # noqa: E501
        :rtype: string
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this Subscription.

        The date the subscription will end or ended  # noqa: E501

        :param ends_at: The ends_at of this Subscription.  # noqa: E501
        :type: string
        """

        self._ends_at = ends_at

    @property
    def days_left(self):
        """Gets the days_left of this Subscription.  # noqa: E501

        The number of days left in the subscription  # noqa: E501

        :return: The days_left of this Subscription.  # noqa: E501
        :rtype: number
        """
        return self._days_left

    @days_left.setter
    def days_left(self, days_left):
        """Sets the days_left of this Subscription.

        The number of days left in the subscription  # noqa: E501

        :param days_left: The days_left of this Subscription.  # noqa: E501
        :type: number
        """

        self._days_left = days_left

    @property
    def subscription_tier(self):
        """Gets the subscription_tier of this Subscription.  # noqa: E501


        :return: The subscription_tier of this Subscription.  # noqa: E501
        :rtype: object
        """
        return self._subscription_tier

    @subscription_tier.setter
    def subscription_tier(self, subscription_tier):
        """Sets the subscription_tier of this Subscription.


        :param subscription_tier: The subscription_tier of this Subscription.  # noqa: E501
        :type: object
        """

        self._subscription_tier = subscription_tier

    @property
    def active(self):
        """Gets the active of this Subscription.  # noqa: E501

        Is the subscription currently active?  # noqa: E501

        :return: The active of this Subscription.  # noqa: E501
        :rtype: boolean
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Subscription.

        Is the subscription currently active?  # noqa: E501

        :param active: The active of this Subscription.  # noqa: E501
        :type: boolean
        """

        self._active = active

    @property
    def id(self):
        """Gets the id of this Subscription.  # noqa: E501

        Id of the subscription  # noqa: E501

        :return: The id of this Subscription.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscription.

        Id of the subscription  # noqa: E501

        :param id: The id of this Subscription.  # noqa: E501
        :type: string
        """

        self._id = id

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
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
