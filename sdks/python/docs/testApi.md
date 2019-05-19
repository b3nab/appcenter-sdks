# appcenter_sdk.testApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_getDeviceSetOfUser**](testApi.md#test_getDeviceSetOfUser) | **GET** /v0.1/apps/{owner_name}/{app_name}/user/device_sets/{id} | 
[**test_updateDeviceSetOfUser**](testApi.md#test_updateDeviceSetOfUser) | **PUT** /v0.1/apps/{owner_name}/{app_name}/user/device_sets/{id} | 
[**test_deleteDeviceSetOfUser**](testApi.md#test_deleteDeviceSetOfUser) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/user/device_sets/{id} | 
[**test_listDeviceSetsOfUser**](testApi.md#test_listDeviceSetsOfUser) | **GET** /v0.1/apps/{owner_name}/{app_name}/user/device_sets | 
[**test_createDeviceSetOfUser**](testApi.md#test_createDeviceSetOfUser) | **POST** /v0.1/apps/{owner_name}/{app_name}/user/device_sets | 
[**test_getAllTestRunsForSeries**](testApi.md#test_getAllTestRunsForSeries) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_series/{test_series_slug}/test_runs | 
[**test_deleteTestSeries**](testApi.md#test_deleteTestSeries) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/test_series/{test_series_slug} | 
[**test_patchTestSeries**](testApi.md#test_patchTestSeries) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/test_series/{test_series_slug} | 
[**test_getAllTestSeries**](testApi.md#test_getAllTestSeries) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_series | 
[**test_createTestSeries**](testApi.md#test_createTestSeries) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_series | 
[**test_stopTestRun**](testApi.md#test_stopTestRun) | **PUT** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/stop | 
[**test_getTestRunState**](testApi.md#test_getTestRunState) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/state | 
[**test_startTestRun**](testApi.md#test_startTestRun) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/start | 
[**test_getTestReport**](testApi.md#test_getTestReport) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/report | 
[**test_uploadHashesBatch**](testApi.md#test_uploadHashesBatch) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/hashes/batch | 
[**test_uploadHash**](testApi.md#test_uploadHash) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/hashes | 
[**test_startUploadingFile**](testApi.md#test_startUploadingFile) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id}/files | 
[**test_getTestRun**](testApi.md#test_getTestRun) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id} | 
[**test_archiveTestRun**](testApi.md#test_archiveTestRun) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/test_runs/{test_run_id} | 
[**test_getTestRuns**](testApi.md#test_getTestRuns) | **GET** /v0.1/apps/{owner_name}/{app_name}/test_runs | 
[**test_createTestRun**](testApi.md#test_createTestRun) | **POST** /v0.1/apps/{owner_name}/{app_name}/test_runs | 
[**test_gdprExportTestRun**](testApi.md#test_gdprExportTestRun) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export/testRuns | 
[**test_gdprExportPipelineTest**](testApi.md#test_gdprExportPipelineTest) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export/pipelineTests | 
[**test_gdprExportHashFile**](testApi.md#test_gdprExportHashFile) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export/hashFiles | 
[**test_gdprExportFileSetFile**](testApi.md#test_gdprExportFileSetFile) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export/fileSetFiles | 
[**test_gdprExportApp**](testApi.md#test_gdprExportApp) | **GET** /v0.1/apps/{owner_name}/{app_name}/test/export | 
[**test_getSubscriptions**](testApi.md#test_getSubscriptions) | **GET** /v0.1/apps/{owner_name}/{app_name}/subscriptions | 
[**test_createSubscription**](testApi.md#test_createSubscription) | **POST** /v0.1/apps/{owner_name}/{app_name}/subscriptions | 
[**test_getDeviceSetOfOwner**](testApi.md#test_getDeviceSetOfOwner) | **GET** /v0.1/apps/{owner_name}/{app_name}/owner/device_sets/{id} | 
[**test_updateDeviceSetOfOwner**](testApi.md#test_updateDeviceSetOfOwner) | **PUT** /v0.1/apps/{owner_name}/{app_name}/owner/device_sets/{id} | 
[**test_deleteDeviceSetOfOwner**](testApi.md#test_deleteDeviceSetOfOwner) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/owner/device_sets/{id} | 
[**test_listDeviceSetsOfOwner**](testApi.md#test_listDeviceSetsOfOwner) | **GET** /v0.1/apps/{owner_name}/{app_name}/owner/device_sets | 
[**test_createDeviceSetOfOwner**](testApi.md#test_createDeviceSetOfOwner) | **POST** /v0.1/apps/{owner_name}/{app_name}/owner/device_sets | 
[**test_createDeviceSelection**](testApi.md#test_createDeviceSelection) | **POST** /v0.1/apps/{owner_name}/{app_name}/device_selection | 
[**test_getDeviceConfigurations**](testApi.md#test_getDeviceConfigurations) | **GET** /v0.1/apps/{owner_name}/{app_name}/device_configurations | 
[**test_gdprExportUser**](testApi.md#test_gdprExportUser) | **GET** /v0.1/account/test/export/users | 
[**test_gdprExportFeatureFlag**](testApi.md#test_gdprExportFeatureFlag) | **GET** /v0.1/account/test/export/featureFlags | 
[**test_gdprExportAccount**](testApi.md#test_gdprExportAccount) | **GET** /v0.1/account/test/export/accounts | 
[**test_gdprExport**](testApi.md#test_gdprExport) | **GET** /v0.1/account/test/export | 

# **test_getDeviceSetOfUser**
> DeviceSet test_getDeviceSetOfUser(id, owner_name, app_name)



Gets a device set belonging to the user

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
id = "string" # string | The UUID of the device set
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_getDeviceSetOfUser(id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_getDeviceSetOfUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string**| The UUID of the device set | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**DeviceSet**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_updateDeviceSetOfUser**
> TestCloudErrorDetails test_updateDeviceSetOfUser(id, owner_name, app_name, body)



Updates a device set belonging to the user

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
id = "string" # string | The UUID of the device set
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"devices":["string"],"name":"string"} # object | 

try:
    api_response = api_instance.test_updateDeviceSetOfUser(id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_updateDeviceSetOfUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string**| The UUID of the device set | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | 

### Return type

[**TestCloudErrorDetails**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_deleteDeviceSetOfUser**
> test_deleteDeviceSetOfUser(id, owner_name, app_name)



Deletes a device set belonging to the user

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
id = "string" # string | The UUID of the device set
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_instance.test_deleteDeviceSetOfUser(id, owner_name, app_name)
except ApiException as e:
    print("Exception when calling testApi->test_deleteDeviceSetOfUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string**| The UUID of the device set | 
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

# **test_listDeviceSetsOfUser**
> array test_listDeviceSetsOfUser(owner_name, app_name)



Lists device sets belonging to the user

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_listDeviceSetsOfUser(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_listDeviceSetsOfUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_createDeviceSetOfUser**
> TestCloudErrorDetails test_createDeviceSetOfUser(owner_name, app_name, body)



Creates a device set belonging to the user

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"devices":["string"],"name":"string"} # object | 

try:
    api_response = api_instance.test_createDeviceSetOfUser(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_createDeviceSetOfUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | 

### Return type

[**TestCloudErrorDetails**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_getAllTestRunsForSeries**
> array test_getAllTestRunsForSeries(test_series_slug, owner_name, app_name)



Returns list of all test runs for a given test series

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_series_slug = "string" # string | The slug of the test series
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_getAllTestRunsForSeries(test_series_slug, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_getAllTestRunsForSeries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_series_slug** | **string**| The slug of the test series | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_deleteTestSeries**
> test_deleteTestSeries(test_series_slug, owner_name, app_name)



Deletes a single test series

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_series_slug = "string" # string | The slug of the test series
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_instance.test_deleteTestSeries(test_series_slug, owner_name, app_name)
except ApiException as e:
    print("Exception when calling testApi->test_deleteTestSeries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_series_slug** | **string**| The slug of the test series | 
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

# **test_patchTestSeries**
> TestSeries test_patchTestSeries(test_series_slug, owner_name, app_name, body)



Updates name and slug of a test series

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_series_slug = "string" # string | The slug of the test series
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"name":"string"} # object | 

try:
    api_response = api_instance.test_patchTestSeries(test_series_slug, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_patchTestSeries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_series_slug** | **string**| The slug of the test series | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | 

### Return type

[**TestSeries**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_getAllTestSeries**
> array test_getAllTestSeries(owner_name, app_name, query=query)



Returns list of all test series for an application

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
query = "string" # string | A query string to filter test series (optional)

try:
    api_response = api_instance.test_getAllTestSeries(owner_name, app_name, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_getAllTestSeries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **query** | **string**| A query string to filter test series | [optional] 

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_createTestSeries**
> TestCloudErrorDetails test_createTestSeries(owner_name, app_name, body)



Creates new test series for an application

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"name":"string"} # object | 

try:
    api_response = api_instance.test_createTestSeries(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_createTestSeries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | 

### Return type

[**TestCloudErrorDetails**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_stopTestRun**
> TestRun test_stopTestRun(test_run_id, owner_name, app_name)



Stop a test run execution

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_run_id = "string" # string | The ID of the test run to be stopped
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_stopTestRun(test_run_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_stopTestRun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **string**| The ID of the test run to be stopped | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**TestRun**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_getTestRunState**
> TestRunState test_getTestRunState(test_run_id, owner_name, app_name)



Gets state of the test run

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_run_id = "string" # string | The ID of the test run
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_getTestRunState(test_run_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_getTestRunState: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **string**| The ID of the test run | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**TestRunState**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_startTestRun**
> TestCloudStartTestRunResult test_startTestRun(test_run_id, owner_name, app_name, body)



Starts test run

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_run_id = "string" # string | The ID of the test run
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"test_framework":"string","device_selection":"string","language":"string","locale":"string","test_series":"string","test_parameters":{}} # object | Option required to start the test run

try:
    api_response = api_instance.test_startTestRun(test_run_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_startTestRun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **string**| The ID of the test run | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Option required to start the test run | 

### Return type

[**TestCloudStartTestRunResult**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_getTestReport**
> TestReport test_getTestReport(test_run_id, owner_name, app_name)



Returns a single test report

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_run_id = "string" # string | The ID of the test run
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_getTestReport(test_run_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_getTestReport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **string**| The ID of the test run | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**TestReport**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_uploadHashesBatch**
> array test_uploadHashesBatch(test_run_id, owner_name, app_name, body)



Adds file with the given hash to a test run

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_run_id = "string" # string | The ID of the test run
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = [{"fileType":"dsym-file","checksum":"string","relativePath":"string"}] # array | File hash information

try:
    api_response = api_instance.test_uploadHashesBatch(test_run_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_uploadHashesBatch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **string**| The ID of the test run | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**array**](object.md)| File hash information | 

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_uploadHash**
> test_uploadHash(test_run_id, owner_name, app_name, body)



Adds file with the given hash to a test run

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_run_id = "string" # string | The ID of the test run
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"file_type":"dsym-file","checksum":"string","relative_path":"string","byte_range":"string"} # object | File hash information

try:
    api_instance.test_uploadHash(test_run_id, owner_name, app_name, body)
except ApiException as e:
    print("Exception when calling testApi->test_uploadHash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **string**| The ID of the test run | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| File hash information | 

### Return type

void (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_startUploadingFile**
> test_startUploadingFile(test_run_id, owner_name, app_name)



Uploads file for a test run

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_run_id = "string" # string | The ID of the test run
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_instance.test_startUploadingFile(test_run_id, owner_name, app_name)
except ApiException as e:
    print("Exception when calling testApi->test_startUploadingFile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **string**| The ID of the test run | 
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

# **test_getTestRun**
> TestRun test_getTestRun(test_run_id, owner_name, app_name)



Returns a single test runs

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_run_id = "string" # string | The ID of the test run
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_getTestRun(test_run_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_getTestRun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **string**| The ID of the test run | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**TestRun**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_archiveTestRun**
> TestRun test_archiveTestRun(test_run_id, owner_name, app_name)



Logically deletes a test run

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
test_run_id = "string" # string | The ID of the test run
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_archiveTestRun(test_run_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_archiveTestRun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_id** | **string**| The ID of the test run | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**TestRun**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_getTestRuns**
> array test_getTestRuns(owner_name, app_name)



Returns a list of test runs

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_getTestRuns(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_getTestRuns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_createTestRun**
> test_createTestRun(owner_name, app_name)



Creates a new test run

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_instance.test_createTestRun(owner_name, app_name)
except ApiException as e:
    print("Exception when calling testApi->test_createTestRun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **test_gdprExportTestRun**
> TestGDPRTestRun test_gdprExportTestRun(owner_name, app_name)



Lists test run data

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_gdprExportTestRun(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_gdprExportTestRun: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**TestGDPRTestRun**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_gdprExportPipelineTest**
> TestGDPRPipelineTest test_gdprExportPipelineTest(owner_name, app_name)



Lists pipeline test data

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_gdprExportPipelineTest(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_gdprExportPipelineTest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**TestGDPRPipelineTest**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_gdprExportHashFile**
> TestGDPRHashFile test_gdprExportHashFile(owner_name, app_name)



Lists hash file data

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_gdprExportHashFile(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_gdprExportHashFile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**TestGDPRHashFile**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_gdprExportFileSetFile**
> TestGDPRFileSetFile test_gdprExportFileSetFile(owner_name, app_name)



Lists file set file data

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_gdprExportFileSetFile(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_gdprExportFileSetFile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**TestGDPRFileSetFile**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_gdprExportApp**
> TestGDPRResourceList test_gdprExportApp(owner_name, app_name)



Lists all the endpoints available for Test app data

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_gdprExportApp(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_gdprExportApp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**TestGDPRResourceList**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_getSubscriptions**
> Subscription test_getSubscriptions(owner_name, app_name)



Get information about the currently active subscriptions, if any

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_getSubscriptions(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_getSubscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Subscription**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_createSubscription**
> Subscription test_createSubscription(owner_name, app_name)



Accept a free trial subscription

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_createSubscription(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_createSubscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Subscription**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_getDeviceSetOfOwner**
> DeviceSet test_getDeviceSetOfOwner(id, owner_name, app_name)



Gets a device set belonging to the owner

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
id = "string" # string | The UUID of the device set
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_getDeviceSetOfOwner(id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_getDeviceSetOfOwner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string**| The UUID of the device set | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**DeviceSet**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_updateDeviceSetOfOwner**
> TestCloudErrorDetails test_updateDeviceSetOfOwner(id, owner_name, app_name, body)



Updates a device set belonging to the owner

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
id = "string" # string | The UUID of the device set
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"devices":["string"],"name":"string"} # object | 

try:
    api_response = api_instance.test_updateDeviceSetOfOwner(id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_updateDeviceSetOfOwner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string**| The UUID of the device set | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | 

### Return type

[**TestCloudErrorDetails**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_deleteDeviceSetOfOwner**
> test_deleteDeviceSetOfOwner(id, owner_name, app_name)



Deletes a device set belonging to the owner

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
id = "string" # string | The UUID of the device set
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_instance.test_deleteDeviceSetOfOwner(id, owner_name, app_name)
except ApiException as e:
    print("Exception when calling testApi->test_deleteDeviceSetOfOwner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string**| The UUID of the device set | 
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

# **test_listDeviceSetsOfOwner**
> array test_listDeviceSetsOfOwner(owner_name, app_name)



Lists device sets belonging to the owner

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.test_listDeviceSetsOfOwner(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_listDeviceSetsOfOwner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_createDeviceSetOfOwner**
> TestCloudErrorDetails test_createDeviceSetOfOwner(owner_name, app_name, body)



Creates a device set belonging to the owner

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"devices":["string"],"name":"string"} # object | 

try:
    api_response = api_instance.test_createDeviceSetOfOwner(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_createDeviceSetOfOwner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | 

### Return type

[**TestCloudErrorDetails**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_createDeviceSelection**
> TestCloudErrorDetails test_createDeviceSelection(owner_name, app_name, body)



Creates a short ID for a list of devices

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"devices":["string"]} # object | 

try:
    api_response = api_instance.test_createDeviceSelection(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_createDeviceSelection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | 

### Return type

[**TestCloudErrorDetails**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_getDeviceConfigurations**
> array test_getDeviceConfigurations(owner_name, app_name, app_upload_id=app_upload_id)



Returns a list of available devices

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
app_upload_id = "string" # string | The ID of the test run (optional)

try:
    api_response = api_instance.test_getDeviceConfigurations(owner_name, app_name, app_upload_id=app_upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_getDeviceConfigurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **app_upload_id** | **string**| The ID of the test run | [optional] 

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_gdprExportUser**
> TestGDPRUser test_gdprExportUser()



Lists user data

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.test_gdprExportUser()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_gdprExportUser: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TestGDPRUser**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_gdprExportFeatureFlag**
> TestGDPRFeatureFlag test_gdprExportFeatureFlag()



Lists feature flag data

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.test_gdprExportFeatureFlag()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_gdprExportFeatureFlag: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TestGDPRFeatureFlag**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_gdprExportAccount**
> TestGDPRAccount test_gdprExportAccount()



Lists account data

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.test_gdprExportAccount()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_gdprExportAccount: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TestGDPRAccount**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_gdprExport**
> TestGDPRResourceList test_gdprExport()



Lists all the endpoints available for Test account data

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
api_instance = appcenter_sdk.testApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.test_gdprExport()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling testApi->test_gdprExport: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TestGDPRResourceList**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

