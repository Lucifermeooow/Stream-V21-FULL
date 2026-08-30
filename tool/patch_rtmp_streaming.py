from pathlib import Path
import re
import sys

if len(sys.argv) != 2:
    raise SystemExit("Usage: patch_rtmp_streaming.py <android/build.gradle>")

path = Path(sys.argv[1])
text = path.read_text()

# AGP 9 uses the new Kotlin compilerOptions DSL; replace only the old block.
pattern = re.compile(r"(?ms)^\s*kotlinOptions\s*\{\s*jvmTarget\s*=\s*['\"]17['\"]\s*\}\s*$")
replacement = '''    kotlin {
        compilerOptions {
            jvmTarget = org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_17
        }
    }'''

new_text, count = pattern.subn(replacement, text, count=1)
if count != 1:
    raise SystemExit("Expected kotlinOptions { jvmTarget = \"17\" } block was not found")

if 'maven { url' not in new_text or 'jitpack.io' not in new_text:
    new_text = new_text.replace(
        "repositories {\n    google()\n    mavenCentral()\n}",
        "repositories {\n    google()\n    mavenCentral()\n    maven { url 'https://jitpack.io' }\n}",
        1,
    )

path.write_text(new_text)
print(f"Patched {path}")
