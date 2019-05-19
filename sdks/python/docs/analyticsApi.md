# appcenter_sdk.analyticsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Devices_BlockLogs**](analyticsApi.md#Devices_BlockLogs) | **PUT** /v0.1/apps/{owner_name}/{app_name}/devices/block_logs/{install_id} | 
[**App_BlockLogs**](analyticsApi.md#App_BlockLogs) | **PUT** /v0.1/apps/{owner_name}/{app_name}/devices/block_logs | 
[**Crashes_ListSessionLogs**](analyticsApi.md#Crashes_ListSessionLogs) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/session_logs | 
[**Analytics_Versions**](analyticsApi.md#Analytics_Versions) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/versions | 
[**Analytics_PerDeviceCounts**](analyticsApi.md#Analytics_PerDeviceCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/sessions_per_device | 
[**Analytics_SessionDurationsDistribution**](analyticsApi.md#Analytics_SessionDurationsDistribution) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/session_durations_distribution | 
[**Analytics_SessionCounts**](analyticsApi.md#Analytics_SessionCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/session_counts | 
[**Analytics_PlaceCounts**](analyticsApi.md#Analytics_PlaceCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/places | 
[**Analytics_OperatingSystemCounts**](analyticsApi.md#Analytics_OperatingSystemCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/oses | 
[**Analytics_ModelCounts**](analyticsApi.md#Analytics_ModelCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/models | 
[**Analytics_LogFlow**](analyticsApi.md#Analytics_LogFlow) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/log_flow | 
[**Analytics_LanguageCounts**](analyticsApi.md#Analytics_LanguageCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/languages | 
[**Analytics_GenericLogFlow**](analyticsApi.md#Analytics_GenericLogFlow) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/generic_log_flow | 
[**Analytics_EventPropertyCounts**](analyticsApi.md#Analytics_EventPropertyCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/properties/{event_property_name}/counts | 
[**Analytics_EventProperties**](analyticsApi.md#Analytics_EventProperties) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/properties | 
[**Analytics_EventCount**](analyticsApi.md#Analytics_EventCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/event_count | 
[**Analytics_EventDeviceCount**](analyticsApi.md#Analytics_EventDeviceCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/device_count | 
[**Analytics_EventPerSessionCount**](analyticsApi.md#Analytics_EventPerSessionCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/count_per_session | 
[**Analytics_EventPerDeviceCount**](analyticsApi.md#Analytics_EventPerDeviceCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/count_per_device | 
[**Analytics_EventsDelete**](analyticsApi.md#Analytics_EventsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name} | 
[**Analytics_Events**](analyticsApi.md#Analytics_Events) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events | 
[**Analytics_EventsDeleteLogs**](analyticsApi.md#Analytics_EventsDeleteLogs) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/analytics/event_logs/{event_name} | 
[**Analytics_DistributionReleaseCounts**](analyticsApi.md#Analytics_DistributionReleaseCounts) | **POST** /v0.1/apps/{owner_name}/{app_name}/analytics/distribution/release_counts | 
[**Analytics_CrashFreeDevicePercentages**](analyticsApi.md#Analytics_CrashFreeDevicePercentages) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crashfree_device_percentages | 
[**Analytics_CrashGroupTotals**](analyticsApi.md#Analytics_CrashGroupTotals) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/overall | Available for UWP apps only.
[**Analytics_CrashGroupOperatingSystemCounts**](analyticsApi.md#Analytics_CrashGroupOperatingSystemCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/operating_systems | Available for UWP apps only.
[**Analytics_CrashGroupModelCounts**](analyticsApi.md#Analytics_CrashGroupModelCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/models | Available for UWP apps only.
[**Analytics_CrashGroupCounts**](analyticsApi.md#Analytics_CrashGroupCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/crash_counts | Available for UWP apps only.
[**Analytics_CrashGroupsTotals**](analyticsApi.md#Analytics_CrashGroupsTotals) | **POST** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups | 
[**Analytics_CrashCounts**](analyticsApi.md#Analytics_CrashCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_counts | Available for UWP apps only.
[**Analytics_AudienceNameExists**](analyticsApi.md#Analytics_AudienceNameExists) | **HEAD** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} | 
[**Analytics_DeleteAudience**](analyticsApi.md#Analytics_DeleteAudience) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} | 
[**Analytics_GetAudience**](analyticsApi.md#Analytics_GetAudience) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} | 
[**Analytics_CreateOrUpdateAudience**](analyticsApi.md#Analytics_CreateOrUpdateAudience) | **PUT** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} | 
[**Analytics_ListDevicePropertyValues**](analyticsApi.md#Analytics_ListDevicePropertyValues) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/device_properties/{property_name}/values | 
[**Analytics_ListDeviceProperties**](analyticsApi.md#Analytics_ListDeviceProperties) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/device_properties | 
[**Analytics_ListCustomProperties**](analyticsApi.md#Analytics_ListCustomProperties) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/custom_properties | 
[**Analytics_TestAudience**](analyticsApi.md#Analytics_TestAudience) | **POST** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/definition/test | 
[**Analytics_ListAudiences**](analyticsApi.md#Analytics_ListAudiences) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences | 
[**Analytics_DeviceCounts**](analyticsApi.md#Analytics_DeviceCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/active_device_counts | 

# **Devices_BlockLogs**
> string Devices_BlockLogs(install_id, owner_name, app_name)



**Warning, this operation is not reversible.**

 A successful call to this API will permanently stop ingesting any logs received via SDK for the given installation ID, and cannot be restored. We advise caution when using this API, it is designed to permanently disable collection from a specific installation of the app on a device, usually following the request from a user.


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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
install_id = "string" # string | The id of the device
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Devices_BlockLogs(install_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Devices_BlockLogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **string**| The id of the device | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

**string**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **App_BlockLogs**
> string App_BlockLogs(owner_name, app_name)



**Warning, this operation is not reversible.** 

A successful call to this API will permanently stop ingesting any logs received via SDK by app_id, and cannot be restored. We advise caution when using this API, it is designed to permanently disable an app_id.


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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.App_BlockLogs(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->App_BlockLogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

**string**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Crashes_ListSessionLogs**
> ErrorResponse Crashes_ListSessionLogs(crash_id, owner_name, app_name, date=date)



Get session logs by crash ID

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
crash_id = "string" # string | The id of the a crash
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
date = "2019-05-18T23:47:08Z" # string | Date of data requested (optional)

try:
    api_response = api_instance.Crashes_ListSessionLogs(crash_id, owner_name, app_name, date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Crashes_ListSessionLogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_id** | **string**| The id of the a crash | 
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

# **Analytics_Versions**
> Error Analytics_Versions(start, owner_name, app_name, end=end, $top=$top, versions=versions)



Count of active versions in the time range ordered by version.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results) (optional) (default to )
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_Versions(start, owner_name, app_name, end=end, $top=$top, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_Versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_PerDeviceCounts**
> Error Analytics_PerDeviceCounts(start, interval, owner_name, app_name, end=end, versions=versions)



Count of sessions per device in the time range

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
interval = "string" # string | Size of interval in ISO 8601 duration format. (PnYnMnDTnHnMnS|PnW|P<date>T<time>). The valid durations are 1 day (P1D), 1 week (P1W), and 30 days (P30D).
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_PerDeviceCounts(start, interval, owner_name, app_name, end=end, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_PerDeviceCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **interval** | **string**| Size of interval in ISO 8601 duration format. (PnYnMnDTnHnMnS|PnW|P&lt;date&gt;T&lt;time&gt;). The valid durations are 1 day (P1D), 1 week (P1W), and 30 days (P30D). | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_SessionDurationsDistribution**
> Error Analytics_SessionDurationsDistribution(start, owner_name, app_name, end=end, versions=versions)



Gets session duration .

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_SessionDurationsDistribution(start, owner_name, app_name, end=end, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_SessionDurationsDistribution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_SessionCounts**
> ErrorResponse Analytics_SessionCounts(start, interval, owner_name, app_name, end=end, versions=versions)



Count of sessions in the time range.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
interval = "string" # string | Size of interval in ISO 8601 duration format. (PnYnMnDTnHnMnS|PnW|P<date>T<time>). The valid durations are 1 day (P1D), 1 week (P1W), and 30 days (P30D).
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_SessionCounts(start, interval, owner_name, app_name, end=end, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_SessionCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **interval** | **string**| Size of interval in ISO 8601 duration format. (PnYnMnDTnHnMnS|PnW|P&lt;date&gt;T&lt;time&gt;). The valid durations are 1 day (P1D), 1 week (P1W), and 30 days (P30D). | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_PlaceCounts**
> Error Analytics_PlaceCounts(start, owner_name, app_name, end=end, $top=$top, versions=versions)



Places in the time range

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results) (optional) (default to )
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_PlaceCounts(start, owner_name, app_name, end=end, $top=$top, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_PlaceCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_OperatingSystemCounts**
> Error Analytics_OperatingSystemCounts(start, owner_name, app_name, end=end, $top=$top, versions=versions)



OSes in the time range

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results) (optional) (default to )
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_OperatingSystemCounts(start, owner_name, app_name, end=end, $top=$top, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_OperatingSystemCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_ModelCounts**
> Error Analytics_ModelCounts(start, owner_name, app_name, end=end, $top=$top, versions=versions)



models in the time range

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results) (optional) (default to )
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_ModelCounts(start, owner_name, app_name, end=end, $top=$top, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_ModelCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_LogFlow**
> ErrorResponse Analytics_LogFlow(owner_name, app_name, start=start)



Logs received between the specified start time and the current time. The API will return a maximum of 100 logs per call.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone. (optional)

try:
    api_response = api_instance.Analytics_LogFlow(owner_name, app_name, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_LogFlow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **start** | **string**| Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone. | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_LanguageCounts**
> Error Analytics_LanguageCounts(start, owner_name, app_name, end=end, $top=$top, versions=versions)



languages in the time range

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results) (optional) (default to )
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_LanguageCounts(start, owner_name, app_name, end=end, $top=$top, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_LanguageCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_GenericLogFlow**
> ErrorResponse Analytics_GenericLogFlow(owner_name, app_name, start=start)



Logs received between the specified start time and the current time. The API will return a maximum of 100 logs per call.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone. (optional)

try:
    api_response = api_instance.Analytics_GenericLogFlow(owner_name, app_name, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_GenericLogFlow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **start** | **string**| Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone. | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_EventPropertyCounts**
> Error Analytics_EventPropertyCounts(event_name, event_property_name, start, owner_name, app_name, end=end, versions=versions, $top=$top)



Event properties value counts during the time range in descending order.  Limited up to 5 values.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
event_name = "string" # string | The id of the event
event_property_name = "string" # string | The id of the event property
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)
$top = 5 # integer | The number of property values to return (optional) (default to )

try:
    api_response = api_instance.Analytics_EventPropertyCounts(event_name, event_property_name, start, owner_name, app_name, end=end, versions=versions, $top=$top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_EventPropertyCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **string**| The id of the event | 
 **event_property_name** | **string**| The id of the event property | 
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 
 **$top** | **integer**| The number of property values to return | [optional] [default to 5]

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_EventProperties**
> Error Analytics_EventProperties(event_name, owner_name, app_name)



Event properties.  Up to the first 5 received properties.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
event_name = "string" # string | The id of the event
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Analytics_EventProperties(event_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_EventProperties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **string**| The id of the event | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_EventCount**
> Error Analytics_EventCount(event_name, start, owner_name, app_name, end=end, versions=versions)



Count of events by interval in the time range.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
event_name = "string" # string | The id of the event
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_EventCount(event_name, start, owner_name, app_name, end=end, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_EventCount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **string**| The id of the event | 
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_EventDeviceCount**
> Error Analytics_EventDeviceCount(event_name, start, owner_name, app_name, end=end, versions=versions)



Count of devices for an event by interval in the time range.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
event_name = "string" # string | The id of the event
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_EventDeviceCount(event_name, start, owner_name, app_name, end=end, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_EventDeviceCount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **string**| The id of the event | 
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_EventPerSessionCount**
> Error Analytics_EventPerSessionCount(event_name, start, owner_name, app_name, end=end, versions=versions)



Count of events per session by interval in the time range.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
event_name = "string" # string | The id of the event
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_EventPerSessionCount(event_name, start, owner_name, app_name, end=end, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_EventPerSessionCount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **string**| The id of the event | 
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_EventPerDeviceCount**
> Error Analytics_EventPerDeviceCount(event_name, start, owner_name, app_name, end=end, versions=versions)



Count of events per device by interval in the time range.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
event_name = "string" # string | The id of the event
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_EventPerDeviceCount(event_name, start, owner_name, app_name, end=end, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_EventPerDeviceCount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **string**| The id of the event | 
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_EventsDelete**
> Error Analytics_EventsDelete(event_name, owner_name, app_name)



Delete the set of Events with the specified event names

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
event_name = "string" # string | The id of the event
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Analytics_EventsDelete(event_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_EventsDelete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **string**| The id of the event | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_Events**
> Error Analytics_Events(start, owner_name, app_name, end=end, versions=versions, event_name=event_name, $top=$top, $skip=$skip, $inlinecount=$inlinecount, $orderby=$orderby)



Count of active events in the time range ordered by event.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)
event_name = ["string"] # array | to select the specific events (optional)
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results) (optional) (default to )
$skip = 0 # integer | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. (optional)
$inlinecount = "none" # string | Controls whether or not to include a count of all the items across all pages. (optional) (default to )
$orderby = "count desc" # string | controls the sorting order and sorting based on which column (optional) (default to )

try:
    api_response = api_instance.Analytics_Events(start, owner_name, app_name, end=end, versions=versions, event_name=event_name, $top=$top, $skip=$skip, $inlinecount=$inlinecount, $orderby=$orderby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_Events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 
 **event_name** | **array**| to select the specific events | [optional] 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]
 **$skip** | **integer**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] 
 **$inlinecount** | **string**| Controls whether or not to include a count of all the items across all pages. | [optional] [default to none]
 **$orderby** | **string**| controls the sorting order and sorting based on which column | [optional] [default to count desc]

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_EventsDeleteLogs**
> Error Analytics_EventsDeleteLogs(event_name, owner_name, app_name)



Delete the set of Events with the specified event names

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
event_name = "string" # string | The id of the event
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Analytics_EventsDeleteLogs(event_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_EventsDeleteLogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_name** | **string**| The id of the event | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_DistributionReleaseCounts**
> ErrorResponse Analytics_DistributionReleaseCounts(owner_name, app_name, body)



Count of total downloads for the provided distribution releases.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"releases":[{"distribution_group":"string","release":"string"}]} # object | The releases to retrieve.

try:
    api_response = api_instance.Analytics_DistributionReleaseCounts(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_DistributionReleaseCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The releases to retrieve. | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_CrashFreeDevicePercentages**
> Error Analytics_CrashFreeDevicePercentages(start, version, owner_name, app_name, end=end)



Percentage of crash-free device by day in the time range based on the selected versions. Api will return -1 if crash devices is greater than active devices.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
version = "string" # string | 
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)

try:
    api_response = api_instance.Analytics_CrashFreeDevicePercentages(start, version, owner_name, app_name, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_CrashFreeDevicePercentages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **version** | **string**|  | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_CrashGroupTotals**
> Error Analytics_CrashGroupTotals(crash_group_id, version, owner_name, app_name)

Available for UWP apps only.

Overall crashes and affected users count of the selected crash group with selected version. Available for UWP apps only.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | The id of the crash group
version = "string" # string | 
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.Analytics_CrashGroupTotals(crash_group_id, version, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_CrashGroupTotals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| The id of the crash group | 
 **version** | **string**|  | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_CrashGroupOperatingSystemCounts**
> Error Analytics_CrashGroupOperatingSystemCounts(crash_group_id, version, owner_name, app_name, $top=$top)

Available for UWP apps only.

top OSes of the selected crash group with selected version. Available for UWP apps only.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | The id of the crash group
version = "string" # string | 
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results) (optional) (default to )

try:
    # 
    api_response = api_instance.Analytics_CrashGroupOperatingSystemCounts(crash_group_id, version, owner_name, app_name, $top=$top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_CrashGroupOperatingSystemCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| The id of the crash group | 
 **version** | **string**|  | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_CrashGroupModelCounts**
> Error Analytics_CrashGroupModelCounts(crash_group_id, version, owner_name, app_name, $top=$top)

Available for UWP apps only.

top models of the selected crash group with selected version. Available for UWP apps only.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | The id of the crash group
version = "string" # string | 
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
$top = 30 # integer | The maximum number of results to return. (0 will fetch all results) (optional) (default to )

try:
    # 
    api_response = api_instance.Analytics_CrashGroupModelCounts(crash_group_id, version, owner_name, app_name, $top=$top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_CrashGroupModelCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| The id of the crash group | 
 **version** | **string**|  | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **$top** | **integer**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30]

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_CrashGroupCounts**
> Error Analytics_CrashGroupCounts(crash_group_id, version, start, owner_name, app_name, end=end)

Available for UWP apps only.

Count of crashes by day in the time range of the selected crash group with selected version. Available for UWP apps only.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | The id of the crash group
version = "string" # string | 
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)

try:
    # 
    api_response = api_instance.Analytics_CrashGroupCounts(crash_group_id, version, start, owner_name, app_name, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_CrashGroupCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| The id of the crash group | 
 **version** | **string**|  | 
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_CrashGroupsTotals**
> Error Analytics_CrashGroupsTotals(owner_name, app_name, body)



Overall crashes and affected users count of the selected crash groups with selected versions

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"crash_groups":[{"crash_group_id":"string","app_version":"string"}]} # object | 

try:
    api_response = api_instance.Analytics_CrashGroupsTotals(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_CrashGroupsTotals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_CrashCounts**
> Error Analytics_CrashCounts(start, owner_name, app_name, end=end, versions=versions)

Available for UWP apps only.

Count of crashes by day in the time range based the selected versions. Available for UWP apps only.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)

try:
    # 
    api_response = api_instance.Analytics_CrashCounts(start, owner_name, app_name, end=end, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_CrashCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_AudienceNameExists**
> ErrorResponse Analytics_AudienceNameExists(audience_name, owner_name, app_name)



Returns whether audience definition exists.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
audience_name = "string" # string | The name of the audience
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Analytics_AudienceNameExists(audience_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_AudienceNameExists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_name** | **string**| The name of the audience | 
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

# **Analytics_DeleteAudience**
> ErrorResponse Analytics_DeleteAudience(audience_name, owner_name, app_name)



Deletes audience definition.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
audience_name = "string" # string | The name of the audience
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Analytics_DeleteAudience(audience_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_DeleteAudience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_name** | **string**| The name of the audience | 
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

# **Analytics_GetAudience**
> ErrorResponse Analytics_GetAudience(audience_name, owner_name, app_name)



Gets audience definition.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
audience_name = "string" # string | The name of the audience
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Analytics_GetAudience(audience_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_GetAudience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_name** | **string**| The name of the audience | 
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

# **Analytics_CreateOrUpdateAudience**
> ErrorResponse Analytics_CreateOrUpdateAudience(audience_name, owner_name, app_name, body)



Creates or updates audience definition.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
audience_name = "string" # string | The name of the audience
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"description":"string","definition":"string","enabled":true,"custom_properties":{"property1":"string","property2":"string"}} # object | Audience definition

try:
    api_response = api_instance.Analytics_CreateOrUpdateAudience(audience_name, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_CreateOrUpdateAudience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_name** | **string**| The name of the audience | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Audience definition | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_ListDevicePropertyValues**
> ErrorResponse Analytics_ListDevicePropertyValues(property_name, owner_name, app_name, contains=contains)



Get list of device property values.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
property_name = "string" # string | Device property
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
contains = "string" # string | Contains string (optional)

try:
    api_response = api_instance.Analytics_ListDevicePropertyValues(property_name, owner_name, app_name, contains=contains)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_ListDevicePropertyValues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_name** | **string**| Device property | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **contains** | **string**| Contains string | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_ListDeviceProperties**
> ErrorResponse Analytics_ListDeviceProperties(owner_name, app_name)



Get list of device properties.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Analytics_ListDeviceProperties(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_ListDeviceProperties: %s\n" % e)
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

# **Analytics_ListCustomProperties**
> ErrorResponse Analytics_ListCustomProperties(owner_name, app_name)



Get list of custom properties.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.Analytics_ListCustomProperties(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_ListCustomProperties: %s\n" % e)
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

# **Analytics_TestAudience**
> ErrorResponse Analytics_TestAudience(owner_name, app_name, body)



Tests audience definition.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"description":"string","definition":"string","enabled":true,"custom_properties":{"property1":"string","property2":"string"}} # object | Audience definition

try:
    api_response = api_instance.Analytics_TestAudience(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_TestAudience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Audience definition | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_ListAudiences**
> ErrorResponse Analytics_ListAudiences(owner_name, app_name, include_disabled=include_disabled)



Get list of audiences.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
include_disabled = true # boolean | Include disabled audience definitions (optional)

try:
    api_response = api_instance.Analytics_ListAudiences(owner_name, app_name, include_disabled=include_disabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_ListAudiences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **include_disabled** | **boolean**| Include disabled audience definitions | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **Analytics_DeviceCounts**
> Error Analytics_DeviceCounts(start, owner_name, app_name, end=end, versions=versions)



Count of active devices by interval in the time range.

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
api_instance = appcenter_sdk.analyticsApi(appcenter_sdk.ApiClient(configuration))
start = "2019-05-18T23:47:08Z" # string | Start date time in data in ISO 8601 date time format
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
end = "2019-05-18T23:47:08Z" # string | Last date time in data in ISO 8601 date time format (optional)
versions = ["string"] # array |  (optional)

try:
    api_response = api_instance.Analytics_DeviceCounts(start, owner_name, app_name, end=end, versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling analyticsApi->Analytics_DeviceCounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **string**| Start date time in data in ISO 8601 date time format | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **end** | **string**| Last date time in data in ISO 8601 date time format | [optional] 
 **versions** | **array**|  | [optional] 

### Return type

[**Error**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

