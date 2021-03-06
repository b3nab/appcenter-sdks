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


class StoresDetails(object):
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
        'id': 'string',
        'name': 'string',
        'type': 'string',
        'publishing_status': 'string',
        'is_latest': 'boolean'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'publishing_status': 'publishing_status',
        'is_latest': 'is_latest'
    }

    def __init__(self, id=None, name=None, type=None, publishing_status=None, is_latest=None):  # noqa: E501
        """StoresDetails - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._type = None
        self._publishing_status = None
        self._is_latest = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if publishing_status is not None:
            self.publishing_status = publishing_status
        if is_latest is not None:
            self.is_latest = is_latest

    @property
    def id(self):
        """Gets the id of this StoresDetails.  # noqa: E501

        ID identifying a unique distribution store.  # noqa: E501

        :return: The id of this StoresDetails.  # noqa: E501
        :rtype: string
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoresDetails.

        ID identifying a unique distribution store.  # noqa: E501

        :param id: The id of this StoresDetails.  # noqa: E501
        :type: string
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StoresDetails.  # noqa: E501

        A name identifying a unique distribution store.  # noqa: E501

        :return: The name of this StoresDetails.  # noqa: E501
        :rtype: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoresDetails.

        A name identifying a unique distribution store.  # noqa: E501

        :param name: The name of this StoresDetails.  # noqa: E501
        :type: string
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this StoresDetails.  # noqa: E501

        A type identifying the type of distribution store.  # noqa: E501

        :return: The type of this StoresDetails.  # noqa: E501
        :rtype: string
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StoresDetails.

        A type identifying the type of distribution store.  # noqa: E501

        :param type: The type of this StoresDetails.  # noqa: E501
        :type: string
        """
        allowed_values = [undefined, undefined, undefined, ]  # noqa: E501

        self._type = type

    @property
    def publishing_status(self):
        """Gets the publishing_status of this StoresDetails.  # noqa: E501

        A status identifying the status of release in the distribution store.  # noqa: E501

        :return: The publishing_status of this StoresDetails.  # noqa: E501
        :rtype: string
        """
        return self._publishing_status

    @publishing_status.setter
    def publishing_status(self, publishing_status):
        """Sets the publishing_status of this StoresDetails.

        A status identifying the status of release in the distribution store.  # noqa: E501

        :param publishing_status: The publishing_status of this StoresDetails.  # noqa: E501
        :type: string
        """

        self._publishing_status = publishing_status

    @property
    def is_latest(self):
        """Gets the is_latest of this StoresDetails.  # noqa: E501

        Is the containing release the latest one in this distribution store.  # noqa: E501

        :return: The is_latest of this StoresDetails.  # noqa: E501
        :rtype: boolean
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """Sets the is_latest of this StoresDetails.

        Is the containing release the latest one in this distribution store.  # noqa: E501

        :param is_latest: The is_latest of this StoresDetails.  # noqa: E501
        :type: boolean
        """

        self._is_latest = is_latest

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
        if not isinstance(other, StoresDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
