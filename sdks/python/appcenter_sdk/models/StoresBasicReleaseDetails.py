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


class StoresBasicReleaseDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    googleplay = "googleplay"
    intune = "intune"
    apple = "apple"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'number',
        'version': 'string',
        'short_version': 'string',
        'uploaded_at': 'string',
        'distribution_stores': 'array'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'short_version': 'short_version',
        'uploaded_at': 'uploaded_at',
        'distribution_stores': 'distribution_stores'
    }

    def __init__(self, id=None, version=None, short_version=None, uploaded_at=None, distribution_stores=None):  # noqa: E501
        """StoresBasicReleaseDetails - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version = None
        self._short_version = None
        self._uploaded_at = None
        self._distribution_stores = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if short_version is not None:
            self.short_version = short_version
        if uploaded_at is not None:
            self.uploaded_at = uploaded_at
        if distribution_stores is not None:
            self.distribution_stores = distribution_stores

    @property
    def id(self):
        """Gets the id of this StoresBasicReleaseDetails.  # noqa: E501

        ID identifying this unique release.  # noqa: E501

        :return: The id of this StoresBasicReleaseDetails.  # noqa: E501
        :rtype: number
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoresBasicReleaseDetails.

        ID identifying this unique release.  # noqa: E501

        :param id: The id of this StoresBasicReleaseDetails.  # noqa: E501
        :type: number
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this StoresBasicReleaseDetails.  # noqa: E501

        The release's version.
For iOS: CFBundleVersion from info.plist.
For Android: android:versionCode from AppManifest.xml.
  # noqa: E501

        :return: The version of this StoresBasicReleaseDetails.  # noqa: E501
        :rtype: string
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this StoresBasicReleaseDetails.

        The release's version.
For iOS: CFBundleVersion from info.plist.
For Android: android:versionCode from AppManifest.xml.
  # noqa: E501

        :param version: The version of this StoresBasicReleaseDetails.  # noqa: E501
        :type: string
        """

        self._version = version

    @property
    def short_version(self):
        """Gets the short_version of this StoresBasicReleaseDetails.  # noqa: E501

        The release's short version.
For iOS: CFBundleShortVersionString from info.plist.
For Android: android:versionName from AppManifest.xml.
  # noqa: E501

        :return: The short_version of this StoresBasicReleaseDetails.  # noqa: E501
        :rtype: string
        """
        return self._short_version

    @short_version.setter
    def short_version(self, short_version):
        """Sets the short_version of this StoresBasicReleaseDetails.

        The release's short version.
For iOS: CFBundleShortVersionString from info.plist.
For Android: android:versionName from AppManifest.xml.
  # noqa: E501

        :param short_version: The short_version of this StoresBasicReleaseDetails.  # noqa: E501
        :type: string
        """

        self._short_version = short_version

    @property
    def uploaded_at(self):
        """Gets the uploaded_at of this StoresBasicReleaseDetails.  # noqa: E501

        UTC time in ISO 8601 format of the uploaded time.  # noqa: E501

        :return: The uploaded_at of this StoresBasicReleaseDetails.  # noqa: E501
        :rtype: string
        """
        return self._uploaded_at

    @uploaded_at.setter
    def uploaded_at(self, uploaded_at):
        """Sets the uploaded_at of this StoresBasicReleaseDetails.

        UTC time in ISO 8601 format of the uploaded time.  # noqa: E501

        :param uploaded_at: The uploaded_at of this StoresBasicReleaseDetails.  # noqa: E501
        :type: string
        """

        self._uploaded_at = uploaded_at

    @property
    def distribution_stores(self):
        """Gets the distribution_stores of this StoresBasicReleaseDetails.  # noqa: E501

        a list of distribution stores that are associated with this release.  # noqa: E501

        :return: The distribution_stores of this StoresBasicReleaseDetails.  # noqa: E501
        :rtype: array
        """
        return self._distribution_stores

    @distribution_stores.setter
    def distribution_stores(self, distribution_stores):
        """Sets the distribution_stores of this StoresBasicReleaseDetails.

        a list of distribution stores that are associated with this release.  # noqa: E501

        :param distribution_stores: The distribution_stores of this StoresBasicReleaseDetails.  # noqa: E501
        :type: array
        """

        self._distribution_stores = distribution_stores

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
        if not isinstance(other, StoresBasicReleaseDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
