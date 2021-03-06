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


class AppleTestFlightGroupResponse(object):
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
        'id': 'string',
        'provider_id': 'number',
        'app_adam_id': 'number',
        'name': 'string',
        'active': 'boolean',
        'is_internal_group': 'boolean'
    }

    attribute_map = {
        'id': 'id',
        'provider_id': 'provider_id',
        'app_adam_id': 'app_adam_id',
        'name': 'name',
        'active': 'active',
        'is_internal_group': 'is_internal_group'
    }

    def __init__(self, id=None, provider_id=None, app_adam_id=None, name=None, active=None, is_internal_group=None):  # noqa: E501
        """AppleTestFlightGroupResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._provider_id = None
        self._app_adam_id = None
        self._name = None
        self._active = None
        self._is_internal_group = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if provider_id is not None:
            self.provider_id = provider_id
        if app_adam_id is not None:
            self.app_adam_id = app_adam_id
        if name is not None:
            self.name = name
        if active is not None:
            self.active = active
        if is_internal_group is not None:
            self.is_internal_group = is_internal_group

    @property
    def id(self):
        """Gets the id of this AppleTestFlightGroupResponse.  # noqa: E501

        id of the group.  # noqa: E501

        :return: The id of this AppleTestFlightGroupResponse.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppleTestFlightGroupResponse.

        id of the group.  # noqa: E501

        :param id: The id of this AppleTestFlightGroupResponse.  # noqa: E501
        :type: string
        """

        self._id = id

    @property
    def provider_id(self):
        """Gets the provider_id of this AppleTestFlightGroupResponse.  # noqa: E501

        provider id of the group.  # noqa: E501

        :return: The provider_id of this AppleTestFlightGroupResponse.  # noqa: E501
        :rtype: number
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this AppleTestFlightGroupResponse.

        provider id of the group.  # noqa: E501

        :param provider_id: The provider_id of this AppleTestFlightGroupResponse.  # noqa: E501
        :type: number
        """

        self._provider_id = provider_id

    @property
    def app_adam_id(self):
        """Gets the app_adam_id of this AppleTestFlightGroupResponse.  # noqa: E501

        apple id of the group.  # noqa: E501

        :return: The app_adam_id of this AppleTestFlightGroupResponse.  # noqa: E501
        :rtype: number
        """
        return self._app_adam_id

    @app_adam_id.setter
    def app_adam_id(self, app_adam_id):
        """Sets the app_adam_id of this AppleTestFlightGroupResponse.

        apple id of the group.  # noqa: E501

        :param app_adam_id: The app_adam_id of this AppleTestFlightGroupResponse.  # noqa: E501
        :type: number
        """

        self._app_adam_id = app_adam_id

    @property
    def name(self):
        """Gets the name of this AppleTestFlightGroupResponse.  # noqa: E501

        name of the group.  # noqa: E501

        :return: The name of this AppleTestFlightGroupResponse.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppleTestFlightGroupResponse.

        name of the group.  # noqa: E501

        :param name: The name of this AppleTestFlightGroupResponse.  # noqa: E501
        :type: string
        """

        self._name = name

    @property
    def active(self):
        """Gets the active of this AppleTestFlightGroupResponse.  # noqa: E501

        true if group is in active state.  # noqa: E501

        :return: The active of this AppleTestFlightGroupResponse.  # noqa: E501
        :rtype: boolean
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AppleTestFlightGroupResponse.

        true if group is in active state.  # noqa: E501

        :param active: The active of this AppleTestFlightGroupResponse.  # noqa: E501
        :type: boolean
        """

        self._active = active

    @property
    def is_internal_group(self):
        """Gets the is_internal_group of this AppleTestFlightGroupResponse.  # noqa: E501

        true if the group is an internal group.  # noqa: E501

        :return: The is_internal_group of this AppleTestFlightGroupResponse.  # noqa: E501
        :rtype: boolean
        """
        return self._is_internal_group

    @is_internal_group.setter
    def is_internal_group(self, is_internal_group):
        """Sets the is_internal_group of this AppleTestFlightGroupResponse.

        true if the group is an internal group.  # noqa: E501

        :param is_internal_group: The is_internal_group of this AppleTestFlightGroupResponse.  # noqa: E501
        :type: boolean
        """

        self._is_internal_group = is_internal_group

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
        if not isinstance(other, AppleTestFlightGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
