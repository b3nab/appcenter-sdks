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


class OrgComplianceSettingsResponse(object):
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
        'org_id': 'string',
        'certificate_connection_id': 'string',
        'is_mam_enabled': 'boolean'
    }

    attribute_map = {
        'id': 'id',
        'org_id': 'org_id',
        'certificate_connection_id': 'certificate_connection_id',
        'is_mam_enabled': 'is_mam_enabled'
    }

    def __init__(self, id=None, org_id=None, certificate_connection_id=None, is_mam_enabled=None):  # noqa: E501
        """OrgComplianceSettingsResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._org_id = None
        self._certificate_connection_id = None
        self._is_mam_enabled = None
        self.discriminator = None
        self.id = id
        self.org_id = org_id
        self.certificate_connection_id = certificate_connection_id
        if is_mam_enabled is not None:
            self.is_mam_enabled = is_mam_enabled

    @property
    def id(self):
        """Gets the id of this OrgComplianceSettingsResponse.  # noqa: E501

        The internal unique id (UUID) of the organization compliance setting  # noqa: E501

        :return: The id of this OrgComplianceSettingsResponse.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrgComplianceSettingsResponse.

        The internal unique id (UUID) of the organization compliance setting  # noqa: E501

        :param id: The id of this OrgComplianceSettingsResponse.  # noqa: E501
        :type: string
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def org_id(self):
        """Gets the org_id of this OrgComplianceSettingsResponse.  # noqa: E501

        The internal unique id (UUID) of the organization.  # noqa: E501

        :return: The org_id of this OrgComplianceSettingsResponse.  # noqa: E501
        :rtype: string
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this OrgComplianceSettingsResponse.

        The internal unique id (UUID) of the organization.  # noqa: E501

        :param org_id: The org_id of this OrgComplianceSettingsResponse.  # noqa: E501
        :type: string
        """
        if org_id is None:
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def certificate_connection_id(self):
        """Gets the certificate_connection_id of this OrgComplianceSettingsResponse.  # noqa: E501

        certificate connection id to wrap and resign the app after wrapping  # noqa: E501

        :return: The certificate_connection_id of this OrgComplianceSettingsResponse.  # noqa: E501
        :rtype: string
        """
        return self._certificate_connection_id

    @certificate_connection_id.setter
    def certificate_connection_id(self, certificate_connection_id):
        """Sets the certificate_connection_id of this OrgComplianceSettingsResponse.

        certificate connection id to wrap and resign the app after wrapping  # noqa: E501

        :param certificate_connection_id: The certificate_connection_id of this OrgComplianceSettingsResponse.  # noqa: E501
        :type: string
        """
        if certificate_connection_id is None:
            raise ValueError("Invalid value for `certificate_connection_id`, must not be `None`")  # noqa: E501

        self._certificate_connection_id = certificate_connection_id

    @property
    def is_mam_enabled(self):
        """Gets the is_mam_enabled of this OrgComplianceSettingsResponse.  # noqa: E501

        flag to tell if mam warpping is enabled on the Org  # noqa: E501

        :return: The is_mam_enabled of this OrgComplianceSettingsResponse.  # noqa: E501
        :rtype: boolean
        """
        return self._is_mam_enabled

    @is_mam_enabled.setter
    def is_mam_enabled(self, is_mam_enabled):
        """Sets the is_mam_enabled of this OrgComplianceSettingsResponse.

        flag to tell if mam warpping is enabled on the Org  # noqa: E501

        :param is_mam_enabled: The is_mam_enabled of this OrgComplianceSettingsResponse.  # noqa: E501
        :type: boolean
        """

        self._is_mam_enabled = is_mam_enabled

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
        if not isinstance(other, OrgComplianceSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
