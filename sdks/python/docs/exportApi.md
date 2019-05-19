# appcenter_sdk.exportApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ExportConfigurations_Enable**](exportApi.md#ExportConfigurations_Enable) | **POST** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}/enable | 
[**ExportConfigurations_Disable**](exportApi.md#ExportConfigurations_Disable) | **POST** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}/disable | 
[**ExportConfigurations_Get**](exportApi.md#ExportConfigurations_Get) | **GET** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id} | 
[**ExportConfigurations_PartialUpdate**](exportApi.md#ExportConfigurations_PartialUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id} | 
[**ExportConfigurations_Delete**](exportApi.md#ExportConfigurations_Delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id} | 
[**ExportConfigurations_List**](exportApi.md#ExportConfigurations_List) | **GET** /v0.1/apps/{owner_name}/{app_name}/export_configurations | 
[**ExportConfigurations_Create**](exportApi.md#ExportConfigurations_Create) | **POST** /v0.1/apps/{owner_name}/{app_name}/export_configurations | 

# **ExportConfigurations_Enable**
> ErrorResponse ExportConfigurations_Enable(export_configuration_id, owner_name, app_name)



Enable export configuration.

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
api_instance = appcenter_sdk.exportApi(appcenter_sdk.ApiClient(configuration))
export_configuration_id = "string" # string | The id of the export configuration.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.ExportConfigurations_Enable(export_configuration_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling exportApi->ExportConfigurations_Enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_configuration_id** | **string**| The id of the export configuration. | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ExportConfigurations_Disable**
> ErrorResponse ExportConfigurations_Disable(export_configuration_id, owner_name, app_name)



Disable export configuration.

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
api_instance = appcenter_sdk.exportApi(appcenter_sdk.ApiClient(configuration))
export_configuration_id = "string" # string | The id of the export configuration.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.ExportConfigurations_Disable(export_configuration_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling exportApi->ExportConfigurations_Disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_configuration_id** | **string**| The id of the export configuration. | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ExportConfigurations_Get**
> ErrorResponse ExportConfigurations_Get(export_configuration_id, owner_name, app_name)



Get export configuration.

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
api_instance = appcenter_sdk.exportApi(appcenter_sdk.ApiClient(configuration))
export_configuration_id = "string" # string | The id of the export configuration.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.ExportConfigurations_Get(export_configuration_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling exportApi->ExportConfigurations_Get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_configuration_id** | **string**| The id of the export configuration. | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ExportConfigurations_PartialUpdate**
> ErrorResponse ExportConfigurations_PartialUpdate(export_configuration_id, owner_name, app_name, body)



Partially update export configuration.

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
api_instance = appcenter_sdk.exportApi(appcenter_sdk.ApiClient(configuration))
export_configuration_id = "string" # string | The id of the export configuration.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"type":"blob_storage_connection_string","export_entities":["crashes"],"resource_name":"string","resource_group":"string"} # object | Export configurations.

try:
    api_response = api_instance.ExportConfigurations_PartialUpdate(export_configuration_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling exportApi->ExportConfigurations_PartialUpdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_configuration_id** | **string**| The id of the export configuration. | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Export configurations. | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ExportConfigurations_Delete**
> ErrorResponse ExportConfigurations_Delete(export_configuration_id, owner_name, app_name)



Delete export configuration.

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
api_instance = appcenter_sdk.exportApi(appcenter_sdk.ApiClient(configuration))
export_configuration_id = "string" # string | The id of the export configuration.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.ExportConfigurations_Delete(export_configuration_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling exportApi->ExportConfigurations_Delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_configuration_id** | **string**| The id of the export configuration. | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ExportConfigurations_List**
> ErrorResponse ExportConfigurations_List(owner_name, app_name)



List export configurations.

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
api_instance = appcenter_sdk.exportApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.ExportConfigurations_List(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling exportApi->ExportConfigurations_List: %s\n" % e)
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
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ExportConfigurations_Create**
> ErrorResponse ExportConfigurations_Create(owner_name, app_name, body)



Create new export configuration

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
api_instance = appcenter_sdk.exportApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"type":"blob_storage_connection_string","export_entities":["crashes"],"resource_name":"string","resource_group":"string"} # object | Export configurations.

try:
    api_response = api_instance.ExportConfigurations_Create(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling exportApi->ExportConfigurations_Create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Export configurations. | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

