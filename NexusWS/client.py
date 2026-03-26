from .engine.connection import Connection
from .engine.dispatcher import Dispatcher
from .engine.parser import default_parser

class Client:
    def __init__(self, url, headers=None):
        self.url = url

        self.parser = default_parser
        self.dispatcher = Dispatcher()

        self.connection = Connection(
            url,
            headers=headers,
            on_message=self._on_raw_message
        )

    def set_parser(self, parser_func):
        self.parser = parser_func

    def register_handler(self, event_type, handler):
        self.dispatcher.register(event_type, handler)

    def on(self, event_type):
        def decorator(func):
            self.register_handler(event_type, func)
            return func
        return decorator

    def _on_raw_message(self, msg):
        parsed = self.parser(msg)
        event_type = parsed.get("type")
        self.dispatcher.dispatch(event_type, parsed)

    def run(self):
        self.connection.connect()