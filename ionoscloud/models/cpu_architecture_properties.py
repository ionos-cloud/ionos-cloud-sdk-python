# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0-SDK.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class CpuArchitectureProperties(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cpu_family': 'str',
        'max_cores': 'int',
        'max_ram': 'int',
        'vendor': 'str',
    }

    attribute_map = {
        'cpu_family': 'cpuFamily',
        'max_cores': 'maxCores',
        'max_ram': 'maxRam',
        'vendor': 'vendor',
    }

    def __init__(self, cpu_family=None, max_cores=None, max_ram=None, vendor=None, local_vars_configuration=None):  # noqa: E501
        """CpuArchitectureProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cpu_family = None
        self._max_cores = None
        self._max_ram = None
        self._vendor = None
        self.discriminator = None

        if cpu_family is not None:
            self.cpu_family = cpu_family
        if max_cores is not None:
            self.max_cores = max_cores
        if max_ram is not None:
            self.max_ram = max_ram
        if vendor is not None:
            self.vendor = vendor

    @property
    def cpu_family(self):
        """Gets the cpu_family of this CpuArchitectureProperties.  # noqa: E501

        A valid CPU family name.  # noqa: E501

        :return: The cpu_family of this CpuArchitectureProperties.  # noqa: E501
        :rtype: str
        """
        return self._cpu_family

    @cpu_family.setter
    def cpu_family(self, cpu_family):
        """Sets the cpu_family of this CpuArchitectureProperties.

        A valid CPU family name.  # noqa: E501

        :param cpu_family: The cpu_family of this CpuArchitectureProperties.  # noqa: E501
        :type cpu_family: str
        """

        self._cpu_family = cpu_family

    @property
    def max_cores(self):
        """Gets the max_cores of this CpuArchitectureProperties.  # noqa: E501

        The maximum number of cores available.  # noqa: E501

        :return: The max_cores of this CpuArchitectureProperties.  # noqa: E501
        :rtype: int
        """
        return self._max_cores

    @max_cores.setter
    def max_cores(self, max_cores):
        """Sets the max_cores of this CpuArchitectureProperties.

        The maximum number of cores available.  # noqa: E501

        :param max_cores: The max_cores of this CpuArchitectureProperties.  # noqa: E501
        :type max_cores: int
        """

        self._max_cores = max_cores

    @property
    def max_ram(self):
        """Gets the max_ram of this CpuArchitectureProperties.  # noqa: E501

        The maximum number of RAM in MB.  # noqa: E501

        :return: The max_ram of this CpuArchitectureProperties.  # noqa: E501
        :rtype: int
        """
        return self._max_ram

    @max_ram.setter
    def max_ram(self, max_ram):
        """Sets the max_ram of this CpuArchitectureProperties.

        The maximum number of RAM in MB.  # noqa: E501

        :param max_ram: The max_ram of this CpuArchitectureProperties.  # noqa: E501
        :type max_ram: int
        """

        self._max_ram = max_ram

    @property
    def vendor(self):
        """Gets the vendor of this CpuArchitectureProperties.  # noqa: E501

        A valid CPU vendor name.  # noqa: E501

        :return: The vendor of this CpuArchitectureProperties.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this CpuArchitectureProperties.

        A valid CPU vendor name.  # noqa: E501

        :param vendor: The vendor of this CpuArchitectureProperties.  # noqa: E501
        :type vendor: str
        """

        self._vendor = vendor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, CpuArchitectureProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CpuArchitectureProperties):
            return True

        return self.to_dict() != other.to_dict()