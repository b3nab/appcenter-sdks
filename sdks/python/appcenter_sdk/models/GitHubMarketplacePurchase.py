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


class GitHubMarketplacePurchase(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    User = "User"
    Organization = "Organization"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account': 'object',
        'plan': 'object'
    }

    attribute_map = {
        'account': 'account',
        'plan': 'plan'
    }

    def __init__(self, account=None, plan=None):  # noqa: E501
        """GitHubMarketplacePurchase - a model defined in Swagger"""  # noqa: E501
        self._account = None
        self._plan = None
        self.discriminator = None
        if account is not None:
            self.account = account
        if plan is not None:
            self.plan = plan

    @property
    def account(self):
        """Gets the account of this GitHubMarketplacePurchase.  # noqa: E501

        GitHub account information  # noqa: E501

        :return: The account of this GitHubMarketplacePurchase.  # noqa: E501
        :rtype: object
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this GitHubMarketplacePurchase.

        GitHub account information  # noqa: E501

        :param account: The account of this GitHubMarketplacePurchase.  # noqa: E501
        :type: object
        """

        self._account = account

    @property
    def plan(self):
        """Gets the plan of this GitHubMarketplacePurchase.  # noqa: E501

        GitHub Marketplace plan  # noqa: E501

        :return: The plan of this GitHubMarketplacePurchase.  # noqa: E501
        :rtype: object
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this GitHubMarketplacePurchase.

        GitHub Marketplace plan  # noqa: E501

        :param plan: The plan of this GitHubMarketplacePurchase.  # noqa: E501
        :type: object
        """

        self._plan = plan

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
        if not isinstance(other, GitHubMarketplacePurchase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
