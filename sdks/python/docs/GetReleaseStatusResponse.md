# GetReleaseStatusResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **string** | The ID for the upload. | 
**upload_url** | **string** | The URL used to upload the release. | 
**upload_status** | **string** | The current upload status. | 
**error_details** | **string** | Details describing what went wrong processing the upload. Will only be set if status = &#39;error&#39;. | [optional] 
**release_distinct_id** | **number** | The distinct ID of the release. Will only be set when the status = &#39;readyToBePublished&#39;. | [optional] 
**release_url** | **** | The URL of the release. Will only be set when the status = &#39;readyToBePublished&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

