# appcenter_sdk.alertingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_getUserEmailSettings**](alertingApi.md#notifications_getUserEmailSettings) | **GET** /v0.1/user/notifications/emailSettings | 
[**webhooks_list**](alertingApi.md#webhooks_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/webhooks | 
[**notifications_getAppEmailSettings**](alertingApi.md#notifications_getAppEmailSettings) | **GET** /v0.1/apps/{owner_name}/{app_name}/notifications/emailSettings | 
[**bugTracker_getRepoIssueFromCrash**](alertingApi.md#bugTracker_getRepoIssueFromCrash) | **GET** /v0.1/apps/{owner_name}/{app_name}/bugtracker/crashGroup/{crash_group_id} | 
[**bugtracker_getSettings**](alertingApi.md#bugtracker_getSettings) | **GET** /v0.1/apps/{owner_name}/{app_name}/bugtracker | 

# **notifications_getUserEmailSettings**
> AlertingError notifications_getUserEmailSettings()



Get Default email notification settings for the user

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
api_instance = appcenter_sdk.alertingApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.notifications_getUserEmailSettings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling alertingApi->notifications_getUserEmailSettings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertingError**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_list**
> AlertingError webhooks_list(owner_name, app_name)



Get web hooks configured for a particular app

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
api_instance = appcenter_sdk.alertingApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.webhooks_list(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling alertingApi->webhooks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**AlertingError**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_getAppEmailSettings**
> AlertingError notifications_getAppEmailSettings(owner_name, app_name)



Get Email notification settings of user for a particular app

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
api_instance = appcenter_sdk.alertingApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.notifications_getAppEmailSettings(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling alertingApi->notifications_getAppEmailSettings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**AlertingError**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bugTracker_getRepoIssueFromCrash**
> AlertingError bugTracker_getRepoIssueFromCrash(crash_group_id, owner_name, app_name)



Get project issue related to a crash group

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
api_instance = appcenter_sdk.alertingApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | CrashGroup Id
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.bugTracker_getRepoIssueFromCrash(crash_group_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling alertingApi->bugTracker_getRepoIssueFromCrash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| CrashGroup Id | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**AlertingError**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bugtracker_getSettings**
> AlertingError bugtracker_getSettings(owner_name, app_name)



Get bug tracker settings for a particular app

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
api_instance = appcenter_sdk.alertingApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.bugtracker_getSettings(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling alertingApi->bugtracker_getSettings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**AlertingError**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

