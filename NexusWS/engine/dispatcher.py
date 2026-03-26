class Dispatcher:
    def __init__(self):
        self.handlers = {}

    def register(self, event_type, handler):
        if event_type not in self.handlers:
            self.handlers[event_type] = []
        self.handlers[event_type].append(handler)

    def dispatch(self, event_type, data):
        handlers = self.handlers.get(event_type, [])

        for handler in handlers:
            try:
                handler(data)
            except Exception as e:
                print(f"[Handler Error] {event_type}: {e}")