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


class SnapshotProperties(object):
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
        'description': 'str',
        'location': 'str',
        'size': 'float',
        'sec_auth_protection': 'bool',
        'cpu_hot_plug': 'bool',
        'cpu_hot_unplug': 'bool',
        'ram_hot_plug': 'bool',
        'ram_hot_unplug': 'bool',
        'nic_hot_plug': 'bool',
        'nic_hot_unplug': 'bool',
        'disc_virtio_hot_plug': 'bool',
        'disc_virtio_hot_unplug': 'bool',
        'disc_scsi_hot_plug': 'bool',
        'disc_scsi_hot_unplug': 'bool',
        'licence_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'location': 'location',
        'size': 'size',
        'sec_auth_protection': 'secAuthProtection',
        'cpu_hot_plug': 'cpuHotPlug',
        'cpu_hot_unplug': 'cpuHotUnplug',
        'ram_hot_plug': 'ramHotPlug',
        'ram_hot_unplug': 'ramHotUnplug',
        'nic_hot_plug': 'nicHotPlug',
        'nic_hot_unplug': 'nicHotUnplug',
        'disc_virtio_hot_plug': 'discVirtioHotPlug',
        'disc_virtio_hot_unplug': 'discVirtioHotUnplug',
        'disc_scsi_hot_plug': 'discScsiHotPlug',
        'disc_scsi_hot_unplug': 'discScsiHotUnplug',
        'licence_type': 'licenceType'
    }

    def __init__(self, name=None, description=None, location=None, size=None, sec_auth_protection=None, cpu_hot_plug=None, cpu_hot_unplug=None, ram_hot_plug=None, ram_hot_unplug=None, nic_hot_plug=None, nic_hot_unplug=None, disc_virtio_hot_plug=None, disc_virtio_hot_unplug=None, disc_scsi_hot_plug=None, disc_scsi_hot_unplug=None, licence_type=None, local_vars_configuration=None):  # noqa: E501
        """SnapshotProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._location = None
        self._size = None
        self._sec_auth_protection = None
        self._cpu_hot_plug = None
        self._cpu_hot_unplug = None
        self._ram_hot_plug = None
        self._ram_hot_unplug = None
        self._nic_hot_plug = None
        self._nic_hot_unplug = None
        self._disc_virtio_hot_plug = None
        self._disc_virtio_hot_unplug = None
        self._disc_scsi_hot_plug = None
        self._disc_scsi_hot_unplug = None
        self._licence_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if location is not None:
            self.location = location
        if size is not None:
            self.size = size
        if sec_auth_protection is not None:
            self.sec_auth_protection = sec_auth_protection
        if cpu_hot_plug is not None:
            self.cpu_hot_plug = cpu_hot_plug
        if cpu_hot_unplug is not None:
            self.cpu_hot_unplug = cpu_hot_unplug
        if ram_hot_plug is not None:
            self.ram_hot_plug = ram_hot_plug
        if ram_hot_unplug is not None:
            self.ram_hot_unplug = ram_hot_unplug
        if nic_hot_plug is not None:
            self.nic_hot_plug = nic_hot_plug
        if nic_hot_unplug is not None:
            self.nic_hot_unplug = nic_hot_unplug
        if disc_virtio_hot_plug is not None:
            self.disc_virtio_hot_plug = disc_virtio_hot_plug
        if disc_virtio_hot_unplug is not None:
            self.disc_virtio_hot_unplug = disc_virtio_hot_unplug
        if disc_scsi_hot_plug is not None:
            self.disc_scsi_hot_plug = disc_scsi_hot_plug
        if disc_scsi_hot_unplug is not None:
            self.disc_scsi_hot_unplug = disc_scsi_hot_unplug
        if licence_type is not None:
            self.licence_type = licence_type

    @property
    def name(self):
        """Gets the name of this SnapshotProperties.  # noqa: E501

        A name of that resource  # noqa: E501

        :return: The name of this SnapshotProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotProperties.

        A name of that resource  # noqa: E501

        :param name: The name of this SnapshotProperties.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this SnapshotProperties.  # noqa: E501

        Human readable description  # noqa: E501

        :return: The description of this SnapshotProperties.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SnapshotProperties.

        Human readable description  # noqa: E501

        :param description: The description of this SnapshotProperties.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def location(self):
        """Gets the location of this SnapshotProperties.  # noqa: E501

        Location of that image/snapshot.   # noqa: E501

        :return: The location of this SnapshotProperties.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SnapshotProperties.

        Location of that image/snapshot.   # noqa: E501

        :param location: The location of this SnapshotProperties.  # noqa: E501
        :type location: str
        """

        self._location = location

    @property
    def size(self):
        """Gets the size of this SnapshotProperties.  # noqa: E501

        The size of the image in GB  # noqa: E501

        :return: The size of this SnapshotProperties.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SnapshotProperties.

        The size of the image in GB  # noqa: E501

        :param size: The size of this SnapshotProperties.  # noqa: E501
        :type size: float
        """

        self._size = size

    @property
    def sec_auth_protection(self):
        """Gets the sec_auth_protection of this SnapshotProperties.  # noqa: E501

        Boolean value representing if the snapshot requires extra protection e.g. two factor protection  # noqa: E501

        :return: The sec_auth_protection of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._sec_auth_protection

    @sec_auth_protection.setter
    def sec_auth_protection(self, sec_auth_protection):
        """Sets the sec_auth_protection of this SnapshotProperties.

        Boolean value representing if the snapshot requires extra protection e.g. two factor protection  # noqa: E501

        :param sec_auth_protection: The sec_auth_protection of this SnapshotProperties.  # noqa: E501
        :type sec_auth_protection: bool
        """

        self._sec_auth_protection = sec_auth_protection

    @property
    def cpu_hot_plug(self):
        """Gets the cpu_hot_plug of this SnapshotProperties.  # noqa: E501

        Is capable of CPU hot plug (no reboot required)  # noqa: E501

        :return: The cpu_hot_plug of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._cpu_hot_plug

    @cpu_hot_plug.setter
    def cpu_hot_plug(self, cpu_hot_plug):
        """Sets the cpu_hot_plug of this SnapshotProperties.

        Is capable of CPU hot plug (no reboot required)  # noqa: E501

        :param cpu_hot_plug: The cpu_hot_plug of this SnapshotProperties.  # noqa: E501
        :type cpu_hot_plug: bool
        """

        self._cpu_hot_plug = cpu_hot_plug

    @property
    def cpu_hot_unplug(self):
        """Gets the cpu_hot_unplug of this SnapshotProperties.  # noqa: E501

        Is capable of CPU hot unplug (no reboot required)  # noqa: E501

        :return: The cpu_hot_unplug of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._cpu_hot_unplug

    @cpu_hot_unplug.setter
    def cpu_hot_unplug(self, cpu_hot_unplug):
        """Sets the cpu_hot_unplug of this SnapshotProperties.

        Is capable of CPU hot unplug (no reboot required)  # noqa: E501

        :param cpu_hot_unplug: The cpu_hot_unplug of this SnapshotProperties.  # noqa: E501
        :type cpu_hot_unplug: bool
        """

        self._cpu_hot_unplug = cpu_hot_unplug

    @property
    def ram_hot_plug(self):
        """Gets the ram_hot_plug of this SnapshotProperties.  # noqa: E501

        Is capable of memory hot plug (no reboot required)  # noqa: E501

        :return: The ram_hot_plug of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._ram_hot_plug

    @ram_hot_plug.setter
    def ram_hot_plug(self, ram_hot_plug):
        """Sets the ram_hot_plug of this SnapshotProperties.

        Is capable of memory hot plug (no reboot required)  # noqa: E501

        :param ram_hot_plug: The ram_hot_plug of this SnapshotProperties.  # noqa: E501
        :type ram_hot_plug: bool
        """

        self._ram_hot_plug = ram_hot_plug

    @property
    def ram_hot_unplug(self):
        """Gets the ram_hot_unplug of this SnapshotProperties.  # noqa: E501

        Is capable of memory hot unplug (no reboot required)  # noqa: E501

        :return: The ram_hot_unplug of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._ram_hot_unplug

    @ram_hot_unplug.setter
    def ram_hot_unplug(self, ram_hot_unplug):
        """Sets the ram_hot_unplug of this SnapshotProperties.

        Is capable of memory hot unplug (no reboot required)  # noqa: E501

        :param ram_hot_unplug: The ram_hot_unplug of this SnapshotProperties.  # noqa: E501
        :type ram_hot_unplug: bool
        """

        self._ram_hot_unplug = ram_hot_unplug

    @property
    def nic_hot_plug(self):
        """Gets the nic_hot_plug of this SnapshotProperties.  # noqa: E501

        Is capable of nic hot plug (no reboot required)  # noqa: E501

        :return: The nic_hot_plug of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._nic_hot_plug

    @nic_hot_plug.setter
    def nic_hot_plug(self, nic_hot_plug):
        """Sets the nic_hot_plug of this SnapshotProperties.

        Is capable of nic hot plug (no reboot required)  # noqa: E501

        :param nic_hot_plug: The nic_hot_plug of this SnapshotProperties.  # noqa: E501
        :type nic_hot_plug: bool
        """

        self._nic_hot_plug = nic_hot_plug

    @property
    def nic_hot_unplug(self):
        """Gets the nic_hot_unplug of this SnapshotProperties.  # noqa: E501

        Is capable of nic hot unplug (no reboot required)  # noqa: E501

        :return: The nic_hot_unplug of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._nic_hot_unplug

    @nic_hot_unplug.setter
    def nic_hot_unplug(self, nic_hot_unplug):
        """Sets the nic_hot_unplug of this SnapshotProperties.

        Is capable of nic hot unplug (no reboot required)  # noqa: E501

        :param nic_hot_unplug: The nic_hot_unplug of this SnapshotProperties.  # noqa: E501
        :type nic_hot_unplug: bool
        """

        self._nic_hot_unplug = nic_hot_unplug

    @property
    def disc_virtio_hot_plug(self):
        """Gets the disc_virtio_hot_plug of this SnapshotProperties.  # noqa: E501

        Is capable of Virt-IO drive hot plug (no reboot required)  # noqa: E501

        :return: The disc_virtio_hot_plug of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._disc_virtio_hot_plug

    @disc_virtio_hot_plug.setter
    def disc_virtio_hot_plug(self, disc_virtio_hot_plug):
        """Sets the disc_virtio_hot_plug of this SnapshotProperties.

        Is capable of Virt-IO drive hot plug (no reboot required)  # noqa: E501

        :param disc_virtio_hot_plug: The disc_virtio_hot_plug of this SnapshotProperties.  # noqa: E501
        :type disc_virtio_hot_plug: bool
        """

        self._disc_virtio_hot_plug = disc_virtio_hot_plug

    @property
    def disc_virtio_hot_unplug(self):
        """Gets the disc_virtio_hot_unplug of this SnapshotProperties.  # noqa: E501

        Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.  # noqa: E501

        :return: The disc_virtio_hot_unplug of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._disc_virtio_hot_unplug

    @disc_virtio_hot_unplug.setter
    def disc_virtio_hot_unplug(self, disc_virtio_hot_unplug):
        """Sets the disc_virtio_hot_unplug of this SnapshotProperties.

        Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.  # noqa: E501

        :param disc_virtio_hot_unplug: The disc_virtio_hot_unplug of this SnapshotProperties.  # noqa: E501
        :type disc_virtio_hot_unplug: bool
        """

        self._disc_virtio_hot_unplug = disc_virtio_hot_unplug

    @property
    def disc_scsi_hot_plug(self):
        """Gets the disc_scsi_hot_plug of this SnapshotProperties.  # noqa: E501

        Is capable of SCSI drive hot plug (no reboot required)  # noqa: E501

        :return: The disc_scsi_hot_plug of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._disc_scsi_hot_plug

    @disc_scsi_hot_plug.setter
    def disc_scsi_hot_plug(self, disc_scsi_hot_plug):
        """Sets the disc_scsi_hot_plug of this SnapshotProperties.

        Is capable of SCSI drive hot plug (no reboot required)  # noqa: E501

        :param disc_scsi_hot_plug: The disc_scsi_hot_plug of this SnapshotProperties.  # noqa: E501
        :type disc_scsi_hot_plug: bool
        """

        self._disc_scsi_hot_plug = disc_scsi_hot_plug

    @property
    def disc_scsi_hot_unplug(self):
        """Gets the disc_scsi_hot_unplug of this SnapshotProperties.  # noqa: E501

        Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.  # noqa: E501

        :return: The disc_scsi_hot_unplug of this SnapshotProperties.  # noqa: E501
        :rtype: bool
        """
        return self._disc_scsi_hot_unplug

    @disc_scsi_hot_unplug.setter
    def disc_scsi_hot_unplug(self, disc_scsi_hot_unplug):
        """Sets the disc_scsi_hot_unplug of this SnapshotProperties.

        Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.  # noqa: E501

        :param disc_scsi_hot_unplug: The disc_scsi_hot_unplug of this SnapshotProperties.  # noqa: E501
        :type disc_scsi_hot_unplug: bool
        """

        self._disc_scsi_hot_unplug = disc_scsi_hot_unplug

    @property
    def licence_type(self):
        """Gets the licence_type of this SnapshotProperties.  # noqa: E501

        OS type of this Snapshot  # noqa: E501

        :return: The licence_type of this SnapshotProperties.  # noqa: E501
        :rtype: str
        """
        return self._licence_type

    @licence_type.setter
    def licence_type(self, licence_type):
        """Sets the licence_type of this SnapshotProperties.

        OS type of this Snapshot  # noqa: E501

        :param licence_type: The licence_type of this SnapshotProperties.  # noqa: E501
        :type licence_type: str
        """
        allowed_values = ["UNKNOWN", "WINDOWS", "WINDOWS2016", "LINUX", "OTHER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and licence_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `licence_type` ({0}), must be one of {1}"  # noqa: E501
                .format(licence_type, allowed_values)
            )

        self._licence_type = licence_type

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
        if not isinstance(other, SnapshotProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotProperties):
            return True

        return self.to_dict() != other.to_dict()
