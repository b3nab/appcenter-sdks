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


class TestRunStatistics(object):
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
        'test_run_statistics': 'object',
        'devices': 'number',
        'devices_finished': 'number',
        'devices_failed': 'number',
        'total': 'number',
        'passed': 'number',
        'failed': 'number',
        'skipped': 'number',
        'peak_memory': 'number',
        'total_device_minutes': 'number'
    }

    attribute_map = {
        'test_run_statistics': 'test_run_statistics',
        'devices': 'devices',
        'devices_finished': 'devices_finished',
        'devices_failed': 'devices_failed',
        'total': 'total',
        'passed': 'passed',
        'failed': 'failed',
        'skipped': 'skipped',
        'peak_memory': 'peak_memory',
        'total_device_minutes': 'total_device_minutes'
    }

    def __init__(self, test_run_statistics=None, devices=None, devices_finished=None, devices_failed=None, total=None, passed=None, failed=None, skipped=None, peak_memory=None, total_device_minutes=None):  # noqa: E501
        """TestRunStatistics - a model defined in Swagger"""  # noqa: E501
        self._test_run_statistics = None
        self._devices = None
        self._devices_finished = None
        self._devices_failed = None
        self._total = None
        self._passed = None
        self._failed = None
        self._skipped = None
        self._peak_memory = None
        self._total_device_minutes = None
        self.discriminator = None
        if test_run_statistics is not None:
            self.test_run_statistics = test_run_statistics
        if devices is not None:
            self.devices = devices
        if devices_finished is not None:
            self.devices_finished = devices_finished
        if devices_failed is not None:
            self.devices_failed = devices_failed
        if total is not None:
            self.total = total
        if passed is not None:
            self.passed = passed
        if failed is not None:
            self.failed = failed
        if skipped is not None:
            self.skipped = skipped
        if peak_memory is not None:
            self.peak_memory = peak_memory
        if total_device_minutes is not None:
            self.total_device_minutes = total_device_minutes

    @property
    def test_run_statistics(self):
        """Gets the test_run_statistics of this TestRunStatistics.  # noqa: E501

        Summary single test run on Xamarin Test Cloud  # noqa: E501

        :return: The test_run_statistics of this TestRunStatistics.  # noqa: E501
        :rtype: object
        """
        return self._test_run_statistics

    @test_run_statistics.setter
    def test_run_statistics(self, test_run_statistics):
        """Sets the test_run_statistics of this TestRunStatistics.

        Summary single test run on Xamarin Test Cloud  # noqa: E501

        :param test_run_statistics: The test_run_statistics of this TestRunStatistics.  # noqa: E501
        :type: object
        """

        self._test_run_statistics = test_run_statistics

    @property
    def devices(self):
        """Gets the devices of this TestRunStatistics.  # noqa: E501

        Number of devices running the test  # noqa: E501

        :return: The devices of this TestRunStatistics.  # noqa: E501
        :rtype: number
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this TestRunStatistics.

        Number of devices running the test  # noqa: E501

        :param devices: The devices of this TestRunStatistics.  # noqa: E501
        :type: number
        """

        self._devices = devices

    @property
    def devices_finished(self):
        """Gets the devices_finished of this TestRunStatistics.  # noqa: E501

        Number of finished devices  # noqa: E501

        :return: The devices_finished of this TestRunStatistics.  # noqa: E501
        :rtype: number
        """
        return self._devices_finished

    @devices_finished.setter
    def devices_finished(self, devices_finished):
        """Sets the devices_finished of this TestRunStatistics.

        Number of finished devices  # noqa: E501

        :param devices_finished: The devices_finished of this TestRunStatistics.  # noqa: E501
        :type: number
        """

        self._devices_finished = devices_finished

    @property
    def devices_failed(self):
        """Gets the devices_failed of this TestRunStatistics.  # noqa: E501

        Number of failed devices  # noqa: E501

        :return: The devices_failed of this TestRunStatistics.  # noqa: E501
        :rtype: number
        """
        return self._devices_failed

    @devices_failed.setter
    def devices_failed(self, devices_failed):
        """Sets the devices_failed of this TestRunStatistics.

        Number of failed devices  # noqa: E501

        :param devices_failed: The devices_failed of this TestRunStatistics.  # noqa: E501
        :type: number
        """

        self._devices_failed = devices_failed

    @property
    def total(self):
        """Gets the total of this TestRunStatistics.  # noqa: E501

        Number of tests in total  # noqa: E501

        :return: The total of this TestRunStatistics.  # noqa: E501
        :rtype: number
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TestRunStatistics.

        Number of tests in total  # noqa: E501

        :param total: The total of this TestRunStatistics.  # noqa: E501
        :type: number
        """

        self._total = total

    @property
    def passed(self):
        """Gets the passed of this TestRunStatistics.  # noqa: E501

        Number of passed tests  # noqa: E501

        :return: The passed of this TestRunStatistics.  # noqa: E501
        :rtype: number
        """
        return self._passed

    @passed.setter
    def passed(self, passed):
        """Sets the passed of this TestRunStatistics.

        Number of passed tests  # noqa: E501

        :param passed: The passed of this TestRunStatistics.  # noqa: E501
        :type: number
        """

        self._passed = passed

    @property
    def failed(self):
        """Gets the failed of this TestRunStatistics.  # noqa: E501

        Number of failed tests  # noqa: E501

        :return: The failed of this TestRunStatistics.  # noqa: E501
        :rtype: number
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this TestRunStatistics.

        Number of failed tests  # noqa: E501

        :param failed: The failed of this TestRunStatistics.  # noqa: E501
        :type: number
        """

        self._failed = failed

    @property
    def skipped(self):
        """Gets the skipped of this TestRunStatistics.  # noqa: E501

        Number of skipped tests  # noqa: E501

        :return: The skipped of this TestRunStatistics.  # noqa: E501
        :rtype: number
        """
        return self._skipped

    @skipped.setter
    def skipped(self, skipped):
        """Sets the skipped of this TestRunStatistics.

        Number of skipped tests  # noqa: E501

        :param skipped: The skipped of this TestRunStatistics.  # noqa: E501
        :type: number
        """

        self._skipped = skipped

    @property
    def peak_memory(self):
        """Gets the peak_memory of this TestRunStatistics.  # noqa: E501

        The max amount of MB used during the test run  # noqa: E501

        :return: The peak_memory of this TestRunStatistics.  # noqa: E501
        :rtype: number
        """
        return self._peak_memory

    @peak_memory.setter
    def peak_memory(self, peak_memory):
        """Sets the peak_memory of this TestRunStatistics.

        The max amount of MB used during the test run  # noqa: E501

        :param peak_memory: The peak_memory of this TestRunStatistics.  # noqa: E501
        :type: number
        """

        self._peak_memory = peak_memory

    @property
    def total_device_minutes(self):
        """Gets the total_device_minutes of this TestRunStatistics.  # noqa: E501

        The number of minutes of device time the test has been runnign  # noqa: E501

        :return: The total_device_minutes of this TestRunStatistics.  # noqa: E501
        :rtype: number
        """
        return self._total_device_minutes

    @total_device_minutes.setter
    def total_device_minutes(self, total_device_minutes):
        """Sets the total_device_minutes of this TestRunStatistics.

        The number of minutes of device time the test has been runnign  # noqa: E501

        :param total_device_minutes: The total_device_minutes of this TestRunStatistics.  # noqa: E501
        :type: number
        """

        self._total_device_minutes = total_device_minutes

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
        if not isinstance(other, TestRunStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
