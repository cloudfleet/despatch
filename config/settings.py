from salmon.server import SMTPReceiver, Relay
from os import environ

RELAY_USERNAME=environ['MAILHOST_USERNAME']
RELAY_PASSWORD=environ['MAILHOST_PASSWORD']
RELAY_HOST=environ.get('MAILHOST_HOST', '127.0.0.1')
RELAY_PORT=environ.get('MAILHOST_PORT', '25')
RELAY_SSL=environ.get('MAILHOST_SSL', 'false')

receiver = SMTPReceiver('0.0.0.0',25)
relay = Relay(host=RELAY_HOST, port=int(RELAY_PORT), username=RELAY_USERNAME, password=RELAY_PASSWORD,
                 ssl=RELAY_SSL.lower() == 'true', starttls=False, debug=0)
