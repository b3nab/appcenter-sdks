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


class ExportConfiguration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    crashes = "crashes"
    errors = "errors"
    attachments = "attachments"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'string',
        'export_entities': 'array',
        'resource_name': 'string',
        'resource_group': 'string'
    }

    attribute_map = {
        'type': 'type',
        'export_entities': 'export_entities',
        'resource_name': 'resource_name',
        'resource_group': 'resource_group'
    }

    def __init__(self, type=None, export_entities=None, resource_name=None, resource_group=None):  # noqa: E501
        """ExportConfiguration - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._export_entities = None
        self._resource_name = None
        self._resource_group = None
        self.discriminator = None
        self.type = type
        if export_entities is not None:
            self.export_entities = export_entities
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_group is not None:
            self.resource_group = resource_group

    @property
    def type(self):
        """Gets the type of this ExportConfiguration.  # noqa: E501

        Type of export configuration  # noqa: E501

        :return: The type of this ExportConfiguration.  # noqa: E501
        :rtype: string
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExportConfiguration.

        Type of export configuration  # noqa: E501

        :param type: The type of this ExportConfiguration.  # noqa: E501
        :type: string
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = [undefined, undefined, undefined, ]  # noqa: E501

        self._type = type

    @property
    def export_entities(self):
        """Gets the export_entities of this ExportConfiguration.  # noqa: E501


        :return: The export_entities of this ExportConfiguration.  # noqa: E501
        :rtype: array
        """
        return self._export_entities

    @export_entities.setter
    def export_entities(self, export_entities):
        """Sets the export_entities of this ExportConfiguration.


        :param export_entities: The export_entities of this ExportConfiguration.  # noqa: E501
        :type: array
        """

        self._export_entities = export_entities

    @property
    def resource_name(self):
        """Gets the resource_name of this ExportConfiguration.  # noqa: E501

        The resource name on azure  # noqa: E501

        :return: The resource_name of this ExportConfiguration.  # noqa: E501
        :rtype: string
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ExportConfiguration.

        The resource name on azure  # noqa: E501

        :param resource_name: The resource_name of this ExportConfiguration.  # noqa: E501
        :type: string
        """

        self._resource_name = resource_name

    @property
    def resource_group(self):
        """Gets the resource_group of this ExportConfiguration.  # noqa: E501

        The resource group name on azure  # noqa: E501

        :return: The resource_group of this ExportConfiguration.  # noqa: E501
        :rtype: string
        """
        return self._resource_group

    @resource_group.setter
    def resource_group(self, resource_group):
        """Sets the resource_group of this ExportConfiguration.

        The resource group name on azure  # noqa: E501

        :param resource_group: The resource_group of this ExportConfiguration.  # noqa: E501
        :type: string
        """

        self._resource_group = resource_group

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
        if not isinstance(other, ExportConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
