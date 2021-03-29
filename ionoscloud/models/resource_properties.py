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


class ResourceProperties(object):
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
        'name': 'str',
        'sec_auth_protection': 'bool',
    }

    attribute_map = {
        'name': 'name',
        'sec_auth_protection': 'secAuthProtection',
    }

    def __init__(self, name=None, sec_auth_protection=None, local_vars_configuration=None):  # noqa: E501
        """ResourceProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._sec_auth_protection = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if sec_auth_protection is not None:
            self.sec_auth_protection = sec_auth_protection

    @property
    def name(self):
        """Gets the name of this ResourceProperties.  # noqa: E501

        name of the resource  # noqa: E501

        :return: The name of this ResourceProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceProperties.

        name of the resource  # noqa: E501

        :param name: The name of this ResourceProperties.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def sec_auth_protection(self):
        """Gets the sec_auth_protection of this ResourceProperties.  # noqa: E501

        Boolean value representing if the resource is multi factor protected or not e.g. using two factor protection. Currently only Data Centers and Snapshots are allowed to be multi factor protected, The value of attribute if null is intentional and it means that the resource doesn't support multi factor protection at all.  # noqa: E501

        :return: The sec_auth_protection of this ResourceProperties.  # noqa: E501
        :rtype: bool
        """
        return self._sec_auth_protection

    @sec_auth_protection.setter
    def sec_auth_protection(self, sec_auth_protection):
        """Sets the sec_auth_protection of this ResourceProperties.

        Boolean value representing if the resource is multi factor protected or not e.g. using two factor protection. Currently only Data Centers and Snapshots are allowed to be multi factor protected, The value of attribute if null is intentional and it means that the resource doesn't support multi factor protection at all.  # noqa: E501

        :param sec_auth_protection: The sec_auth_protection of this ResourceProperties.  # noqa: E501
        :type sec_auth_protection: bool
        """

        self._sec_auth_protection = sec_auth_protection

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
        if not isinstance(other, ResourceProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceProperties):
            return True

        return self.to_dict() != other.to_dict()
