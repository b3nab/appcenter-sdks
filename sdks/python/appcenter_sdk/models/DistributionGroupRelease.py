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


class DistributionGroupRelease(object):
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
        'id': 'integer',
        'version': 'string',
        'short_version': 'string',
        'mandatory_update': 'boolean',
        'uploaded_at': 'string',
        'enabled': 'boolean'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'short_version': 'short_version',
        'mandatory_update': 'mandatory_update',
        'uploaded_at': 'uploaded_at',
        'enabled': 'enabled'
    }

    def __init__(self, id=None, version=None, short_version=None, mandatory_update=None, uploaded_at=None, enabled=None):  # noqa: E501
        """DistributionGroupRelease - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version = None
        self._short_version = None
        self._mandatory_update = None
        self._uploaded_at = None
        self._enabled = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if short_version is not None:
            self.short_version = short_version
        if mandatory_update is not None:
            self.mandatory_update = mandatory_update
        if uploaded_at is not None:
            self.uploaded_at = uploaded_at
        if enabled is not None:
            self.enabled = enabled

    @property
    def id(self):
        """Gets the id of this DistributionGroupRelease.  # noqa: E501

        ID identifying this unique release.  # noqa: E501

        :return: The id of this DistributionGroupRelease.  # noqa: E501
        :rtype: integer
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DistributionGroupRelease.

        ID identifying this unique release.  # noqa: E501

        :param id: The id of this DistributionGroupRelease.  # noqa: E501
        :type: integer
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this DistributionGroupRelease.  # noqa: E501

        The release's version.<br>
For iOS: CFBundleVersion from info.plist.<br>
For Android: android:versionCode from AppManifest.xml.
  # noqa: E501

        :return: The version of this DistributionGroupRelease.  # noqa: E501
        :rtype: string
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DistributionGroupRelease.

        The release's version.<br>
For iOS: CFBundleVersion from info.plist.<br>
For Android: android:versionCode from AppManifest.xml.
  # noqa: E501

        :param version: The version of this DistributionGroupRelease.  # noqa: E501
        :type: string
        """

        self._version = version

    @property
    def short_version(self):
        """Gets the short_version of this DistributionGroupRelease.  # noqa: E501

        The release's short version.<br>
For iOS: CFBundleShortVersionString from info.plist.<br>
For Android: android:versionName from AppManifest.xml.
  # noqa: E501

        :return: The short_version of this DistributionGroupRelease.  # noqa: E501
        :rtype: string
        """
        return self._short_version

    @short_version.setter
    def short_version(self, short_version):
        """Sets the short_version of this DistributionGroupRelease.

        The release's short version.<br>
For iOS: CFBundleShortVersionString from info.plist.<br>
For Android: android:versionName from AppManifest.xml.
  # noqa: E501

        :param short_version: The short_version of this DistributionGroupRelease.  # noqa: E501
        :type: string
        """

        self._short_version = short_version

    @property
    def mandatory_update(self):
        """Gets the mandatory_update of this DistributionGroupRelease.  # noqa: E501

        A boolean which determines whether the release is a mandatory update or not.  # noqa: E501

        :return: The mandatory_update of this DistributionGroupRelease.  # noqa: E501
        :rtype: boolean
        """
        return self._mandatory_update

    @mandatory_update.setter
    def mandatory_update(self, mandatory_update):
        """Sets the mandatory_update of this DistributionGroupRelease.

        A boolean which determines whether the release is a mandatory update or not.  # noqa: E501

        :param mandatory_update: The mandatory_update of this DistributionGroupRelease.  # noqa: E501
        :type: boolean
        """

        self._mandatory_update = mandatory_update

    @property
    def uploaded_at(self):
        """Gets the uploaded_at of this DistributionGroupRelease.  # noqa: E501

        UTC time in ISO 8601 format of the uploaded time.  # noqa: E501

        :return: The uploaded_at of this DistributionGroupRelease.  # noqa: E501
        :rtype: string
        """
        return self._uploaded_at

    @uploaded_at.setter
    def uploaded_at(self, uploaded_at):
        """Sets the uploaded_at of this DistributionGroupRelease.

        UTC time in ISO 8601 format of the uploaded time.  # noqa: E501

        :param uploaded_at: The uploaded_at of this DistributionGroupRelease.  # noqa: E501
        :type: string
        """

        self._uploaded_at = uploaded_at

    @property
    def enabled(self):
        """Gets the enabled of this DistributionGroupRelease.  # noqa: E501

        This value determines the whether a release currently is enabled or disabled.  # noqa: E501

        :return: The enabled of this DistributionGroupRelease.  # noqa: E501
        :rtype: boolean
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DistributionGroupRelease.

        This value determines the whether a release currently is enabled or disabled.  # noqa: E501

        :param enabled: The enabled of this DistributionGroupRelease.  # noqa: E501
        :type: boolean
        """

        self._enabled = enabled

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
        if not isinstance(other, DistributionGroupRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
