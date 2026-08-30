plugins {
    id("com.android.application")
    id("dev.flutter.flutter-gradle-plugin")
}

android {
    namespace = "com.ahmed.streamv21"
    compileSdk = 37

    defaultConfig {
        applicationId = "com.ahmed.streamv21"
        minSdk = 24
        targetSdk = 37
        versionCode = 21
        versionName = "21.0.0"
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("debug")
        }
    }
}

flutter {
    source = "../.."
}
