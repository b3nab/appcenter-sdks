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


class AppFeatures(object):
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
        'crashgroup_modify_status': 'boolean',
        'crashgroup_modify_annotation': 'boolean',
        'search': 'boolean',
        'crashgroup_analytics_crashfreeusers': 'boolean',
        'crashgroup_analytics_impactedusers': 'boolean',
        'crash_download_raw': 'boolean'
    }

    attribute_map = {
        'crashgroup_modify_status': 'crashgroup_modify_status',
        'crashgroup_modify_annotation': 'crashgroup_modify_annotation',
        'search': 'search',
        'crashgroup_analytics_crashfreeusers': 'crashgroup_analytics_crashfreeusers',
        'crashgroup_analytics_impactedusers': 'crashgroup_analytics_impactedusers',
        'crash_download_raw': 'crash_download_raw'
    }

    def __init__(self, crashgroup_modify_status=None, crashgroup_modify_annotation=None, search=None, crashgroup_analytics_crashfreeusers=None, crashgroup_analytics_impactedusers=None, crash_download_raw=None):  # noqa: E501
        """AppFeatures - a model defined in Swagger"""  # noqa: E501
        self._crashgroup_modify_status = None
        self._crashgroup_modify_annotation = None
        self._search = None
        self._crashgroup_analytics_crashfreeusers = None
        self._crashgroup_analytics_impactedusers = None
        self._crash_download_raw = None
        self.discriminator = None
        if crashgroup_modify_status is not None:
            self.crashgroup_modify_status = crashgroup_modify_status
        if crashgroup_modify_annotation is not None:
            self.crashgroup_modify_annotation = crashgroup_modify_annotation
        if search is not None:
            self.search = search
        if crashgroup_analytics_crashfreeusers is not None:
            self.crashgroup_analytics_crashfreeusers = crashgroup_analytics_crashfreeusers
        if crashgroup_analytics_impactedusers is not None:
            self.crashgroup_analytics_impactedusers = crashgroup_analytics_impactedusers
        if crash_download_raw is not None:
            self.crash_download_raw = crash_download_raw

    @property
    def crashgroup_modify_status(self):
        """Gets the crashgroup_modify_status of this AppFeatures.  # noqa: E501

        App supports modification of crashgroup status  # noqa: E501

        :return: The crashgroup_modify_status of this AppFeatures.  # noqa: E501
        :rtype: boolean
        """
        return self._crashgroup_modify_status

    @crashgroup_modify_status.setter
    def crashgroup_modify_status(self, crashgroup_modify_status):
        """Sets the crashgroup_modify_status of this AppFeatures.

        App supports modification of crashgroup status  # noqa: E501

        :param crashgroup_modify_status: The crashgroup_modify_status of this AppFeatures.  # noqa: E501
        :type: boolean
        """

        self._crashgroup_modify_status = crashgroup_modify_status

    @property
    def crashgroup_modify_annotation(self):
        """Gets the crashgroup_modify_annotation of this AppFeatures.  # noqa: E501

        App supports modification of crashgroup annotation  # noqa: E501

        :return: The crashgroup_modify_annotation of this AppFeatures.  # noqa: E501
        :rtype: boolean
        """
        return self._crashgroup_modify_annotation

    @crashgroup_modify_annotation.setter
    def crashgroup_modify_annotation(self, crashgroup_modify_annotation):
        """Sets the crashgroup_modify_annotation of this AppFeatures.

        App supports modification of crashgroup annotation  # noqa: E501

        :param crashgroup_modify_annotation: The crashgroup_modify_annotation of this AppFeatures.  # noqa: E501
        :type: boolean
        """

        self._crashgroup_modify_annotation = crashgroup_modify_annotation

    @property
    def search(self):
        """Gets the search of this AppFeatures.  # noqa: E501

        App supports search API  # noqa: E501

        :return: The search of this AppFeatures.  # noqa: E501
        :rtype: boolean
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this AppFeatures.

        App supports search API  # noqa: E501

        :param search: The search of this AppFeatures.  # noqa: E501
        :type: boolean
        """

        self._search = search

    @property
    def crashgroup_analytics_crashfreeusers(self):
        """Gets the crashgroup_analytics_crashfreeusers of this AppFeatures.  # noqa: E501

        App supports the 'crash free user' metric  # noqa: E501

        :return: The crashgroup_analytics_crashfreeusers of this AppFeatures.  # noqa: E501
        :rtype: boolean
        """
        return self._crashgroup_analytics_crashfreeusers

    @crashgroup_analytics_crashfreeusers.setter
    def crashgroup_analytics_crashfreeusers(self, crashgroup_analytics_crashfreeusers):
        """Sets the crashgroup_analytics_crashfreeusers of this AppFeatures.

        App supports the 'crash free user' metric  # noqa: E501

        :param crashgroup_analytics_crashfreeusers: The crashgroup_analytics_crashfreeusers of this AppFeatures.  # noqa: E501
        :type: boolean
        """

        self._crashgroup_analytics_crashfreeusers = crashgroup_analytics_crashfreeusers

    @property
    def crashgroup_analytics_impactedusers(self):
        """Gets the crashgroup_analytics_impactedusers of this AppFeatures.  # noqa: E501

        App supports the 'impacted users' metric  # noqa: E501

        :return: The crashgroup_analytics_impactedusers of this AppFeatures.  # noqa: E501
        :rtype: boolean
        """
        return self._crashgroup_analytics_impactedusers

    @crashgroup_analytics_impactedusers.setter
    def crashgroup_analytics_impactedusers(self, crashgroup_analytics_impactedusers):
        """Sets the crashgroup_analytics_impactedusers of this AppFeatures.

        App supports the 'impacted users' metric  # noqa: E501

        :param crashgroup_analytics_impactedusers: The crashgroup_analytics_impactedusers of this AppFeatures.  # noqa: E501
        :type: boolean
        """

        self._crashgroup_analytics_impactedusers = crashgroup_analytics_impactedusers

    @property
    def crash_download_raw(self):
        """Gets the crash_download_raw of this AppFeatures.  # noqa: E501

        App supports download of raw crashes  # noqa: E501

        :return: The crash_download_raw of this AppFeatures.  # noqa: E501
        :rtype: boolean
        """
        return self._crash_download_raw

    @crash_download_raw.setter
    def crash_download_raw(self, crash_download_raw):
        """Sets the crash_download_raw of this AppFeatures.

        App supports download of raw crashes  # noqa: E501

        :param crash_download_raw: The crash_download_raw of this AppFeatures.  # noqa: E501
        :type: boolean
        """

        self._crash_download_raw = crash_download_raw

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
        if not isinstance(other, AppFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
