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


class OrganizationAADGroupResponse(object):
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
        'aad_group_id': 'string',
        'azure_aad_group_id': 'string',
        'role': 'string',
        'display_name': 'string'
    }

    attribute_map = {
        'aad_group_id': 'aad_group_id',
        'azure_aad_group_id': 'azure_aad_group_id',
        'role': 'role',
        'display_name': 'display_name'
    }

    def __init__(self, aad_group_id=None, azure_aad_group_id=None, role=None, display_name=None):  # noqa: E501
        """OrganizationAADGroupResponse - a model defined in Swagger"""  # noqa: E501
        self._aad_group_id = None
        self._azure_aad_group_id = None
        self._role = None
        self._display_name = None
        self.discriminator = None
        self.aad_group_id = aad_group_id
        self.azure_aad_group_id = azure_aad_group_id
        self.role = role
        self.display_name = display_name

    @property
    def aad_group_id(self):
        """Gets the aad_group_id of this OrganizationAADGroupResponse.  # noqa: E501

        The id of the aad group  # noqa: E501

        :return: The aad_group_id of this OrganizationAADGroupResponse.  # noqa: E501
        :rtype: string
        """
        return self._aad_group_id

    @aad_group_id.setter
    def aad_group_id(self, aad_group_id):
        """Sets the aad_group_id of this OrganizationAADGroupResponse.

        The id of the aad group  # noqa: E501

        :param aad_group_id: The aad_group_id of this OrganizationAADGroupResponse.  # noqa: E501
        :type: string
        """
        if aad_group_id is None:
            raise ValueError("Invalid value for `aad_group_id`, must not be `None`")  # noqa: E501

        self._aad_group_id = aad_group_id

    @property
    def azure_aad_group_id(self):
        """Gets the azure_aad_group_id of this OrganizationAADGroupResponse.  # noqa: E501

        The azure id of the aad group  # noqa: E501

        :return: The azure_aad_group_id of this OrganizationAADGroupResponse.  # noqa: E501
        :rtype: string
        """
        return self._azure_aad_group_id

    @azure_aad_group_id.setter
    def azure_aad_group_id(self, azure_aad_group_id):
        """Sets the azure_aad_group_id of this OrganizationAADGroupResponse.

        The azure id of the aad group  # noqa: E501

        :param azure_aad_group_id: The azure_aad_group_id of this OrganizationAADGroupResponse.  # noqa: E501
        :type: string
        """
        if azure_aad_group_id is None:
            raise ValueError("Invalid value for `azure_aad_group_id`, must not be `None`")  # noqa: E501

        self._azure_aad_group_id = azure_aad_group_id

    @property
    def role(self):
        """Gets the role of this OrganizationAADGroupResponse.  # noqa: E501

        The role the user has within the organization  # noqa: E501

        :return: The role of this OrganizationAADGroupResponse.  # noqa: E501
        :rtype: string
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this OrganizationAADGroupResponse.

        The role the user has within the organization  # noqa: E501

        :param role: The role of this OrganizationAADGroupResponse.  # noqa: E501
        :type: string
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def display_name(self):
        """Gets the display_name of this OrganizationAADGroupResponse.  # noqa: E501

        The display name of the aad group  # noqa: E501

        :return: The display_name of this OrganizationAADGroupResponse.  # noqa: E501
        :rtype: string
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this OrganizationAADGroupResponse.

        The display name of the aad group  # noqa: E501

        :param display_name: The display_name of this OrganizationAADGroupResponse.  # noqa: E501
        :type: string
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

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
        if not isinstance(other, OrganizationAADGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
