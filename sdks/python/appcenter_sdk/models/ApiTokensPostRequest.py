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


class ApiTokensPostRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    public = "public"
    in_app_update = "in_app_update"
    build = "build"
    session = "session"
    tester_app = "tester_app"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'string',
        'encrypted_token': 'string',
        'scope': 'array',
        'token_hash': 'string',
        'token_type': 'string'
    }

    attribute_map = {
        'description': 'description',
        'encrypted_token': 'encrypted_token',
        'scope': 'scope',
        'token_hash': 'token_hash',
        'token_type': 'token_type'
    }

    def __init__(self, description=None, encrypted_token=None, scope=None, token_hash=None, token_type=None):  # noqa: E501
        """ApiTokensPostRequest - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._encrypted_token = None
        self._scope = None
        self._token_hash = None
        self._token_type = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if encrypted_token is not None:
            self.encrypted_token = encrypted_token
        if scope is not None:
            self.scope = scope
        if token_hash is not None:
            self.token_hash = token_hash
        if token_type is not None:
            self.token_type = token_type

    @property
    def description(self):
        """Gets the description of this ApiTokensPostRequest.  # noqa: E501

        The description of the token  # noqa: E501

        :return: The description of this ApiTokensPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiTokensPostRequest.

        The description of the token  # noqa: E501

        :param description: The description of this ApiTokensPostRequest.  # noqa: E501
        :type: string
        """

        self._description = description

    @property
    def encrypted_token(self):
        """Gets the encrypted_token of this ApiTokensPostRequest.  # noqa: E501

        An encrypted value of the token.  # noqa: E501

        :return: The encrypted_token of this ApiTokensPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._encrypted_token

    @encrypted_token.setter
    def encrypted_token(self, encrypted_token):
        """Sets the encrypted_token of this ApiTokensPostRequest.

        An encrypted value of the token.  # noqa: E501

        :param encrypted_token: The encrypted_token of this ApiTokensPostRequest.  # noqa: E501
        :type: string
        """

        self._encrypted_token = encrypted_token

    @property
    def scope(self):
        """Gets the scope of this ApiTokensPostRequest.  # noqa: E501

        The scope for this token. An array of supported roles.  # noqa: E501

        :return: The scope of this ApiTokensPostRequest.  # noqa: E501
        :rtype: array
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ApiTokensPostRequest.

        The scope for this token. An array of supported roles.  # noqa: E501

        :param scope: The scope of this ApiTokensPostRequest.  # noqa: E501
        :type: array
        """

        self._scope = scope

    @property
    def token_hash(self):
        """Gets the token_hash of this ApiTokensPostRequest.  # noqa: E501

        The hashed value of api token  # noqa: E501

        :return: The token_hash of this ApiTokensPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._token_hash

    @token_hash.setter
    def token_hash(self, token_hash):
        """Sets the token_hash of this ApiTokensPostRequest.

        The hashed value of api token  # noqa: E501

        :param token_hash: The token_hash of this ApiTokensPostRequest.  # noqa: E501
        :type: string
        """

        self._token_hash = token_hash

    @property
    def token_type(self):
        """Gets the token_type of this ApiTokensPostRequest.  # noqa: E501

        The token's type. public:managed by the user; in_app_update:special token for in-app update scenario; buid:dedicated for CI usage for now; session:for CLI session management; tester_app: used for tester mobile app; default is "public".'  # noqa: E501

        :return: The token_type of this ApiTokensPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this ApiTokensPostRequest.

        The token's type. public:managed by the user; in_app_update:special token for in-app update scenario; buid:dedicated for CI usage for now; session:for CLI session management; tester_app: used for tester mobile app; default is "public".'  # noqa: E501

        :param token_type: The token_type of this ApiTokensPostRequest.  # noqa: E501
        :type: string
        """
        allowed_values = [undefinedundefinedundefinedundefinedundefined]  # noqa: E501

        self._token_type = token_type

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
        if not isinstance(other, ApiTokensPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other