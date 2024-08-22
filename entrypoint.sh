#!/bin/bash

set -eux

git clone https://github.com/Docile-Alligator/Infinity-For-Reddit

wget -P ./Infinity-For-Reddit/app "https://github.com/TanukiAI/Infinity-keystore/raw/main/Infinity.jks"

python3 script.py

cd Infinity-For-Reddit

./gradlew clean updateLintBaseline
./gradlew clean assembleRelease

cp ./app/build/outputs/apk/release/*.apk /output/

echo "Build successful"
