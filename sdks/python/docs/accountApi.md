# appcenter_sdk.accountApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgInvitations_reject**](accountApi.md#orgInvitations_reject) | **POST** /v0.1/user/invitations/orgs/{invitation_token}/reject | 
[**orgInvitations_accept**](accountApi.md#orgInvitations_accept) | **POST** /v0.1/user/invitations/orgs/{invitation_token}/accept | 
[**distributionGroupInvitations_acceptAll**](accountApi.md#distributionGroupInvitations_acceptAll) | **POST** /v0.1/user/invitations/distribution_groups/accept | 
[**appInvitations_reject**](accountApi.md#appInvitations_reject) | **POST** /v0.1/user/invitations/apps/{invitation_token}/reject | 
[**appInvitations_accept**](accountApi.md#appInvitations_accept) | **POST** /v0.1/user/invitations/apps/{invitation_token}/accept | 
[**sharedconnection_Connections**](accountApi.md#sharedconnection_Connections) | **GET** /v0.1/user/export/serviceConnections | 
[**users_get**](accountApi.md#users_get) | **GET** /v0.1/user | 
[**users_update**](accountApi.md#users_update) | **PATCH** /v0.1/user | 
[**users_updateOrgRole**](accountApi.md#users_updateOrgRole) | **PATCH** /v0.1/orgs/{org_name}/users/{user_name} | 
[**users_removeFromOrg**](accountApi.md#users_removeFromOrg) | **DELETE** /v0.1/orgs/{org_name}/users/{user_name} | 
[**users_listForOrg**](accountApi.md#users_listForOrg) | **GET** /v0.1/orgs/{org_name}/users | 
[**distributionGroups_listAllTestersForOrg**](accountApi.md#distributionGroups_listAllTestersForOrg) | **GET** /v0.1/orgs/{org_name}/testers | 
[**teams_removeUser**](accountApi.md#teams_removeUser) | **DELETE** /v0.1/orgs/{org_name}/teams/{team_name}/users/{user_name} | 
[**teams_getUsers**](accountApi.md#teams_getUsers) | **GET** /v0.1/orgs/{org_name}/teams/{team_name}/users | 
[**teams_addUser**](accountApi.md#teams_addUser) | **POST** /v0.1/orgs/{org_name}/teams/{team_name}/users | 
[**teams_updatePermissions**](accountApi.md#teams_updatePermissions) | **PATCH** /v0.1/orgs/{org_name}/teams/{team_name}/apps/{app_name} | 
[**teams_removeApp**](accountApi.md#teams_removeApp) | **DELETE** /v0.1/orgs/{org_name}/teams/{team_name}/apps/{app_name} | 
[**teams_addApp**](accountApi.md#teams_addApp) | **POST** /v0.1/orgs/{org_name}/teams/{team_name}/apps | 
[**teams_listApps**](accountApi.md#teams_listApps) | **GET** /v0.1/orgs/{org_name}/teams/{team_name}/apps | 
[**teams_getTeam**](accountApi.md#teams_getTeam) | **GET** /v0.1/orgs/{org_name}/teams/{team_name} | 
[**teams_delete**](accountApi.md#teams_delete) | **DELETE** /v0.1/orgs/{org_name}/teams/{team_name} | 
[**teams_update**](accountApi.md#teams_update) | **PATCH** /v0.1/orgs/{org_name}/teams/{team_name} | 
[**teams_listAll**](accountApi.md#teams_listAll) | **GET** /v0.1/orgs/{org_name}/teams | 
[**teams_createTeam**](accountApi.md#teams_createTeam) | **POST** /v0.1/orgs/{org_name}/teams | 
[**orgInvitations_**](accountApi.md#orgInvitations_) | **POST** /v0.1/orgs/{org_name}/invitations/{email}/revoke | 
[**orgInvitations_sendNewInvitation**](accountApi.md#orgInvitations_sendNewInvitation) | **POST** /v0.1/orgs/{org_name}/invitations/{email}/resend | 
[**orgInvitations_update**](accountApi.md#orgInvitations_update) | **PATCH** /v0.1/orgs/{org_name}/invitations/{email} | 
[**orgInvitations_create**](accountApi.md#orgInvitations_create) | **POST** /v0.1/orgs/{org_name}/invitations | 
[**orgInvitations_delete**](accountApi.md#orgInvitations_delete) | **DELETE** /v0.1/orgs/{org_name}/invitations | 
[**orgInvitations_listPending**](accountApi.md#orgInvitations_listPending) | **GET** /v0.1/orgs/{org_name}/invitations | 
[**distributionGroups_detailsForOrg**](accountApi.md#distributionGroups_detailsForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups_details | 
[**distributionGroups_resendSharedInvite**](accountApi.md#distributionGroups_resendSharedInvite) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/resend_invite | 
[**distributionGroups_bulkDeleteUsers**](accountApi.md#distributionGroups_bulkDeleteUsers) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members/bulk_delete | 
[**distributionGroups_listUsersForOrg**](accountApi.md#distributionGroups_listUsersForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members | 
[**distributionGroups_addUsersForOrg**](accountApi.md#distributionGroups_addUsersForOrg) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members | 
[**distributionGroups_bulkDeleteApps**](accountApi.md#distributionGroups_bulkDeleteApps) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps/bulk_delete | 
[**distributionGroups_getApps**](accountApi.md#distributionGroups_getApps) | **GET** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps | 
[**distributionGroups_addApps**](accountApi.md#distributionGroups_addApps) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps | 
[**distributionGroups_getForOrg**](accountApi.md#distributionGroups_getForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroups_patchForOrg**](accountApi.md#distributionGroups_patchForOrg) | **PATCH** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroups_deleteForOrg**](accountApi.md#distributionGroups_deleteForOrg) | **DELETE** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroups_createForOrg**](accountApi.md#distributionGroups_createForOrg) | **POST** /v0.1/orgs/{org_name}/distribution_groups | 
[**distributionGroups_listForOrg**](accountApi.md#distributionGroups_listForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups | 
[**azureSubscription_listForOrg**](accountApi.md#azureSubscription_listForOrg) | **GET** /v0.1/orgs/{org_name}/azure_subscriptions | 
[**organization_updateAvatar**](accountApi.md#organization_updateAvatar) | **POST** /v0.1/orgs/{org_name}/avatar | 
[**organization_deleteAvatar**](accountApi.md#organization_deleteAvatar) | **DELETE** /v0.1/orgs/{org_name}/avatar | 
[**apps_createForOrg**](accountApi.md#apps_createForOrg) | **POST** /v0.1/orgs/{org_name}/apps | 
[**apps_listForOrg**](accountApi.md#apps_listForOrg) | **GET** /v0.1/orgs/{org_name}/apps | 
[**aadGroup_listForOrg**](accountApi.md#aadGroup_listForOrg) | **GET** /v0.1/orgs/{org_name}/aad_groups | 
[**organization_addAADGroups**](accountApi.md#organization_addAADGroups) | **POST** /v0.1/orgs/{org_name}/aad_groups | 
[**organizations_get**](accountApi.md#organizations_get) | **GET** /v0.1/orgs/{org_name} | 
[**organizations_update**](accountApi.md#organizations_update) | **PATCH** /v0.1/orgs/{org_name} | 
[**organizations_delete**](accountApi.md#organizations_delete) | **DELETE** /v0.1/orgs/{org_name} | 
[**organizations_createOrUpdate**](accountApi.md#organizations_createOrUpdate) | **POST** /v0.1/orgs | 
[**organizations_list**](accountApi.md#organizations_list) | **GET** /v0.1/orgs | 
[**invitations_sent**](accountApi.md#invitations_sent) | **GET** /v0.1/invitations/sent | 
[**azureSubscription_listForUser**](accountApi.md#azureSubscription_listForUser) | **GET** /v0.1/azure_subscriptions | 
[**apps_removeUser**](accountApi.md#apps_removeUser) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/users/{user_email} | 
[**apps_updateUserPermissions**](accountApi.md#apps_updateUserPermissions) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/users/{user_email} | 
[**users_list**](accountApi.md#users_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/users | 
[**apps_transferToOrg**](accountApi.md#apps_transferToOrg) | **POST** /v0.1/apps/{owner_name}/{app_name}/transfer_to_org | 
[**apps_transferOwnership**](accountApi.md#apps_transferOwnership) | **POST** /v0.1/apps/{owner_name}/{app_name}/transfer/{destination_owner_name} | 
[**apps_listTesters**](accountApi.md#apps_listTesters) | **GET** /v0.1/apps/{owner_name}/{app_name}/testers | 
[**apps_getTeams**](accountApi.md#apps_getTeams) | **GET** /v0.1/apps/{owner_name}/{app_name}/teams | 
[**appInvitations_createByEmail**](accountApi.md#appInvitations_createByEmail) | **POST** /v0.1/apps/{owner_name}/{app_name}/invitations/{user_email} | 
[**appInvitations_updatePermissions**](accountApi.md#appInvitations_updatePermissions) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/invitations/{user_email} | 
[**appInvitations_delete**](accountApi.md#appInvitations_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/invitations/{user_email} | 
[**appInvitations_create**](accountApi.md#appInvitations_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/invitations | 
[**appInvitations_list**](accountApi.md#appInvitations_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/invitations | 
[**distributionGroups_resendInvite**](accountApi.md#distributionGroups_resendInvite) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/resend_invite | 
[**distributionGroups_removeUser**](accountApi.md#distributionGroups_removeUser) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members/bulk_delete | 
[**distributionGroups_listUsers**](accountApi.md#distributionGroups_listUsers) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members | 
[**distributionGroups_addUser**](accountApi.md#distributionGroups_addUser) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members | 
[**distributionGroups_get**](accountApi.md#distributionGroups_get) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroups_update**](accountApi.md#distributionGroups_update) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroups_delete**](accountApi.md#distributionGroups_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name} | 
[**distributionGroups_list**](accountApi.md#distributionGroups_list) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups | 
[**distributionGroups_create**](accountApi.md#distributionGroups_create) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups | 
[**azureSubscription_deleteForApp**](accountApi.md#azureSubscription_deleteForApp) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/azure_subscriptions/{azure_subscription_id} | 
[**azureSubscription_listForApp**](accountApi.md#azureSubscription_listForApp) | **GET** /v0.1/apps/{owner_name}/{app_name}/azure_subscriptions | 
[**azureSubscription_linkForApp**](accountApi.md#azureSubscription_linkForApp) | **POST** /v0.1/apps/{owner_name}/{app_name}/azure_subscriptions | 
[**apps_updateAvatar**](accountApi.md#apps_updateAvatar) | **POST** /v0.1/apps/{owner_name}/{app_name}/avatar | 
[**apps_deleteAvatar**](accountApi.md#apps_deleteAvatar) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/avatar | 
[**apps_get**](accountApi.md#apps_get) | **GET** /v0.1/apps/{owner_name}/{app_name} | 
[**apps_update**](accountApi.md#apps_update) | **PATCH** /v0.1/apps/{owner_name}/{app_name} | 
[**apps_delete**](accountApi.md#apps_delete) | **DELETE** /v0.1/apps/{owner_name}/{app_name} | 
[**apps_create**](accountApi.md#apps_create) | **POST** /v0.1/apps | 
[**apps_list**](accountApi.md#apps_list) | **GET** /v0.1/apps | 
[**apiTokens_delete**](accountApi.md#apiTokens_delete) | **DELETE** /v0.1/api_tokens/{api_token_id} | 
[**apiTokens_list**](accountApi.md#apiTokens_list) | **GET** /v0.1/api_tokens | 
[**apiTokens_new**](accountApi.md#apiTokens_new) | **POST** /v0.1/api_tokens | 

# **orgInvitations_reject**
> ErrorResponse orgInvitations_reject(invitation_token)



Rejects a pending organization invitation

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
invitation_token = "string" # string | The app invitation token that was sent to the user

try:
    api_response = api_instance.orgInvitations_reject(invitation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->orgInvitations_reject: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_token** | **string**| The app invitation token that was sent to the user | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgInvitations_accept**
> ErrorResponse orgInvitations_accept(invitation_token)



Accepts a pending organization invitation for the specified user

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
invitation_token = "string" # string | The app invitation token that was sent to the user

try:
    api_response = api_instance.orgInvitations_accept(invitation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->orgInvitations_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_token** | **string**| The app invitation token that was sent to the user | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroupInvitations_acceptAll**
> ErrorResponse distributionGroupInvitations_acceptAll()



Accepts all pending invitations to distribution groups for the specified user

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.distributionGroupInvitations_acceptAll()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroupInvitations_acceptAll: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appInvitations_reject**
> ErrorResponse appInvitations_reject(invitation_token)



Rejects a pending invitation for the specified user

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
invitation_token = "string" # string | The app invitation token that was sent to the user

try:
    api_response = api_instance.appInvitations_reject(invitation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->appInvitations_reject: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_token** | **string**| The app invitation token that was sent to the user | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appInvitations_accept**
> ErrorResponse appInvitations_accept(invitation_token)



Accepts a pending invitation for the specified user

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
invitation_token = "string" # string | The app invitation token that was sent to the user

try:
    api_response = api_instance.appInvitations_accept(invitation_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->appInvitations_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_token** | **string**| The app invitation token that was sent to the user | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sharedconnection_Connections**
> ErrorDetails sharedconnection_Connections()



Gets all service connections of the service type for GDPR export.

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.sharedconnection_Connections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->sharedconnection_Connections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorDetails**](.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> ErrorResponse users_get()



Returns the user profile data

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->users_get: %s\n" % e)
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

# **users_update**
> ErrorResponse users_update(body)



Updates the user profile and returns the updated user data

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
body = {"display_name":"string"} # object | The data for the created user

try:
    api_response = api_instance.users_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The data for the created user | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_updateOrgRole**
> ErrorResponse users_updateOrgRole(org_name, user_name, body)



Updates the given organization user

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
user_name = "string" # string | The slug name of the user
body = {"role":"admin"} # object | 

try:
    api_response = api_instance.users_updateOrgRole(org_name, user_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->users_updateOrgRole: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **user_name** | **string**| The slug name of the user | 
 **body** | [**object**](object.md)|  | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_removeFromOrg**
> ErrorResponse users_removeFromOrg(org_name, user_name)



Removes a user from an organization.

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
user_name = "string" # string | The slug name of the user

try:
    api_response = api_instance.users_removeFromOrg(org_name, user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->users_removeFromOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **user_name** | **string**| The slug name of the user | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_listForOrg**
> ErrorResponse users_listForOrg(org_name)



Returns a list of users that belong to an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.users_listForOrg(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->users_listForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_listAllTestersForOrg**
> ErrorResponse distributionGroups_listAllTestersForOrg(org_name)



Returns a unique list of users including the whole organization members plus testers in any shared group of that org

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.distributionGroups_listAllTestersForOrg(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_listAllTestersForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_removeUser**
> ErrorResponse teams_removeUser(org_name, team_name, user_name)



Removes a user from a team that is owned by an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
team_name = "string" # string | The team's name
user_name = "string" # string | The slug name of the user

try:
    api_response = api_instance.teams_removeUser(org_name, team_name, user_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_removeUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **team_name** | **string**| The team&#39;s name | 
 **user_name** | **string**| The slug name of the user | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_getUsers**
> ErrorResponse teams_getUsers(org_name, team_name)



Returns the users of a team which is owned by an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
team_name = "string" # string | The team's name

try:
    api_response = api_instance.teams_getUsers(org_name, team_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_getUsers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **team_name** | **string**| The team&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_addUser**
> ErrorResponse teams_addUser(org_name, team_name, body=body)



Adds a new user to a team that is owned by an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
team_name = "string" # string | The team's name
body = {"user_email":"string","role":"admin"} # object | The email of the user to add to the team (optional)

try:
    api_response = api_instance.teams_addUser(org_name, team_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_addUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **team_name** | **string**| The team&#39;s name | 
 **body** | [**object**](object.md)| The email of the user to add to the team | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_updatePermissions**
> ErrorResponse teams_updatePermissions(org_name, team_name, app_name, body=body)



Updates the permissions the team has to the app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
team_name = "string" # string | The team's name
app_name = "string" # string | The name of the application
body = {"permissions":["manager"]} # object |  (optional)

try:
    api_response = api_instance.teams_updatePermissions(org_name, team_name, app_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_updatePermissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **team_name** | **string**| The team&#39;s name | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_removeApp**
> ErrorResponse teams_removeApp(org_name, team_name, app_name)



Removes an app from a team

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
team_name = "string" # string | The team's name
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.teams_removeApp(org_name, team_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_removeApp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **team_name** | **string**| The team&#39;s name | 
 **app_name** | **string**| The name of the application | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_addApp**
> ErrorResponse teams_addApp(org_name, team_name, body)



Adds an app to a team

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
team_name = "string" # string | The team's name
body = {"name":"string"} # object | The name of the app to be added to the team. The app has to be owned by the organization.

try:
    api_response = api_instance.teams_addApp(org_name, team_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_addApp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **team_name** | **string**| The team&#39;s name | 
 **body** | [**object**](object.md)| The name of the app to be added to the team. The app has to be owned by the organization. | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_listApps**
> ErrorResponse teams_listApps(org_name, team_name)



Returns the apps a team has access to

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
team_name = "string" # string | The team's name

try:
    api_response = api_instance.teams_listApps(org_name, team_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_listApps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **team_name** | **string**| The team&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_getTeam**
> ErrorResponse teams_getTeam(org_name, team_name)



Returns the details of a single team

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
team_name = "string" # string | The team's name

try:
    api_response = api_instance.teams_getTeam(org_name, team_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_getTeam: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **team_name** | **string**| The team&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_delete**
> ErrorResponse teams_delete(org_name, team_name)



Deletes a single team

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
team_name = "string" # string | The team's name

try:
    api_response = api_instance.teams_delete(org_name, team_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **team_name** | **string**| The team&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_update**
> ErrorResponse teams_update(org_name, team_name, body=body)



Updates a single team

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
team_name = "string" # string | The team's name
body = {"display_name":"string","name":"string","description":"string"} # object | The information used to create the team (optional)

try:
    api_response = api_instance.teams_update(org_name, team_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **team_name** | **string**| The team&#39;s name | 
 **body** | [**object**](object.md)| The information used to create the team | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_listAll**
> ErrorResponse teams_listAll(org_name)



Returns the list of all teams in this org

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.teams_listAll(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_listAll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_createTeam**
> ErrorResponse teams_createTeam(org_name, body=body)



Creates a team and returns it

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
body = {"display_name":"string","name":"string","description":"string"} # object | The information used to create the team (optional)

try:
    api_response = api_instance.teams_createTeam(org_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->teams_createTeam: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **body** | [**object**](object.md)| The information used to create the team | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgInvitations_**
> ErrorResponse orgInvitations_(org_name, email)



Removes a user's invitation to an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
email = "string" # string | The email address of the user to send the password reset mail to.

try:
    api_response = api_instance.orgInvitations_(org_name, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->orgInvitations_: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **email** | **string**| The email address of the user to send the password reset mail to. | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgInvitations_sendNewInvitation**
> ErrorResponse orgInvitations_sendNewInvitation(org_name, email, body=body)



Cancels an existing organization invitation for the user and sends a new one

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
email = "string" # string | The email address of the user to send the password reset mail to.
body = {"role":"admin"} # object | The role of the user to be added (optional)

try:
    api_response = api_instance.orgInvitations_sendNewInvitation(org_name, email, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->orgInvitations_sendNewInvitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **email** | **string**| The email address of the user to send the password reset mail to. | 
 **body** | [**object**](object.md)| The role of the user to be added | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgInvitations_update**
> ErrorResponse orgInvitations_update(org_name, email, body)



Allows the role of an invited user to be changed

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
email = "string" # string | The email address of the user to send the password reset mail to.
body = {"role":"admin"} # object | The new role of the user

try:
    api_response = api_instance.orgInvitations_update(org_name, email, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->orgInvitations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **email** | **string**| The email address of the user to send the password reset mail to. | 
 **body** | [**object**](object.md)| The new role of the user | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgInvitations_create**
> ErrorResponse orgInvitations_create(org_name, body=body)



Invites a new or existing user to an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
body = {"user_email":"string","role":"admin"} # object | The email of the user to invite (optional)

try:
    api_response = api_instance.orgInvitations_create(org_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->orgInvitations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **body** | [**object**](object.md)| The email of the user to invite | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgInvitations_delete**
> ErrorResponse orgInvitations_delete(org_name, body=body)



Removes a user's invitation to an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
body = {"user_email":"string","role":"admin"} # object | The email of the user whose invitation should be removed (optional)

try:
    api_response = api_instance.orgInvitations_delete(org_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->orgInvitations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **body** | [**object**](object.md)| The email of the user whose invitation should be removed | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgInvitations_listPending**
> ErrorResponse orgInvitations_listPending(org_name)



Gets the pending invitations for the organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.orgInvitations_listPending(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->orgInvitations_listPending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_detailsForOrg**
> ErrorResponse distributionGroups_detailsForOrg(org_name, apps_limit=apps_limit)



Returns a list of distribution groups with details for an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
apps_limit = 0 # number | The max number of apps to include in the response (optional)

try:
    api_response = api_instance.distributionGroups_detailsForOrg(org_name, apps_limit=apps_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_detailsForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **apps_limit** | **number**| The max number of apps to include in the response | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_resendSharedInvite**
> ErrorResponse distributionGroups_resendSharedInvite(org_name, distribution_group_name, body)



Resend shared distribution group invite notification to previously invited testers

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
distribution_group_name = "string" # string | The name of the distribution group
body = {"user_emails":["string"]} # object | The list of members to add

try:
    api_response = api_instance.distributionGroups_resendSharedInvite(org_name, distribution_group_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_resendSharedInvite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **body** | [**object**](object.md)| The list of members to add | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_bulkDeleteUsers**
> distributionGroups_bulkDeleteUsers(org_name, distribution_group_name, body)



Delete apps from distribution group in an org

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
distribution_group_name = "string" # string | The name of the distribution group
body = {"user_emails":["string"]} # object | The list of members to add

try:
    api_instance.distributionGroups_bulkDeleteUsers(org_name, distribution_group_name, body)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_bulkDeleteUsers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **body** | [**object**](object.md)| The list of members to add | 

### Return type

void (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_listUsersForOrg**
> ErrorResponse distributionGroups_listUsersForOrg(org_name, distribution_group_name)



Returns a list of member in the distribution group specified

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
distribution_group_name = "string" # string | The name of the distribution group

try:
    api_response = api_instance.distributionGroups_listUsersForOrg(org_name, distribution_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_listUsersForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **distribution_group_name** | **string**| The name of the distribution group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_addUsersForOrg**
> ErrorResponse distributionGroups_addUsersForOrg(org_name, distribution_group_name, body)



Accepts an array of user email addresses to get added to the specified group

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
distribution_group_name = "string" # string | The name of the distribution group
body = {"user_emails":["string"]} # object | list of user email addresses that should get added as members to the specified group

try:
    api_response = api_instance.distributionGroups_addUsersForOrg(org_name, distribution_group_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_addUsersForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **body** | [**object**](object.md)| list of user email addresses that should get added as members to the specified group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_bulkDeleteApps**
> distributionGroups_bulkDeleteApps(org_name, distribution_group_name, body)



Delete apps from distribution group in an org

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
distribution_group_name = "string" # string | The name of the distribution group
body = {"apps":[{"name":"string"}]} # object | The name of the apps to be deleted from the distribution group. The apps have to be owned by the organization.

try:
    api_instance.distributionGroups_bulkDeleteApps(org_name, distribution_group_name, body)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_bulkDeleteApps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **body** | [**object**](object.md)| The name of the apps to be deleted from the distribution group. The apps have to be owned by the organization. | 

### Return type

void (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_getApps**
> array distributionGroups_getApps(org_name, distribution_group_name)



Get apps from a distribution group in an org

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
distribution_group_name = "string" # string | The name of the distribution group

try:
    api_response = api_instance.distributionGroups_getApps(org_name, distribution_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_getApps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **distribution_group_name** | **string**| The name of the distribution group | 

### Return type

**array**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_addApps**
> distributionGroups_addApps(org_name, distribution_group_name, body)



Add apps to distribution group in an org

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
distribution_group_name = "string" # string | The name of the distribution group
body = {"apps":[{"name":"string"}]} # object | The name of the apps to be added to the distribution group. The apps have to be owned by the organization.

try:
    api_instance.distributionGroups_addApps(org_name, distribution_group_name, body)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_addApps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **body** | [**object**](object.md)| The name of the apps to be added to the distribution group. The apps have to be owned by the organization. | 

### Return type

void (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_getForOrg**
> ErrorResponse distributionGroups_getForOrg(org_name, distribution_group_name)



Returns a single distribution group in org for a given distribution group name

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
distribution_group_name = "string" # string | The name of the distribution group

try:
    api_response = api_instance.distributionGroups_getForOrg(org_name, distribution_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_getForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **distribution_group_name** | **string**| The name of the distribution group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_patchForOrg**
> ErrorResponse distributionGroups_patchForOrg(org_name, distribution_group_name, body)



Update one given distribution group name in an org

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
distribution_group_name = "string" # string | The name of the distribution group
body = {"name":"string","is_public":true} # object | The attributes to update for the distribution group

try:
    api_response = api_instance.distributionGroups_patchForOrg(org_name, distribution_group_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_patchForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **body** | [**object**](object.md)| The attributes to update for the distribution group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_deleteForOrg**
> ErrorResponse distributionGroups_deleteForOrg(org_name, distribution_group_name)



Deletes a single distribution group from an org with a given distribution group name

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
distribution_group_name = "string" # string | The name of the distribution group

try:
    api_response = api_instance.distributionGroups_deleteForOrg(org_name, distribution_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_deleteForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **distribution_group_name** | **string**| The name of the distribution group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_createForOrg**
> ErrorResponse distributionGroups_createForOrg(org_name, body)



Creates a disribution goup which can be shared across apps under an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
body = {"name":"string","display_name":"string"} # object | The attributes to update for the distribution group

try:
    api_response = api_instance.distributionGroups_createForOrg(org_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_createForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **body** | [**object**](object.md)| The attributes to update for the distribution group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_listForOrg**
> ErrorResponse distributionGroups_listForOrg(org_name)



Returns a list of distribution groups in the org specified

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.distributionGroups_listForOrg(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_listForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azureSubscription_listForOrg**
> ErrorResponse azureSubscription_listForOrg(org_name)



Returns a list of azure subscriptions for the organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.azureSubscription_listForOrg(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->azureSubscription_listForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_updateAvatar**
> ErrorResponse organization_updateAvatar(org_name, body=body)



Sets the organization avatar

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
body = {"avatar":"string"} # object |  (optional)

try:
    api_response = api_instance.organization_updateAvatar(org_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->organization_updateAvatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_deleteAvatar**
> ErrorResponse organization_deleteAvatar(org_name)



Deletes the uploaded organization avatar

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.organization_deleteAvatar(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->organization_deleteAvatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_createForOrg**
> ErrorResponse apps_createForOrg(org_name, body)



Creates a new app for the organization and returns it to the caller

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
body = {"description":"string","release_type":"string","display_name":"string","name":"string","os":"Android","platform":"Java"} # object | The data for the app

try:
    api_response = api_instance.apps_createForOrg(org_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_createForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **body** | [**object**](object.md)| The data for the app | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_listForOrg**
> ErrorResponse apps_listForOrg(org_name)



Returns a list of apps for the organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.apps_listForOrg(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_listForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aadGroup_listForOrg**
> ErrorResponse aadGroup_listForOrg(org_name)



Returns a list of aad groups that belong to an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.aadGroup_listForOrg(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->aadGroup_listForOrg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_addAADGroups**
> ErrorResponse organization_addAADGroups(org_name, body)



Adds aad groups to an organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
body = {"aad_group_id":"string","tenant_id":"string","display_name":"string"} # object | the AAD group added

try:
    api_response = api_instance.organization_addAADGroups(org_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->organization_addAADGroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **body** | [**object**](object.md)| the AAD group added | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_get**
> ErrorResponse organizations_get(org_name)



Returns the details of a single organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.organizations_get(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_update**
> ErrorResponse organizations_update(org_name, body)



Returns a list of organizations the requesting user has access to

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name
body = {"display_name":"string","name":"string"} # object | The data for the org

try:
    api_response = api_instance.organizations_update(org_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->organizations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 
 **body** | [**object**](object.md)| The data for the org | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_delete**
> ErrorResponse organizations_delete(org_name)



Deletes a single organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
org_name = "string" # string | The organization's name

try:
    api_response = api_instance.organizations_delete(org_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->organizations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_name** | **string**| The organization&#39;s name | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_createOrUpdate**
> ErrorResponse organizations_createOrUpdate(body)



Creates a new organization and returns it to the caller

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
body = {"display_name":"string","name":"string"} # object | The organization data

try:
    api_response = api_instance.organizations_createOrUpdate(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->organizations_createOrUpdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The organization data | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_list**
> ErrorResponse organizations_list()



Returns a list of organizations the requesting user has access to

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.organizations_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->organizations_list: %s\n" % e)
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

# **invitations_sent**
> ErrorResponse invitations_sent()



Returns all invitations sent by the caller

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.invitations_sent()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->invitations_sent: %s\n" % e)
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

# **azureSubscription_listForUser**
> ErrorResponse azureSubscription_listForUser()



Returns a list of azure subscriptions for the user

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.azureSubscription_listForUser()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->azureSubscription_listForUser: %s\n" % e)
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

# **apps_removeUser**
> ErrorResponse apps_removeUser(owner_name, app_name, user_email)



Removes the user from the app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
user_email = "string" # string | The user email of the user to delete

try:
    api_response = api_instance.apps_removeUser(owner_name, app_name, user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_removeUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **user_email** | **string**| The user email of the user to delete | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_updateUserPermissions**
> ErrorResponse apps_updateUserPermissions(owner_name, app_name, user_email, body=body)



Update user permission for the app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
user_email = "string" # string | The user email of the user to patch
body = {"permissions":["manager"]} # object | The value to update the user permission for the app. (optional)

try:
    api_response = api_instance.apps_updateUserPermissions(owner_name, app_name, user_email, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_updateUserPermissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **user_email** | **string**| The user email of the user to patch | 
 **body** | [**object**](object.md)| The value to update the user permission for the app. | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list**
> ErrorResponse users_list(owner_name, app_name)



Returns the users associated with the app specified with the given app name which belongs to the given owner.

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.users_list(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->users_list: %s\n" % e)
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

# **apps_transferToOrg**
> ErrorResponse apps_transferToOrg(owner_name, app_name)



Transfers ownership of an app to a new organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.apps_transferToOrg(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_transferToOrg: %s\n" % e)
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

# **apps_transferOwnership**
> ErrorResponse apps_transferOwnership(owner_name, app_name, destination_owner_name)



Transfers ownership of an app to a different user or organization

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
destination_owner_name = "string" # string | The name of the owner (user or organization) to which the app is being transferred

try:
    api_response = api_instance.apps_transferOwnership(owner_name, app_name, destination_owner_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_transferOwnership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **destination_owner_name** | **string**| The name of the owner (user or organization) to which the app is being transferred | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_listTesters**
> ErrorResponse apps_listTesters(owner_name, app_name)



Returns the testers associated with the app specified with the given app name which belongs to the given owner.

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.apps_listTesters(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_listTesters: %s\n" % e)
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

# **apps_getTeams**
> ErrorResponse apps_getTeams(app_name, owner_name)



Returns the details of all teams that have access to the app.

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
app_name = "string" # string | The name of the application
owner_name = "string" # string | The name of the owner

try:
    api_response = api_instance.apps_getTeams(app_name, owner_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_getTeams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **string**| The name of the application | 
 **owner_name** | **string**| The name of the owner | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appInvitations_createByEmail**
> ErrorResponse appInvitations_createByEmail(owner_name, app_name, user_email)



Invites a new or existing user to an app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
user_email = "string" # string | The email of the user to invite

try:
    api_response = api_instance.appInvitations_createByEmail(owner_name, app_name, user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->appInvitations_createByEmail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **user_email** | **string**| The email of the user to invite | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appInvitations_updatePermissions**
> ErrorResponse appInvitations_updatePermissions(owner_name, app_name, user_email, body=body)



Update pending invitation permission

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
user_email = "string" # string | The email of the user to invite
body = {"permissions":["manager"]} # object | The value to update the user permission in the invite. (optional)

try:
    api_response = api_instance.appInvitations_updatePermissions(owner_name, app_name, user_email, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->appInvitations_updatePermissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **user_email** | **string**| The email of the user to invite | 
 **body** | [**object**](object.md)| The value to update the user permission in the invite. | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appInvitations_delete**
> ErrorResponse appInvitations_delete(owner_name, app_name, user_email)



Removes a user's invitation to an app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
user_email = "string" # string | The email of the user to invite

try:
    api_response = api_instance.appInvitations_delete(owner_name, app_name, user_email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->appInvitations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **user_email** | **string**| The email of the user to invite | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appInvitations_create**
> ErrorResponse appInvitations_create(owner_name, app_name, body=body)



Invites a new or existing user to an app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"user_email":"string","role":"admin"} # object | The email of the user to invite (optional)

try:
    api_response = api_instance.appInvitations_create(owner_name, app_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->appInvitations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The email of the user to invite | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appInvitations_list**
> ErrorResponse appInvitations_list(owner_name, app_name)



Gets the pending invitations for the app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.appInvitations_list(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->appInvitations_list: %s\n" % e)
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

# **distributionGroups_resendInvite**
> ErrorResponse distributionGroups_resendInvite(owner_name, app_name, distribution_group_name, body)



Resend distribution group app invite notification to previously invited testers

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
distribution_group_name = "string" # string | The name of the distribution group
body = {"user_emails":["string"]} # object | The list of members to add

try:
    api_response = api_instance.distributionGroups_resendInvite(owner_name, app_name, distribution_group_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_resendInvite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **body** | [**object**](object.md)| The list of members to add | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_removeUser**
> ErrorResponse distributionGroups_removeUser(owner_name, app_name, distribution_group_name, body)



Remove the users from the distribution group

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
distribution_group_name = "string" # string | The name of the distribution group
body = {"user_emails":["string"]} # object | The list of members to add

try:
    api_response = api_instance.distributionGroups_removeUser(owner_name, app_name, distribution_group_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_removeUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **body** | [**object**](object.md)| The list of members to add | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_listUsers**
> ErrorResponse distributionGroups_listUsers(owner_name, app_name, distribution_group_name, exclude_pending_invitations=exclude_pending_invitations)



Returns a list of member details in the distribution group specified

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
distribution_group_name = "string" # string | The name of the distribution group
exclude_pending_invitations = true # boolean | Whether to exclude pending invitations in the response (optional)

try:
    api_response = api_instance.distributionGroups_listUsers(owner_name, app_name, distribution_group_name, exclude_pending_invitations=exclude_pending_invitations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_listUsers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **exclude_pending_invitations** | **boolean**| Whether to exclude pending invitations in the response | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_addUser**
> ErrorResponse distributionGroups_addUser(owner_name, app_name, distribution_group_name, body)



Adds the members to the specified distribution group

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
distribution_group_name = "string" # string | The name of the distribution group
body = {"user_emails":["string"]} # object | The list of members to add

try:
    api_response = api_instance.distributionGroups_addUser(owner_name, app_name, distribution_group_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_addUser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **body** | [**object**](object.md)| The list of members to add | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_get**
> ErrorResponse distributionGroups_get(owner_name, app_name, distribution_group_name)



Returns a single distribution group for a given distribution group name

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
distribution_group_name = "string" # string | The name of the distribution group

try:
    api_response = api_instance.distributionGroups_get(owner_name, app_name, distribution_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **distribution_group_name** | **string**| The name of the distribution group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_update**
> ErrorResponse distributionGroups_update(owner_name, app_name, distribution_group_name, body)



Updates the attributes of distribution group

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
distribution_group_name = "string" # string | The name of the distribution group
body = {"name":"string","is_public":true} # object | The attributes to update for the distribution group

try:
    api_response = api_instance.distributionGroups_update(owner_name, app_name, distribution_group_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **distribution_group_name** | **string**| The name of the distribution group | 
 **body** | [**object**](object.md)| The attributes to update for the distribution group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_delete**
> ErrorResponse distributionGroups_delete(app_name, owner_name, distribution_group_name)



Deletes a distribution group

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
app_name = "string" # string | The name of the application
owner_name = "string" # string | The name of the owner
distribution_group_name = "string" # string | The name of the distribution group

try:
    api_response = api_instance.distributionGroups_delete(app_name, owner_name, distribution_group_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **string**| The name of the application | 
 **owner_name** | **string**| The name of the owner | 
 **distribution_group_name** | **string**| The name of the distribution group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distributionGroups_list**
> ErrorResponse distributionGroups_list(owner_name, app_name)



Returns a list of distribution groups in the app specified

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.distributionGroups_list(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_list: %s\n" % e)
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

# **distributionGroups_create**
> ErrorResponse distributionGroups_create(owner_name, app_name, body)



Creates a new distribution group and returns it to the caller

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"name":"string","display_name":"string"} # object | The attributes to update for the distribution group

try:
    api_response = api_instance.distributionGroups_create(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->distributionGroups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The attributes to update for the distribution group | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **azureSubscription_deleteForApp**
> ErrorResponse azureSubscription_deleteForApp(azure_subscription_id, owner_name, app_name)



Delete the azure subscriptions for the app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
azure_subscription_id = "string" # string | The unique ID (UUID) of the azure subscription
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.azureSubscription_deleteForApp(azure_subscription_id, owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->azureSubscription_deleteForApp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_subscription_id** | **string**| The unique ID (UUID) of the azure subscription | 
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

# **azureSubscription_listForApp**
> ErrorResponse azureSubscription_listForApp(owner_name, app_name)



Returns a list of azure subscriptions for the app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.azureSubscription_listForApp(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->azureSubscription_listForApp: %s\n" % e)
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

# **azureSubscription_linkForApp**
> ErrorResponse azureSubscription_linkForApp(owner_name, app_name, body)



Link azure subscription to an app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"subscription_id":"string"} # object | The azure subscription data needed to be link to the app.

try:
    api_response = api_instance.azureSubscription_linkForApp(owner_name, app_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->azureSubscription_linkForApp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)| The azure subscription data needed to be link to the app. | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_updateAvatar**
> ErrorResponse apps_updateAvatar(owner_name, app_name, body=body)



Sets the app avatar

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application
body = {"avatar":"string"} # object |  (optional)

try:
    api_response = api_instance.apps_updateAvatar(owner_name, app_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_updateAvatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_name** | **string**| The name of the owner | 
 **app_name** | **string**| The name of the application | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_deleteAvatar**
> ErrorResponse apps_deleteAvatar(owner_name, app_name)



Deletes the uploaded app avatar

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.apps_deleteAvatar(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_deleteAvatar: %s\n" % e)
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

# **apps_get**
> ErrorResponse apps_get(owner_name, app_name)



Return a specific app with the given app name which belongs to the given owner.

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
owner_name = "string" # string | The name of the owner
app_name = "string" # string | The name of the application

try:
    api_response = api_instance.apps_get(owner_name, app_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_get: %s\n" % e)
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

# **apps_update**
> ErrorResponse apps_update(app_name, owner_name, body=body)



Partially updates a single app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
app_name = "string" # string | The name of the application
owner_name = "string" # string | The name of the owner
body = {"description":"string","display_name":"string","release_type":"string","name":"string","icon_url":"string"} # object | The partial data for the app (optional)

try:
    api_response = api_instance.apps_update(app_name, owner_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **string**| The name of the application | 
 **owner_name** | **string**| The name of the owner | 
 **body** | [**object**](object.md)| The partial data for the app | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_delete**
> ErrorResponse apps_delete(app_name, owner_name)



Delete an app

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
app_name = "string" # string | The name of the application
owner_name = "string" # string | The name of the owner

try:
    api_response = api_instance.apps_delete(app_name, owner_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_name** | **string**| The name of the application | 
 **owner_name** | **string**| The name of the owner | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_create**
> ErrorResponse apps_create(body)



Creates a new app and returns it to the caller

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
body = {"description":"string","release_type":"string","display_name":"string","name":"string","os":"Android","platform":"Java"} # object | The data for the app

try:
    api_response = api_instance.apps_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| The data for the app | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_list**
> ErrorResponse apps_list($orderBy=$orderBy)



Returns a list of apps

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
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
$orderBy = "display_name" # string | The name of the attribute by which to order the response by. By default, apps are in order of creation. All results are ordered in ascending order. (optional)

try:
    api_response = api_instance.apps_list($orderBy=$orderBy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apps_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **$orderBy** | **string**| The name of the attribute by which to order the response by. By default, apps are in order of creation. All results are ordered in ascending order. | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiTokens_delete**
> ErrorResponse apiTokens_delete(api_token_id)



Delete the api_token object with the specific id

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = appcenter_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
api_token_id = "string" # string | The unique ID (UUID) of the api token

try:
    api_response = api_instance.apiTokens_delete(api_token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apiTokens_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token_id** | **string**| The unique ID (UUID) of the api token | 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiTokens_list**
> ErrorResponse apiTokens_list()



Returns api tokens for the authenticated user

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = appcenter_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))

try:
    api_response = api_instance.apiTokens_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apiTokens_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ErrorResponse**](object.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data, application/json-patch+json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiTokens_new**
> ErrorResponse apiTokens_new(body=body)



Creates a new API token

### Example
```python
from __future__ import print_function
import time
import appcenter_sdk
from appcenter_sdk.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: Basic
configuration = appcenter_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = appcenter_sdk.accountApi(appcenter_sdk.ApiClient(configuration))
body = {"description":"string","scope":["all"]} # object | Description of the token (optional)

try:
    api_response = api_instance.apiTokens_new(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling accountApi->apiTokens_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Description of the token | [optional] 

### Return type

[**ErrorResponse**](object.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

