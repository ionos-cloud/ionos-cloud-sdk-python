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
from ionoscloud.models.groups import Groups  # noqa: E501
from ionoscloud.rest import ApiException

class TestGroups(unittest.TestCase):
    """Groups unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Groups
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ionoscloud.models.groups.Groups()  # noqa: E501
        if include_optional :
            return Groups(
                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c'
                type = "groups"
                href = 'https://<API_HOST>/cloudapi/v5/um/groups'
                items = [
                    ionoscloud.models.group.Group(
                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        type = "group", 
                        href = 'https://<API_HOST>/cloudapi/v5/um/groups/15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                        properties = ionoscloud.models.group_properties.GroupProperties(
                            name = 'My resource', 
                            create_data_center = True, 
                            create_snapshot = True, 
                            reserve_ip = True, 
                            access_activity_log = True, 
                            create_pcc = True, 
                            s3_privilege = True, 
                            create_backup_unit = True, 
                            create_internet_access = True, 
                            create_k8s_cluster = True, ), 
                        entities = ionoscloud.models.group_entities.GroupEntities(
                            users = ionoscloud.models.group_members.GroupMembers(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "collection", 
                                href = 'https://<API_HOST>/cloudapi/v5/um/groups/30740c22-1def-11e7-aac9-d7a3646ca7fd/users', 
                                items = [
                                    ionoscloud.models.user.User(
                                        id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                        type = "user", 
                                        href = '<RESOURCE-URI>', 
                                        metadata = ionoscloud.models.user_metadata.UserMetadata(
                                            etag = '45480eb3fbfc31f1d916c1eaa4abdcc3', 
                                            created_date = '2015-12-04T14:34:09.809Z', 
                                            last_login = '2015-12-04T14:34:09.809Z', ), 
                                        properties = ionoscloud.models.user_properties.UserProperties(
                                            firstname = '', 
                                            lastname = '', 
                                            email = '', 
                                            administrator = True, 
                                            force_sec_auth = True, 
                                            sec_auth_active = True, 
                                            s3_canonical_user_id = '', 
                                            password = '', ), )
                                    ], ), 
                            resources = ionoscloud.models.resource_groups.ResourceGroups(
                                id = '15f67991-0f51-4efc-a8ad-ef1fb31a480c', 
                                type = "collection", 
                                href = 'https://<API_HOST>/cloudapi/v5/um/groups/30740c22-1def-11e7-aac9-d7a3646ca7fd/resources', ), ), )
                    ]
            )
        else :
            return Groups(
        )

    def testGroups(self):
        """Test Groups"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
