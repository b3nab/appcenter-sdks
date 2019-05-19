# DistributionGroupRelease

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **integer** | ID identifying this unique release. | [optional] 
**version** | **string** | The release&#39;s version.&lt;br&gt;
For iOS: CFBundleVersion from info.plist.&lt;br&gt;
For Android: android:versionCode from AppManifest.xml.
 | [optional] 
**short_version** | **string** | The release&#39;s short version.&lt;br&gt;
For iOS: CFBundleShortVersionString from info.plist.&lt;br&gt;
For Android: android:versionName from AppManifest.xml.
 | [optional] 
**mandatory_update** | **boolean** | A boolean which determines whether the release is a mandatory update or not. | [optional] 
**uploaded_at** | **string** | UTC time in ISO 8601 format of the uploaded time. | [optional] 
**enabled** | **boolean** | This value determines the whether a release currently is enabled or disabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

