# DistributionGroupWithUsersResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | The unique ID of the distribution group | 
**name** | **string** | The name of the distribution group used in URLs | 
**total_user_count** | **number** | The count of users in the distribution group | 
**total_groups_count** | **number** | The count of aad groups in the distribution group | [optional] 
**notified_user_count** | **number** | The count of non-pending users in the distribution group who will be notified by new releases | 
**is_public** | **boolean** | Whether the distribution group is public | [optional] 
**users** | [**array**](.md) | The distribution group users | 
**aad_groups** | [**array**](.md) | The distribution group aad groups | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

