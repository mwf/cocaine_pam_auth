#!/usr/bin/env python
from __future__ import unicode_literals
from __future__ import print_function

import pam
import json

from cocaine.worker import Worker
from cocaine.logging import Logger

log = Logger()


def login(request, response):
    msg = yield request.read()
    log.debug("Recieved:\n{0}".format(msg))
    d = json.loads(msg)
    log.debug("Json-unpacked:\n{0}".format(d))

    d["login"] = str(d["login"])
    d["password"] = str(d["password"])

    log.debug("utf-8 decoded:\n{0}".format(d))

    auth = yield pam.authenticate(d["login"], d["password"])
    log.debug("Authenticated: {0}".format(auth))
    log.debug("Writing response...")

    response.write("Authenticated: {0}".format(auth))
    response.close()


W = Worker()
W.run({
    'login': login
})
