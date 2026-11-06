[app]

title = CRIS CHAT
package.name = crischat
package.domain = org.cris
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.sdk = 30
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

p4c_debug = 2
