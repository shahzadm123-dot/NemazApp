[app]
title = Nemaz Times Rajjar Charsadda
package.name = nemaztimes
package.domain = org.rajjar
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,csv
source.exclude_exts = spec
requirements = python3,kivy==2.1.0
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
android.accept_sdk_license = True
orientation = portrait
version = 0.1
android.archs = armeabi-v7a
android.minapi = 24
android.gradle_dependencies =
[buildozer]
log_level = 2
warn_on_root = 1
