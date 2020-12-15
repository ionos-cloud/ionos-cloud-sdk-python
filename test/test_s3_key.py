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
from ionoscloud.models.s3_key import S3Key  # noqa: E501
from ionoscloud.rest import ApiException

class TestS3Key(unittest.TestCase):
    """S3Key unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test S3Key
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.s3_key.S3Key()  # noqa: E501
        if include_optional :
            return S3Key(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c'
                type = "group"
                href = 'https://<API_HOST>/cloudapi/v5/um/users/15f67991-0f51-4efc-a8ad-ef1fb31a480c/s3keys/78fa888e106456c1482d'
                metadata = ionoscloud.models.s3_key_metadata.S3KeyMetadata(
                    etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                    created_date = '2015-12-04T14:34:09.809Z', )
                properties = ionoscloud.models.s3_key_properties.S3KeyProperties(
                    secret_key = 'tFVkUARsoeCdntQs2jVSyGG6TMPfPZ+ghnsWj/gG', 
                    active = True, )
            )
        else :
            return S3Key(
                properties = ionoscloud.models.s3_key_properties.S3KeyProperties(
                    secret_key = 'tFVkUARsoeCdntQs2jVSyGG6TMPfPZ+ghnsWj/gG', 
                    active = True, ),
        )

    def testS3Key(self):
        """Test S3Key"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
