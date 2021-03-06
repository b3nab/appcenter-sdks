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


class TestCloudProject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    Appium = "Appium"
    Calabash = "Calabash"
    Espresso = "Espresso"
    UITest = "UITest"
    Generated = "Generated"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'path': 'string',
        'framework_type': 'string',
        'framework_properties': ''
    }

    attribute_map = {
        'path': 'path',
        'framework_type': 'framework_type',
        'framework_properties': 'framework_properties'
    }

    def __init__(self, path=None, framework_type=None, framework_properties=None):  # noqa: E501
        """TestCloudProject - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._framework_type = None
        self._framework_properties = None
        self.discriminator = None
        self.path = path
        if framework_type is not None:
            self.framework_type = framework_type
        if framework_properties is not None:
            self.framework_properties = framework_properties

    @property
    def path(self):
        """Gets the path of this TestCloudProject.  # noqa: E501

        The path to the TestCloud project  # noqa: E501

        :return: The path of this TestCloudProject.  # noqa: E501
        :rtype: string
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TestCloudProject.

        The path to the TestCloud project  # noqa: E501

        :param path: The path of this TestCloudProject.  # noqa: E501
        :type: string
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def framework_type(self):
        """Gets the framework_type of this TestCloudProject.  # noqa: E501


        :return: The framework_type of this TestCloudProject.  # noqa: E501
        :rtype: string
        """
        return self._framework_type

    @framework_type.setter
    def framework_type(self, framework_type):
        """Sets the framework_type of this TestCloudProject.


        :param framework_type: The framework_type of this TestCloudProject.  # noqa: E501
        :type: string
        """
        allowed_values = [undefined, undefined, undefined, undefined, undefined, ]  # noqa: E501

        self._framework_type = framework_type

    @property
    def framework_properties(self):
        """Gets the framework_properties of this TestCloudProject.  # noqa: E501


        :return: The framework_properties of this TestCloudProject.  # noqa: E501
        :rtype: 
        """
        return self._framework_properties

    @framework_properties.setter
    def framework_properties(self, framework_properties):
        """Sets the framework_properties of this TestCloudProject.


        :param framework_properties: The framework_properties of this TestCloudProject.  # noqa: E501
        :type: 
        """

        self._framework_properties = framework_properties

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
        if not isinstance(other, TestCloudProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
