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


class TestCloudErrorDetails(object):
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
        'test_cloud_error_details': 'object',
        'status': 'string',
        'message': 'string'
    }

    attribute_map = {
        'test_cloud_error_details': 'test_cloud_error_details',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, test_cloud_error_details=None, status=None, message=None):  # noqa: E501
        """TestCloudErrorDetails - a model defined in Swagger"""  # noqa: E501
        self._test_cloud_error_details = None
        self._status = None
        self._message = None
        self.discriminator = None
        if test_cloud_error_details is not None:
            self.test_cloud_error_details = test_cloud_error_details
        self.status = status
        self.message = message

    @property
    def test_cloud_error_details(self):
        """Gets the test_cloud_error_details of this TestCloudErrorDetails.  # noqa: E501

        Details of a failed operation  # noqa: E501

        :return: The test_cloud_error_details of this TestCloudErrorDetails.  # noqa: E501
        :rtype: object
        """
        return self._test_cloud_error_details

    @test_cloud_error_details.setter
    def test_cloud_error_details(self, test_cloud_error_details):
        """Sets the test_cloud_error_details of this TestCloudErrorDetails.

        Details of a failed operation  # noqa: E501

        :param test_cloud_error_details: The test_cloud_error_details of this TestCloudErrorDetails.  # noqa: E501
        :type: object
        """

        self._test_cloud_error_details = test_cloud_error_details

    @property
    def status(self):
        """Gets the status of this TestCloudErrorDetails.  # noqa: E501

        Status of the operation  # noqa: E501

        :return: The status of this TestCloudErrorDetails.  # noqa: E501
        :rtype: string
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TestCloudErrorDetails.

        Status of the operation  # noqa: E501

        :param status: The status of this TestCloudErrorDetails.  # noqa: E501
        :type: string
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this TestCloudErrorDetails.  # noqa: E501

        Human-readable message that describes the error  # noqa: E501

        :return: The message of this TestCloudErrorDetails.  # noqa: E501
        :rtype: string
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this TestCloudErrorDetails.

        Human-readable message that describes the error  # noqa: E501

        :param message: The message of this TestCloudErrorDetails.  # noqa: E501
        :type: string
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, TestCloudErrorDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
