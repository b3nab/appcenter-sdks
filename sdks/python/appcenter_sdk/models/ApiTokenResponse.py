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


class ApiTokenResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    all = "all"
    in_app_update = "in_app_update"
    viewer = "viewer"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'string',
        'created_at': 'string',
        'scope': 'array',
        'encrypted_token': 'string',
        'description': 'string'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'scope': 'scope',
        'encrypted_token': 'encrypted_token',
        'description': 'description'
    }

    def __init__(self, id=None, created_at=None, scope=None, encrypted_token=None, description=None):  # noqa: E501
        """ApiTokenResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._scope = None
        self._encrypted_token = None
        self._description = None
        self.discriminator = None
        self.id = id
        self.created_at = created_at
        if scope is not None:
            self.scope = scope
        if encrypted_token is not None:
            self.encrypted_token = encrypted_token
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this ApiTokenResponse.  # noqa: E501

        The unique id (UUID) of the api token  # noqa: E501

        :return: The id of this ApiTokenResponse.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiTokenResponse.

        The unique id (UUID) of the api token  # noqa: E501

        :param id: The id of this ApiTokenResponse.  # noqa: E501
        :type: string
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this ApiTokenResponse.  # noqa: E501

        The creation time  # noqa: E501

        :return: The created_at of this ApiTokenResponse.  # noqa: E501
        :rtype: string
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiTokenResponse.

        The creation time  # noqa: E501

        :param created_at: The created_at of this ApiTokenResponse.  # noqa: E501
        :type: string
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def scope(self):
        """Gets the scope of this ApiTokenResponse.  # noqa: E501

        The token's scope. A list of allowed roles.  # noqa: E501

        :return: The scope of this ApiTokenResponse.  # noqa: E501
        :rtype: array
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ApiTokenResponse.

        The token's scope. A list of allowed roles.  # noqa: E501

        :param scope: The scope of this ApiTokenResponse.  # noqa: E501
        :type: array
        """

        self._scope = scope

    @property
    def encrypted_token(self):
        """Gets the encrypted_token of this ApiTokenResponse.  # noqa: E501

        The encrypted value of a token. This value will only be returned for token of type in_app_update.  # noqa: E501

        :return: The encrypted_token of this ApiTokenResponse.  # noqa: E501
        :rtype: string
        """
        return self._encrypted_token

    @encrypted_token.setter
    def encrypted_token(self, encrypted_token):
        """Sets the encrypted_token of this ApiTokenResponse.

        The encrypted value of a token. This value will only be returned for token of type in_app_update.  # noqa: E501

        :param encrypted_token: The encrypted_token of this ApiTokenResponse.  # noqa: E501
        :type: string
        """

        self._encrypted_token = encrypted_token

    @property
    def description(self):
        """Gets the description of this ApiTokenResponse.  # noqa: E501

        The description of the token  # noqa: E501

        :return: The description of this ApiTokenResponse.  # noqa: E501
        :rtype: string
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiTokenResponse.

        The description of the token  # noqa: E501

        :param description: The description of this ApiTokenResponse.  # noqa: E501
        :type: string
        """

        self._description = description

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
        if not isinstance(other, ApiTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
