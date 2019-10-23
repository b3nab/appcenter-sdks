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


class UpdateDevicesRequest(object):
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
        'release_id': 'number',
        'username': 'string',
        'password': 'string',
        'account_service_connection_id': 'string',
        'p12_base64': 'string',
        'p12_service_connection_id': 'string',
        'p12_password': 'string',
        'publish_all_devices': 'boolean',
        'devices': 'array',
        'destinations': 'array'
    }

    attribute_map = {
        'release_id': 'release_id',
        'username': 'username',
        'password': 'password',
        'account_service_connection_id': 'account_service_connection_id',
        'p12_base64': 'p12_base64',
        'p12_service_connection_id': 'p12_service_connection_id',
        'p12_password': 'p12_password',
        'publish_all_devices': 'publish_all_devices',
        'devices': 'devices',
        'destinations': 'destinations'
    }

    def __init__(self, release_id=None, username=None, password=None, account_service_connection_id=None, p12_base64=None, p12_service_connection_id=None, p12_password=None, publish_all_devices=None, devices=None, destinations=None):  # noqa: E501
        """UpdateDevicesRequest - a model defined in Swagger"""  # noqa: E501
        self._release_id = None
        self._username = None
        self._password = None
        self._account_service_connection_id = None
        self._p12_base64 = None
        self._p12_service_connection_id = None
        self._p12_password = None
        self._publish_all_devices = None
        self._devices = None
        self._destinations = None
        self.discriminator = None
        if release_id is not None:
            self.release_id = release_id
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if account_service_connection_id is not None:
            self.account_service_connection_id = account_service_connection_id
        if p12_base64 is not None:
            self.p12_base64 = p12_base64
        if p12_service_connection_id is not None:
            self.p12_service_connection_id = p12_service_connection_id
        if p12_password is not None:
            self.p12_password = p12_password
        if publish_all_devices is not None:
            self.publish_all_devices = publish_all_devices
        if devices is not None:
            self.devices = devices
        if destinations is not None:
            self.destinations = destinations

    @property
    def release_id(self):
        """Gets the release_id of this UpdateDevicesRequest.  # noqa: E501

        When provided, will update the provided release with the new set of devices. By default the latest release of the distribution group is used when this property is omitted. If `release_id` is passed in the path, there is no need to pass in the body as well.  # noqa: E501

        :return: The release_id of this UpdateDevicesRequest.  # noqa: E501
        :rtype: number
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """Sets the release_id of this UpdateDevicesRequest.

        When provided, will update the provided release with the new set of devices. By default the latest release of the distribution group is used when this property is omitted. If `release_id` is passed in the path, there is no need to pass in the body as well.  # noqa: E501

        :param release_id: The release_id of this UpdateDevicesRequest.  # noqa: E501
        :type: number
        """

        self._release_id = release_id

    @property
    def username(self):
        """Gets the username of this UpdateDevicesRequest.  # noqa: E501

        The username for the Apple Developer account to publish the devices to.  # noqa: E501

        :return: The username of this UpdateDevicesRequest.  # noqa: E501
        :rtype: string
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateDevicesRequest.

        The username for the Apple Developer account to publish the devices to.  # noqa: E501

        :param username: The username of this UpdateDevicesRequest.  # noqa: E501
        :type: string
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this UpdateDevicesRequest.  # noqa: E501

        The password for the Apple Developer account to publish the devices to.  # noqa: E501

        :return: The password of this UpdateDevicesRequest.  # noqa: E501
        :rtype: string
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateDevicesRequest.

        The password for the Apple Developer account to publish the devices to.  # noqa: E501

        :param password: The password of this UpdateDevicesRequest.  # noqa: E501
        :type: string
        """

        self._password = password

    @property
    def account_service_connection_id(self):
        """Gets the account_service_connection_id of this UpdateDevicesRequest.  # noqa: E501

        The service_connection_id of the stored Apple credentials instead of username, password.  # noqa: E501

        :return: The account_service_connection_id of this UpdateDevicesRequest.  # noqa: E501
        :rtype: string
        """
        return self._account_service_connection_id

    @account_service_connection_id.setter
    def account_service_connection_id(self, account_service_connection_id):
        """Sets the account_service_connection_id of this UpdateDevicesRequest.

        The service_connection_id of the stored Apple credentials instead of username, password.  # noqa: E501

        :param account_service_connection_id: The account_service_connection_id of this UpdateDevicesRequest.  # noqa: E501
        :type: string
        """

        self._account_service_connection_id = account_service_connection_id

    @property
    def p12_base64(self):
        """Gets the p12_base64 of this UpdateDevicesRequest.  # noqa: E501

        The certificate to use for resigning the application with the updated provisioning profiles.  # noqa: E501

        :return: The p12_base64 of this UpdateDevicesRequest.  # noqa: E501
        :rtype: string
        """
        return self._p12_base64

    @p12_base64.setter
    def p12_base64(self, p12_base64):
        """Sets the p12_base64 of this UpdateDevicesRequest.

        The certificate to use for resigning the application with the updated provisioning profiles.  # noqa: E501

        :param p12_base64: The p12_base64 of this UpdateDevicesRequest.  # noqa: E501
        :type: string
        """

        self._p12_base64 = p12_base64

    @property
    def p12_service_connection_id(self):
        """Gets the p12_service_connection_id of this UpdateDevicesRequest.  # noqa: E501

        The service_connection_id of the stored Apple certificate instead of p12_base64 value.  # noqa: E501

        :return: The p12_service_connection_id of this UpdateDevicesRequest.  # noqa: E501
        :rtype: string
        """
        return self._p12_service_connection_id

    @p12_service_connection_id.setter
    def p12_service_connection_id(self, p12_service_connection_id):
        """Sets the p12_service_connection_id of this UpdateDevicesRequest.

        The service_connection_id of the stored Apple certificate instead of p12_base64 value.  # noqa: E501

        :param p12_service_connection_id: The p12_service_connection_id of this UpdateDevicesRequest.  # noqa: E501
        :type: string
        """

        self._p12_service_connection_id = p12_service_connection_id

    @property
    def p12_password(self):
        """Gets the p12_password of this UpdateDevicesRequest.  # noqa: E501

        The password certificate if one is needed.  # noqa: E501

        :return: The p12_password of this UpdateDevicesRequest.  # noqa: E501
        :rtype: string
        """
        return self._p12_password

    @p12_password.setter
    def p12_password(self, p12_password):
        """Sets the p12_password of this UpdateDevicesRequest.

        The password certificate if one is needed.  # noqa: E501

        :param p12_password: The p12_password of this UpdateDevicesRequest.  # noqa: E501
        :type: string
        """

        self._p12_password = p12_password

    @property
    def publish_all_devices(self):
        """Gets the publish_all_devices of this UpdateDevicesRequest.  # noqa: E501

        When set to true, all unprovisioned devices will be published to the Apple Developer account.  When false, only the provided devices will be published to the Apple Developer account.  # noqa: E501

        :return: The publish_all_devices of this UpdateDevicesRequest.  # noqa: E501
        :rtype: boolean
        """
        return self._publish_all_devices

    @publish_all_devices.setter
    def publish_all_devices(self, publish_all_devices):
        """Sets the publish_all_devices of this UpdateDevicesRequest.

        When set to true, all unprovisioned devices will be published to the Apple Developer account.  When false, only the provided devices will be published to the Apple Developer account.  # noqa: E501

        :param publish_all_devices: The publish_all_devices of this UpdateDevicesRequest.  # noqa: E501
        :type: boolean
        """

        self._publish_all_devices = publish_all_devices

    @property
    def devices(self):
        """Gets the devices of this UpdateDevicesRequest.  # noqa: E501

        Array of device UDID's to be published to the Apple Developer account.  # noqa: E501

        :return: The devices of this UpdateDevicesRequest.  # noqa: E501
        :rtype: array
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this UpdateDevicesRequest.

        Array of device UDID's to be published to the Apple Developer account.  # noqa: E501

        :param devices: The devices of this UpdateDevicesRequest.  # noqa: E501
        :type: array
        """

        self._devices = devices

    @property
    def destinations(self):
        """Gets the destinations of this UpdateDevicesRequest.  # noqa: E501

        Array of distribution groups that the devices should be provisioned from.  # noqa: E501

        :return: The destinations of this UpdateDevicesRequest.  # noqa: E501
        :rtype: array
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this UpdateDevicesRequest.

        Array of distribution groups that the devices should be provisioned from.  # noqa: E501

        :param destinations: The destinations of this UpdateDevicesRequest.  # noqa: E501
        :type: array
        """

        self._destinations = destinations

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
        if not isinstance(other, UpdateDevicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other