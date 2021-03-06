# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 5.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ionoscloud
from ionoscloud.models.ip_block import IpBlock  # noqa: E501
from ionoscloud.rest import ApiException

class TestIpBlock(unittest.TestCase):
    """IpBlock unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IpBlock
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.ip_block.IpBlock()  # noqa: E501
        if include_optional :
            return IpBlock(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c',
                type = "ipblock",
                href = '<RESOURCE-URI>',
                metadata = ionoscloud.models.datacenter_element_metadata.DatacenterElementMetadata(
                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                    created_date = '2015-12-04T14:34:09.809Z', 
                    created_by = 'user@example.com', 
                    created_by_user_id = 'user@example.com', 
                    last_modified_date = '2015-12-04T14:34:09.809Z', 
                    last_modified_by = 'user@example.com', 
                    last_modified_by_user_id = '63cef532-26fe-4a64-a4e0-de7c8a506c90', 
                    state = 'AVAILABLE', ),
                properties = ionoscloud.models.ip_block_properties.IpBlockProperties(
                    ips = ["22.231.113.64", "22.231.113.65", "22.231.113.66"], 
                    location = 'us/las', 
                    size = 5, 
                    name = 'My resource', 
                    ip_consumers = { "ipConsumers": [ { "ip" : "192.18.2.11", "mac" : "02:01:3f:52:6e:57", "nicId" : "0e8ee463-1174-46f2-87ba-a5c79c14d8e5", "serverId" : "e6a3466f-8d6e-4cb6-8001-f4e245f222b7", "serverName" : "Unnamed Server", "datacenterId" : "6e54a9ec-aace-4176-8ee4-1c3a704fccfc", "datacenterName" : "IpConsumerDC", "k8sNodePoolUuid" : "6e54a9ec-aace-4176-8ee4-1c3a704fcc12", "k8sClusterUuid" : "6e54a9ec-aace-4176-8ee4-1c3a704fcc23"} ] }, )
            )
        else :
            return IpBlock(
                properties = ionoscloud.models.ip_block_properties.IpBlockProperties(
                    ips = ["22.231.113.64", "22.231.113.65", "22.231.113.66"], 
                    location = 'us/las', 
                    size = 5, 
                    name = 'My resource', 
                    ip_consumers = { "ipConsumers": [ { "ip" : "192.18.2.11", "mac" : "02:01:3f:52:6e:57", "nicId" : "0e8ee463-1174-46f2-87ba-a5c79c14d8e5", "serverId" : "e6a3466f-8d6e-4cb6-8001-f4e245f222b7", "serverName" : "Unnamed Server", "datacenterId" : "6e54a9ec-aace-4176-8ee4-1c3a704fccfc", "datacenterName" : "IpConsumerDC", "k8sNodePoolUuid" : "6e54a9ec-aace-4176-8ee4-1c3a704fcc12", "k8sClusterUuid" : "6e54a9ec-aace-4176-8ee4-1c3a704fcc23"} ] }, ),
        )

    def testIpBlock(self):
        """Test IpBlock"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
