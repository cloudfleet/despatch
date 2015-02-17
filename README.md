# despatch

The inbound mail relay for CloudFleet blimps.

As [Pagekite doesn't support SMTP](https://pagekite.net/wiki/Forum/Jun2011/130746832fb/#c34),
despatch runs [Salmon](https://github.com/moggers87/salmon),
a Python SMTP server, and relays all e-mails to the
[blimp-mailbox](https://github.com/cloudfleet/blimp-mailbox/tree/master)
service on the designated blimp.
