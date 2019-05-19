# appcenter_sdk.codepushApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**codePushAcquisition_updateCheck**](codepushApi.md#codePushAcquisition_updateCheck) | **GET** /v0.1/public/codepush/update_check | 
[**codePushAcquisition_getAcquisitionStatus**](codepushApi.md#codePushAcquisition_getAcquisitionStatus) | **GET** /v0.1/public/codepush/status | 
[**codePushAcquisition_updateDownloadStatus**](codepushApi.md#codePushAcquisition_updateDownloadStatus) | **POST** /v0.1/public/codepush/report_status/download | 
[**codePushAcquisition_updateDeployStatus**](codepushApi.md#codePushAcquisition_updateDeployStatus) | **POST** /v0.1/public/codepush/report_status/deploy | 
[**codePushDeploymentRelease_rollback**](codepushApi.md#codePushDeploymentRelease_rollback) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/rollback_release | 
[**deploymentReleases_update**](codepushApi.md#deploymentReleases_update) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases/{release_label} | 
[**codePushDeploymentReleases_delete**](codepushApi.md#codePushDeploymentReleases_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases | 
[**codePushDeploymentReleases_get**](codepushApi.md#codePushDeploymentReleases_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases | 
[**codePushDeploymentReleases_create**](codepushApi.md#codePushDeploymentReleases_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases | 
[**codePushDeployments_promote**](codepushApi.md#codePushDeployments_promote) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/promote_release/{promote_deployment_name} | 
[**codePushDeploymentMetrics_get**](codepushApi.md#codePushDeploymentMetrics_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/metrics | 
[**codePushDeployments_delete**](codepushApi.md#codePushDeployments_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name} | 
[**codePushDeployments_get**](codepushApi.md#codePushDeployments_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name} | 
[**codePushDeployments_update**](codepushApi.md#codePushDeployments_update) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name} | 
[**codePushDeployments_list**](codepushApi.md#codePushDeployments_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments | 
[**codePushDeployments_create**](codepushApi.md#codePushDeployments_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments | 

# **codePushAcquisition_updateCheck**
> Failure codePushAcquisition_updateCheck(deployment_key, app_version, package_hash=package_hash, label=label, client_unique_id=client_unique_id, is_companion=is_companion, previous_label_or_app_version=previous_label_or_app_version, previous_deployment_key=previous_deployment_key)



Check for updates

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_key = "string" # string | 
app_version = "string" # string | 
package_hash = "string" # string |  (optional)
label = "string" # string |  (optional)
client_unique_id = "string" # string |  (optional)
is_companion = true # boolean |  (optional)
previous_label_or_app_version = "string" # string |  (optional)
previous_deployment_key = "string" # string |  (optional)

try:
    api_response = api_instance.codePushAcquisition_updateCheck(deployment_key, app_version, package_hash=package_hash, label=label, client_unique_id=client_unique_id, is_companion=is_companion, previous_label_or_app_version=previous_label_or_app_version, previous_deployment_key=previous_deployment_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushAcquisition_updateCheck: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_key** | **string**|  | 
 **app_version** | **string**|  | 
 **package_hash** | **string**|  | [optional] 
 **label** | **string**|  | [optional] 
 **client_unique_id** | **string**|  | [optional] 
 **is_companion** | **boolean**|  | [optional] 
 **previous_label_or_app_version** | **string**|  | [optional] 
 **previous_deployment_key** | **string**|  | [optional] 

### Return type

[**Failure**](.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codePushAcquisition_getAcquisitionStatus**
> Failure codePushAcquisition_getAcquisitionStatus()



Returns the acquisition service status to the caller

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.codePushAcquisition_getAcquisitionStatus()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushAcquisition_getAcquisitionStatus: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Failure**](.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codePushAcquisition_updateDownloadStatus**
> Failure codePushAcquisition_updateDownloadStatus(body)



Report download of specified release

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
body = {"deployment_key":"string","label":"string","app_version":"string","previous_deployment_key":"string","previous_label_or_app_version":"string","status":"string","client_unique_id":"string"} # object | Deployment status metric properties

try:
    api_response = api_instance.codePushAcquisition_updateDownloadStatus(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushAcquisition_updateDownloadStatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Deployment status metric properties | 

### Return type

[**Failure**](.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codePushAcquisition_updateDeployStatus**
> Failure codePushAcquisition_updateDeployStatus(body)



Report Deployment status metric

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
body = {"deployment_key":"string","label":"string","app_version":"string","previous_deployment_key":"string","previous_label_or_app_version":"string","status":"string","client_unique_id":"string"} # object | Deployment status metric properties

try:
    api_response = api_instance.codePushAcquisition_updateDeployStatus(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushAcquisition_updateDeployStatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Deployment status metric properties | 

### Return type

[**Failure**](.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codePushDeploymentRelease_rollback**
> Failure codePushDeploymentRelease_rollback(deployment_name, owner_name, app_name, body=body)



Rollback the latest or a specific release for an app deployment

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_name = "string" # string | deployment name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"label":"string"} # object | The specific release label that you want to rollback to (optional)

try:
    api_response = api_instance.codePushDeploymentRelease_rollback(deployment_name, owner_name, app_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeploymentRelease_rollback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_name** | **string**| deployment name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The specific release label that you want to rollback to | [optional] 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploymentReleases_update**
> Failure deploymentReleases_update(deployment_name, release_label, owner_name, app_name, body)



Modifies a CodePush release metadata under the given Deployment

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_name = "string" # string | deployment name
release_label = "string" # string | release label
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"target_binary_range":"string","description":"string","is_disabled":true,"is_mandatory":true,"rollout":1} # object | Release modification. All fields are optional and only provided fields will get updated.

try:
    api_response = api_instance.deploymentReleases_update(deployment_name, release_label, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->deploymentReleases_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_name** | **string**| deployment name | 
 **release_label** | **string**| release label | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Release modification. All fields are optional and only provided fields will get updated. | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codePushDeploymentReleases_delete**
> Failure codePushDeploymentReleases_delete(deployment_name, owner_name, app_name)



Clears a Deployment of releases

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_name = "string" # string | deployment name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.codePushDeploymentReleases_delete(deployment_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeploymentReleases_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_name** | **string**| deployment name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codePushDeploymentReleases_get**
> Failure codePushDeploymentReleases_get(deployment_name, owner_name, app_name)



Gets the history of releases on a Deployment

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_name = "string" # string | deployment name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.codePushDeploymentReleases_get(deployment_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeploymentReleases_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_name** | **string**| deployment name | 
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

# **codePushDeploymentReleases_create**
> Failure codePushDeploymentReleases_create(deployment_name, owner_name, app_name, body=body)



Create a new CodePush release for the specified deployment

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_name = "string" # string | deployment name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"package":"string","targetBinaryVersion":"string","deploymentName":"string","description":"string","disabled":true,"mandatory":true,"noDuplicateReleaseError":true,"rollout":0} # object |  (optional)

try:
    api_response = api_instance.codePushDeploymentReleases_create(deployment_name, owner_name, app_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeploymentReleases_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_name** | **string**| deployment name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codePushDeployments_promote**
> Failure codePushDeployments_promote(deployment_name, promote_deployment_name, owner_name, app_name, body=body)



Promote one release (default latest one) from one deployment to another

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_name = "string" # string | deployment name
promote_deployment_name = "string" # string | deployment name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"target_binary_range":"string","description":"string","is_disabled":true,"is_mandatory":true,"rollout":1,"label":"string"} # object | Release to be promoted, only needs to provide optional fields, description, label, disabled, mandatory, rollout, targetBinaryVersion (optional)

try:
    api_response = api_instance.codePushDeployments_promote(deployment_name, promote_deployment_name, owner_name, app_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeployments_promote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_name** | **string**| deployment name | 
 **promote_deployment_name** | **string**| deployment name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Release to be promoted, only needs to provide optional fields, description, label, disabled, mandatory, rollout, targetBinaryVersion | [optional] 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codePushDeploymentMetrics_get**
> Failure codePushDeploymentMetrics_get(deployment_name, owner_name, app_name)



Gets all releases metrics for specified Deployment

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_name = "string" # string | deployment name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.codePushDeploymentMetrics_get(deployment_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeploymentMetrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_name** | **string**| deployment name | 
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

# **codePushDeployments_delete**
> Failure codePushDeployments_delete(deployment_name, owner_name, app_name)



Deletes a CodePush Deployment for the given app

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_name = "string" # string | deployment name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.codePushDeployments_delete(deployment_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeployments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_name** | **string**| deployment name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codePushDeployments_get**
> Failure codePushDeployments_get(deployment_name, owner_name, app_name)



Gets a CodePush Deployment for the given app

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_name = "string" # string | deployment name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.codePushDeployments_get(deployment_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeployments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_name** | **string**| deployment name | 
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

# **codePushDeployments_update**
> Failure codePushDeployments_update(deployment_name, owner_name, app_name, body)



Modifies a CodePush Deployment for the given app

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
deployment_name = "string" # string | deployment name
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"name":"string"} # object | Deployment modification. All fields are optional and only provided fields will get updated.

try:
    api_response = api_instance.codePushDeployments_update(deployment_name, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeployments_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_name** | **string**| deployment name | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Deployment modification. All fields are optional and only provided fields will get updated. | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codePushDeployments_list**
> Failure codePushDeployments_list(owner_name, app_name)



Gets a list of CodePush deployments for the given app

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.codePushDeployments_list(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeployments_list: %s\n" % e)
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

# **codePushDeployments_create**
> Failure codePushDeployments_create(owner_name, app_name, body)



Creates a CodePush Deployment for the given app

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
api_instance = appcenter_sdk.codepushApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"key":"string","name":"string","latest_release":{"target_binary_range":"string","description":"string","is_disabled":true,"is_mandatory":true,"rollout":1,"label":"string","package_hash":"string","blob_url":"string","diff_package_map":{"property1":{"size":0,"url":"string"},"property2":{"size":0,"url":"string"}},"original_deployment":"string","original_label":"string","released_by":"string","release_method":"Upload","size":0,"upload_time":0}} # object | Deployment to be created

try:
    api_response = api_instance.codePushDeployments_create(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling codepushApi->codePushDeployments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Deployment to be created | 

### Return type

[**Failure**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

