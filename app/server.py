import requests
from salmon.routing import nolocking, route, stateless
import json

import logging

log = logging.getLogger(__name__)
log.level = logging.DEBUG

@route("(inbox)@(domain)", inbox=".+", domain=".+")
@stateless
@nolocking
def START(message, inbox=None, domain=None):

    log.info("===============================")
    log.info("received mail for %s@%s" % (inbox, domain))
    target_url = "http://" + domain + "/mailbox/raw/" + inbox  # FIXME change to https
    r = requests.post(target_url, headers={"Content-transfer-encoding": "binary"}, data=message.to_message().as_string())
    log.info("Server Response: %s" % r.text)





