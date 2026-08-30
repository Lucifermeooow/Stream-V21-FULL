# Stream V21 — Agent Instructions

## Current state
This repository is a Flutter Android live-streaming application. The goal of the current branch is to preserve the existing UI and streaming behavior while making the Android/GitHub Actions toolchain build reliably.

## Streaming library
- Dart dependency: `rtmp_streaming: 2.0.1` (pinned exactly).
- Android implementation is based on RootEncoder 2.8.0.
- Do not invent or change rtmp_streaming APIs. Use the package's published API and documentation.
- Current app flow uses `initialize`, `CameraPreview`, encoder settings, `startVideoStreaming`, `stopVideoStreaming`, camera switching, audio mute, and stream statistics.

## Important Android/build rules
- Use Java 17.
- Use Android Gradle Plugin 9.3.1.
- Use Gradle 9.5.0.
- Use Kotlin 2.4.10.
- AGP 9 requires the new DSL; keep `android.newDsl=true` and `android.builtInKotlin=true`.
- Android compile/target SDK is 37.
- JitPack is required because RootEncoder is published as a GitHub/JitPack dependency.
- Gradle file watching is disabled in this project to avoid the GitHub runner watcher conflict seen previously.

## GitHub Actions
The workflow is `.github/workflows/build-apk.yml`.
It should:
1. install Java 17 and Flutter 3.47.2,
2. accept Android licenses,
3. generate `android/local.properties` on the runner,
4. run `flutter pub get`,
5. precache Android artifacts,
6. patch only the obsolete `kotlinOptions` block in the cached rtmp_streaming Android build file,
7. run `flutter analyze`,
8. run the lightweight repository test suite,
9. build a release APK,
10. upload `Stream-V21-release.apk` as the GitHub Actions artifact `Stream-V21-APK`.

## Secrets
Never place RTMP stream keys, passwords, OAuth secrets, access tokens, or other credentials in the repository or AGENTS.md.

## Scope discipline
Do not redesign the application or change product behavior while fixing build issues. Prefer deterministic, source-backed changes over bypass flags such as `--android-skip-build-dependency-validation`.
