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


class PatchReleaseRequest(object):
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
        'status': 'string',
        'dest_publish_id': 'string',
        'error_details': 'string',
        'error_contextid': 'string',
        'wrap_package_url': 'string',
        'is_wrapper_request': 'boolean'
    }

    attribute_map = {
        'status': 'status',
        'dest_publish_id': 'dest_publish_id',
        'error_details': 'error_details',
        'error_contextid': 'error_contextid',
        'wrap_package_url': 'wrap_package_url',
        'is_wrapper_request': 'is_wrapper_request'
    }

    def __init__(self, status=None, dest_publish_id=None, error_details=None, error_contextid=None, wrap_package_url=None, is_wrapper_request=None):  # noqa: E501
        """PatchReleaseRequest - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._dest_publish_id = None
        self._error_details = None
        self._error_contextid = None
        self._wrap_package_url = None
        self._is_wrapper_request = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if dest_publish_id is not None:
            self.dest_publish_id = dest_publish_id
        if error_details is not None:
            self.error_details = error_details
        if error_contextid is not None:
            self.error_contextid = error_contextid
        if wrap_package_url is not None:
            self.wrap_package_url = wrap_package_url
        if is_wrapper_request is not None:
            self.is_wrapper_request = is_wrapper_request

    @property
    def status(self):
        """Gets the status of this PatchReleaseRequest.  # noqa: E501

        updated status of release  # noqa: E501

        :return: The status of this PatchReleaseRequest.  # noqa: E501
        :rtype: string
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PatchReleaseRequest.

        updated status of release  # noqa: E501

        :param status: The status of this PatchReleaseRequest.  # noqa: E501
        :type: string
        """

        self._status = status

    @property
    def dest_publish_id(self):
        """Gets the dest_publish_id of this PatchReleaseRequest.  # noqa: E501

        Destination Publish Id  # noqa: E501

        :return: The dest_publish_id of this PatchReleaseRequest.  # noqa: E501
        :rtype: string
        """
        return self._dest_publish_id

    @dest_publish_id.setter
    def dest_publish_id(self, dest_publish_id):
        """Sets the dest_publish_id of this PatchReleaseRequest.

        Destination Publish Id  # noqa: E501

        :param dest_publish_id: The dest_publish_id of this PatchReleaseRequest.  # noqa: E501
        :type: string
        """

        self._dest_publish_id = dest_publish_id

    @property
    def error_details(self):
        """Gets the error_details of this PatchReleaseRequest.  # noqa: E501

        failure error details from store  # noqa: E501

        :return: The error_details of this PatchReleaseRequest.  # noqa: E501
        :rtype: string
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this PatchReleaseRequest.

        failure error details from store  # noqa: E501

        :param error_details: The error_details of this PatchReleaseRequest.  # noqa: E501
        :type: string
        """

        self._error_details = error_details

    @property
    def error_contextid(self):
        """Gets the error_contextid of this PatchReleaseRequest.  # noqa: E501

        contextId for failed error message  # noqa: E501

        :return: The error_contextid of this PatchReleaseRequest.  # noqa: E501
        :rtype: string
        """
        return self._error_contextid

    @error_contextid.setter
    def error_contextid(self, error_contextid):
        """Sets the error_contextid of this PatchReleaseRequest.

        contextId for failed error message  # noqa: E501

        :param error_contextid: The error_contextid of this PatchReleaseRequest.  # noqa: E501
        :type: string
        """

        self._error_contextid = error_contextid

    @property
    def wrap_package_url(self):
        """Gets the wrap_package_url of this PatchReleaseRequest.  # noqa: E501

        package url for wrapping request  # noqa: E501

        :return: The wrap_package_url of this PatchReleaseRequest.  # noqa: E501
        :rtype: string
        """
        return self._wrap_package_url

    @wrap_package_url.setter
    def wrap_package_url(self, wrap_package_url):
        """Sets the wrap_package_url of this PatchReleaseRequest.

        package url for wrapping request  # noqa: E501

        :param wrap_package_url: The wrap_package_url of this PatchReleaseRequest.  # noqa: E501
        :type: string
        """

        self._wrap_package_url = wrap_package_url

    @property
    def is_wrapper_request(self):
        """Gets the is_wrapper_request of this PatchReleaseRequest.  # noqa: E501

        request is for wrapping or not  # noqa: E501

        :return: The is_wrapper_request of this PatchReleaseRequest.  # noqa: E501
        :rtype: boolean
        """
        return self._is_wrapper_request

    @is_wrapper_request.setter
    def is_wrapper_request(self, is_wrapper_request):
        """Sets the is_wrapper_request of this PatchReleaseRequest.

        request is for wrapping or not  # noqa: E501

        :param is_wrapper_request: The is_wrapper_request of this PatchReleaseRequest.  # noqa: E501
        :type: boolean
        """

        self._is_wrapper_request = is_wrapper_request

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
        if not isinstance(other, PatchReleaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other