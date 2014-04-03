cocaine_pam_auth
================

Test python PAM authentication as cocaine worker

###Installation:

```
pip install -r requirements.txt
./deploy.sh
```

###Usage:

```
cocaine-tool call pam_auth enqueue "'login', '{\"login\": \"test_user\", \"password\": \"123\"}'"
```
