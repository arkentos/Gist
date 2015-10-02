# Introduction to the Android Platform

[Getting Started](http://developer.android.com/training/index.html)

**The Android Architecture (bottom to top)**

- Linux Kernel
- Libraries & Android Runtime
- Application Framework
- Applications

**Typical Workflow**

- Application is written in Java
- Compiled to Java bytecode files
- DX converts Java bytecode files to a single dex bytecode file (classes.dex)
- The dex file is packaged with other application resources and installed on the device
- Dalvik VM executes the dex bytecode file

[Dalvik VM Internals by Dan Bornstein](http://www.youtube.com/watch?v=ptjedOZEXPM)

# The Android Development Environment

The Android Development Environment is your workbench for creating Android applications. Like any skilled crafts person, the more comfortable you are with your tools the easier it's going to be to produce top quality work.

**Resources**

- [Package Index - The Android APIs](http://developer.android.com/reference/packages.html)
- [Android SDK](http://developer.android.com/sdk/index.html)
- [Java Development Kit (JDK6)](http://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase6-419409.html)
- [AVDs and the AVD Manager](http://developer.android.com/tools/devices/managing-avds.html)
- [Using the Emulator](http://developer.android.com/tools/devices/emulator.html)
  - [Using the Emulator Console](http://developer.android.com/tools/devices/emulator.html#console)
- [Debugging](http://developer.android.com/tools/debugging/index.html)
  - [Java Debugging with Eclipse](http://www.vogella.com/tutorials/EclipseDebugging/article.html)
  - [Log](http://developer.android.com/reference/android/util/Log.html)
  - [Dalvik Debug Monitor Server (DDMS)](http://developer.android.com/tools/debugging/ddms.html)
  - [Profiling with Traceview and dmtracedump](http://developer.android.com/tools/debugging/debugging-tracing.html)
  - [Using Hierarchy Viewer](http://developer.android.com/tools/debugging/debugging-ui.html)