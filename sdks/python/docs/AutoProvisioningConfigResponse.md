# AutoProvisioningConfigResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** | The identifier of the config. | [optional] 
**app_id** | **string** | The identifier of the App. | [optional] 
**destination_id** | **string** | The identifier of the destination. | [optional] 
**apple_developer_account_key** | **string** | A key to a secret in customer-credential-store. apple_developer_account refers to the user&#39;s developer account that is used to log into https://developer.apple.com. Normally the user&#39;s email. | [optional] 
**apple_distribution_certificate_key** | **string** | A key to a secret in customer-credential-store. distribution_certificate refers to the cusomer&#39;s certificate (that holds the private key) that will be used to sign the app. | [optional] 
**allow_auto_provisioning** | **boolean** | When *true* enables auto provisioning | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

