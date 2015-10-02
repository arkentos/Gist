# User Notifications

Notifications are messages that applications show to users outside the normal user interface of the application.

Two different kinds of user notifications that Android supports:

1. [Toasts](http://developer.android.com/guide/topics/ui/notifiers/toasts.html)
2. [Notification Area Notifications](http://developer.android.com/guide/topics/ui/notifiers/notifications.html)

For user feedback you can use:

- [Toasts](http://developer.android.com/guide/topics/ui/notifiers/toasts.html)
- [Dialogs](http://developer.android.com/guide/topics/ui/dialogs.html)

For event notifications you can use:

- [Notification Area Notifications](http://developer.android.com/guide/topics/ui/notifiers/notifications.html)

## Toast

Toast messages are temporary messages that pop-up on the display. They automatically fade in and fade out of view.

- [Toast.makeText](http://developer.android.com/reference/android/widget/Toast.html#makeText(android.content.Context, java.lang.CharSequence, int))
- [show](http://developer.android.com/reference/android/widget/Toast.html#show())
- [Creating a Custom Toast View](http://developer.android.com/guide/topics/ui/notifiers/toasts.html#CustomToastView)

## Notification Area Notifications

This kind of user notification appears in the system controlled area at the top of the device called the notification area or the status bar. Applications and the Android system itself can use this area to inform users about the occurrence of various events.

- [Creating a Notification](http://developer.android.com/guide/topics/ui/notifiers/notifications.html#CreateNotification)
- [Notification](http://developer.android.com/reference/android/app/Notification.html)
- [NotificationCompat](http://developer.android.com/reference/android/support/v4/app/NotificationCompat.html)
- [NotificationManager](http://developer.android.com/reference/android/app/NotificationManager.html)
- [Notification Design Guidelines](http://developer.android.com/design/patterns/notifications.html)

A pending intent is essentially a permission slip that allows one piece of code to stand in for another piece of code. This permission slip allows the second piece of code to activate the underlying intent as if it were the first piece of code, i.e. it does it with the permissions and identity of that first piece of code.

- [Using a Pending Intent](http://developer.android.com/guide/components/intents-filters.html#PendingIntent)
- [PendingIntent](http://developer.android.com/reference/android/app/PendingIntent.html)