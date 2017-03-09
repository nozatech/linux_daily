#!/bin/bash
set -e

new_env="$1"
apk_original_path="$2"
apk_rebuilt_path="$3"

if [[ ! -f "$apk_original_path" ]]
then
    echo "FATAL no APK at path $apk_original_path"
    exit 1
fi

if [[ -z "$apk_rebuilt_path" ]]
then
    echo "FATAL no rebuild path given"
    exit 1
fi

apk_name=`basename "$apk_original_path"`

echo "Creating temp dir..."
mkdir exploded
cp "$apk_original_path" "exploded/${apk_name}"
cd exploded

echo "Exploding APK..."
unzip "${apk_name}" -d content

env_file_name="content/assets/GS_Settings.json"

if [[ ! -f "$env_file_name" ]]
then
    echo "FATAL didn't find the environment file in the given APK"
    exit 1
fi

echo "Writing new environment setting ($new_env)..."
sed -i .bak "s/\"ServerMode\" : \".*\"/\"ServerMode\" : \"${new_env}\"/g" "${env_file_name}"
rm "${env_file_name}.bak"

echo "Repackaging APK to ${apk_rebuilt_path}..."
cd content
zip -r "$apk_rebuilt_path" ./

echo "Cleaning up..."
cd ../..
rm -rf exploded

echo "Done!"