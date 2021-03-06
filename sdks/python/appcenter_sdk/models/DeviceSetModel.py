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


class DeviceSetModel(object):
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
        'name': 'string',
        'manufacturer': 'string',
        'release_date': 'string',
        'form_factor': 'string'
    }

    attribute_map = {
        'name': 'name',
        'manufacturer': 'manufacturer',
        'release_date': 'release_date',
        'form_factor': 'form_factor'
    }

    def __init__(self, name=None, manufacturer=None, release_date=None, form_factor=None):  # noqa: E501
        """DeviceSetModel - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._manufacturer = None
        self._release_date = None
        self._form_factor = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if manufacturer is not None:
            self.manufacturer = manufacturer
        if release_date is not None:
            self.release_date = release_date
        if form_factor is not None:
            self.form_factor = form_factor

    @property
    def name(self):
        """Gets the name of this DeviceSetModel.  # noqa: E501


        :return: The name of this DeviceSetModel.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceSetModel.


        :param name: The name of this DeviceSetModel.  # noqa: E501
        :type: string
        """

        self._name = name

    @property
    def manufacturer(self):
        """Gets the manufacturer of this DeviceSetModel.  # noqa: E501


        :return: The manufacturer of this DeviceSetModel.  # noqa: E501
        :rtype: string
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """Sets the manufacturer of this DeviceSetModel.


        :param manufacturer: The manufacturer of this DeviceSetModel.  # noqa: E501
        :type: string
        """

        self._manufacturer = manufacturer

    @property
    def release_date(self):
        """Gets the release_date of this DeviceSetModel.  # noqa: E501


        :return: The release_date of this DeviceSetModel.  # noqa: E501
        :rtype: string
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this DeviceSetModel.


        :param release_date: The release_date of this DeviceSetModel.  # noqa: E501
        :type: string
        """

        self._release_date = release_date

    @property
    def form_factor(self):
        """Gets the form_factor of this DeviceSetModel.  # noqa: E501


        :return: The form_factor of this DeviceSetModel.  # noqa: E501
        :rtype: string
        """
        return self._form_factor

    @form_factor.setter
    def form_factor(self, form_factor):
        """Sets the form_factor of this DeviceSetModel.


        :param form_factor: The form_factor of this DeviceSetModel.  # noqa: E501
        :type: string
        """

        self._form_factor = form_factor

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
        if not isinstance(other, DeviceSetModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
