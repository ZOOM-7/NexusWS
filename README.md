
# WSForge (Alpha)

##  Overview

`WSForge` is a lightweight Python library for managing **WebSocket connections** in an **event-driven** way.
It allows you to create a WebSocket client that keeps the connection open and lets you bind **handlers for each message type**.

**Note:** This is an **Alpha release**. Some features like smart reconnect, internal message queue, and heartbeat are not fully implemented yet.

---

##  Features

* Persistent WebSocket connection (wss://) with SSL support
* Event Dispatcher to handle messages by their `type`
* Customizable parser for message processing (JSON or any protocol)
* Support for custom headers (Authorization, Cookies, etc.)
* Decorator interface: `@client.on("event_type")` for easy handler registration
* Send messages using `client.connection.send(...)`

---

##  Installation

```bash
pip install websocket-client
pip install WSForge
```

---

##  Basic Usage

```python
import json
from NexusWS import WebSocketClient

# Optional headers for authentication or custom requirements
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "User-Agent": "WSForge/1.0"
}

client = WebSocketClient(
    "wss://example.com",
    headers=headers
)

# Custom parser
client.set_parser(lambda msg: json.loads(msg))

# Event handlers using decorators
@client.on("0:0")
def handle_text(data):
    print("Text message received:", data)

@client.on("0:100")
def handle_image(data):
    print("Image message received:", data)

# Run the WebSocket connection
client.run()

# Send a message
client.connection.send(json.dumps({
    "type": "0:0",
    "data": "Hello"
}))
```

---

##  Main Methods

| Method                                  | Description                                       |
| --------------------------------------- | ------------------------------------------------- |
| `WebSocketClient(url, headers=None)`    | Create a new client with URL and optional headers |
| `set_parser(func)`                      | Set a custom parser to process incoming messages  |
| `register_handler(event_type, handler)` | Bind a handler function to a specific event type  |
| `on(event_type)`                        | Decorator to bind a handler to an event           |
| `run()`                                 | Start the WebSocket connection                    |
| `connection.send(message)`              | Send a message to the server                      |
| `connection.reconnect()`                | Reconnect manually (basic)                        |

---

##  Limitations (Alpha)

* Handlers execute sequentially; a slow handler can block others
* No internal message queue; rapid incoming messages may cause delays
* Reconnect logic is basic (no exponential backoff)
* No heartbeat (ping/pong) implemented
* Parser errors may crash the library if messages are invalid
* Limited error handling; errors are only printed

---

## 🧠 Recommendations

* Use this version for testing, experimentation, or MVP projects
* Do **not rely on it for production-critical systems** yet
* Future updates will include:

  * Threaded handler execution (non-blocking)
  * Internal message queue
  * Smart reconnect with backoff
  * Heartbeat/ping mechanism
  * Better error handling and validation
