import requests
from salmon.routing import nolocking, route, stateless, route_like
from salmon.mail import MailResponse
from config import settings
import json

import logging

log = logging.getLogger(__name__)
log.level = logging.DEBUG

def forward_postmaster(message, domain):
    log.info("===============================")
    log.info("received mail for %s@%s. Forwarding ..." % ("postmaster", domain))
    log.debug("Content: \n %s" % message.to_message().as_string())

    try:
        settings.relay.deliver(MailResponse(To='admiralty@cloudfleet.io', From=message.From, Subject="[%s] %s" % (domain, message['subject']), Body=message.body()))
    except Exception, e:
        log.error(str(e))

    log.info("===============================")
    log.info("forwarded mail to admiralty")

def deliver_to_blimp(message, inbox, domain):
    log.info("===============================")
    log.info("received mail for %s@%s" % (inbox, domain))
    target_url = "https://blimp." + domain + "/mailbox/raw/" + inbox  # FIXME change to https
    r = requests.post(target_url, headers={"Content-transfer-encoding": "binary"}, data=message.to_message().as_string(), verify=False) # FIXME verify SSL
    log.info("Server Response: %s" % r.text)


@route("(inbox)@(domain)", inbox=".+", domain=".+")
@stateless
def START(message, inbox=None, domain=None):
    if inbox == 'postmaster':
        return forward_postmaster(message, domain)
    else:
        return deliver_to_blimp(message, inbox, domain)
