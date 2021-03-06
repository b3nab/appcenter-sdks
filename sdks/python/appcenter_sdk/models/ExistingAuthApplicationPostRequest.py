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


class ExistingAuthApplicationPostRequest(object):
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
        'tenant_id': 'string',
        'tenant_name': 'string',
        'id': 'string',
        'policy_id': 'string',
        'scope_id': 'string',
        'scope_url': 'string'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'tenant_name': 'tenant_name',
        'id': 'id',
        'policy_id': 'policy_id',
        'scope_id': 'scope_id',
        'scope_url': 'scope_url'
    }

    def __init__(self, tenant_id=None, tenant_name=None, id=None, policy_id=None, scope_id=None, scope_url=None):  # noqa: E501
        """ExistingAuthApplicationPostRequest - a model defined in Swagger"""  # noqa: E501
        self._tenant_id = None
        self._tenant_name = None
        self._id = None
        self._policy_id = None
        self._scope_id = None
        self._scope_url = None
        self.discriminator = None
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if tenant_name is not None:
            self.tenant_name = tenant_name
        self.id = id
        if policy_id is not None:
            self.policy_id = policy_id
        if scope_id is not None:
            self.scope_id = scope_id
        if scope_url is not None:
            self.scope_url = scope_url

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ExistingAuthApplicationPostRequest.  # noqa: E501


        :return: The tenant_id of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ExistingAuthApplicationPostRequest.


        :param tenant_id: The tenant_id of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :type: string
        """

        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """Gets the tenant_name of this ExistingAuthApplicationPostRequest.  # noqa: E501


        :return: The tenant_name of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this ExistingAuthApplicationPostRequest.


        :param tenant_name: The tenant_name of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :type: string
        """

        self._tenant_name = tenant_name

    @property
    def id(self):
        """Gets the id of this ExistingAuthApplicationPostRequest.  # noqa: E501


        :return: The id of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExistingAuthApplicationPostRequest.


        :param id: The id of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :type: string
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def policy_id(self):
        """Gets the policy_id of this ExistingAuthApplicationPostRequest.  # noqa: E501


        :return: The policy_id of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ExistingAuthApplicationPostRequest.


        :param policy_id: The policy_id of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :type: string
        """

        self._policy_id = policy_id

    @property
    def scope_id(self):
        """Gets the scope_id of this ExistingAuthApplicationPostRequest.  # noqa: E501


        :return: The scope_id of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        """Sets the scope_id of this ExistingAuthApplicationPostRequest.


        :param scope_id: The scope_id of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :type: string
        """

        self._scope_id = scope_id

    @property
    def scope_url(self):
        """Gets the scope_url of this ExistingAuthApplicationPostRequest.  # noqa: E501


        :return: The scope_url of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :rtype: string
        """
        return self._scope_url

    @scope_url.setter
    def scope_url(self, scope_url):
        """Sets the scope_url of this ExistingAuthApplicationPostRequest.


        :param scope_url: The scope_url of this ExistingAuthApplicationPostRequest.  # noqa: E501
        :type: string
        """

        self._scope_url = scope_url

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
        if not isinstance(other, ExistingAuthApplicationPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
