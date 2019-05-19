# AppInvitationDetailResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | The unique ID (UUID) of the invitation | 
**app** | **** |  | 
**email** | **string** | The email address of the invited user | 
**invite_type** | **string** | The invitation type | 
**invited_by** | **** |  | 
**is_existing_user** | **boolean** | Indicates whether the invited user already exists | 
**permissions** | [**array**](.md) | The permissions the user has for the app | [optional] 
**app_count** | **number** | The number of apps in the group | [optional] 
**distribution_group** | [**object**](.md) | The organization that owns the distribution group, if it exists | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

