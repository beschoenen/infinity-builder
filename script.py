import os, sys, re

username = os.environ['REDDIT_USERNAME'].replace('"', '')
api_token = os.environ['REDDIT_API_TOKEN'].replace('"', '')

user_agent = f"android:personal-app:0.0.1 (by /u/{username})"

######
# Replace vars in app code
######

apiutils_file = "./Infinity-For-Reddit/app/src/main/java/ml/docilealligator/infinityforreddit/utils/APIUtils.java"
apiutils_code = open(apiutils_file, "r", encoding="utf-8-sig").read()
apiutils_code = apiutils_code.replace("NOe2iKrPPzwscA", api_token)
apiutils_code = apiutils_code.replace("infinity://localhost", 'http://127.0.0.1')
apiutils_code = re.sub(r'public static final String USER_AGENT = ".*?";', f'public static final String USER_AGENT = "{user_agent}";', apiutils_code)

with open(apiutils_file, "w", encoding="utf-8") as f:
    f.write(apiutils_code)

######
# Prepare gradle build
######

build_gradle_file = "./Infinity-For-Reddit/app/build.gradle"
build_gradle_code = open(build_gradle_file, "r", encoding="utf-8-sig").read()
build_gradle_code = build_gradle_code.replace(r"""    buildTypes {""", r"""    signingConfigs {
        release {
            storeFile file("./Infinity.jks")
            storePassword "Infinity"
            keyAlias "Infinity"
            keyPassword "Infinity"
        }
    }
    buildTypes {""")
build_gradle_code = build_gradle_code.replace(r"""    buildTypes {
        release {""", r"""    buildTypes {
        release {
            signingConfig signingConfigs.release""")
build_gradle_code = build_gradle_code.replace(r"""    lint {
        disable 'MissingTranslation'
    }""", r"""    lint {
        disable 'MissingTranslation'
        baseline = file("lint-baseline.xml")
    }""")

with open(build_gradle_file, "w", encoding="utf-8") as f:
    f.write(build_gradle_code)
