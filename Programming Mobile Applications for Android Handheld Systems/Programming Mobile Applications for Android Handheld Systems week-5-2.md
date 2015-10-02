# Broadcast Receivers

- [BroadcastReceiver](http://developer.android.com/reference/android/content/BroadcastReceiver.html)

Typical use case:

1. [BroadcastReceiver](http://developer.android.com/reference/android/content/BroadcastReceiver.html)s register to receive specific intents.
2. Some component generates an intent and then broadcasts it to the system.
3. Android delivers that intent to the [BroadcastReceiver](http://developer.android.com/reference/android/content/BroadcastReceiver.html)'s registered to receive it.
4. The [BroadcastReceiver](http://developer.android.com/reference/android/content/BroadcastReceiver.html)s then get a call to their `onReceive()` method during which they handle the incoming event.

[BroadcastReceiver](http://developer.android.com/reference/android/content/BroadcastReceiver.html)s can register in two ways:

1. Statically, in `AndroidManaifest.xml`.

  - [receiver element](http://developer.android.com/guide/topics/manifest/receiver-element.html)
  - [intent-filter element](http://developer.android.com/guide/topics/manifest/intent-filter-element.html)

2. Dynamically, by calling a `registerReceiver()` method.

  - [IntentFilter](http://developer.android.com/reference/android/content/IntentFilter.html)
  - [LocalBroadcastManager](http://developer.android.com/reference/android/support/v4/content/LocalBroadcastManager.html)
  - [Context#registerReceiver](http://developer.android.com/reference/android/content/Context.html#registerReceiver(android.content.BroadcastReceiver, android.content.IntentFilter))

Intents can be broadcast normally or in-order. Normal broadcasts are delivered to subscribed [BroadcastReceiver](http://developer.android.com/reference/android/content/BroadcastReceiver.html)s in an undefined order. Ordered broadcasts deliver the intent to multiple [BroadcastReceiver](http://developer.android.com/reference/android/content/BroadcastReceiver.html)s one at a time in priority order.

Broadcasts can also be sticky or non-sticky. A sticky broadcast sticks around after its initial broadcast. Non-sticky broadcasts are discarded after their initial broadcast.

**Some debugging tips**

- Log extra intent resolution information by setting `Intent.setFlag(FLAG_DEBUG_LOG_RESOLUTION)`
- List registered [BroadcastReceiver](http://developer.android.com/reference/android/content/BroadcastReceiver.html)s
  - Dynamically registered, `$ adb shell dumpsys activity b`
  - Statically registered, `$ adb shell dumpsys package`