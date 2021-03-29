# coding: utf-8

"""
    CLOUD API

    An enterprise-grade Infrastructure is provided as a Service (IaaS) solution that can be managed through a browser-based \"Data Center Designer\" (DCD) tool or via an easy to use API.   The API allows you to perform a variety of management tasks such as spinning up additional servers, adding volumes, adjusting networking, and so forth. It is designed to allow users to leverage the same power and flexibility found within the DCD visual tool. Both tools are consistent with their concepts and lend well to making the experience smooth and intuitive.  # noqa: E501

    The version of the OpenAPI document: 6.0-SDK.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ionoscloud
from ionoscloud.models.kubernetes_node import KubernetesNode  # noqa: E501
from ionoscloud.rest import ApiException

class TestKubernetesNode(unittest.TestCase):
    """KubernetesNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubernetesNode
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.kubernetes_node.KubernetesNode()  # noqa: E501
        if include_optional :
            return KubernetesNode(
                id = '1e072e52-2ed3-492f-b6b6-c6b116907527',
                type = 'node',
                href = '<RESOURCE-URI>',
                metadata = ionoscloud.models.kubernetes_node_metadata.KubernetesNodeMetadata(
                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                    created_date = '2015-12-04T14:34:09.809Z', 
                    last_modified_date = '2015-12-04T14:34:09.809Z', 
                    state = 'AVAILABLE', 
                    last_software_updated_date = '2015-12-04T14:34:09.809Z', ),
                properties = ionoscloud.models.kubernetes_node_properties.KubernetesNodeProperties(
                    name = 'k8s-node', 
                    public_ip = '192.168.23.2', 
                    private_ip = '192.168.23.2', 
                    k8s_version = '1.15.4', )
            )
        else :
            return KubernetesNode(
                properties = ionoscloud.models.kubernetes_node_properties.KubernetesNodeProperties(
                    name = 'k8s-node', 
                    public_ip = '192.168.23.2', 
                    private_ip = '192.168.23.2', 
                    k8s_version = '1.15.4', ),
        )

    def testKubernetesNode(self):
        """Test KubernetesNode"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
