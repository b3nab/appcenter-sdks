# appcenter_sdk.mbaasApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_getResourceProvisioning**](mbaasApi.md#data_getResourceProvisioning) | **GET** /v0.1/apps/{owner_name}/{app_name}/data/resource_provisioning | 
[**data_postResourceProvisioning**](mbaasApi.md#data_postResourceProvisioning) | **POST** /v0.1/apps/{owner_name}/{app_name}/data/resource_provisioning | Creates Cosmos DB or attaches an existing one
[**data_getOverview**](mbaasApi.md#data_getOverview) | **GET** /v0.1/apps/{owner_name}/{app_name}/data/overview | Gets general data about the provisioned database
[**data_checkNameExists**](mbaasApi.md#data_checkNameExists) | **HEAD** /v0.1/apps/{owner_name}/{app_name}/data/database_account_names/{accountName} | Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the &#39;-&#39; character, and must be between 3 and 31 characters.
[**identity_getUsers**](mbaasApi.md#identity_getUsers) | **GET** /v0.1/apps/{owner_name}/{app_name}/auth/users | Returns users of a tenant.
Returns all users if no searchTerm param is specified.

# **data_getResourceProvisioning**
> ErrorResponse data_getResourceProvisioning(owner_name, app_name)





### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIToken
configuration = appcenter_sdk.Configuration()
configuration.api_key['X-API-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Token'] = 'Bearer'

# create an instance of the API class
api_instance = appcenter_sdk.mbaasApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.data_getResourceProvisioning(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling mbaasApi->data_getResourceProvisioning: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: text/plain, text/plain, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_postResourceProvisioning**
> ErrorResponse data_postResourceProvisioning(AC-Authorization-ARM, owner_name, app_name, body=body)

Creates Cosmos DB or attaches an existing one



### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIToken
configuration = appcenter_sdk.Configuration()
configuration.api_key['X-API-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Token'] = 'Bearer'

# create an instance of the API class
api_instance = appcenter_sdk.mbaasApi(appcenter_sdk.ApiClient(configuration))
AC-Authorization-ARM = "string" # string | 
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"subscriptionId":"string","databaseConnectionString":"string","resourceRegion":"East Asia","database":"string","collection":"string","requestUnits":400,"accountName":"string"} # object |  (optional)

try:
    # 
    api_response = api_instance.data_postResourceProvisioning(AC-Authorization-ARM, owner_name, app_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling mbaasApi->data_postResourceProvisioning: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **AC-Authorization-ARM** | **string**|  | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: text/plain, text/plain, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_getOverview**
> ErrorResponse data_getOverview(AC-Authorization-ARM, owner_name, app_name)

Gets general data about the provisioned database



### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIToken
configuration = appcenter_sdk.Configuration()
configuration.api_key['X-API-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Token'] = 'Bearer'

# create an instance of the API class
api_instance = appcenter_sdk.mbaasApi(appcenter_sdk.ApiClient(configuration))
AC-Authorization-ARM = "string" # string | ARM token
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.data_getOverview(AC-Authorization-ARM, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling mbaasApi->data_getOverview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **AC-Authorization-ARM** | **string**| ARM token | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: text/plain, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_checkNameExists**
> data_checkNameExists(accountName, owner_name, app_name)

Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the '-' character, and must be between 3 and 31 characters.



### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIToken
configuration = appcenter_sdk.Configuration()
configuration.api_key['X-API-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Token'] = 'Bearer'

# create an instance of the API class
api_instance = appcenter_sdk.mbaasApi(appcenter_sdk.ApiClient(configuration))
accountName = "string" # string | 
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_instance.data_checkNameExists(accountName, owner_name, app_name)
except ApiException as e:
    print("Exception when calling mbaasApi->data_checkNameExists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountName** | **string**|  | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

void (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, text/csv, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_getUsers**
> ErrorResponse identity_getUsers(owner_name, app_name, AC-Authorization-AAD-Graph=AC-Authorization-AAD-Graph, searchTerm=searchTerm)

Returns users of a tenant.
Returns all users if no searchTerm param is specified.



### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIToken
configuration = appcenter_sdk.Configuration()
configuration.api_key['X-API-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Token'] = 'Bearer'

# create an instance of the API class
api_instance = appcenter_sdk.mbaasApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
AC-Authorization-AAD-Graph = "string" # string | MSGraph Auth Token (optional)
searchTerm = "string" # string | User search term (optional)

try:
    # 
    api_response = api_instance.identity_getUsers(owner_name, app_name, AC-Authorization-AAD-Graph=AC-Authorization-AAD-Graph, searchTerm=searchTerm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling mbaasApi->identity_getUsers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **AC-Authorization-AAD-Graph** | **string**| MSGraph Auth Token | [optional] 
 **searchTerm** | **string**| User search term | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: text/plain, text/plain, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

