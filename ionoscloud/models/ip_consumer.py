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


class IpConsumer(object):
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
        'mac': 'str',
        'nic_id': 'str',
        'server_id': 'str',
        'server_name': 'str',
        'datacenter_id': 'str',
        'datacenter_name': 'str',
    }

    attribute_map = {
        'ip': 'ip',
        'mac': 'mac',
        'nic_id': 'nicId',
        'server_id': 'serverId',
        'server_name': 'serverName',
        'datacenter_id': 'datacenterId',
        'datacenter_name': 'datacenterName',
    }

    def __init__(self, ip=None, mac=None, nic_id=None, server_id=None, server_name=None, datacenter_id=None, datacenter_name=None, local_vars_configuration=None):  # noqa: E501
        """IpConsumer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ip = None
        self._mac = None
        self._nic_id = None
        self._server_id = None
        self._server_name = None
        self._datacenter_id = None
        self._datacenter_name = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if mac is not None:
            self.mac = mac
        if nic_id is not None:
            self.nic_id = nic_id
        if server_id is not None:
            self.server_id = server_id
        if server_name is not None:
            self.server_name = server_name
        if datacenter_id is not None:
            self.datacenter_id = datacenter_id
        if datacenter_name is not None:
            self.datacenter_name = datacenter_name

    @property
    def ip(self):
        """Gets the ip of this IpConsumer.  # noqa: E501


        :return: The ip of this IpConsumer.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this IpConsumer.


        :param ip: The ip of this IpConsumer.  # noqa: E501
        :type ip: str
        """

        self._ip = ip

    @property
    def mac(self):
        """Gets the mac of this IpConsumer.  # noqa: E501


        :return: The mac of this IpConsumer.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this IpConsumer.


        :param mac: The mac of this IpConsumer.  # noqa: E501
        :type mac: str
        """

        self._mac = mac

    @property
    def nic_id(self):
        """Gets the nic_id of this IpConsumer.  # noqa: E501


        :return: The nic_id of this IpConsumer.  # noqa: E501
        :rtype: str
        """
        return self._nic_id

    @nic_id.setter
    def nic_id(self, nic_id):
        """Sets the nic_id of this IpConsumer.


        :param nic_id: The nic_id of this IpConsumer.  # noqa: E501
        :type nic_id: str
        """

        self._nic_id = nic_id

    @property
    def server_id(self):
        """Gets the server_id of this IpConsumer.  # noqa: E501


        :return: The server_id of this IpConsumer.  # noqa: E501
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this IpConsumer.


        :param server_id: The server_id of this IpConsumer.  # noqa: E501
        :type server_id: str
        """

        self._server_id = server_id

    @property
    def server_name(self):
        """Gets the server_name of this IpConsumer.  # noqa: E501


        :return: The server_name of this IpConsumer.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this IpConsumer.


        :param server_name: The server_name of this IpConsumer.  # noqa: E501
        :type server_name: str
        """

        self._server_name = server_name

    @property
    def datacenter_id(self):
        """Gets the datacenter_id of this IpConsumer.  # noqa: E501


        :return: The datacenter_id of this IpConsumer.  # noqa: E501
        :rtype: str
        """
        return self._datacenter_id

    @datacenter_id.setter
    def datacenter_id(self, datacenter_id):
        """Sets the datacenter_id of this IpConsumer.


        :param datacenter_id: The datacenter_id of this IpConsumer.  # noqa: E501
        :type datacenter_id: str
        """

        self._datacenter_id = datacenter_id

    @property
    def datacenter_name(self):
        """Gets the datacenter_name of this IpConsumer.  # noqa: E501


        :return: The datacenter_name of this IpConsumer.  # noqa: E501
        :rtype: str
        """
        return self._datacenter_name

    @datacenter_name.setter
    def datacenter_name(self, datacenter_name):
        """Sets the datacenter_name of this IpConsumer.


        :param datacenter_name: The datacenter_name of this IpConsumer.  # noqa: E501
        :type datacenter_name: str
        """

        self._datacenter_name = datacenter_name

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
        if not isinstance(other, IpConsumer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpConsumer):
            return True

        return self.to_dict() != other.to_dict()