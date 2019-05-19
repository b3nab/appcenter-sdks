# BasicReleaseDetailsResponse

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
**enabled** | **boolean** | This value determines the whether a release currently is enabled or disabled. | [optional] 
**uploaded_at** | **string** | UTC time in ISO 8601 format of the uploaded time. | [optional] 
**destination_type** | **string** | OBSOLETE. Will be removed in next version. The destination type.&lt;br&gt;
&lt;b&gt;group&lt;/b&gt;: The release distributed to internal groups and distribution_groups details will be returned.&lt;br&gt;
&lt;b&gt;store&lt;/b&gt;: The release distributed to external stores and distribution_stores details will be returned. &lt;br&gt;
 | [optional] 
**distribution_groups** | [**array**](.md) | OBSOLETE. Will be removed in next version. A list of distribution groups that are associated with this release. | [optional] 
**distribution_stores** | [**array**](.md) | OBSOLETE. Will be removed in next version. A list of distribution stores that are associated with this release. | [optional] 
**destinations** | [**array**](.md) | A list of distribution groups or stores. | [optional] 
**build** | [**object**](.md) | Contains metadata about the build that produced the release being uploaded | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

