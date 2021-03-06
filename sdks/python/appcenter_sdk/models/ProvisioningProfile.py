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


class ProvisioningProfile(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    adhoc = "adhoc"
    enterprise = "enterprise"
    other = "other"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'string',
        'application_identifier': 'string',
        'team_identifier': 'string',
        'profile_type': 'string',
        'expired_at': 'string',
        'udids': 'array'
    }

    attribute_map = {
        'name': 'name',
        'application_identifier': 'application_identifier',
        'team_identifier': 'team_identifier',
        'profile_type': 'profile_type',
        'expired_at': 'expired_at',
        'udids': 'udids'
    }

    def __init__(self, name=None, application_identifier=None, team_identifier=None, profile_type=None, expired_at=None, udids=None):  # noqa: E501
        """ProvisioningProfile - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._application_identifier = None
        self._team_identifier = None
        self._profile_type = None
        self._expired_at = None
        self._udids = None
        self.discriminator = None
        self.name = name
        self.application_identifier = application_identifier
        self.team_identifier = team_identifier
        self.profile_type = profile_type
        self.expired_at = expired_at
        if udids is not None:
            self.udids = udids

    @property
    def name(self):
        """Gets the name of this ProvisioningProfile.  # noqa: E501

        The name of the provisioning profile.  # noqa: E501

        :return: The name of this ProvisioningProfile.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProvisioningProfile.

        The name of the provisioning profile.  # noqa: E501

        :param name: The name of this ProvisioningProfile.  # noqa: E501
        :type: string
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def application_identifier(self):
        """Gets the application_identifier of this ProvisioningProfile.  # noqa: E501

        The application identifier.  # noqa: E501

        :return: The application_identifier of this ProvisioningProfile.  # noqa: E501
        :rtype: string
        """
        return self._application_identifier

    @application_identifier.setter
    def application_identifier(self, application_identifier):
        """Sets the application_identifier of this ProvisioningProfile.

        The application identifier.  # noqa: E501

        :param application_identifier: The application_identifier of this ProvisioningProfile.  # noqa: E501
        :type: string
        """
        if application_identifier is None:
            raise ValueError("Invalid value for `application_identifier`, must not be `None`")  # noqa: E501

        self._application_identifier = application_identifier

    @property
    def team_identifier(self):
        """Gets the team_identifier of this ProvisioningProfile.  # noqa: E501

        The team identifier.  # noqa: E501

        :return: The team_identifier of this ProvisioningProfile.  # noqa: E501
        :rtype: string
        """
        return self._team_identifier

    @team_identifier.setter
    def team_identifier(self, team_identifier):
        """Sets the team_identifier of this ProvisioningProfile.

        The team identifier.  # noqa: E501

        :param team_identifier: The team_identifier of this ProvisioningProfile.  # noqa: E501
        :type: string
        """
        if team_identifier is None:
            raise ValueError("Invalid value for `team_identifier`, must not be `None`")  # noqa: E501

        self._team_identifier = team_identifier

    @property
    def profile_type(self):
        """Gets the profile_type of this ProvisioningProfile.  # noqa: E501


        :return: The profile_type of this ProvisioningProfile.  # noqa: E501
        :rtype: string
        """
        return self._profile_type

    @profile_type.setter
    def profile_type(self, profile_type):
        """Sets the profile_type of this ProvisioningProfile.


        :param profile_type: The profile_type of this ProvisioningProfile.  # noqa: E501
        :type: string
        """
        if profile_type is None:
            raise ValueError("Invalid value for `profile_type`, must not be `None`")  # noqa: E501
        allowed_values = [undefined, undefined, undefined, ]  # noqa: E501

        self._profile_type = profile_type

    @property
    def expired_at(self):
        """Gets the expired_at of this ProvisioningProfile.  # noqa: E501

        The profile's expiration date in RFC 3339 format, i.e. 2017-07-21T17:32:28Z  # noqa: E501

        :return: The expired_at of this ProvisioningProfile.  # noqa: E501
        :rtype: string
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        """Sets the expired_at of this ProvisioningProfile.

        The profile's expiration date in RFC 3339 format, i.e. 2017-07-21T17:32:28Z  # noqa: E501

        :param expired_at: The expired_at of this ProvisioningProfile.  # noqa: E501
        :type: string
        """
        if expired_at is None:
            raise ValueError("Invalid value for `expired_at`, must not be `None`")  # noqa: E501

        self._expired_at = expired_at

    @property
    def udids(self):
        """Gets the udids of this ProvisioningProfile.  # noqa: E501


        :return: The udids of this ProvisioningProfile.  # noqa: E501
        :rtype: array
        """
        return self._udids

    @udids.setter
    def udids(self, udids):
        """Sets the udids of this ProvisioningProfile.


        :param udids: The udids of this ProvisioningProfile.  # noqa: E501
        :type: array
        """

        self._udids = udids

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
        if not isinstance(other, ProvisioningProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
