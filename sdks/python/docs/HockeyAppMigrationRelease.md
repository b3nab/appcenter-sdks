# HockeyAppMigrationRelease

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] 
**shortversion** | **string** |  | [optional] 
**version** | **string** |  | [optional] 
**appsize** | **integer** |  | [optional] 
**minimum_os_version** | **string** |  | [optional] 
**md5_fingerprint** | **string** |  | [optional] 
**created_at** | **string** |  | [optional] 
**build_url** | **string** |  | [optional] 
**bundle_identifier** | **string** |  | [optional] 
**device_family** | **string** |  | [optional] 
**languages** | [**array**](.md) |  | [optional] 
**uuids** | [**object**](.md) | For iOS apps, a dictionary of UUIDs for architectures (in format `{&quot;armv7&quot;: &quot;353df799-d450-3308-8492-928ecf1ebf53&quot;, &quot;arm64&quot;: &quot;e67c0e93-b6d6-3f5a-b3a7-68d2b215bf27&quot;}`) | [optional] 
**is_external_build** | **boolean** |  | [optional] 
**mandatory** | **boolean** |  | [optional] 
**status** | **integer** | The status of the release in HockeyApp. Maps to HockeyAppSchema.AppVersionStatus. Possible values: Deleted = -1, New = 0, Inactive = 1, Active = 2, Hidden = 3, SonomaActive = 4 | [optional] 
**notes** | **string** |  | [optional] 
**distribution_group_ids** | [**array**](.md) | List of DistributionGroup IDs the release is distributed to | [optional] 
**distribution_user_ids** | [**array**](.md) | List of User IDs the release is distributed to | [optional] 
**provisioning_profiles** | [**array**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

