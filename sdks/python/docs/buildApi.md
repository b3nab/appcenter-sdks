# appcenter_sdk.buildApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**builds_webhook**](buildApi.md#builds_webhook) | **POST** /v0.1/public/hooks | 
[**builds_listXcodeVersions**](buildApi.md#builds_listXcodeVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/xcode_versions | 
[**builds_listXamarinSDKBundles**](buildApi.md#builds_listXamarinSDKBundles) | **GET** /v0.1/apps/{owner_name}/{app_name}/xamarin_sdk_bundles | 
[**repositories_list**](buildApi.md#repositories_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/source_hosts/{source_host}/repositories | 
[**repositoryConfigurations_list**](buildApi.md#repositoryConfigurations_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/repo_config | 
[**repositoryConfigurations_createOrUpdate**](buildApi.md#repositoryConfigurations_createOrUpdate) | **POST** /v0.1/apps/{owner_name}/{app_name}/repo_config | 
[**repositoryConfigurations_delete**](buildApi.md#repositoryConfigurations_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/repo_config | 
[**fileAssets_create**](buildApi.md#fileAssets_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/file_asset | 
[**commits_listByShaList**](buildApi.md#commits_listByShaList) | **GET** /v0.1/apps/{owner_name}/{app_name}/commits/batch | 
[**builds_getLog**](buildApi.md#builds_getLog) | **GET** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/logs | 
[**builds_getDownloadUri**](buildApi.md#builds_getDownloadUri) | **GET** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/downloads/{download_type} | 
[**builds_distribute**](buildApi.md#builds_distribute) | **POST** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/distribute | 
[**builds_get**](buildApi.md#builds_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id} | 
[**builds_update**](buildApi.md#builds_update) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id} | 
[**builds_getStatusByAppId**](buildApi.md#builds_getStatusByAppId) | **GET** /v0.1/apps/{owner_name}/{app_name}/build_service_status | 
[**builds_listToolsetProjects**](buildApi.md#builds_listToolsetProjects) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/toolset_projects | 
[**branchConfigurations_get**](buildApi.md#branchConfigurations_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config | 
[**branchConfigurations_create**](buildApi.md#branchConfigurations_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config | 
[**branchConfigurations_update**](buildApi.md#branchConfigurations_update) | **PUT** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config | 
[**branchConfigurations_delete**](buildApi.md#branchConfigurations_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config | 
[**builds_listByBranch**](buildApi.md#builds_listByBranch) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/builds | 
[**builds_create**](buildApi.md#builds_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/builds | 
[**builds_listBranches**](buildApi.md#builds_listBranches) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches | 

# **builds_webhook**
> ValidationErrorResponse builds_webhook()



Public webhook sink

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.builds_webhook()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_webhook: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ValidationErrorResponse**](.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_listXcodeVersions**
> ValidationErrorResponse builds_listXcodeVersions(owner_name, app_name)



Gets the Xcode versions available to this app

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.builds_listXcodeVersions(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_listXcodeVersions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ValidationErrorResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_listXamarinSDKBundles**
> ValidationErrorResponse builds_listXamarinSDKBundles(owner_name, app_name)



Gets the Xamarin SDK bundles available to this app

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.builds_listXamarinSDKBundles(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_listXamarinSDKBundles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ValidationErrorResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_list**
> ValidationErrorResponse repositories_list(source_host, owner_name, app_name, vstsAccountName=vstsAccountName, vstsProjectId=vstsProjectId, form=form)



Gets the repositories available from the source code host

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
source_host = "github" # string | The source host
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
vstsAccountName = "string" # string | Filter repositories only for specified account and project, "vstsProjectId" is required (optional)
vstsProjectId = "string" # string | Filter repositories only for specified account and project, "vstsAccountName" is required (optional)
form = "lite" # string | The selected form of the object (optional)

try:
    api_response = api_instance.repositories_list(source_host, owner_name, app_name, vstsAccountName=vstsAccountName, vstsProjectId=vstsProjectId, form=form)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->repositories_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_host** | **string**| The source host | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **vstsAccountName** | **string**| Filter repositories only for specified account and project, &quot;vstsProjectId&quot; is required | [optional] 
 **vstsProjectId** | **string**| Filter repositories only for specified account and project, &quot;vstsAccountName&quot; is required | [optional] 
 **form** | **string**| The selected form of the object | [optional] 

### Return type

[**ValidationErrorResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositoryConfigurations_list**
> ValidationErrorResponse repositoryConfigurations_list(owner_name, app_name, includeInactive=includeInactive)



Returns the repository build configuration status of the app

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
includeInactive = true # boolean | Include inactive configurations if none are active (optional)

try:
    api_response = api_instance.repositoryConfigurations_list(owner_name, app_name, includeInactive=includeInactive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->repositoryConfigurations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **includeInactive** | **boolean**| Include inactive configurations if none are active | [optional] 

### Return type

[**ValidationErrorResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositoryConfigurations_createOrUpdate**
> ValidationErrorResponse repositoryConfigurations_createOrUpdate(owner_name, app_name, body)



Configures the repository for build

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"repo_url":"string"} # object | The repository information

try:
    api_response = api_instance.repositoryConfigurations_createOrUpdate(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->repositoryConfigurations_createOrUpdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The repository information | 

### Return type

[**ValidationErrorResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositoryConfigurations_delete**
> ValidationErrorResponse repositoryConfigurations_delete(owner_name, app_name)



Removes the configuration for the respository

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.repositoryConfigurations_delete(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->repositoryConfigurations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ValidationErrorResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fileAssets_create**
> ValidationErrorResponse fileAssets_create(owner_name, app_name)



Create a new asset to upload a file

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.fileAssets_create(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->fileAssets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ValidationErrorResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commits_listByShaList**
> CommitDetailsList commits_listByShaList(hashes, owner_name, app_name)



Returns commit information for a batch of shas

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
hashes = ["string"] # array | A collection of commit SHAs comma-delimited
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.commits_listByShaList(hashes, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->commits_listByShaList: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hashes** | **array**| A collection of commit SHAs comma-delimited | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**CommitDetailsList**](array.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_getLog**
> BuildLog builds_getLog(build_id, owner_name, app_name)



Get the build log

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
build_id = 0 # integer | The build ID
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.builds_getLog(build_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_getLog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **integer**| The build ID | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**BuildLog**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_getDownloadUri**
> DownloadContainer builds_getDownloadUri(build_id, download_type, owner_name, app_name)



Gets the download URI

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
build_id = 0 # integer | The build ID
download_type = "build" # string | The download type
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.builds_getDownloadUri(build_id, download_type, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_getDownloadUri: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **integer**| The build ID | 
 **download_type** | **string**| The download type | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**DownloadContainer**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_distribute**
> DistributionResponse builds_distribute(build_id, owner_name, app_name, body)



Distribute a build

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
build_id = 0 # integer | The build ID
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"destinations":[{"id":"string","type":"store"}],"releaseNotes":"string","mandatoryUpdate":true,"notifyTesters":true} # object | The distribution details

try:
    api_response = api_instance.builds_distribute(build_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_distribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **integer**| The build ID | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The distribution details | 

### Return type

[**DistributionResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_get**
> Build builds_get(build_id, owner_name, app_name)



Returns the build detail for the given build ID

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
build_id = 0 # integer | The build ID
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.builds_get(build_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **integer**| The build ID | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Build**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_update**
> Build builds_update(build_id, owner_name, app_name, body)



Cancels a build

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
build_id = 0 # integer | The build ID
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"status":"cancelling"} # object | 

try:
    api_response = api_instance.builds_update(build_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **integer**| The build ID | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | 

### Return type

[**Build**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_getStatusByAppId**
> BuildServiceStatus builds_getStatusByAppId(owner_name, app_name)



Application specific build service status

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.builds_getStatusByAppId(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_getStatusByAppId: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**BuildServiceStatus**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_listToolsetProjects**
> ToolsetProjects builds_listToolsetProjects(branch, os, platform, owner_name, app_name)



Returns the projects in the repository for the branch, for all toolsets

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
branch = "string" # string | The branch name
os = "iOS" # string | The desired OS for the project scan; normally the same as the app OS
platform = "Objective-C-Swift" # string | The desired platform for the project scan
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.builds_listToolsetProjects(branch, os, platform, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_listToolsetProjects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **string**| The branch name | 
 **os** | **string**| The desired OS for the project scan; normally the same as the app OS | 
 **platform** | **string**| The desired platform for the project scan | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ToolsetProjects**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **branchConfigurations_get**
> ValidationErrorResponse branchConfigurations_get(branch, owner_name, app_name)



Gets the branch configuration

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
branch = "string" # string | The branch name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.branchConfigurations_get(branch, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->branchConfigurations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **string**| The branch name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ValidationErrorResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **branchConfigurations_create**
> BranchConfiguration branchConfigurations_create(branch, owner_name, app_name)



Configures the branch for build

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
branch = "string" # string | The branch name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.branchConfigurations_create(branch, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->branchConfigurations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **string**| The branch name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**BranchConfiguration**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **branchConfigurations_update**
> BranchConfiguration branchConfigurations_update(branch, owner_name, app_name)



Reconfigures the branch for build

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
branch = "string" # string | The branch name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.branchConfigurations_update(branch, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->branchConfigurations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **string**| The branch name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**BranchConfiguration**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **branchConfigurations_delete**
> SuccessResponse branchConfigurations_delete(branch, owner_name, app_name)



Deletes the branch build configuration

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
branch = "string" # string | The branch name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.branchConfigurations_delete(branch, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->branchConfigurations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **string**| The branch name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**SuccessResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_listByBranch**
> Builds builds_listByBranch(branch, owner_name, app_name)



Returns the list of builds for the branch

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
branch = "string" # string | The branch name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.builds_listByBranch(branch, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_listByBranch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **string**| The branch name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Builds**](array.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_create**
> Build builds_create(branch, owner_name, app_name, body=body)



Create a build

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
branch = "string" # string | The branch name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"sourceVersion":"1d71331f19e6830dbf99aa2c53cb264e4a490bab","debug":true} # object | Parameters of the build (optional)

try:
    api_response = api_instance.builds_create(branch, owner_name, app_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **string**| The branch name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Parameters of the build | [optional] 

### Return type

[**Build**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **builds_listBranches**
> ValidationErrorResponse builds_listBranches(owner_name, app_name)



Returns the list of Git branches for this application

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
api_instance = appcenter_sdk.buildApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.builds_listBranches(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling buildApi->builds_listBranches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ValidationErrorResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

