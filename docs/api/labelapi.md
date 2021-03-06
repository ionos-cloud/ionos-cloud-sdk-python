# LabelApi

## LabelApi

All URIs are relative to [https://api.ionos.com/cloudapi/v5](https://api.ionos.com/cloudapi/v5)

| Method | HTTP request | Description |
| :--- | :--- | :--- |
| [**datacenters\_labels\_delete**](labelapi.md#datacenters_labels_delete) | **DELETE** /datacenters/{datacenterId}/labels/{key} | Delete a Label from Data Center |
| [**datacenters\_labels\_find\_by\_key**](labelapi.md#datacenters_labels_find_by_key) | **GET** /datacenters/{datacenterId}/labels/{key} | Retrieve a Label of Data Center |
| [**datacenters\_labels\_get**](labelapi.md#datacenters_labels_get) | **GET** /datacenters/{datacenterId}/labels | List all Data Center Labels |
| [**datacenters\_labels\_post**](labelapi.md#datacenters_labels_post) | **POST** /datacenters/{datacenterId}/labels | Add a Label to Data Center |
| [**datacenters\_labels\_put**](labelapi.md#datacenters_labels_put) | **PUT** /datacenters/{datacenterId}/labels/{key} | Modify a Label of Data Center |
| [**datacenters\_servers\_labels\_delete**](labelapi.md#datacenters_servers_labels_delete) | **DELETE** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Delete a Label from Server |
| [**datacenters\_servers\_labels\_find\_by\_key**](labelapi.md#datacenters_servers_labels_find_by_key) | **GET** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Retrieve a Label of Server |
| [**datacenters\_servers\_labels\_get**](labelapi.md#datacenters_servers_labels_get) | **GET** /datacenters/{datacenterId}/servers/{serverId}/labels | List all Server Labels |
| [**datacenters\_servers\_labels\_post**](labelapi.md#datacenters_servers_labels_post) | **POST** /datacenters/{datacenterId}/servers/{serverId}/labels | Add a Label to Server |
| [**datacenters\_servers\_labels\_put**](labelapi.md#datacenters_servers_labels_put) | **PUT** /datacenters/{datacenterId}/servers/{serverId}/labels/{key} | Modify a Label of Server |
| [**datacenters\_volumes\_labels\_delete**](labelapi.md#datacenters_volumes_labels_delete) | **DELETE** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Delete a Label from Volume |
| [**datacenters\_volumes\_labels\_find\_by\_key**](labelapi.md#datacenters_volumes_labels_find_by_key) | **GET** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Retrieve a Label of Volume |
| [**datacenters\_volumes\_labels\_get**](labelapi.md#datacenters_volumes_labels_get) | **GET** /datacenters/{datacenterId}/volumes/{volumeId}/labels | List all Volume Labels |
| [**datacenters\_volumes\_labels\_post**](labelapi.md#datacenters_volumes_labels_post) | **POST** /datacenters/{datacenterId}/volumes/{volumeId}/labels | Add a Label to Volume |
| [**datacenters\_volumes\_labels\_put**](labelapi.md#datacenters_volumes_labels_put) | **PUT** /datacenters/{datacenterId}/volumes/{volumeId}/labels/{key} | Modify a Label of Volume |
| [**ipblocks\_labels\_delete**](labelapi.md#ipblocks_labels_delete) | **DELETE** /ipblocks/{ipblockId}/labels/{key} | Delete a Label from IP Block |
| [**ipblocks\_labels\_find\_by\_key**](labelapi.md#ipblocks_labels_find_by_key) | **GET** /ipblocks/{ipblockId}/labels/{key} | Retrieve a Label of IP Block |
| [**ipblocks\_labels\_get**](labelapi.md#ipblocks_labels_get) | **GET** /ipblocks/{ipblockId}/labels | List all Ip Block Labels |
| [**ipblocks\_labels\_post**](labelapi.md#ipblocks_labels_post) | **POST** /ipblocks/{ipblockId}/labels | Add a Label to IP Block |
| [**ipblocks\_labels\_put**](labelapi.md#ipblocks_labels_put) | **PUT** /ipblocks/{ipblockId}/labels/{key} | Modify a Label of IP Block |
| [**labels\_find\_by\_urn**](labelapi.md#labels_find_by_urn) | **GET** /labels/{labelurn} | Returns the label by its URN. |
| [**labels\_get**](labelapi.md#labels_get) | **GET** /labels | List Labels |
| [**snapshots\_labels\_delete**](labelapi.md#snapshots_labels_delete) | **DELETE** /snapshots/{snapshotId}/labels/{key} | Delete a Label from Snapshot |
| [**snapshots\_labels\_find\_by\_key**](labelapi.md#snapshots_labels_find_by_key) | **GET** /snapshots/{snapshotId}/labels/{key} | Retrieve a Label of Snapshot |
| [**snapshots\_labels\_get**](labelapi.md#snapshots_labels_get) | **GET** /snapshots/{snapshotId}/labels | List all Snapshot Labels |
| [**snapshots\_labels\_post**](labelapi.md#snapshots_labels_post) | **POST** /snapshots/{snapshotId}/labels | Add a Label to Snapshot |
| [**snapshots\_labels\_put**](labelapi.md#snapshots_labels_put) | **PUT** /snapshots/{snapshotId}/labels/{key} | Modify a Label of Snapshot |

## **datacenters\_labels\_delete**

> object datacenters\_labels\_delete\(datacenter\_id, key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Label from Data Center

This will remove a label from the data center.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Label from Data Center
        api_response = api_instance.datacenters_labels_delete(datacenter_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_delete: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Label from Data Center
        api_response = api_instance.datacenters_labels_delete(datacenter_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_delete: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Data Center |  |
| **key** | **str** | The key of the Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_labels\_find\_by\_key**

> LabelResource datacenters\_labels\_find\_by\_key\(datacenter\_id, key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Label of Data Center

This will retrieve the properties of a associated label to a data center.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Label of Data Center
        api_response = api_instance.datacenters_labels_find_by_key(datacenter_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_find_by_key: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Label of Data Center
        api_response = api_instance.datacenters_labels_find_by_key(datacenter_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_find_by_key: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Data Center |  |
| **key** | **str** | The key of the Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_labels\_get**

> LabelResources datacenters\_labels\_get\(datacenter\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number, offset=offset, limit=limit\)

List all Data Center Labels

You can retrieve a list of all labels associated with a data center

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)
    try:
        # List all Data Center Labels
        api_response = api_instance.datacenters_labels_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_get: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)
    try:
        # List all Data Center Labels
        api_response = api_instance.datacenters_labels_get(datacenter_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_get: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Data Center |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |
| **offset** | **int** | the first element \(of the total list of elements\) to include in the response \(use together with &lt;code&gt;limit&lt;/code&gt; for pagination\) | \[optional\] \[default to 0\] |
| **limit** | **int** | the maximum number of elements to return \(use together with &lt;code&gt;offset&lt;/code&gt; for pagination\) | \[optional\] \[default to 1000\] |

### Return type

[**LabelResources**](../models/labelresources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_labels\_post**

> LabelResource datacenters\_labels\_post\(datacenter\_id, label, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Add a Label to Data Center

This will add a label to the data center.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Label to Data Center
        api_response = api_instance.datacenters_labels_post(datacenter_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_post: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Label to Data Center
        api_response = api_instance.datacenters_labels_post(datacenter_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_post: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Data Center |  |
| **label** | [**LabelResource**](../models/labelresource.md) | Label to be added |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **datacenters\_labels\_put**

> LabelResource datacenters\_labels\_put\(datacenter\_id, key, label, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a Label of Data Center

This will modify the value of the label on a data center.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Label of Data Center
        api_response = api_instance.datacenters_labels_put(datacenter_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_put: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Data Center
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Label of Data Center
        api_response = api_instance.datacenters_labels_put(datacenter_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_labels_put: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Data Center |  |
| **key** | **str** | The key of the Label |  |
| **label** | [**LabelResource**](../models/labelresource.md) | Modified Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **datacenters\_servers\_labels\_delete**

> object datacenters\_servers\_labels\_delete\(datacenter\_id, server\_id, key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Label from Server

This will remove a label from the server.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Label from Server
        api_response = api_instance.datacenters_servers_labels_delete(datacenter_id, server_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_delete: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Label from Server
        api_response = api_instance.datacenters_servers_labels_delete(datacenter_id, server_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_delete: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **key** | **str** | The key of the Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_servers\_labels\_find\_by\_key**

> LabelResource datacenters\_servers\_labels\_find\_by\_key\(datacenter\_id, server\_id, key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Label of Server

This will retrieve the properties of a associated label to a server.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Label of Server
        api_response = api_instance.datacenters_servers_labels_find_by_key(datacenter_id, server_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_find_by_key: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Label of Server
        api_response = api_instance.datacenters_servers_labels_find_by_key(datacenter_id, server_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_find_by_key: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **key** | **str** | The key of the Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_servers\_labels\_get**

> LabelResources datacenters\_servers\_labels\_get\(datacenter\_id, server\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number, offset=offset, limit=limit\)

List all Server Labels

You can retrieve a list of all labels associated with a server

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)
    try:
        # List all Server Labels
        api_response = api_instance.datacenters_servers_labels_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_get: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)
    try:
        # List all Server Labels
        api_response = api_instance.datacenters_servers_labels_get(datacenter_id, server_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_get: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |
| **offset** | **int** | the first element \(of the total list of elements\) to include in the response \(use together with &lt;code&gt;limit&lt;/code&gt; for pagination\) | \[optional\] \[default to 0\] |
| **limit** | **int** | the maximum number of elements to return \(use together with &lt;code&gt;offset&lt;/code&gt; for pagination\) | \[optional\] \[default to 1000\] |

### Return type

[**LabelResources**](../models/labelresources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_servers\_labels\_post**

> LabelResource datacenters\_servers\_labels\_post\(datacenter\_id, server\_id, label, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Add a Label to Server

This will add a label to the server.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Label to Server
        api_response = api_instance.datacenters_servers_labels_post(datacenter_id, server_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_post: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Label to Server
        api_response = api_instance.datacenters_servers_labels_post(datacenter_id, server_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_post: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **label** | [**LabelResource**](../models/labelresource.md) | Label to be added |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **datacenters\_servers\_labels\_put**

> LabelResource datacenters\_servers\_labels\_put\(datacenter\_id, server\_id, key, label, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a Label of Server

This will modify the value of the label on a server.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Label of Server
        api_response = api_instance.datacenters_servers_labels_put(datacenter_id, server_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_put: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    server_id = 'server_id_example' # str | The unique ID of the Server
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Label of Server
        api_response = api_instance.datacenters_servers_labels_put(datacenter_id, server_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_servers_labels_put: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Datacenter |  |
| **server\_id** | **str** | The unique ID of the Server |  |
| **key** | **str** | The key of the Label |  |
| **label** | [**LabelResource**](../models/labelresource.md) | Modified Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **datacenters\_volumes\_labels\_delete**

> object datacenters\_volumes\_labels\_delete\(datacenter\_id, volume\_id, key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Label from Volume

This will remove a label from the volume.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Label from Volume
        api_response = api_instance.datacenters_volumes_labels_delete(datacenter_id, volume_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_delete: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Label from Volume
        api_response = api_instance.datacenters_volumes_labels_delete(datacenter_id, volume_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_delete: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **key** | **str** | The key of the Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_volumes\_labels\_find\_by\_key**

> LabelResource datacenters\_volumes\_labels\_find\_by\_key\(datacenter\_id, volume\_id, key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Label of Volume

This will retrieve the properties of a associated label to a volume.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Label of Volume
        api_response = api_instance.datacenters_volumes_labels_find_by_key(datacenter_id, volume_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_find_by_key: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Label of Volume
        api_response = api_instance.datacenters_volumes_labels_find_by_key(datacenter_id, volume_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_find_by_key: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **key** | **str** | The key of the Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_volumes\_labels\_get**

> LabelResources datacenters\_volumes\_labels\_get\(datacenter\_id, volume\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number, offset=offset, limit=limit\)

List all Volume Labels

You can retrieve a list of all labels associated with a volume

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)
    try:
        # List all Volume Labels
        api_response = api_instance.datacenters_volumes_labels_get(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_get: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    offset = 0 # int | the first element (of the total list of elements) to include in the response (use together with <code>limit</code> for pagination) (optional) (default to 0)
    limit = 1000 # int | the maximum number of elements to return (use together with <code>offset</code> for pagination) (optional) (default to 1000)
    try:
        # List all Volume Labels
        api_response = api_instance.datacenters_volumes_labels_get(datacenter_id, volume_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number, offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_get: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |
| **offset** | **int** | the first element \(of the total list of elements\) to include in the response \(use together with &lt;code&gt;limit&lt;/code&gt; for pagination\) | \[optional\] \[default to 0\] |
| **limit** | **int** | the maximum number of elements to return \(use together with &lt;code&gt;offset&lt;/code&gt; for pagination\) | \[optional\] \[default to 1000\] |

### Return type

[**LabelResources**](../models/labelresources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **datacenters\_volumes\_labels\_post**

> LabelResource datacenters\_volumes\_labels\_post\(datacenter\_id, volume\_id, label, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Add a Label to Volume

This will add a label to the volume.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Label to Volume
        api_response = api_instance.datacenters_volumes_labels_post(datacenter_id, volume_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_post: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Label to Volume
        api_response = api_instance.datacenters_volumes_labels_post(datacenter_id, volume_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_post: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **label** | [**LabelResource**](../models/labelresource.md) | Label to be added |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **datacenters\_volumes\_labels\_put**

> LabelResource datacenters\_volumes\_labels\_put\(datacenter\_id, volume\_id, key, label, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a Label of Volume

This will modify the value of the label on a volume.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Label of Volume
        api_response = api_instance.datacenters_volumes_labels_put(datacenter_id, volume_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_put: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    datacenter_id = 'datacenter_id_example' # str | The unique ID of the Datacenter
    volume_id = 'volume_id_example' # str | The unique ID of the Volume
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Label of Volume
        api_response = api_instance.datacenters_volumes_labels_put(datacenter_id, volume_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.datacenters_volumes_labels_put: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **datacenter\_id** | **str** | The unique ID of the Datacenter |  |
| **volume\_id** | **str** | The unique ID of the Volume |  |
| **key** | **str** | The key of the Label |  |
| **label** | [**LabelResource**](../models/labelresource.md) | Modified Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **ipblocks\_labels\_delete**

> object ipblocks\_labels\_delete\(ipblock\_id, key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Label from IP Block

This will remove a label from the Ip Block.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Label from IP Block
        api_response = api_instance.ipblocks_labels_delete(ipblock_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_delete: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Label from IP Block
        api_response = api_instance.ipblocks_labels_delete(ipblock_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_delete: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **ipblock\_id** | **str** | The unique ID of the Ip Block |  |
| **key** | **str** | The key of the Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **ipblocks\_labels\_find\_by\_key**

> LabelResource ipblocks\_labels\_find\_by\_key\(ipblock\_id, key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Label of IP Block

This will retrieve the properties of a associated label to a Ip Block.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Label of IP Block
        api_response = api_instance.ipblocks_labels_find_by_key(ipblock_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_find_by_key: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Label of IP Block
        api_response = api_instance.ipblocks_labels_find_by_key(ipblock_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_find_by_key: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **ipblock\_id** | **str** | The unique ID of the Ip Block |  |
| **key** | **str** | The key of the Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **ipblocks\_labels\_get**

> LabelResources ipblocks\_labels\_get\(ipblock\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List all Ip Block Labels

You can retrieve a list of all labels associated with a IP Block

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List all Ip Block Labels
        api_response = api_instance.ipblocks_labels_get(ipblock_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_get: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List all Ip Block Labels
        api_response = api_instance.ipblocks_labels_get(ipblock_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_get: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **ipblock\_id** | **str** | The unique ID of the Ip Block |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResources**](../models/labelresources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **ipblocks\_labels\_post**

> LabelResource ipblocks\_labels\_post\(ipblock\_id, label, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Add a Label to IP Block

This will add a label to the Ip Block.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Label to IP Block
        api_response = api_instance.ipblocks_labels_post(ipblock_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_post: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Label to IP Block
        api_response = api_instance.ipblocks_labels_post(ipblock_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_post: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **ipblock\_id** | **str** | The unique ID of the Ip Block |  |
| **label** | [**LabelResource**](../models/labelresource.md) | Label to be added |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **ipblocks\_labels\_put**

> LabelResource ipblocks\_labels\_put\(ipblock\_id, key, label, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a Label of IP Block

This will modify the value of the label on a Ip Block.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Label of IP Block
        api_response = api_instance.ipblocks_labels_put(ipblock_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_put: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    ipblock_id = 'ipblock_id_example' # str | The unique ID of the Ip Block
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Label of IP Block
        api_response = api_instance.ipblocks_labels_put(ipblock_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.ipblocks_labels_put: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **ipblock\_id** | **str** | The unique ID of the Ip Block |  |
| **key** | **str** | The key of the Label |  |
| **label** | [**LabelResource**](../models/labelresource.md) | Modified Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **labels\_find\_by\_urn**

> Label labels\_find\_by\_urn\(labelurn, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Returns the label by its URN.

You can retrieve the details of a specific label using its URN. A URN is for uniqueness of a Label and composed using urn:label:::

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    labelurn = 'labelurn_example' # str | The URN representing the unique ID of the label. A URN is for uniqueness of a Label and composed using urn:label:<resource_type>:<resource_uuid>:<key>
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Returns the label by its URN.
        api_response = api_instance.labels_find_by_urn(labelurn, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.labels_find_by_urn: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    labelurn = 'labelurn_example' # str | The URN representing the unique ID of the label. A URN is for uniqueness of a Label and composed using urn:label:<resource_type>:<resource_uuid>:<key>
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Returns the label by its URN.
        api_response = api_instance.labels_find_by_urn(labelurn, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.labels_find_by_urn: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **labelurn** | **str** | The URN representing the unique ID of the label. A URN is for uniqueness of a Label and composed using urn:label:&lt;resource\_type&gt;:&lt;resource\_uuid&gt;:&lt;key&gt; |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Label**](../models/label.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **labels\_get**

> Labels labels\_get\(pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List Labels

You can retrieve a complete list of labels that you have access to.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List Labels 
        api_response = api_instance.labels_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.labels_get: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List Labels 
        api_response = api_instance.labels_get(pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.labels_get: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**Labels**](../models/labels.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **snapshots\_labels\_delete**

> object snapshots\_labels\_delete\(snapshot\_id, key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Delete a Label from Snapshot

This will remove a label from the snapshot.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Label from Snapshot
        api_response = api_instance.snapshots_labels_delete(snapshot_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_delete: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Delete a Label from Snapshot
        api_response = api_instance.snapshots_labels_delete(snapshot_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_delete: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **snapshot\_id** | **str** | The unique ID of the Snapshot |  |
| **key** | **str** | The key of the Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

**object**

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **snapshots\_labels\_find\_by\_key**

> LabelResource snapshots\_labels\_find\_by\_key\(snapshot\_id, key, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Retrieve a Label of Snapshot

This will retrieve the properties of a associated label to a snapshot.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Label of Snapshot
        api_response = api_instance.snapshots_labels_find_by_key(snapshot_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_find_by_key: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    key = 'key_example' # str | The key of the Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Retrieve a Label of Snapshot
        api_response = api_instance.snapshots_labels_find_by_key(snapshot_id, key, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_find_by_key: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **snapshot\_id** | **str** | The unique ID of the Snapshot |  |
| **key** | **str** | The key of the Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **snapshots\_labels\_get**

> LabelResources snapshots\_labels\_get\(snapshot\_id, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

List all Snapshot Labels

You can retrieve a list of all labels associated with a snapshot

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List all Snapshot Labels
        api_response = api_instance.snapshots_labels_get(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_get: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # List all Snapshot Labels
        api_response = api_instance.snapshots_labels_get(snapshot_id, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_get: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **snapshot\_id** | **str** | The unique ID of the Snapshot |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResources**](../models/labelresources.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: Not defined
* **Accept**: application/json

## **snapshots\_labels\_post**

> LabelResource snapshots\_labels\_post\(snapshot\_id, label, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Add a Label to Snapshot

This will add a label to the snapshot.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Label to Snapshot
        api_response = api_instance.snapshots_labels_post(snapshot_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_post: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    label = ionoscloud.LabelResource() # LabelResource | Label to be added
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Add a Label to Snapshot
        api_response = api_instance.snapshots_labels_post(snapshot_id, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_post: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **snapshot\_id** | **str** | The unique ID of the Snapshot |  |
| **label** | [**LabelResource**](../models/labelresource.md) | Label to be added |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

## **snapshots\_labels\_put**

> LabelResource snapshots\_labels\_put\(snapshot\_id, key, label, pretty=pretty, depth=depth, x\_contract\_number=x\_contract\_number\)

Modify a Label of Snapshot

This will modify the value of the label on a snapshot.

### Example

* Basic Authentication \(Basic Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure HTTP basic authorization: Basic Authentication
  configuration.username = 'YOUR_USERNAME'
  configuration.password = 'YOUR_PASSWORD'
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Label of Snapshot
        api_response = api_instance.snapshots_labels_put(snapshot_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_put: %s\n' % e)
  ```

* Api Key Authentication \(Token Authentication\):

  ```python
  from __future__ import print_function
  import time
  import ionoscloud
  from ionoscloud.rest import ApiException
  from pprint import pprint
  # Defining the host is optional and defaults to https://api.ionos.com/cloudapi/v5
  # See configuration.py for a list of all supported configuration parameters.
  configuration = ionoscloud.Configuration(
    host = 'https://api.ionos.com/cloudapi/v5',
  )
  # The client must configure the authentication and authorization parameters
  # in accordance with the API server security policy.
  # Examples with auth method are provided below
  # Configure Api Key access token for authorization: Token Authentication
  configuration.api_key = {
    'Token Authentication': 'YOUR_API_TOKEN',
  }
  # Enter a context with an instance of the API client
  with ionoscloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud.LabelApi(api_client)
    snapshot_id = 'snapshot_id_example' # str | The unique ID of the Snapshot
    key = 'key_example' # str | The key of the Label
    label = ionoscloud.LabelResource() # LabelResource | Modified Label
    pretty = True # bool | Controls whether response is pretty-printed (with indentation and new lines) (optional) (default to True)
    depth = 0 # int | Controls the details depth of response objects.  Eg. GET /datacenters/[ID]  - depth=0: only direct properties are included. Children (servers etc.) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on (optional) (default to 0)
    x_contract_number = 56 # int | Users having more than 1 contract need to provide contract number, against which all API requests should be executed (optional)
    try:
        # Modify a Label of Snapshot
        api_response = api_instance.snapshots_labels_put(snapshot_id, key, label, pretty=pretty, depth=depth, x_contract_number=x_contract_number)
        pprint(api_response)
    except ApiException as e:
        print('Exception when calling LabelApi.snapshots_labels_put: %s\n' % e)
  ```

### Parameters

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **snapshot\_id** | **str** | The unique ID of the Snapshot |  |
| **key** | **str** | The key of the Label |  |
| **label** | [**LabelResource**](../models/labelresource.md) | Modified Label |  |
| **pretty** | **bool** | Controls whether response is pretty-printed \(with indentation and new lines\) | \[optional\] \[default to True\] |
| **depth** | **int** | Controls the details depth of response objects.  Eg. GET /datacenters/\[ID\]  - depth=0: only direct properties are included. Children \(servers etc.\) are not included  - depth=1: direct properties and children references are included  - depth=2: direct properties and children properties are included  - depth=3: direct properties and children properties and children's children are included  - depth=... and so on | \[optional\] \[default to 0\] |
| **x\_contract\_number** | **int** | Users having more than 1 contract need to provide contract number, against which all API requests should be executed | \[optional\] |

### Return type

[**LabelResource**](../models/labelresource.md)

### Authorization

Basic Authentication, Token Authentication

### HTTP request headers

* **Content-Type**: application/json
* **Accept**: application/json

