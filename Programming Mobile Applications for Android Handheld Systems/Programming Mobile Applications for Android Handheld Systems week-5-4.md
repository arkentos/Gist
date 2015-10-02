# Alarms

Alarms are a mechanism for sending intents at some point (or points) in the future. This is useful because it allows an application to cause some other code to execute, even when that application is no longer running. Once alarms have been created and registered they are retained and monitored even if the device goes to sleep.

**Alarm examples**

- MMS - Retry scheduler
- Settings - Bluetooth discoverable timeout
- Phone - User info cache

## Using Alarms

To use alarms you do so by interacting with the [AlarmManager](http://developer.android.com/reference/android/app/AlarmManager.html). You do not instantiate this class directly; instead, retrieve it through [Context.getSystemService(Context.ALARM_SERVICE)](http://developer.android.com/reference/android/content/Context.html#getSystemService(java.lang.String)).