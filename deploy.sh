tar czvf pam.tar.gz pam_auth.py

cocaine-tool profile upload -n pam_profile --profile profile.json

cocaine-tool app stop -n pam_auth
cocaine-tool app upload --name pam_auth --manifest manifest.json --package pam.tar.gz
cocaine-tool app start -n pam_auth -r pam_profile
