import requests
from salmon.routing import nolocking, route, stateless
from salmon.mail include MailResponse
from config import settings
import json

import logging

log = logging.getLogger(__name__)
log.level = logging.DEBUG

@route("postmaster@(domain)", inbox=".+", domain=".+")
@stateless
def forward_postmaster(message, to=None, host=None):
    logging.debug("MESSAGE to %s@%s forwarded to the relay host.", to, host)
    settings.relay.deliver(MailResponse(To='admiralty@cloudfleet.io', From=message.From, Subject="[%s] %s" % (host, message.Subject), Body=message.body()))



@route("(inbox)@(domain)", inbox=".+", domain=".+")
@stateless
@nolocking
def START(message, inbox=None, domain=None):

    log.info("===============================")
    log.info("received mail for %s@%s" % (inbox, domain))
    target_url = "http://blimp." + domain + "/mailbox/raw/" + inbox  # FIXME change to https
    r = requests.post(target_url, headers={"Content-transfer-encoding": "binary"}, data=message.to_message().as_string())
    log.info("Server Response: %s" % r.text)
