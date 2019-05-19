# appcenter_sdk.gdprApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DataSubjectRight_CancelExportRequest**](gdprApi.md#DataSubjectRight_CancelExportRequest) | **POST** /v0.1/user/dsr/export/{token}/cancel | 
[**DataSubjectRight_ExportStatusRequest**](gdprApi.md#DataSubjectRight_ExportStatusRequest) | **GET** /v0.1/user/dsr/export/{token} | 
[**DataSubjectRight_ExportRequest**](gdprApi.md#DataSubjectRight_ExportRequest) | **POST** /v0.1/user/dsr/export | 
[**DataSubjectRight_CancelDeleteRequest**](gdprApi.md#DataSubjectRight_CancelDeleteRequest) | **POST** /v0.1/user/dsr/delete/{token}/cancel | 
[**DataSubjectRight_DeleteStatusRequest**](gdprApi.md#DataSubjectRight_DeleteStatusRequest) | **GET** /v0.1/user/dsr/delete/{token} | 
[**DataSubjectRight_DeleteRequest**](gdprApi.md#DataSubjectRight_DeleteRequest) | **POST** /v0.1/user/dsr/delete | 

# **DataSubjectRight_CancelExportRequest**
> ErrorResponse DataSubjectRight_CancelExportRequest(token)





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
api_instance = appcenter_sdk.gdprApi(appcenter_sdk.ApiClient(configuration))
token = "string" # string | Unique request ID (GUID)

try:
    api_response = api_instance.DataSubjectRight_CancelExportRequest(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling gdprApi->DataSubjectRight_CancelExportRequest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **string**| Unique request ID (GUID) | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DataSubjectRight_ExportStatusRequest**
> ErrorResponse DataSubjectRight_ExportStatusRequest(token)





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
api_instance = appcenter_sdk.gdprApi(appcenter_sdk.ApiClient(configuration))
token = "string" # string | Unique request ID (GUID)

try:
    api_response = api_instance.DataSubjectRight_ExportStatusRequest(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling gdprApi->DataSubjectRight_ExportStatusRequest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **string**| Unique request ID (GUID) | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DataSubjectRight_ExportRequest**
> ErrorResponse DataSubjectRight_ExportRequest()





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
api_instance = appcenter_sdk.gdprApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.DataSubjectRight_ExportRequest()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling gdprApi->DataSubjectRight_ExportRequest: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DataSubjectRight_CancelDeleteRequest**
> ErrorResponse DataSubjectRight_CancelDeleteRequest(token, body=body)





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
api_instance = appcenter_sdk.gdprApi(appcenter_sdk.ApiClient(configuration))
token = "string" # string | Unique request ID (GUID)
body = {"email":"string"} # object |  (optional)

try:
    api_response = api_instance.DataSubjectRight_CancelDeleteRequest(token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling gdprApi->DataSubjectRight_CancelDeleteRequest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **string**| Unique request ID (GUID) | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DataSubjectRight_DeleteStatusRequest**
> ErrorResponse DataSubjectRight_DeleteStatusRequest(token, email)





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
api_instance = appcenter_sdk.gdprApi(appcenter_sdk.ApiClient(configuration))
token = "string" # string | Unique request ID (GUID)
email = "string" # string | Email used for delete with x-authz-bypass headers

try:
    api_response = api_instance.DataSubjectRight_DeleteStatusRequest(token, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling gdprApi->DataSubjectRight_DeleteStatusRequest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **string**| Unique request ID (GUID) | 
 **email** | **string**| Email used for delete with x-authz-bypass headers | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DataSubjectRight_DeleteRequest**
> ErrorResponse DataSubjectRight_DeleteRequest()





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
api_instance = appcenter_sdk.gdprApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.DataSubjectRight_DeleteRequest()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling gdprApi->DataSubjectRight_DeleteRequest: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

