# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud.configuration import Configuration


class IPFailover(object):
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
        'ip': 'str',
        'nic_uuid': 'str',
    }

    attribute_map = {
        'ip': 'ip',
        'nic_uuid': 'nicUuid',
    }

    def __init__(self, ip=None, nic_uuid=None, local_vars_configuration=None):  # noqa: E501
        """IPFailover - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ip = None
        self._nic_uuid = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if nic_uuid is not None:
            self.nic_uuid = nic_uuid

    @property
    def ip(self):
        """Gets the ip of this IPFailover.  # noqa: E501


        :return: The ip of this IPFailover.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this IPFailover.


        :param ip: The ip of this IPFailover.  # noqa: E501
        :type ip: str
        """

        self._ip = ip

    @property
    def nic_uuid(self):
        """Gets the nic_uuid of this IPFailover.  # noqa: E501


        :return: The nic_uuid of this IPFailover.  # noqa: E501
        :rtype: str
        """
        return self._nic_uuid

    @nic_uuid.setter
    def nic_uuid(self, nic_uuid):
        """Sets the nic_uuid of this IPFailover.


        :param nic_uuid: The nic_uuid of this IPFailover.  # noqa: E501
        :type nic_uuid: str
        """

        self._nic_uuid = nic_uuid

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
        if not isinstance(other, IPFailover):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IPFailover):
            return True

        return self.to_dict() != other.to_dict()
