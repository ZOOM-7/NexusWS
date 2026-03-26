import websocket
import ssl
import threading


class Connection:
    def __init__(self, url, headers=None, on_message=None, on_open=None, on_close=None, on_error=None):
        self.url = url
        self.ws = None
        self.headers = headers or {}

        self.on_message = on_message
        self.on_open = on_open
        self.on_close = on_close
        self.on_error = on_error

    def _message(self, ws, message):
        if self.on_message:
            self.on_message(message)

    def _open(self, ws):
        print("[Connected]")
        if self.on_open:
            self.on_open()

    def _close(self, ws, code, msg):
        print("[Disconnected]")
        if self.on_close:
            self.on_close()

    def _error(self, ws, error):
        print("[Error]", error)
        if self.on_error:
            self.on_error(error)


    def connect(self):
        headerList = [f"{k}: {v}" for k, v in self.headers.items()]

        self.ws = websocket.WebSocketApp(
            self.url,
            header=headerList,
            on_message=self._message,
            on_open=self._open,
            on_close=self._close,
            on_error=self._error
        )

        thread = threading.Thread(target=self._run, daemon=True)
        thread.start()

    def _run(self):
        self.ws.run_forever(
            sslopt={
                "cert_reqs": ssl.CERT_NONE
            }
        )


    def send(self, message):
        if self.ws:
            self.ws.send(message)

    def reconnect(self):
        print("[Reconnecting...]")
        self.connect()