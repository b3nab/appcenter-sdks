# appcenter_sdk.crashApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crashes_getAppVersions**](crashApi.md#crashes_getAppVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/versions | Available for UWP apps only.
[**symbols_getStatus**](crashApi.md#symbols_getStatus) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/status | 
[**symbols_getLocation**](crashApi.md#symbols_getLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/location | 
[**symbols_ignore**](crashApi.md#symbols_ignore) | **POST** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/ignore | 
[**symbols_get**](crashApi.md#symbols_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id} | 
[**symbols_list**](crashApi.md#symbols_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols | 
[**symbolUploads_getLocation**](crashApi.md#symbolUploads_getLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id}/location | 
[**symbolUploads_get**](crashApi.md#symbolUploads_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id} | 
[**symbolUploads_complete**](crashApi.md#symbolUploads_complete) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id} | 
[**symbolUploads_delete**](crashApi.md#symbolUploads_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id} | 
[**symbolUploads_list**](crashApi.md#symbolUploads_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads | 
[**symbolUploads_create**](crashApi.md#symbolUploads_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads | 
[**crashes_getHockeyAppCrashForwardingStatus**](crashApi.md#crashes_getHockeyAppCrashForwardingStatus) | **GET** /v0.1/apps/{owner_name}/{app_name}/hockeyapp_crash_forwarding | Gets the state of HockeyApp Crash forwarding for SxS apps
[**crashes_updateHockeyAppCrashForwarding**](crashApi.md#crashes_updateHockeyAppCrashForwarding) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/hockeyapp_crash_forwarding | Enable HockeyApp crash forwarding for SxS apps
[**missingSymbolGroups_info**](crashApi.md#missingSymbolGroups_info) | **GET** /v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups_info | Gets application level statistics for all missing symbol groups
[**missingSymbolGroups_get**](crashApi.md#missingSymbolGroups_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups/{symbol_group_id} | Gets missing symbol crash group by its id
[**missingSymbolGroups_list**](crashApi.md#missingSymbolGroups_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups | Gets top N (ordered by crash count) of crash groups by missing symbol
[**crashes_getAppCrashesInfo**](crashApi.md#crashes_getAppCrashesInfo) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes_info | Available for UWP apps only.
[**crashes_getCrashTextAttachmentContent**](crashApi.md#crashes_getCrashTextAttachmentContent) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments/{attachment_id}/text | Available for UWP apps only.
[**crashes_getCrashAttachmentLocation**](crashApi.md#crashes_getCrashAttachmentLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments/{attachment_id}/location | Available for UWP apps only.
[**crashes_listAttachments**](crashApi.md#crashes_listAttachments) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments | Available for UWP apps only.
[**crashGroups_getStacktrace**](crashApi.md#crashGroups_getStacktrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/stacktrace | Available for UWP apps only.
[**crashes_getStacktrace**](crashApi.md#crashes_getStacktrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/stacktrace | Available for UWP apps only.
[**crashes_getRawCrashLocation**](crashApi.md#crashes_getRawCrashLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/raw/location | Available for UWP apps only.
[**crashes_getNativeCrashDownload**](crashApi.md#crashes_getNativeCrashDownload) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/native/download | Available for UWP apps only.
[**crashes_getNativeCrash**](crashApi.md#crashes_getNativeCrash) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/native | Available for UWP apps only.
[**crashes_get**](crashApi.md#crashes_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id} | Available for UWP apps only.
[**crashes_delete**](crashApi.md#crashes_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id} | Available for UWP apps only.
[**crashes_list**](crashApi.md#crashes_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes | Available for UWP apps only.
[**crashGroups_get**](crashApi.md#crashGroups_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id} | Available for UWP apps only.
[**crashGroups_update**](crashApi.md#crashGroups_update) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id} | Available for UWP apps only.
[**crashGroups_list**](crashApi.md#crashGroups_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups | Available for UWP apps only.

# **crashes_getAppVersions**
> Failure crashes_getAppVersions(owner_name, app_name)

Available for UWP apps only.

Gets a list of application versions. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.crashes_getAppVersions(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_getAppVersions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbols_getStatus**
> Failure symbols_getStatus(symbol_id, owner_name, app_name)



Returns a particular symbol by id (uuid) for the provided application

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
symbol_id = "string" # string | The ID of the symbol (uuid of the symbol)
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.symbols_getStatus(symbol_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbols_getStatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_id** | **string**| The ID of the symbol (uuid of the symbol) | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbols_getLocation**
> Failure symbols_getLocation(symbol_id, owner_name, app_name)



Gets the URL to download the symbol

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
symbol_id = "string" # string | The ID of the symbol (uuid of the symbol)
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.symbols_getLocation(symbol_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbols_getLocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_id** | **string**| The ID of the symbol (uuid of the symbol) | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbols_ignore**
> Failure symbols_ignore(symbol_id, owner_name, app_name)



Marks a symbol by id (uuid) as ignored

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
symbol_id = "string" # string | The ID of the symbol (uuid of the symbol)
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.symbols_ignore(symbol_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbols_ignore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_id** | **string**| The ID of the symbol (uuid of the symbol) | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbols_get**
> Failure symbols_get(symbol_id, owner_name, app_name)



Returns a particular symbol by id (uuid) for the provided application

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
symbol_id = "string" # string | The ID of the symbol (uuid of the symbol)
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.symbols_get(symbol_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbols_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_id** | **string**| The ID of the symbol (uuid of the symbol) | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbols_list**
> Failure symbols_list(owner_name, app_name)



Returns the list of all symbols for the provided application

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.symbols_list(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbols_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbolUploads_getLocation**
> Failure symbolUploads_getLocation(symbol_upload_id, owner_name, app_name)



Gets the URL to download the symbol upload

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
symbol_upload_id = "string" # string | The ID of the symbol upload
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.symbolUploads_getLocation(symbol_upload_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbolUploads_getLocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_upload_id** | **string**| The ID of the symbol upload | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbolUploads_get**
> Failure symbolUploads_get(symbol_upload_id, owner_name, app_name)



Gets a symbol upload by id for the specified application

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
symbol_upload_id = "string" # string | The ID of the symbol upload
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.symbolUploads_get(symbol_upload_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbolUploads_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_upload_id** | **string**| The ID of the symbol upload | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbolUploads_complete**
> Failure symbolUploads_complete(symbol_upload_id, owner_name, app_name, body)



Commits or aborts the symbol upload process for a new set of symbols for the specified application

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
symbol_upload_id = "string" # string | The ID of the symbol upload
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"status":"committed"} # object | The symbol information

try:
    api_response = api_instance.symbolUploads_complete(symbol_upload_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbolUploads_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_upload_id** | **string**| The ID of the symbol upload | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The symbol information | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbolUploads_delete**
> Failure symbolUploads_delete(symbol_upload_id, owner_name, app_name)



Deletes a symbol upload by id for the specified application

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
symbol_upload_id = "string" # string | The ID of the symbol upload
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.symbolUploads_delete(symbol_upload_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbolUploads_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_upload_id** | **string**| The ID of the symbol upload | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbolUploads_list**
> Failure symbolUploads_list(owner_name, app_name, top=top, status=status)



Gets a list of all uploads for the specified application

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
top = 30 # integer | The maximum number of results to return. (optional) (default to )
status = "all" # string | Filter results by the current status of a symbol upload: * all: all states in the symbol upload process. Includes created, aborted, committed, processing, indexed and failed states * uploaded: all states after package is uploaded. Includes committed, processing, indexed and failed states * processed: symbol upload processing is completed. Includes indexed and failed states.
 (optional)

try:
    api_response = api_instance.symbolUploads_list(owner_name, app_name, top=top, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbolUploads_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **top** | **integer**| The maximum number of results to return. | [optional] [default to 30]
 **status** | **string**| Filter results by the current status of a symbol upload: * all: all states in the symbol upload process. Includes created, aborted, committed, processing, indexed and failed states * uploaded: all states after package is uploaded. Includes committed, processing, indexed and failed states * processed: symbol upload processing is completed. Includes indexed and failed states.
 | [optional] 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **symbolUploads_create**
> Failure symbolUploads_create(owner_name, app_name, body)



Begins the symbol upload process for a new set of symbols for the specified application

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"symbol_type":"Apple","client_callback":"string","file_name":"string","build":"string","version":"string"} # object | The symbol information

try:
    api_response = api_instance.symbolUploads_create(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->symbolUploads_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The symbol information | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_getHockeyAppCrashForwardingStatus**
> Failure crashes_getHockeyAppCrashForwardingStatus(owner_name, app_name)

Gets the state of HockeyApp Crash forwarding for SxS apps

Gets the state of HockeyApp Crash forwarding for SxS apps

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.crashes_getHockeyAppCrashForwardingStatus(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_getHockeyAppCrashForwardingStatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_updateHockeyAppCrashForwarding**
> Failure crashes_updateHockeyAppCrashForwarding(owner_name, app_name, body)

Enable HockeyApp crash forwarding for SxS apps

Enable HockeyApp crash forwarding for SxS apps

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"enable_forwarding":true} # object | Enable Forwarding

try:
    # 
    api_response = api_instance.crashes_updateHockeyAppCrashForwarding(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_updateHockeyAppCrashForwarding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Enable Forwarding | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missingSymbolGroups_info**
> v2FailureResponse missingSymbolGroups_info(owner_name, app_name)

Gets application level statistics for all missing symbol groups

Gets application level statistics for all missing symbol groups

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.missingSymbolGroups_info(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->missingSymbolGroups_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**v2FailureResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missingSymbolGroups_get**
> v2FailureResponse missingSymbolGroups_get(symbol_group_id, owner_name, app_name)

Gets missing symbol crash group by its id

Gets missing symbol crash group by its id

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
symbol_group_id = "string" # string | missing symbol crash group id
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.missingSymbolGroups_get(symbol_group_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->missingSymbolGroups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol_group_id** | **string**| missing symbol crash group id | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**v2FailureResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **missingSymbolGroups_list**
> v2FailureResponse missingSymbolGroups_list(top, owner_name, app_name, filter=filter)

Gets top N (ordered by crash count) of crash groups by missing symbol

Gets top N (ordered by crash count) of crash groups by missing symbol

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
top = 0 # integer | top N elements
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
filter = "string" # string | query filter (optional)

try:
    # 
    api_response = api_instance.missingSymbolGroups_list(top, owner_name, app_name, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->missingSymbolGroups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top** | **integer**| top N elements | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **filter** | **string**| query filter | [optional] 

### Return type

[**v2FailureResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_getAppCrashesInfo**
> Failure crashes_getAppCrashesInfo(owner_name, app_name)

Available for UWP apps only.

Gets whether the application has any crashes. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.crashes_getAppCrashesInfo(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_getAppCrashesInfo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_getCrashTextAttachmentContent**
> Failure crashes_getCrashTextAttachmentContent(crash_id, attachment_id, owner_name, app_name)

Available for UWP apps only.

Gets content of the text attachment. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_id = "string" # string | id of a specific crash
attachment_id = "string" # string | attachment id
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.crashes_getCrashTextAttachmentContent(crash_id, attachment_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_getCrashTextAttachmentContent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_id** | **string**| id of a specific crash | 
 **attachment_id** | **string**| attachment id | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_getCrashAttachmentLocation**
> Failure crashes_getCrashAttachmentLocation(crash_id, attachment_id, owner_name, app_name)

Available for UWP apps only.

Gets the URI location to download crash attachment. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_id = "string" # string | id of a specific crash
attachment_id = "string" # string | attachment id
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.crashes_getCrashAttachmentLocation(crash_id, attachment_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_getCrashAttachmentLocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_id** | **string**| id of a specific crash | 
 **attachment_id** | **string**| attachment id | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_listAttachments**
> Failure crashes_listAttachments(crash_id, owner_name, app_name)

Available for UWP apps only.

Gets all attachments for a specific crash. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_id = "string" # string | id of a specific crash
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.crashes_listAttachments(crash_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_listAttachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_id** | **string**| id of a specific crash | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashGroups_getStacktrace**
> Failure crashGroups_getStacktrace(crash_group_id, owner_name, app_name, grouping_only=grouping_only)

Available for UWP apps only.

Gets a stacktrace for a specific crash. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | id of a specific group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
grouping_only = false # boolean | true if the stacktrace should be only the relevant thread / exception. Default is false (optional)

try:
    # 
    api_response = api_instance.crashGroups_getStacktrace(crash_group_id, owner_name, app_name, grouping_only=grouping_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashGroups_getStacktrace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| id of a specific group | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **grouping_only** | **boolean**| true if the stacktrace should be only the relevant thread / exception. Default is false | [optional] 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_getStacktrace**
> Failure crashes_getStacktrace(crash_group_id, crash_id, owner_name, app_name, grouping_only=grouping_only)

Available for UWP apps only.

Gets a stacktrace for a specific crash. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | id of a specific group
crash_id = "string" # string | id of a specific crash
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
grouping_only = false # boolean | true if the stacktrace should be only the relevant thread / exception. Default is false (optional)

try:
    # 
    api_response = api_instance.crashes_getStacktrace(crash_group_id, crash_id, owner_name, app_name, grouping_only=grouping_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_getStacktrace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| id of a specific group | 
 **crash_id** | **string**| id of a specific crash | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **grouping_only** | **boolean**| true if the stacktrace should be only the relevant thread / exception. Default is false | [optional] 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_getRawCrashLocation**
> Failure crashes_getRawCrashLocation(crash_group_id, crash_id, owner_name, app_name)

Available for UWP apps only.

Gets the URI location to download json of a specific crash. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | id of a specific group
crash_id = "string" # string | id of a specific crash
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.crashes_getRawCrashLocation(crash_group_id, crash_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_getRawCrashLocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| id of a specific group | 
 **crash_id** | **string**| id of a specific crash | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_getNativeCrashDownload**
> Failure crashes_getNativeCrashDownload(crash_group_id, crash_id, owner_name, app_name)

Available for UWP apps only.

Gets the native log of a specific crash as a text attachment. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | id of a specific group
crash_id = "string" # string | id of a specific crash
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.crashes_getNativeCrashDownload(crash_group_id, crash_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_getNativeCrashDownload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| id of a specific group | 
 **crash_id** | **string**| id of a specific crash | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_getNativeCrash**
> Failure crashes_getNativeCrash(crash_group_id, crash_id, owner_name, app_name)

Available for UWP apps only.

Gets the native log of a specific crash. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | id of a specific group
crash_id = "string" # string | id of a specific crash
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.crashes_getNativeCrash(crash_group_id, crash_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_getNativeCrash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| id of a specific group | 
 **crash_id** | **string**| id of a specific crash | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_get**
> Failure crashes_get(crash_group_id, crash_id, owner_name, app_name, include_report=include_report, include_log=include_log, include_details=include_details, include_stacktrace=include_stacktrace, grouping_only=grouping_only)

Available for UWP apps only.

Gets a specific crash for an app. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | id of a specific group
crash_id = "string" # string | id of a specific crash
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
include_report = false # boolean | true if the crash should include the raw crash report. Default is false (optional)
include_log = false # boolean | true if the crash should include the custom log report. Default is false (optional)
include_details = false # boolean | true if the crash should include in depth crash details (optional)
include_stacktrace = false # boolean | true if the crash should include the stacktrace information (optional)
grouping_only = false # boolean | true if the stacktrace should be only the relevant thread / exception. Default is false (optional)

try:
    # 
    api_response = api_instance.crashes_get(crash_group_id, crash_id, owner_name, app_name, include_report=include_report, include_log=include_log, include_details=include_details, include_stacktrace=include_stacktrace, grouping_only=grouping_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| id of a specific group | 
 **crash_id** | **string**| id of a specific crash | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **include_report** | **boolean**| true if the crash should include the raw crash report. Default is false | [optional] 
 **include_log** | **boolean**| true if the crash should include the custom log report. Default is false | [optional] 
 **include_details** | **boolean**| true if the crash should include in depth crash details | [optional] 
 **include_stacktrace** | **boolean**| true if the crash should include the stacktrace information | [optional] 
 **grouping_only** | **boolean**| true if the stacktrace should be only the relevant thread / exception. Default is false | [optional] 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_delete**
> Failure crashes_delete(crash_group_id, crash_id, owner_name, app_name, retention_delete=retention_delete)

Available for UWP apps only.

Delete a specific crash and related attachments and blobs for an app. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | id of a specific group
crash_id = "string" # string | id of a specific crash
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
retention_delete = false # boolean | true in that case if the method should skip update counts (optional)

try:
    # 
    api_response = api_instance.crashes_delete(crash_group_id, crash_id, owner_name, app_name, retention_delete=retention_delete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| id of a specific group | 
 **crash_id** | **string**| id of a specific crash | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **retention_delete** | **boolean**| true in that case if the method should skip update counts | [optional] 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashes_list**
> Failure crashes_list(crash_group_id, owner_name, app_name, include_report=include_report, include_log=include_log, date_from=date_from, date_to=date_to, app_version=app_version, error_type=error_type)

Available for UWP apps only.

Gets all crashes of a group. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | id of a specific group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
include_report = false # boolean | true if the crash should include the raw crash report. Default is false (optional)
include_log = false # boolean | true if the crash should include the custom log report. Default is false (optional)
date_from = "2019-05-18T23:47:08Z" # string |  (optional)
date_to = "2019-05-18T23:47:08Z" # string |  (optional)
app_version = "string" # string | version (optional)
error_type = "CrashingErrors" # string |  (optional)

try:
    # 
    api_response = api_instance.crashes_list(crash_group_id, owner_name, app_name, include_report=include_report, include_log=include_log, date_from=date_from, date_to=date_to, app_version=app_version, error_type=error_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| id of a specific group | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **include_report** | **boolean**| true if the crash should include the raw crash report. Default is false | [optional] 
 **include_log** | **boolean**| true if the crash should include the custom log report. Default is false | [optional] 
 **date_from** | **string**|  | [optional] 
 **date_to** | **string**|  | [optional] 
 **app_version** | **string**| version | [optional] 
 **error_type** | **string**|  | [optional] 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashGroups_get**
> Failure crashGroups_get(crash_group_id, owner_name, app_name)

Available for UWP apps only.

Gets a specific group. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | id of a specific group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    # 
    api_response = api_instance.crashGroups_get(crash_group_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashGroups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| id of a specific group | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashGroups_update**
> Failure crashGroups_update(crash_group_id, owner_name, app_name, body)

Available for UWP apps only.

Updates a group. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
crash_group_id = "string" # string | id of a specific group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"status":"open","annotation":"string"} # object | Group change object. All fields are optional and only provided fields will get updated.

try:
    # 
    api_response = api_instance.crashGroups_update(crash_group_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashGroups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crash_group_id** | **string**| id of a specific group | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Group change object. All fields are optional and only provided fields will get updated. | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crashGroups_list**
> Failure crashGroups_list(owner_name, app_name, last_occurrence_from=last_occurrence_from, last_occurrence_to=last_occurrence_to, app_version=app_version, group_type=group_type, group_status=group_status, group_text_search=group_text_search, $orderby=$orderby, continuation_token=continuation_token)

Available for UWP apps only.

Gets a list of crash groups and whether the list contains all available groups. Available for UWP apps only.

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
api_instance = appcenter_sdk.crashApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
last_occurrence_from = "2019-05-18T23:47:08Z" # string | Earliest date when the last time a crash occured in a crash group (optional)
last_occurrence_to = "2019-05-18T23:47:08Z" # string | Latest date when the last time a crash occured in a crash group (optional)
app_version = "string" # string | version (optional)
group_type = "GroupType1" # string |  (optional)
group_status = "open" # string |  (optional)
group_text_search = "string" # string | A freetext search that matches in crash, crash types, crash stack_traces and crash user (optional)
$orderby = "last_occurrence desc" # string | the OData-like $orderby argument (optional) (default to )
continuation_token = "string" # string | Cassandra request continuation token. The token is used for pagination. (optional)

try:
    # 
    api_response = api_instance.crashGroups_list(owner_name, app_name, last_occurrence_from=last_occurrence_from, last_occurrence_to=last_occurrence_to, app_version=app_version, group_type=group_type, group_status=group_status, group_text_search=group_text_search, $orderby=$orderby, continuation_token=continuation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling crashApi->crashGroups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **last_occurrence_from** | **string**| Earliest date when the last time a crash occured in a crash group | [optional] 
 **last_occurrence_to** | **string**| Latest date when the last time a crash occured in a crash group | [optional] 
 **app_version** | **string**| version | [optional] 
 **group_type** | **string**|  | [optional] 
 **group_status** | **string**|  | [optional] 
 **group_text_search** | **string**| A freetext search that matches in crash, crash types, crash stack_traces and crash user | [optional] 
 **$orderby** | **string**| the OData-like $orderby argument | [optional] [default to last_occurrence desc]
 **continuation_token** | **string**| Cassandra request continuation token. The token is used for pagination. | [optional] 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

