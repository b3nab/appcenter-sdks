# appcenter_sdk.distributeApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_registerUserForDevice**](distributeApi.md#devices_registerUserForDevice) | **POST** /v0.1/users/{user_id}/devices/register | 
[**devices_deviceDetails**](distributeApi.md#devices_deviceDetails) | **GET** /v0.1/user/devices/{device_udid} | 
[**devices_removeUserDevice**](distributeApi.md#devices_removeUserDevice) | **DELETE** /v0.1/user/devices/{device_udid} | 
[**devices_userDevicesList**](distributeApi.md#devices_userDevicesList) | **GET** /v0.1/user/devices | 
[**releases_listTesterApps**](distributeApi.md#releases_listTesterApps) | **GET** /v0.1/tester/apps | 
[**releases_getLatestByHash**](distributeApi.md#releases_getLatestByHash) | **GET** /v0.1/sdk/apps/{app_secret}/releases/{release_hash} | 
[**releases_getLatestByPublicDistributionGroup**](distributeApi.md#releases_getLatestByPublicDistributionGroup) | **GET** /v0.1/public/sdk/apps/{app_secret}/distribution_groups/{distribution_group_id}/releases/latest | 
[**distibutionReleases_installAnalytics**](distributeApi.md#distibutionReleases_installAnalytics) | **POST** /v0.1/public/apps/{owner_name}/{app_name}/install_analytics | 
[**releases_getIosManifest**](distributeApi.md#releases_getIosManifest) | **GET** /v0.1/public/apps/{app_id}/releases/{release_id}/ios_manifest | 
[**storeNotifications_getNotificationByAppId**](distributeApi.md#storeNotifications_getNotificationByAppId) | **GET** /v0.1/apps/{owner_name}/{app_name}/store_service_status | 
[**devices_getReleaseUpdateDevicesStatus**](distributeApi.md#devices_getReleaseUpdateDevicesStatus) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/update_devices/{resign_id} | 
[**releases_putDistributionTester**](distributeApi.md#releases_putDistributionTester) | **PUT** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers/{tester_id} | 
[**releases_deleteDistributionTester**](distributeApi.md#releases_deleteDistributionTester) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers/{tester_id} | 
[**releases_addTesters**](distributeApi.md#releases_addTesters) | **POST** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/testers | 
[**releases_deleteDistributionStore**](distributeApi.md#releases_deleteDistributionStore) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/stores/{store_id} | 
[**releases_addStore**](distributeApi.md#releases_addStore) | **POST** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/stores | 
[**provisioning_profile**](distributeApi.md#provisioning_profile) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/provisioning_profile | 
[**releases_putDistributionGroup**](distributeApi.md#releases_putDistributionGroup) | **PUT** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups/{group_id} | 
[**releases_deleteDistributionGroup**](distributeApi.md#releases_deleteDistributionGroup) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups/{group_id} | 
[**releases_addDistributionGroup**](distributeApi.md#releases_addDistributionGroup) | **POST** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id}/groups | 
[**releases_getLatestByUser**](distributeApi.md#releases_getLatestByUser) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} | 
[**releases_updateDetails**](distributeApi.md#releases_updateDetails) | **PUT** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} | 
[**releases_update**](distributeApi.md#releases_update) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} | 
[**releases_delete**](distributeApi.md#releases_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/releases/{release_id} | 
[**releases_availableToTester**](distributeApi.md#releases_availableToTester) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases/filter_by_tester | 
[**releases_list**](distributeApi.md#releases_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/releases | 
[**releaseUploads_complete**](distributeApi.md#releaseUploads_complete) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/release_uploads/{upload_id} | 
[**releaseUploads_create**](distributeApi.md#releaseUploads_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/release_uploads | 
[**releases_listLatest**](distributeApi.md#releases_listLatest) | **GET** /v0.1/apps/{owner_name}/{app_name}/recent_releases | 
[**storeReleases_getRealTimeStatusByReleaseId**](distributeApi.md#storeReleases_getRealTimeStatusByReleaseId) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/realtimestatus | 
[**storeReleasePublishLogs_get**](distributeApi.md#storeReleasePublishLogs_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/publish_logs | 
[**storeReleases_getPublishError**](distributeApi.md#storeReleases_getPublishError) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id}/publish_error_details | 
[**storeReleases_get**](distributeApi.md#storeReleases_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id} | 
[**storeReleases_delete**](distributeApi.md#storeReleases_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases/{release_id} | 
[**storeReleases_list**](distributeApi.md#storeReleases_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/releases | 
[**storeReleases_getLatest**](distributeApi.md#storeReleases_getLatest) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name}/latest_release | 
[**stores_get**](distributeApi.md#stores_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name} | 
[**stores_patch**](distributeApi.md#stores_patch) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name} | 
[**stores_delete**](distributeApi.md#stores_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_stores/{store_name} | 
[**stores_create**](distributeApi.md#stores_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_stores | 
[**stores_list**](distributeApi.md#stores_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_stores | 
[**releases_getLatestByDistributionGroup**](distributeApi.md#releases_getLatestByDistributionGroup) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases/{release_id} | 
[**releases_deleteWithDistributionGroupId**](distributeApi.md#releases_deleteWithDistributionGroupId) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases/{release_id} | 
[**releases_listByDistributionGroup**](distributeApi.md#releases_listByDistributionGroup) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/releases | 
[**devices_listCsvFormat**](distributeApi.md#devices_listCsvFormat) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/devices/download_devices_list | 
[**devices_list**](distributeApi.md#devices_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/devices | 
[**appleMapping_TestFlightGroups**](distributeApi.md#appleMapping_TestFlightGroups) | **GET** /v0.1/apps/{owner_name}/{app_name}/apple_test_flight_groups | 
[**appleMapping_get**](distributeApi.md#appleMapping_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/apple_mapping | 
[**appleMapping_delete**](distributeApi.md#appleMapping_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/apple_mapping | 
[**appleMapping_create**](distributeApi.md#appleMapping_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/apple_mapping | 

# **devices_registerUserForDevice**
> ErrorDetails devices_registerUserForDevice(user_id, body)



Registers a user for an existing device

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
user_id = "string" # string | The ID of the user
body = {"udid":"string","model":"string","os_build":"string","os_version":"string","serial":"string","imei":"string","owner_id":"string"} # object | The device info.

try:
    api_response = api_instance.devices_registerUserForDevice(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->devices_registerUserForDevice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **string**| The ID of the user | 
 **body** | [**object**](object.md)| The device info. | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_deviceDetails**
> ErrorDetails devices_deviceDetails(device_udid)



Returns the device details.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
device_udid = "string" # string | The UDID of the device

try:
    api_response = api_instance.devices_deviceDetails(device_udid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->devices_deviceDetails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_udid** | **string**| The UDID of the device | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_removeUserDevice**
> ErrorDetails devices_removeUserDevice(device_udid)



Removes an existing device from a user

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
device_udid = "string" # string | The UDID of the device

try:
    api_response = api_instance.devices_removeUserDevice(device_udid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->devices_removeUserDevice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_udid** | **string**| The UDID of the device | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_userDevicesList**
> ErrorDetails devices_userDevicesList()



Returns all devices associated with the given user.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.devices_userDevicesList()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->devices_userDevicesList: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_listTesterApps**
> array releases_listTesterApps()



Return a list of applications that the user has tester permission to with the latest release for each.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.releases_listTesterApps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_listTesterApps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_getLatestByHash**
> ErrorDetails releases_getLatestByHash(app_secret, release_hash, udid=udid)



Get a release with hash 'release_hash' or the 'latest' from all the distribution groups assigned to the current user.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
app_secret = "string" # string | The secret of the target application
release_hash = "string" # string | The hash of the release or 'latest' to get the latest release from all the distribution groups assigned to the current user.
udid = "string" # string | When passing `udid` in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms. (optional)

try:
    api_response = api_instance.releases_getLatestByHash(app_secret, release_hash, udid=udid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_getLatestByHash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_secret** | **string**| The secret of the target application | 
 **release_hash** | **string**| The hash of the release or &#39;latest&#39; to get the latest release from all the distribution groups assigned to the current user. | 
 **udid** | **string**| When passing `udid` in the query string, a provisioning check for the given device ID will be done. Will be ignored for non-iOS platforms. | [optional] 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_getLatestByPublicDistributionGroup**
> ErrorDetails releases_getLatestByPublicDistributionGroup(app_secret, distribution_group_id)



Get a release with 'latest' for the given public group.

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
app_secret = "string" # string | The secret of the target application
distribution_group_id = "string" # string | the id for destination

try:
    api_response = api_instance.releases_getLatestByPublicDistributionGroup(app_secret, distribution_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_getLatestByPublicDistributionGroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_secret** | **string**| The secret of the target application | 
 **distribution_group_id** | **string**| the id for destination | 

### Return type

[**ErrorDetails**](.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distibutionReleases_installAnalytics**
> distibutionReleases_installAnalytics(owner_name, app_name, body)



Notify download(s) for the provided distribution release(s).

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the app owner
app_name = "string" # string | The name of the app
body = {"releases":[{"release_id":0,"distribution_group_id":"string","user_id":"string"}]} # object | The install analytics request payload

try:
    api_instance.distibutionReleases_installAnalytics(owner_name, app_name, body)
except ApiException as e:
    print("Exception when calling distributeApi->distibutionReleases_installAnalytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the app owner | 
 **app_name** | **string**| The name of the app | 
 **body** | [**object**](object.md)| The install analytics request payload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_getIosManifest**
> ErrorDetails releases_getIosManifest(app_id, release_id, token)



Returns the manifest.plist in XML format for installing the release on a device. Only available for iOS.

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
app_id = "string" # string | The ID of the application
release_id = 0 # integer | The release_id
token = "string" # string | A hash that authorizes the download if it matches the release info.

try:
    api_response = api_instance.releases_getIosManifest(app_id, release_id, token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_getIosManifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **string**| The ID of the application | 
 **release_id** | **integer**| The release_id | 
 **token** | **string**| A hash that authorizes the download if it matches the release info. | 

### Return type

[**ErrorDetails**](.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storeNotifications_getNotificationByAppId**
> ErrorDetails storeNotifications_getNotificationByAppId(owner_name, app_name)



Application specific store service status

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.storeNotifications_getNotificationByAppId(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->storeNotifications_getNotificationByAppId: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_getReleaseUpdateDevicesStatus**
> ErrorDetails devices_getReleaseUpdateDevicesStatus(release_id, resign_id, owner_name, app_name, include_provisioning_profile=include_provisioning_profile)



Returns the resign status to the caller

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = "string" # string | The ID of the release.
resign_id = "string" # string | The ID of the resign operation.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
include_provisioning_profile = true # boolean | A boolean value that indicates if the provisioning profile should be return in addition to the status. When set to true, the provisioning profile will be returned only when status is 'complete' or 'preparing_for_testers'. (optional)

try:
    api_response = api_instance.devices_getReleaseUpdateDevicesStatus(release_id, resign_id, owner_name, app_name, include_provisioning_profile=include_provisioning_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->devices_getReleaseUpdateDevicesStatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **string**| The ID of the release. | 
 **resign_id** | **string**| The ID of the resign operation. | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **include_provisioning_profile** | **boolean**| A boolean value that indicates if the provisioning profile should be return in addition to the status. When set to true, the provisioning profile will be returned only when status is &#39;complete&#39; or &#39;preparing_for_testers&#39;. | [optional] 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_putDistributionTester**
> ErrorDetails releases_putDistributionTester(release_id, tester_id, owner_name, app_name, body=body)



Update details about the specified tester associated with the release

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
tester_id = "string" # string | The id of the tester
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"mandatory_update":true} # object |  (optional)

try:
    api_response = api_instance.releases_putDistributionTester(release_id, tester_id, owner_name, app_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_putDistributionTester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **tester_id** | **string**| The id of the tester | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_deleteDistributionTester**
> ErrorDetails releases_deleteDistributionTester(release_id, tester_id, owner_name, app_name)



Delete the given tester from the release

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
tester_id = "string" # string | The id of the tester
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.releases_deleteDistributionTester(release_id, tester_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_deleteDistributionTester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **tester_id** | **string**| The id of the tester | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_addTesters**
> ErrorDetails releases_addTesters(release_id, owner_name, app_name, body)



Distributes a release to a user

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"mandatory_update":true,"email":"string","notify_testers":true} # object | The release information.

try:
    api_response = api_instance.releases_addTesters(release_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_addTesters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The release information. | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_deleteDistributionStore**
> ErrorDetails releases_deleteDistributionStore(release_id, store_id, owner_name, app_name)



Delete the given distribution store from the release

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
store_id = "string" # string | The id of the distribution store
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.releases_deleteDistributionStore(release_id, store_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_deleteDistributionStore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **store_id** | **string**| The id of the distribution store | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_addStore**
> ErrorDetails releases_addStore(release_id, owner_name, app_name, body)



Distributes a release to a store

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"id":"string"} # object | The release information.

try:
    api_response = api_instance.releases_addStore(release_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_addStore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The release information. | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provisioning_profile**
> ErrorDetails provisioning_profile(release_id, owner_name, app_name)



Return information about the provisioning profile. Only available for iOS.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The release_id
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.provisioning_profile(release_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->provisioning_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The release_id | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_putDistributionGroup**
> ErrorDetails releases_putDistributionGroup(release_id, group_id, owner_name, app_name, body=body)



Update details about the specified distribution group associated with the release

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
group_id = "string" # string | The id of the releases destination
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"mandatory_update":true} # object |  (optional)

try:
    api_response = api_instance.releases_putDistributionGroup(release_id, group_id, owner_name, app_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_putDistributionGroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **group_id** | **string**| The id of the releases destination | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_deleteDistributionGroup**
> ErrorDetails releases_deleteDistributionGroup(release_id, group_id, owner_name, app_name)



Delete the given distribution group from the release

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
group_id = "string" # string | The id of the distribution group
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.releases_deleteDistributionGroup(release_id, group_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_deleteDistributionGroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **group_id** | **string**| The id of the distribution group | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_addDistributionGroup**
> ErrorDetails releases_addDistributionGroup(release_id, owner_name, app_name, body)



Distributes a release to a group

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"id":"string","mandatory_update":true,"notify_testers":true} # object | The release information.

try:
    api_response = api_instance.releases_addDistributionGroup(release_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_addDistributionGroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The release information. | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_getLatestByUser**
> ErrorDetails releases_getLatestByUser(release_id, owner_name, app_name, udid=udid)



Get a release with id `release_id`. If `release_id` is `latest`, return the latest release that was distributed to the current user (from all the distribution groups).

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = "string" # string | The ID of the release, or `latest` to get the latest release from all the distribution groups assigned to the current user.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
udid = "string" # string | when supplied, this call will also check if the given UDID is provisioned. Will be ignored for non-iOS platforms. The value will be returned in the property is_udid_provisioned. (optional)

try:
    api_response = api_instance.releases_getLatestByUser(release_id, owner_name, app_name, udid=udid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_getLatestByUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **string**| The ID of the release, or `latest` to get the latest release from all the distribution groups assigned to the current user. | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **udid** | **string**| when supplied, this call will also check if the given UDID is provisioned. Will be ignored for non-iOS platforms. The value will be returned in the property is_udid_provisioned. | [optional] 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_updateDetails**
> ErrorDetails releases_updateDetails(release_id, owner_name, app_name, body)



Update details of a release.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"enabled":true,"release_notes":"string","build":{"branch":"string","commit_hash":"string","commit_message":"string"}} # object | The release information.

try:
    api_response = api_instance.releases_updateDetails(release_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_updateDetails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The release information. | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_update**
> ErrorDetails releases_update(release_id, owner_name, app_name, body)



Updates a release.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"distribution_group_name":"string","distribution_group_id":"string","destination_name":"string","destination_id":"string","destination_type":"string","release_notes":"string","mandatory_update":true,"destinations":[{"name":"string","id":"string"}],"build":{"branch":"string","commit_hash":"string","commit_message":"string"},"notify_testers":false} # object | The release information.

try:
    api_response = api_instance.releases_update(release_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The release information. | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_delete**
> ErrorDetails releases_delete(release_id, owner_name, app_name)



Deletes a release.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
release_id = 0 # integer | The ID of the release
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.releases_delete(release_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **release_id** | **integer**| The ID of the release | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_availableToTester**
> array releases_availableToTester(owner_name, app_name, published_only=published_only)



Return detailed information about releases avaiable to a tester.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
published_only = true # boolean | when *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out. (optional)

try:
    api_response = api_instance.releases_availableToTester(owner_name, app_name, published_only=published_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_availableToTester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **published_only** | **boolean**| when *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out. | [optional] 

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_list**
> array releases_list(owner_name, app_name, published_only=published_only, scope=scope)



Return basic information about releases.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
published_only = true # boolean | When *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out. (optional)
scope = "string" # string | When the scope is 'tester', only includes releases that have been distributed to groups that the user belongs to. (optional)

try:
    api_response = api_instance.releases_list(owner_name, app_name, published_only=published_only, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **published_only** | **boolean**| When *true*, filters out releases that were uploaded but were never distributed. Releases that under deleted distribution groups will not be filtered out. | [optional] 
 **scope** | **string**| When the scope is &#39;tester&#39;, only includes releases that have been distributed to groups that the user belongs to. | [optional] 

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releaseUploads_complete**
> ReleaseUploadEndResponse releaseUploads_complete(upload_id, owner_name, app_name, body)



Commits or aborts the upload process for a release for the specified application

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
upload_id = "string" # string | The ID of the upload
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"status":"committed"} # object | The release information

try:
    api_response = api_instance.releaseUploads_complete(upload_id, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releaseUploads_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **string**| The ID of the upload | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The release information | 

### Return type

[**ReleaseUploadEndResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releaseUploads_create**
> ReleaseUploadBeginResponse releaseUploads_create(owner_name, app_name, body)



Begins the upload process for a new release for the specified application.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"release_id":0} # object | The release information

try:
    api_response = api_instance.releaseUploads_create(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releaseUploads_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The release information | 

### Return type

[**ReleaseUploadBeginResponse**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_listLatest**
> array releases_listLatest(owner_name, app_name)



Get the latest release from every distribution group associated with an application.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.releases_listLatest(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_listLatest: %s\n" % e)
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

# **storeReleases_getRealTimeStatusByReleaseId**
> ErrorDetails storeReleases_getRealTimeStatusByReleaseId(store_name, release_id, owner_name, app_name)



Return the Real time Status publishing of release from store.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
store_name = "string" # string | The name of the store
release_id = 0 # number | The id of the release
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.storeReleases_getRealTimeStatusByReleaseId(store_name, release_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->storeReleases_getRealTimeStatusByReleaseId: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_name** | **string**| The name of the store | 
 **release_id** | **number**| The id of the release | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storeReleasePublishLogs_get**
> ErrorDetails storeReleasePublishLogs_get(store_name, release_id, owner_name, app_name)



Returns publish logs for a particular release published to a particular store

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
store_name = "string" # string | The name of the store
release_id = "string" # string | The ID of the realease
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.storeReleasePublishLogs_get(store_name, release_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->storeReleasePublishLogs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_name** | **string**| The name of the store | 
 **release_id** | **string**| The ID of the realease | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storeReleases_getPublishError**
> ErrorDetails storeReleases_getPublishError(store_name, release_id, owner_name, app_name)



Return the Error Details of release which failed in publishing.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
store_name = "string" # string | The name of the store
release_id = 0 # number | The id of the release
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.storeReleases_getPublishError(store_name, release_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->storeReleases_getPublishError: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_name** | **string**| The name of the store | 
 **release_id** | **number**| The id of the release | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storeReleases_get**
> ErrorDetails storeReleases_get(store_name, release_id, owner_name, app_name)



Return releases published in a store for releaseId and storeId

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
store_name = "string" # string | The name of the store
release_id = "string" # string | The name of the store
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.storeReleases_get(store_name, release_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->storeReleases_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_name** | **string**| The name of the store | 
 **release_id** | **string**| The name of the store | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storeReleases_delete**
> ErrorDetails storeReleases_delete(store_name, release_id, owner_name, app_name)



delete the release with release Id

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
store_name = "string" # string | The name of the store
release_id = "string" # string | The id of the release
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.storeReleases_delete(store_name, release_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->storeReleases_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_name** | **string**| The name of the store | 
 **release_id** | **string**| The id of the release | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storeReleases_list**
> ErrorDetails storeReleases_list(store_name, owner_name, app_name)



Return all releases published  in a store

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
store_name = "string" # string | The name of the store
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.storeReleases_list(store_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->storeReleases_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_name** | **string**| The name of the store | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storeReleases_getLatest**
> ErrorDetails storeReleases_getLatest(store_name, owner_name, app_name)



Returns the latest release published in a store.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
store_name = "string" # string | The name of the store
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.storeReleases_getLatest(store_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->storeReleases_getLatest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_name** | **string**| The name of the store | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_get**
> ErrorDetails stores_get(store_name, owner_name, app_name)



Return the store details for specified store name.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
store_name = "string" # string | The name of the store
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.stores_get(store_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->stores_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_name** | **string**| The name of the store | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_patch**
> ErrorDetails stores_patch(store_name, owner_name, app_name, body)



Update the store.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
store_name = "string" # string | The name of the store
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"service_connection_id":"string"} # object | Store update request

try:
    api_response = api_instance.stores_patch(store_name, owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->stores_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_name** | **string**| The name of the store | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| Store update request | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_delete**
> ErrorDetails stores_delete(store_name, owner_name, app_name)



delete the store based on specific store name.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
store_name = "string" # string | The name of the store
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.stores_delete(store_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->stores_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_name** | **string**| The name of the store | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_create**
> ErrorDetails stores_create(owner_name, app_name, body)



Create a new external store for the specified application.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"type":"googleplay","name":"string","track":"production","intune_details":{"secret_json":{"id_token":"string","refresh_token":"string","refresh_token_expiry":"string"},"target_audience":{"name":"string"},"app_category":{"name":"string"},"tenant_id":"string"},"service_connection_id":"string"} # object | The store request

try:
    api_response = api_instance.stores_create(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->stores_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The store request | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stores_list**
> array stores_list(owner_name, app_name)



Get all the store details from Storage store table for a particular application.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.stores_list(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->stores_list: %s\n" % e)
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

# **releases_getLatestByDistributionGroup**
> ErrorDetails releases_getLatestByDistributionGroup(owner_name, app_name, distribution_group_name, release_id)



Return detailed information about a distributed release in a given distribution group.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the app owner
app_name = "string" # string | The name of the app
distribution_group_name = "string" # string | The name of the distribution group.
release_id = "string" # string | Only supports the constant `latest`, specific IDs are not supported. `latest` will return the latest release in the distribution group.

try:
    api_response = api_instance.releases_getLatestByDistributionGroup(owner_name, app_name, distribution_group_name, release_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_getLatestByDistributionGroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the app owner | 
 **app_name** | **string**| The name of the app | 
 **distribution_group_name** | **string**| The name of the distribution group. | 
 **release_id** | **string**| Only supports the constant `latest`, specific IDs are not supported. `latest` will return the latest release in the distribution group. | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_deleteWithDistributionGroupId**
> ErrorDetails releases_deleteWithDistributionGroupId(owner_name, app_name, distribution_group_name, release_id)



Deletes a release with id 'release_id' in a given distribution group.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the app owner
app_name = "string" # string | The name of the app
distribution_group_name = "string" # string | The name of the distribution group.
release_id = 0 # integer | The ID identifying the unique release.

try:
    api_response = api_instance.releases_deleteWithDistributionGroupId(owner_name, app_name, distribution_group_name, release_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_deleteWithDistributionGroupId: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the app owner | 
 **app_name** | **string**| The name of the app | 
 **distribution_group_name** | **string**| The name of the distribution group. | 
 **release_id** | **integer**| The ID identifying the unique release. | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **releases_listByDistributionGroup**
> ErrorDetails releases_listByDistributionGroup(distribution_group_name, owner_name, app_name)



Return basic information about distributed releases in a given distribution group.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
distribution_group_name = "string" # string | The name of the distribution group.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.releases_listByDistributionGroup(distribution_group_name, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->releases_listByDistributionGroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_group_name** | **string**| The name of the distribution group. | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_listCsvFormat**
> ErrorDetails devices_listCsvFormat(distribution_group_name, owner_name, app_name, unprovisioned_only=unprovisioned_only, udids=udids)



Returns all devices associated with the given distribution group.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
distribution_group_name = "string" # string | The name of the distribution group.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
unprovisioned_only = false # boolean | when true, filters out provisioned devices (optional)
udids = ["string"] # array | multiple UDIDs which should be part of the resulting CSV. (optional)

try:
    api_response = api_instance.devices_listCsvFormat(distribution_group_name, owner_name, app_name, unprovisioned_only=unprovisioned_only, udids=udids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->devices_listCsvFormat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_group_name** | **string**| The name of the distribution group. | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **unprovisioned_only** | **boolean**| when true, filters out provisioned devices | [optional] 
 **udids** | **array**| multiple UDIDs which should be part of the resulting CSV. | [optional] 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: text/csv, text/csv, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_list**
> ErrorDetails devices_list(distribution_group_name, owner_name, app_name, release_id=release_id)



Returns all devices associated with the given distribution group

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
distribution_group_name = "string" # string | The name of the distribution group.
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
release_id = 0 # number | when provided, gets the provisioning state of the devices owned by users of this distribution group when compared to the provided release. (optional)

try:
    api_response = api_instance.devices_list(distribution_group_name, owner_name, app_name, release_id=release_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->devices_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distribution_group_name** | **string**| The name of the distribution group. | 
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **release_id** | **number**| when provided, gets the provisioning state of the devices owned by users of this distribution group when compared to the provided release. | [optional] 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appleMapping_TestFlightGroups**
> ErrorDetails appleMapping_TestFlightGroups(owner_name, app_name)



Fetch all apple test flight groups

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.appleMapping_TestFlightGroups(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->appleMapping_TestFlightGroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appleMapping_get**
> ErrorDetails appleMapping_get(owner_name, app_name)



Get mapping of apple app to an existing app in apple store.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.appleMapping_get(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->appleMapping_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appleMapping_delete**
> ErrorDetails appleMapping_delete(owner_name, app_name)



Delete mapping of apple app to an existing app in apple store.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.appleMapping_delete(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->appleMapping_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appleMapping_create**
> ErrorDetails appleMapping_create(owner_name, app_name, body)



Create a mapping for an existing app in apple store for the specified application.

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
api_instance = appcenter_sdk.distributeApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"service_connection_id":"string","apple_id":"string","bundle_identifier":"string","team_identifier":"string"} # object | The apple app mapping object

try:
    api_response = api_instance.appleMapping_create(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling distributeApi->appleMapping_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The apple app mapping object | 

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

