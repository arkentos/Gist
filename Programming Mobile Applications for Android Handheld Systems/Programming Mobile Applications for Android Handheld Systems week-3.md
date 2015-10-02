# The Intent Class

An intent is an abstract description of an operation to be performed.

**Intent Fields**

- Action
- Data
- Category
- Type
- Component
- Extras
- Flags

**Resources**

- [Interacting with Other Apps](http://developer.android.com/training/basics/intents/index.html)
- [Integrating Application with Intents](http://android-developers.blogspot.com/2009/11/integrating-application-with-intents.html)
- [Intents and Intent Filters](http://developer.android.com/guide/components/intents-filters.html)
- [Common Intents](http://developer.android.com/guide/components/intents-common.html)
- [The Intent Class](http://developer.android.com/reference/android/content/Intent.html)

To learn/investigate more about Intent Filters look at the following command:

```
$ adb shell dumpsys package
```

# Permissions

Android uses permissions to protect data, resources and operations.

- [uses-permission element](http://developer.android.com/guide/topics/manifest/uses-permission-element.html)

Applications can also define and enforce their own permissions.

- [permission element](http://developer.android.com/guide/topics/manifest/permission-element.html)

**Resources**

- [Permissions](http://developer.android.com/guide/topics/manifest/manifest-intro.html#perms)
- [A list of built-in permissions](http://developer.android.com/reference/android/Manifest.permission.html)
- [System Permissions](http://developer.android.com/guide/topics/security/permissions.html)
- [Security Tips](http://developer.android.com/training/articles/security-tips.html)

# The Fragment Class

Fragments were added to Android in version 3.0 to better support user interfaces for devices with large screens such as tablets. They represent a portion of an activity's user interface. Fragments have a lifecycle which is coordinated with the lifecycle of its containing activity.

## Configuration Changes

If you call `setRetainInstance(true)`, Android won't destroy the fragment on configuration changes.

**Resources**

- [Fragments](http://developer.android.com/guide/components/fragments.html)
- [Creating a Fragment](http://developer.android.com/guide/components/fragments.html#Creating)
- [The Fragment Lifecycle](http://developer.android.com/guide/components/fragments.html#Lifecycle)
- [Building a Dynamic UI with Fragments](http://developer.android.com/training/basics/fragments/index.html)