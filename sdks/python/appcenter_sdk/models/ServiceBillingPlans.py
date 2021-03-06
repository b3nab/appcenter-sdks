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


class ServiceBillingPlans(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    Build = "Build"
    Test = "Test"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'can_select_trial_plan': 'boolean',
        'last_trial_plan_expiration_time': 'string',
        'current_billing_period': ''
    }

    attribute_map = {
        'can_select_trial_plan': 'can_select_trial_plan',
        'last_trial_plan_expiration_time': 'last_trial_plan_expiration_time',
        'current_billing_period': 'current_billing_period'
    }

    def __init__(self, can_select_trial_plan=None, last_trial_plan_expiration_time=None, current_billing_period=None):  # noqa: E501
        """ServiceBillingPlans - a model defined in Swagger"""  # noqa: E501
        self._can_select_trial_plan = None
        self._last_trial_plan_expiration_time = None
        self._current_billing_period = None
        self.discriminator = None
        if can_select_trial_plan is not None:
            self.can_select_trial_plan = can_select_trial_plan
        if last_trial_plan_expiration_time is not None:
            self.last_trial_plan_expiration_time = last_trial_plan_expiration_time
        if current_billing_period is not None:
            self.current_billing_period = current_billing_period

    @property
    def can_select_trial_plan(self):
        """Gets the can_select_trial_plan of this ServiceBillingPlans.  # noqa: E501

        Can customer select trial plan for that service (if it exists)?  # noqa: E501

        :return: The can_select_trial_plan of this ServiceBillingPlans.  # noqa: E501
        :rtype: boolean
        """
        return self._can_select_trial_plan

    @can_select_trial_plan.setter
    def can_select_trial_plan(self, can_select_trial_plan):
        """Sets the can_select_trial_plan of this ServiceBillingPlans.

        Can customer select trial plan for that service (if it exists)?  # noqa: E501

        :param can_select_trial_plan: The can_select_trial_plan of this ServiceBillingPlans.  # noqa: E501
        :type: boolean
        """

        self._can_select_trial_plan = can_select_trial_plan

    @property
    def last_trial_plan_expiration_time(self):
        """Gets the last_trial_plan_expiration_time of this ServiceBillingPlans.  # noqa: E501

        Expiration time of the last selected trial plan. Will be null if trial plan was not used.  # noqa: E501

        :return: The last_trial_plan_expiration_time of this ServiceBillingPlans.  # noqa: E501
        :rtype: string
        """
        return self._last_trial_plan_expiration_time

    @last_trial_plan_expiration_time.setter
    def last_trial_plan_expiration_time(self, last_trial_plan_expiration_time):
        """Sets the last_trial_plan_expiration_time of this ServiceBillingPlans.

        Expiration time of the last selected trial plan. Will be null if trial plan was not used.  # noqa: E501

        :param last_trial_plan_expiration_time: The last_trial_plan_expiration_time of this ServiceBillingPlans.  # noqa: E501
        :type: string
        """

        self._last_trial_plan_expiration_time = last_trial_plan_expiration_time

    @property
    def current_billing_period(self):
        """Gets the current_billing_period of this ServiceBillingPlans.  # noqa: E501

        Billing plans for a given period  # noqa: E501

        :return: The current_billing_period of this ServiceBillingPlans.  # noqa: E501
        :rtype: 
        """
        return self._current_billing_period

    @current_billing_period.setter
    def current_billing_period(self, current_billing_period):
        """Sets the current_billing_period of this ServiceBillingPlans.

        Billing plans for a given period  # noqa: E501

        :param current_billing_period: The current_billing_period of this ServiceBillingPlans.  # noqa: E501
        :type: 
        """

        self._current_billing_period = current_billing_period

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
        if not isinstance(other, ServiceBillingPlans):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
