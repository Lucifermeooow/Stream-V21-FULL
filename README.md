# Stream V21

GitHub-ready Flutter Android live-streaming client.

## What is included

- Camera + microphone permissions.
- Camera preview.
- RTMP publishing from the phone.
- 1080p-class `ResolutionPreset.high` capture with 30 FPS target and 1500 kbps video / 128 kbps audio defaults.
- Start / stop live controls.
- Camera switching.
- Microphone mute/unmute.
- Screen wakelock while live.
- Basic live statistics: bitrate, FPS and RTT when the RTMP plugin exposes them.
- YouTube / Facebook / TikTok destination switches as server-routing configuration.
- HTTPS OAuth backend buttons for `/auth/youtube/start`, `/auth/facebook/start`, `/auth/tiktok/start`.
- GitHub Actions workflow that installs Android API 37, pins Flutter 3.47.2, runs format/analyze/tests, and builds a release APK.

## Important architecture

The Android app publishes **one** RTMP stream to your media server. The server is responsible for fan-out to YouTube, Facebook and TikTok. The destination switches in the app are configuration/UI only; they do not fake provider APIs.

OAuth client secrets, access tokens, refresh tokens and stream keys must stay on the backend. Do not commit them to GitHub.

## Local build

```bash
flutter pub get
flutter analyze
flutter test
flutter build apk --release
```

APK:

`build/app/outputs/flutter-apk/app-release.apk`

## GitHub

1. Create an empty GitHub repository.
2. Copy the contents of this folder into it.
3. Push to the `main` branch.
4. Open **Actions** → **Build Stream V21 APK**.
5. Download the `Stream-V21-APK` artifact after a successful build.

## Backend

The app expects an HTTPS backend with these entry points:

- `GET /auth/youtube/start`
- `GET /auth/facebook/start`
- `GET /auth/tiktok/start`

The repository does not include fake OAuth credentials or pretend provider integrations. Implement the real provider OAuth/API flows on a secure backend and keep secrets in GitHub Actions secrets or your server secret manager.

## Toolchain decision

The previous build failed because `rtmp_streaming`/RootEncoder required Android API 37 while the project compiled against API 36. Stream V21 compiles against API 37 and uses AGP 9.1.1 + Gradle 9.3.1-compatible tooling. Android documents AGP 9.1.1 as supporting API 37, and the plugin itself now uses RootEncoder 2.8.0 in its 2.x line.
