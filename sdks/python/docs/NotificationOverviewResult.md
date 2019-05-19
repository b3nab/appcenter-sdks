# NotificationOverviewResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_id** | **string** | Notification id. | 
**name** | **string** | Notification name | [optional] 
**notification_target** | [**object**](.md) | Type of Notification target (audiences, devices, user ids or account ids). The object must include the correct properties for the specified target type. | [optional] 
**send_time** | **string** | Notification send time | [optional] 
**pns_send_failure** | **integer** | Number of the notifications failed to send to the push provider. | [optional] 
**pns_send_success** | **integer** | Number of the notifications successfully sent to push the provider. | [optional] 
**state** | **string** | State of the notification. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

