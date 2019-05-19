# TestCloudHashUploadStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_cloud_hash_upload_status** | [**object**](.md) | Result of uploading a single file hash | [optional] 
**status_code** | **number** | HTTP status code that represent result of upload | [optional] 
**location** | **string** | URI that should be used to make POST request if file with given hash doesn&#39;t exist. This is set when status_code is equal to 412 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

