from salmon import queue
from salmon.routing import Router


Router.defaults(**{})
Router.load(['app.server'])
Router.RELOAD=False
Router.LOG_EXCEPTIONS=True
Router.UNDELIVERABLE_QUEUE=queue.Queue("run/undeliverable")