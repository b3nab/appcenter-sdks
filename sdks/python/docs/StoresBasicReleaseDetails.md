# StoresBasicReleaseDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** | ID identifying this unique release. | [optional] 
**version** | **string** | The release&#39;s version.
For iOS: CFBundleVersion from info.plist.
For Android: android:versionCode from AppManifest.xml.
 | [optional] 
**short_version** | **string** | The release&#39;s short version.
For iOS: CFBundleShortVersionString from info.plist.
For Android: android:versionName from AppManifest.xml.
 | [optional] 
**uploaded_at** | **string** | UTC time in ISO 8601 format of the uploaded time. | [optional] 
**distribution_stores** | [**array**](.md) | a list of distribution stores that are associated with this release. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

