# appcenter_sdk.billingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingAggregatedInformation_getForOrg**](billingApi.md#billingAggregatedInformation_getForOrg) | **GET** /v0.1/orgs/{orgName}/billing/aggregated | 
[**billingAggregatedInformation_getByApp**](billingApi.md#billingAggregatedInformation_getByApp) | **GET** /v0.1/apps/{owner_name}/{app_name}/billing/aggregated | 

# **billingAggregatedInformation_getForOrg**
> BillingError billingAggregatedInformation_getForOrg(orgName, service=service, period=period, showOriginalPlans=showOriginalPlans)



Aggregated Billing Information for a given Organization.

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
api_instance = appcenter_sdk.billingApi(appcenter_sdk.ApiClient(configuration))
orgName = "string" # string | The name of the Organization
service = "Test" # string | Type of service that should be included in the Billing Information (optional)
period = "Previous" # string | Type of period that should be included in the Billing Information (optional)
showOriginalPlans = true # boolean | Controls whether the API should show the original plan when Azure Subscription is not enabled (optional)

try:
    api_response = api_instance.billingAggregatedInformation_getForOrg(orgName, service=service, period=period, showOriginalPlans=showOriginalPlans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling billingApi->billingAggregatedInformation_getForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orgName** | **string**| The name of the Organization | 
 **service** | **string**| Type of service that should be included in the Billing Information | [optional] 
 **period** | **string**| Type of period that should be included in the Billing Information | [optional] 
 **showOriginalPlans** | **boolean**| Controls whether the API should show the original plan when Azure Subscription is not enabled | [optional] 

### Return type

[**BillingError**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billingAggregatedInformation_getByApp**
> BillingError billingAggregatedInformation_getByApp(owner_name, app_name, service=service, period=period, showOriginalPlans=showOriginalPlans)



Aggregated Billing Information for owner of a given app.

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
api_instance = appcenter_sdk.billingApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
service = "Test" # string | Type of service that should be included in the Billing Information (optional)
period = "Previous" # string | Type of period that should be included in the Billing Information (optional)
showOriginalPlans = true # boolean | Controls whether the API should show the original plan when Azure Subscription is not enabled (optional)

try:
    api_response = api_instance.billingAggregatedInformation_getByApp(owner_name, app_name, service=service, period=period, showOriginalPlans=showOriginalPlans)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling billingApi->billingAggregatedInformation_getByApp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **service** | **string**| Type of service that should be included in the Billing Information | [optional] 
 **period** | **string**| Type of period that should be included in the Billing Information | [optional] 
 **showOriginalPlans** | **boolean**| Controls whether the API should show the original plan when Azure Subscription is not enabled | [optional] 

### Return type

[**BillingError**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

