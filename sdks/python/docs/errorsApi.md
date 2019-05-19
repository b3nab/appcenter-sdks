# appcenter_sdk.errorsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Errors_ListSessionLogs**](errorsApi.md#Errors_ListSessionLogs) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/sessionLogs | 
[**Errors_ErrorAttachmentText**](errorsApi.md#Errors_ErrorAttachmentText) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/attachments/{attachmentId}/text | 
[**Errors_ErrorAttachmentLocation**](errorsApi.md#Errors_ErrorAttachmentLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/attachments/{attachmentId}/location | 
[**Errors_ErrorAttachments**](errorsApi.md#Errors_ErrorAttachments) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/attachments | 
[**Errors_ErrorSearch**](errorsApi.md#Errors_ErrorSearch) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/search | 
[**errors_putRetentionSettings**](errorsApi.md#errors_putRetentionSettings) | **PUT** /v0.1/apps/{owner_name}/{app_name}/errors/retention_settings | Creates and updates the retention settings in days
[**errors_getRetentionSettings**](errorsApi.md#errors_getRetentionSettings) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/retention_settings | gets the retention settings in days
[**Errors_ErrorFreeDevicePercentages**](errorsApi.md#Errors_ErrorFreeDevicePercentages) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorfreeDevicePercentages | 
[**Errors_GroupErrorStackTrace**](errorsApi.md#Errors_GroupErrorStackTrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/stacktrace | 
[**Errors_GroupOperatingSystemCounts**](errorsApi.md#Errors_GroupOperatingSystemCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/operatingSystems | 
[**Errors_GroupModelCounts**](errorsApi.md#Errors_GroupModelCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/models | 
[**Errors_ErrorStackTrace**](errorsApi.md#Errors_ErrorStackTrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId}/stacktrace | 
[**Errors_ErrorLocation**](errorsApi.md#Errors_ErrorLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId}/location | 
[**Errors_ErrorDownload**](errorsApi.md#Errors_ErrorDownload) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId}/download | 
[**Errors_GetErrorDetails**](errorsApi.md#Errors_GetErrorDetails) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId} | 
[**Errors_DeleteError**](errorsApi.md#Errors_DeleteError) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId} | 
[**Errors_LatestErrorDetails**](errorsApi.md#Errors_LatestErrorDetails) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/latest | 
[**Errors_ListForGroup**](errorsApi.md#Errors_ListForGroup) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors | 
[**Errors_GroupErrorFreeDevicePercentages**](errorsApi.md#Errors_GroupErrorFreeDevicePercentages) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errorfreeDevicePercentages | 
[**Errors_GroupCountsPerDay**](errorsApi.md#Errors_GroupCountsPerDay) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errorCountsPerDay | 
[**Errors_GroupDetails**](errorsApi.md#Errors_GroupDetails) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId} | 
[**Errors_UpdateState**](errorsApi.md#Errors_UpdateState) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId} | 
[**Errors_ErrorGroupsSearch**](errorsApi.md#Errors_ErrorGroupsSearch) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/search | 
[**Errors_GroupList**](errorsApi.md#Errors_GroupList) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups | 
[**Errors_CountsPerDay**](errorsApi.md#Errors_CountsPerDay) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorCountsPerDay | 
[**Errors_AvailableVersions**](errorsApi.md#Errors_AvailableVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/available_versions | 

# **Errors_ListSessionLogs**
> ErrorResponse Errors_ListSessionLogs(errorId, owner_name, app_name, date=date)



Get session logs by error ID

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorId = "string" # string | The id of the error
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
date = "2019-05-18T23:47:08Z" # string | Date of data requested (optional)

try:
    api_response = api_instance.Errors_ListSessionLogs(errorId, owner_name, app_name, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ListSessionLogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorId** | **string**| The id of the error | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **date** | **string**| Date of data requested | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_ErrorAttachmentText**
> ErrorResponse Errors_ErrorAttachmentText(errorId, attachmentId, owner_name, app_name)



Error attachment text.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorId = "string" # string | The id of the error
attachmentId = "string" # string | Error attachment id.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Errors_ErrorAttachmentText(errorId, attachmentId, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ErrorAttachmentText: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorId** | **string**| The id of the error | 
 **attachmentId** | **string**| Error attachment id. | 
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

# **Errors_ErrorAttachmentLocation**
> ErrorResponse Errors_ErrorAttachmentLocation(errorId, attachmentId, owner_name, app_name)



Error attachment location.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorId = "string" # string | The id of the error
attachmentId = "string" # string | Error attachment id.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Errors_ErrorAttachmentLocation(errorId, attachmentId, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ErrorAttachmentLocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorId** | **string**| The id of the error | 
 **attachmentId** | **string**| Error attachment id. | 
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

# **Errors_ErrorAttachments**
> ErrorResponse Errors_ErrorAttachments(errorId, owner_name, app_name)



List error attachments.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorId = "string" # string | The id of the error
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Errors_ErrorAttachments(errorId, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ErrorAttachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorId** | **string**| The id of the error | 
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

# **Errors_ErrorSearch**
> ErrorResponse Errors_ErrorSearch(owner_name, app_name, filter=filter, q=q, order=order, sort=sort, $top=$top, $skip=$skip)



Errors list based on search parameters

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
filter = "string" # string | A filter as specified in OData notation (optional)
q = "string" # string | A query string (optional)
order = "desc" # string | It controls the order of sorting (optional) (default to )
sort = "timestamp" # string | It controls the sort based on specified field (optional) (default to )
$top = 100 # integer | The maximum number of results to return (optional) (default to )
$skip = 0 # integer | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. (optional)

try:
    api_response = api_instance.Errors_ErrorSearch(owner_name, app_name, filter=filter, q=q, order=order, sort=sort, $top=$top, $skip=$skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ErrorSearch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **filter** | **string**| A filter as specified in OData notation | [optional] 
 **q** | **string**| A query string | [optional] 
 **order** | **string**| It controls the order of sorting | [optional] [default to desc]
 **sort** | **string**| It controls the sort based on specified field | [optional] [default to timestamp]
 **$top** | **integer**| The maximum number of results to return | [optional] [default to 100]
 **$skip** | **integer**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **errors_putRetentionSettings**
> ErrorResponse errors_putRetentionSettings(owner_name, app_name, body)

Creates and updates the retention settings in days

Creates and updates the retention settings in days

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"retention_in_days":28} # object | The amount of days to keep the crashes for this application. retention_in_days is an enum value, can only be 28 or 90.

try:
    # 
    api_response = api_instance.errors_putRetentionSettings(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->errors_putRetentionSettings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The amount of days to keep the crashes for this application. retention_in_days is an enum value, can only be 28 or 90. | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **errors_getRetentionSettings**
> ErrorResponse errors_getRetentionSettings(owner_name, app_name)

gets the retention settings in days

gets the retention settings in days

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.errors_getRetentionSettings(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->errors_getRetentionSettings: %s\n" % e)
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

# **Errors_ErrorFreeDevicePercentages**
> ErrorResponse Errors_ErrorFreeDevicePercentages(start, owner_name, app_name, end=end, versions=versions, errorType=errorType)



Percentage of error-free devices by day in the time range based on the selected versions. If SingleErrorTypeParameter is not provided, defaults to handlederror. API will return -1 if crash devices is greater than active devices

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)
errorType = "unhandledError" # string | Type of error (handled vs unhandled), excluding All (optional)

try:
    api_response = api_instance.Errors_ErrorFreeDevicePercentages(start, owner_name, app_name, end=end, versions=versions, errorType=errorType)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ErrorFreeDevicePercentages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 
 **errorType** | **string**| Type of error (handled vs unhandled), excluding All | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_GroupErrorStackTrace**
> ErrorResponse Errors_GroupErrorStackTrace(errorGroupId, owner_name, app_name)



Gets the stack trace for the error group.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Errors_GroupErrorStackTrace(errorGroupId, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_GroupErrorStackTrace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
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

# **Errors_GroupOperatingSystemCounts**
> ErrorResponse Errors_GroupOperatingSystemCounts(errorGroupId, owner_name, app_name, $top=$top)



Top OSes of the selected error group.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results till the max number.) (optional) (default to )

try:
    api_response = api_instance.Errors_GroupOperatingSystemCounts(errorGroupId, owner_name, app_name, $top=$top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_GroupOperatingSystemCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30]

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_GroupModelCounts**
> ErrorResponse Errors_GroupModelCounts(errorGroupId, owner_name, app_name, $top=$top)



Top models of the selected error group.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results till the max number.) (optional) (default to )

try:
    api_response = api_instance.Errors_GroupModelCounts(errorGroupId, owner_name, app_name, $top=$top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_GroupModelCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30]

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_ErrorStackTrace**
> ErrorResponse Errors_ErrorStackTrace(errorGroupId, errorId, owner_name, app_name)



Error Stacktrace details.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
errorId = "string" # string | The id of the error
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Errors_ErrorStackTrace(errorGroupId, errorId, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ErrorStackTrace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **errorId** | **string**| The id of the error | 
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

# **Errors_ErrorLocation**
> ErrorResponse Errors_ErrorLocation(errorGroupId, errorId, owner_name, app_name)



Error location.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
errorId = "string" # string | The id of the error
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Errors_ErrorLocation(errorGroupId, errorId, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ErrorLocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **errorId** | **string**| The id of the error | 
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

# **Errors_ErrorDownload**
> ErrorResponse Errors_ErrorDownload(errorGroupId, errorId, owner_name, app_name, format=format)



Download details for a specific error.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
errorId = "string" # string | The id of the error
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
format = "json" # string | the format of the crash log (optional)

try:
    api_response = api_instance.Errors_ErrorDownload(errorGroupId, errorId, owner_name, app_name, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ErrorDownload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **errorId** | **string**| The id of the error | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **format** | **string**| the format of the crash log | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_GetErrorDetails**
> ErrorResponse Errors_GetErrorDetails(errorGroupId, errorId, owner_name, app_name)



Error details.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
errorId = "string" # string | The id of the error
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Errors_GetErrorDetails(errorGroupId, errorId, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_GetErrorDetails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **errorId** | **string**| The id of the error | 
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

# **Errors_DeleteError**
> ErrorResponse Errors_DeleteError(errorGroupId, errorId, owner_name, app_name)



Delete a specific error and related attachments and blobs for an app. Searchable data will not be deleted immediately and may take up to 30 days.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
errorId = "string" # string | The id of the error
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Errors_DeleteError(errorGroupId, errorId, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_DeleteError: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **errorId** | **string**| The id of the error | 
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

# **Errors_LatestErrorDetails**
> ErrorResponse Errors_LatestErrorDetails(errorGroupId, owner_name, app_name)



Latest error details.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Errors_LatestErrorDetails(errorGroupId, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_LatestErrorDetails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
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

# **Errors_ListForGroup**
> ErrorResponse Errors_ListForGroup(errorGroupId, start, owner_name, app_name, end=end, model=model, os=os)



Get all errors for group

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
model = "string" # string |  (optional)
os = "string" # string |  (optional)

try:
    api_response = api_instance.Errors_ListForGroup(errorGroupId, start, owner_name, app_name, end=end, model=model, os=os)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ListForGroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **model** | **string**|  | [optional] 
 **os** | **string**|  | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_GroupErrorFreeDevicePercentages**
> ErrorResponse Errors_GroupErrorFreeDevicePercentages(errorGroupId, start, owner_name, app_name, end=end)



Percentage of error-free devices by day in the time range. Api will return -1 if crash devices is greater than active devices

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)

try:
    api_response = api_instance.Errors_GroupErrorFreeDevicePercentages(errorGroupId, start, owner_name, app_name, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_GroupErrorFreeDevicePercentages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_GroupCountsPerDay**
> ErrorResponse Errors_GroupCountsPerDay(errorGroupId, start, owner_name, app_name, version=version, end=end)



Count of errors by day in the time range of the selected error group with selected version

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
version = "string" # string |  (optional)
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)

try:
    api_response = api_instance.Errors_GroupCountsPerDay(errorGroupId, start, owner_name, app_name, version=version, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_GroupCountsPerDay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **version** | **string**|  | [optional] 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_GroupDetails**
> ErrorResponse Errors_GroupDetails(errorGroupId, owner_name, app_name)



Error group details

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Errors_GroupDetails(errorGroupId, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_GroupDetails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
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

# **Errors_UpdateState**
> ErrorResponse Errors_UpdateState(errorGroupId, owner_name, app_name, body)



Update error group state

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
errorGroupId = "string" # string | The id of the error group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"state":"open","annotation":"string"} # object | The state of the error group

try:
    api_response = api_instance.Errors_UpdateState(errorGroupId, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_UpdateState: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **errorGroupId** | **string**| The id of the error group | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The state of the error group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_ErrorGroupsSearch**
> ErrorResponse Errors_ErrorGroupsSearch(owner_name, app_name, filter=filter, q=q, order=order, sort=sort, $top=$top, $skip=$skip)



Error groups list based on search parameters

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
filter = "string" # string | A filter as specified in OData notation (optional)
q = "string" # string | A query string (optional)
order = "desc" # string | It controls the order of sorting (optional) (default to )
sort = "matchingReportsCount" # string | It controls the sort based on specified field (optional) (default to )
$top = 100 # integer | The maximum number of results to return (optional) (default to )
$skip = 0 # integer | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. (optional)

try:
    api_response = api_instance.Errors_ErrorGroupsSearch(owner_name, app_name, filter=filter, q=q, order=order, sort=sort, $top=$top, $skip=$skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_ErrorGroupsSearch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **filter** | **string**| A filter as specified in OData notation | [optional] 
 **q** | **string**| A query string | [optional] 
 **order** | **string**| It controls the order of sorting | [optional] [default to desc]
 **sort** | **string**| It controls the sort based on specified field | [optional] [default to matchingReportsCount]
 **$top** | **integer**| The maximum number of results to return | [optional] [default to 100]
 **$skip** | **integer**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_GroupList**
> ErrorResponse Errors_GroupList(start, owner_name, app_name, version=version, groupState=groupState, end=end, $orderby=$orderby, $top=$top, errorType=errorType)



List of error groups

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
version = "string" # string |  (optional)
groupState = "string" # string |  (optional)
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
$orderby = "count desc" # string | controls the sorting order and sorting based on which column (optional) (default to )
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results till the max number.) (optional) (default to )
errorType = "all" # string | Type of error (handled vs unhandled), including All (optional)

try:
    api_response = api_instance.Errors_GroupList(start, owner_name, app_name, version=version, groupState=groupState, end=end, $orderby=$orderby, $top=$top, errorType=errorType)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_GroupList: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **version** | **string**|  | [optional] 
 **groupState** | **string**|  | [optional] 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **$orderby** | **string**| controls the sorting order and sorting based on which column | [optional] [default to count desc]
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30]
 **errorType** | **string**| Type of error (handled vs unhandled), including All | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_CountsPerDay**
> ErrorResponse Errors_CountsPerDay(start, owner_name, app_name, version=version, end=end, errorType=errorType)



Count of crashes or errors by day in the time range based the selected versions. If SingleErrorTypeParameter is not provided, defaults to handlederror.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
version = "string" # string |  (optional)
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
errorType = "unhandledError" # string | Type of error (handled vs unhandled), excluding All (optional)

try:
    api_response = api_instance.Errors_CountsPerDay(start, owner_name, app_name, version=version, end=end, errorType=errorType)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_CountsPerDay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **version** | **string**|  | [optional] 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **errorType** | **string**| Type of error (handled vs unhandled), excluding All | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Errors_AvailableVersions**
> ErrorResponse Errors_AvailableVersions(start, owner_name, app_name, end=end, $top=$top, $skip=$skip, $filter=$filter, $inlinecount=$inlinecount, errorType=errorType)



Get all available versions in the time range.

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
api_instance = appcenter_sdk.errorsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results till the max number.) (optional) (default to )
$skip = 0 # integer | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. (optional)
$filter = "string" # string | A filter as specified in https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md#97-filtering. (optional)
$inlinecount = "none" # string | Controls whether or not to include a count of all the items across all pages. (optional) (default to )
errorType = "all" # string | Type of error (handled vs unhandled), including All (optional)

try:
    api_response = api_instance.Errors_AvailableVersions(start, owner_name, app_name, end=end, $top=$top, $skip=$skip, $filter=$filter, $inlinecount=$inlinecount, errorType=errorType)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling errorsApi->Errors_AvailableVersions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30]
 **$skip** | **integer**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] 
 **$filter** | **string**| A filter as specified in https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md#97-filtering. | [optional] 
 **$inlinecount** | **string**| Controls whether or not to include a count of all the items across all pages. | [optional] [default to none]
 **errorType** | **string**| Type of error (handled vs unhandled), including All | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

