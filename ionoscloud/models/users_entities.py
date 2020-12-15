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


class UsersEntities(object):
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
        'owns': 'ResourcesUsers',
        'groups': 'GroupUsers',
    }

    attribute_map = {
        'owns': 'owns',
        'groups': 'groups',
    }

    def __init__(self, owns=None, groups=None, local_vars_configuration=None):  # noqa: E501
        """UsersEntities - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._owns = None
        self._groups = None
        self.discriminator = None

        if owns is not None:
            self.owns = owns
        if groups is not None:
            self.groups = groups

    @property
    def owns(self):
        """Gets the owns of this UsersEntities.  # noqa: E501


        :return: The owns of this UsersEntities.  # noqa: E501
        :rtype: ResourcesUsers
        """
        return self._owns

    @owns.setter
    def owns(self, owns):
        """Sets the owns of this UsersEntities.


        :param owns: The owns of this UsersEntities.  # noqa: E501
        :type owns: ResourcesUsers
        """

        self._owns = owns

    @property
    def groups(self):
        """Gets the groups of this UsersEntities.  # noqa: E501


        :return: The groups of this UsersEntities.  # noqa: E501
        :rtype: GroupUsers
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UsersEntities.


        :param groups: The groups of this UsersEntities.  # noqa: E501
        :type groups: GroupUsers
        """

        self._groups = groups

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
        if not isinstance(other, UsersEntities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsersEntities):
            return True

        return self.to_dict() != other.to_dict()