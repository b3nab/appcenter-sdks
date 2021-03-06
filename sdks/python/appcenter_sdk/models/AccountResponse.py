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


class AccountResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    user = "user"
    org = "org"
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
        'email': 'string',
        'origin': 'string',
        'type': 'string'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name',
        'name': 'name',
        'email': 'email',
        'origin': 'origin',
        'type': 'type'
    }

    def __init__(self, id=None, display_name=None, name=None, email=None, origin=None, type=None):  # noqa: E501
        """AccountResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._display_name = None
        self._name = None
        self._email = None
        self._origin = None
        self._type = None
        self.discriminator = None
        self.id = id
        self.display_name = display_name
        self.name = name
        if email is not None:
            self.email = email
        self.origin = origin
        self.type = type

    @property
    def id(self):
        """Gets the id of this AccountResponse.  # noqa: E501

        The internal unique id (UUID) of the account.  # noqa: E501

        :return: The id of this AccountResponse.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountResponse.

        The internal unique id (UUID) of the account.  # noqa: E501

        :param id: The id of this AccountResponse.  # noqa: E501
        :type: string
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this AccountResponse.  # noqa: E501

        The display name of the account  # noqa: E501

        :return: The display_name of this AccountResponse.  # noqa: E501
        :rtype: string
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AccountResponse.

        The display name of the account  # noqa: E501

        :param display_name: The display_name of this AccountResponse.  # noqa: E501
        :type: string
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def name(self):
        """Gets the name of this AccountResponse.  # noqa: E501

        The slug name of the account  # noqa: E501

        :return: The name of this AccountResponse.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountResponse.

        The slug name of the account  # noqa: E501

        :param name: The name of this AccountResponse.  # noqa: E501
        :type: string
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this AccountResponse.  # noqa: E501

        The account's email. For org that value might be empty.  # noqa: E501

        :return: The email of this AccountResponse.  # noqa: E501
        :rtype: string
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AccountResponse.

        The account's email. For org that value might be empty.  # noqa: E501

        :param email: The email of this AccountResponse.  # noqa: E501
        :type: string
        """

        self._email = email

    @property
    def origin(self):
        """Gets the origin of this AccountResponse.  # noqa: E501

        The creation origin of this account  # noqa: E501

        :return: The origin of this AccountResponse.  # noqa: E501
        :rtype: string
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this AccountResponse.

        The creation origin of this account  # noqa: E501

        :param origin: The origin of this AccountResponse.  # noqa: E501
        :type: string
        """
        if origin is None:
            raise ValueError("Invalid value for `origin`, must not be `None`")  # noqa: E501
        allowed_values = [undefined, undefined, ]  # noqa: E501

        self._origin = origin

    @property
    def type(self):
        """Gets the type of this AccountResponse.  # noqa: E501

        The type of this account  # noqa: E501

        :return: The type of this AccountResponse.  # noqa: E501
        :rtype: string
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountResponse.

        The type of this account  # noqa: E501

        :param type: The type of this AccountResponse.  # noqa: E501
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
        if not isinstance(other, AccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
