# ReleaseCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **string** | The display name of the app, extracted from the build. | 
**version** | **string** | The release&#39;s version.&lt;br&gt;
For iOS: CFBundleVersion from info.plist.&lt;br&gt;
For Android: android:versionCode from AppManifest.xml.
 | 
**build_version** | **string** | The release&#39;s short version.&lt;br&gt;
For iOS: CFBundleShortVersionString from info.plist.&lt;br&gt;
For Android: android:versionName from AppManifest.xml.
 | 
**unique_identifier** | **string** | The identifier of the app&#39;s bundle. | 
**minimum_os_version** | **string** | The release&#39;s minimum required operating system. | 
**device_family** | **string** | The release&#39;s device family. | [optional] 
**languages** | [**array**](.md) | The languages supported by the release. | [optional] 
**fingerprint** | **string** | MD5 checksum of the release binary. | 
**size** | **integer** | The release&#39;s size in bytes. | 
**package_url** | **string** | The URL to the release&#39;s binary. | 
**upload_id** | **string** | The upload id associated with the release, to map to the releases upload table. | 
**icon_url** | **string** | The URL to the release&#39;s icon. | [optional] 
**ipa_uuids** | [**array**](.md) | A list of UUIDs for architectures for an iOS app. | [optional] 
**provision** | [**object**](.md) | An object containing information about an iOS provisioning profile. | [optional] 
**appex_provisioning_profiles** | [**array**](.md) | iOS app extension provisioning profiles included in the release. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

