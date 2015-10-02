# Application Fundamentals

Core [application components](http://developer.android.com/guide/components/index.html) include:

- [Activities](http://developer.android.com/guide/components/activities.html)
- [Services](http://developer.android.com/guide/components/services.html)
- [Broadcast Receivers](http://developer.android.com/reference/android/content/BroadcastReceiver.html)
- [Content Providers](http://developer.android.com/guide/topics/providers/content-providers.html)

**Resources**

- [The Build Process](http://developer.android.com/tools/building/index.html)
- [App Resources](http://developer.android.com/guide/topics/resources/index.html)
  - [String Resources](http://developer.android.com/guide/topics/resources/string-resource.html)
  - [Layout Resource](http://developer.android.com/guide/topics/resources/layout-resource.html)
  - [Accessing Resources](http://developer.android.com/guide/topics/resources/accessing-resources.html)
- [Code Style Guidelines](https://source.android.com/source/code-style.html)

# The Activity Class

- [Activities](http://developer.android.com/guide/components/activities.html)
- [Tasks and Back Stack](http://developer.android.com/guide/components/tasks-and-back-stack.html)

## Configuration Changes

Device configuration can change at runtime. For e.g. keyboard, orientation and locale.

- [Handling Runtime Changes](http://developer.android.com/guide/topics/resources/runtime-changes.html)
- [Activity - Configuration Changes](http://developer.android.com/reference/android/app/Activity.html#ConfigurationChanges)
- [Manual Reconfiguration](http://developer.android.com/guide/topics/resources/runtime-changes.html#HandlingTheChange)
  - [onConfigurationChanged](http://developer.android.com/reference/android/app/Activity.html#onConfigurationChanged(android.content.res.Configuration))

**N.B.** [onRetainNonConfigurationInstance](http://developer.android.com/reference/android/app/Activity.html#onRetainNonConfigurationInstance()) was deprecated in API Level 13.