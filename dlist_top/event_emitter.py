class EventEmitter:
    receivers = {}

    def on(self, event):
        def decorator(fn):
            self.receivers.setdefault(event, []).append(fn)

        return decorator

    def emit(self, event, data):
        for fn in self.receivers[event]:
            fn(data)