# appcenter_sdk.pushApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Push_ConfigExists**](pushApi.md#Push_ConfigExists) | **HEAD** /v0.1/apps/{owner_name}/{app_name}/push/notifications_config | 
[**Push_GetConfig**](pushApi.md#Push_GetConfig) | **GET** /v0.1/apps/{owner_name}/{app_name}/push/notifications_config | 
[**Push_SetConfig**](pushApi.md#Push_SetConfig) | **PUT** /v0.1/apps/{owner_name}/{app_name}/push/notifications_config | 
[**Push_DeleteConfig**](pushApi.md#Push_DeleteConfig) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/push/notifications_config | 
[**Push_Get**](pushApi.md#Push_Get) | **GET** /v0.1/apps/{owner_name}/{app_name}/push/notifications/{notification_id} | 
[**Push_List**](pushApi.md#Push_List) | **GET** /v0.1/apps/{owner_name}/{app_name}/push/notifications | 
[**Push_Send**](pushApi.md#Push_Send) | **POST** /v0.1/apps/{owner_name}/{app_name}/push/notifications | 
[**Push_Delete**](pushApi.md#Push_Delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/push/notifications | 
[**Push_DeleteInstallId**](pushApi.md#Push_DeleteInstallId) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/push/devices/{install_id} | 
[**Push_ExportDevicesStatus**](pushApi.md#Push_ExportDevicesStatus) | **GET** /v0.1/apps/{owner_name}/{app_name}/push/device_exports/{export_id} | 
[**Push_ExportDevices**](pushApi.md#Push_ExportDevices) | **POST** /v0.1/apps/{owner_name}/{app_name}/push/device_exports | 

# **Push_ConfigExists**
> ErrorResponse Push_ConfigExists(owner_name, app_name)



Returns whether a push configuration exists for the selected app.

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Push_ConfigExists(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_ConfigExists: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Push_GetConfig**
> ErrorResponse Push_GetConfig(owner_name, app_name)



Get the push configuration for the selected app.

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Push_GetConfig(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_GetConfig: %s\n" % e)
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

# **Push_SetConfig**
> ErrorResponse Push_SetConfig(owner_name, app_name, body)



Set the push configuration for the selected app.

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"type":"apns_token_config"} # object | Notification configurations.

try:
    api_response = api_instance.Push_SetConfig(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_SetConfig: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Notification configurations. | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Push_DeleteConfig**
> ErrorResponse Push_DeleteConfig(owner_name, app_name)



Delete the push configuration for the selected app.

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Push_DeleteConfig(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_DeleteConfig: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Push_Get**
> ErrorResponse Push_Get(notification_id, owner_name, app_name)



Get details about a specific notification.

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
notification_id = "string" # string | The id of the notification.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Push_Get(notification_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_Get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **string**| The id of the notification. | 
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

# **Push_List**
> ErrorResponse Push_List(owner_name, app_name, $top=$top, $skiptoken=$skiptoken, $orderby=$orderby, $inlinecount=$inlinecount, include_archived=include_archived)



Get a list of notifications from the service.

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results) (optional) (default to )
$skiptoken = "string" # string | The value identifies a starting point in the collection of entities. This parameter along with limit is used to perform pagination. (optional)
$orderby = "count desc" # string | controls the sorting order and sorting based on which column (optional) (default to )
$inlinecount = "none" # string | Controls whether or not to include a count of all the items across all pages. (optional) (default to )
include_archived = true # boolean | Include arhived push notifications (optional)

try:
    api_response = api_instance.Push_List(owner_name, app_name, $top=$top, $skiptoken=$skiptoken, $orderby=$orderby, $inlinecount=$inlinecount, include_archived=include_archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_List: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **$skiptoken** | **string**| The value identifies a starting point in the collection of entities. This parameter along with limit is used to perform pagination. | [optional] 
 **$orderby** | **string**| controls the sorting order and sorting based on which column | [optional] [default to count desc]
 **$inlinecount** | **string**| Controls whether or not to include a count of all the items across all pages. | [optional] [default to none]
 **include_archived** | **boolean**| Include arhived push notifications | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Push_Send**
> ErrorResponse Push_Send(owner_name, app_name, body)



Send a notification to one or more devices.

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"notification_target":{"type":"devices_target","devices":["146fbdde-0aaf-444d-bcc0-6d84520c9080","746fbdde-0aaf-444d-bcc0-6d84520c9111"]},"notification_content":{"name":"Transaction 23-09814","title":"Sales Order Update","body":"Sales order 18987 for customer Acme Dynamite status changed to SHIPPED"}} # object | Notification specifications.

try:
    api_response = api_instance.Push_Send(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_Send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Notification specifications. | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Push_Delete**
> ErrorResponse Push_Delete(owner_name, app_name, body)



Delete a notification.

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"values":["string"]} # object | List of notification ids

try:
    api_response = api_instance.Push_Delete(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_Delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| List of notification ids | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Push_DeleteInstallId**
> ErrorResponse Push_DeleteInstallId(install_id, owner_name, app_name)



Delete a device with the selected installId.

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
install_id = "string" # string | device install id
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Push_DeleteInstallId(install_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_DeleteInstallId: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **string**| device install id | 
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

# **Push_ExportDevicesStatus**
> ErrorResponse Push_ExportDevicesStatus(export_id, owner_name, app_name)



Get the status of an export operation.

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
export_id = "string" # string | The id of the export.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Push_ExportDevicesStatus(export_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_ExportDevicesStatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **string**| The id of the export. | 
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

# **Push_ExportDevices**
> ErrorResponse Push_ExportDevices(owner_name, app_name, body)



Exports information for all devices using Push to Azure Blob Storage

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
api_instance = appcenter_sdk.pushApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"blob_container_sas_uri":"string"} # object | Export configurations.

try:
    api_response = api_instance.Push_ExportDevices(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling pushApi->Push_ExportDevices: %s\n" % e)
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

