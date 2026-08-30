# Stream V21 modifications

- Renamed the project/application metadata from V19 to V21.
- Updated Android package/application id to `com.ahmed.streamv21`.
- Updated AGP/Kotlin/Gradle toolchain to AGP 9.3.1, Kotlin 2.4.10, Gradle 9.5.0, with AGP 9 new DSL and built-in Kotlin enabled.
- Disabled Gradle file watching to avoid the previously observed GitHub runner watcher collision.
- Added deterministic GitHub Actions build configuration.
- Added a narrowly scoped build-time patch for the obsolete `kotlinOptions` block in `rtmp_streaming 2.0.1`.
- Replaced the old render test that assumed a `MyApp` class and camera/plugin initialization with a lightweight deterministic test, so the test suite does not depend on platform channels.
- No stream keys, OAuth secrets, passwords, or access tokens were added.
