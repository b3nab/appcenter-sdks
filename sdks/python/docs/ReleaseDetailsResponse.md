# ReleaseDetailsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **integer** | ID identifying this unique release. | [optional] 
**app_name** | **string** | The app&#39;s name (extracted from the uploaded release). | [optional] 
**app_display_name** | **string** | The app&#39;s display name. | [optional] 
**version** | **string** | The release&#39;s version.&lt;br&gt;
For iOS: CFBundleVersion from info.plist.
For Android: android:versionCode from AppManifest.xml.
 | [optional] 
**short_version** | **string** | The release&#39;s short version.&lt;br&gt;
For iOS: CFBundleShortVersionString from info.plist.
For Android: android:versionName from AppManifest.xml.
 | [optional] 
**release_notes** | **string** | The release&#39;s release notes. | [optional] 
**provisioning_profile_name** | **string** | The release&#39;s provisioning profile name. | [optional] 
**provisioning_profile_type** | **string** | The type of the provisioning profile for the requested app version. | [optional] 
**provisioning_profile_expiry_date** | **string** | expiration date of provisioning profile in UTC format. | [optional] 
**is_provisioning_profile_syncing** | **boolean** | A flag that determines whether the release&#39;s provisioning profile is still extracted or not. | [optional] 
**size** | **integer** | The release&#39;s size in bytes. | [optional] 
**min_os** | **string** | The release&#39;s minimum required operating system. | [optional] 
**device_family** | **string** | The release&#39;s device family. | [optional] 
**android_min_api_level** | **string** | The release&#39;s minimum required Android API level. | [optional] 
**bundle_identifier** | **string** | The identifier of the apps bundle. | [optional] 
**fingerprint** | **string** | MD5 checksum of the release binary. | [optional] 
**uploaded_at** | **string** | UTC time in ISO 8601 format of the uploaded time. | [optional] 
**download_url** | **string** | The URL that hosts the binary for this release. | [optional] 
**app_icon_url** | **string** | A URL to the app&#39;s icon. | [optional] 
**install_url** | **string** | The href required to install a release on a mobile device. On iOS devices will be prefixed with `itms-services://?action=download-manifest&amp;url=` | [optional] 
**destination_type** | **string** | OBSOLETE. Will be removed in next version. The destination type.&lt;br&gt;
&lt;b&gt;group&lt;/b&gt;: The release distributed to internal groups and distribution_groups details will be returned.&lt;br&gt;
&lt;b&gt;store&lt;/b&gt;: The release distributed to external stores and distribution_stores details will be returned.&lt;br&gt;
&lt;b&gt;tester&lt;/b&gt;: The release distributed testers details will be returned.&lt;br&gt;
 | [optional] 
**distribution_groups** | [**array**](.md) | OBSOLETE. Will be removed in next version. A list of distribution groups that are associated with this release. | [optional] 
**distribution_stores** | [**array**](.md) | OBSOLETE. Will be removed in next version. A list of distribution stores that are associated with this release. | [optional] 
**destinations** | [**array**](.md) | A list of distribution groups or stores. | [optional] 
**is_udid_provisioned** | **boolean** | In calls that allow passing `udid` in the query string, this value will hold the provisioning status of that UDID in this release. Will be ignored for non-iOS platforms. | [optional] 
**can_resign** | **boolean** | In calls that allow passing `udid` in the query string, this value determines if a release can be re-signed. When true, after a re-sign, the tester will be able to install the release from his registered devices. Will not be returned for non-iOS platforms. | [optional] 
**build** | [**object**](.md) | Contains metadata about the build that produced the release being uploaded | [optional] 
**enabled** | **boolean** | This value determines the whether a release currently is enabled or disabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

