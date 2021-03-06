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


class GitHubBillingAccount(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    org = "org"
    user = "user"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'string',
        'display_name': 'string',
        'name': 'string',
        'type': 'string'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, id=None, display_name=None, name=None, type=None):  # noqa: E501
        """GitHubBillingAccount - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._display_name = None
        self._name = None
        self._type = None
        self.discriminator = None
        self.id = id
        self.display_name = display_name
        self.name = name
        self.type = type

    @property
    def id(self):
        """Gets the id of this GitHubBillingAccount.  # noqa: E501

        The unique id (UUID) of the account  # noqa: E501

        :return: The id of this GitHubBillingAccount.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GitHubBillingAccount.

        The unique id (UUID) of the account  # noqa: E501

        :param id: The id of this GitHubBillingAccount.  # noqa: E501
        :type: string
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this GitHubBillingAccount.  # noqa: E501

        The account's display name  # noqa: E501

        :return: The display_name of this GitHubBillingAccount.  # noqa: E501
        :rtype: string
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GitHubBillingAccount.

        The account's display name  # noqa: E501

        :param display_name: The display_name of this GitHubBillingAccount.  # noqa: E501
        :type: string
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def name(self):
        """Gets the name of this GitHubBillingAccount.  # noqa: E501

        The unique name that used to identify the owner  # noqa: E501

        :return: The name of this GitHubBillingAccount.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GitHubBillingAccount.

        The unique name that used to identify the owner  # noqa: E501

        :param name: The name of this GitHubBillingAccount.  # noqa: E501
        :type: string
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this GitHubBillingAccount.  # noqa: E501

        The owner type. Can either be 'org' or 'user'  # noqa: E501

        :return: The type of this GitHubBillingAccount.  # noqa: E501
        :rtype: string
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GitHubBillingAccount.

        The owner type. Can either be 'org' or 'user'  # noqa: E501

        :param type: The type of this GitHubBillingAccount.  # noqa: E501
        :type: string
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = [undefinedundefined]  # noqa: E501

        self._type = type

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
        if not isinstance(other, GitHubBillingAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
