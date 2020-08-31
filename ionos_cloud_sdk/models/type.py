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

from ionos_cloud_sdk.configuration import Configuration


class Type(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    DATACENTER = "datacenter"
    SERVER = "server"
    VOLUME = "volume"
    NIC = "nic"
    LOADBALANCER = "loadbalancer"
    LOCATION = "location"
    FIREWALL_RULE = "firewall-rule"
    IMAGE = "image"
    SNAPSHOT = "snapshot"
    LAN = "lan"
    IPBLOCK = "ipblock"
    PCC = "pcc"
    CONTRACT = "contract"
    USER = "user"
    GROUP = "group"
    COLLECTION = "collection"
    RESOURCE = "resource"
    REQUEST = "request"
    REQUEST_STATUS = "request-status"
    S3KEY = "s3key"
    BACKUPUNIT = "backupunit"
    LABEL = "label"
    K8S = "k8s"
    NODEPOOL = "nodepool"

    allowable_values = [DATACENTER, SERVER, VOLUME, NIC, LOADBALANCER, LOCATION, FIREWALL_RULE, IMAGE, SNAPSHOT, LAN, IPBLOCK, PCC, CONTRACT, USER, GROUP, COLLECTION, RESOURCE, REQUEST, REQUEST_STATUS, S3KEY, BACKUPUNIT, LABEL, K8S, NODEPOOL]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """Type - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, Type):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Type):
            return True

        return self.to_dict() != other.to_dict()
