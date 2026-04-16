[app]
title = System Security Service
package.name = pantauapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml
version = 0.1

# Izin yang sangat penting
android.permissions = INTERNET, CAMERA, RECORD_AUDIO, BIND_DEVICE_ADMIN

# Supaya folder 'res' ikut terbungkus
android.add_resources = res

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a
