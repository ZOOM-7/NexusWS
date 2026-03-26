# NexusWS (Alpha)

## Overview

`NexusWS` is a lightweight Python library for managing **WebSocket connections** in an **event-driven** architecture.
It provides a persistent connection model and allows developers to bind **custom handlers to specific message types**.

**Note:** This is an **Alpha release**. Core functionality is stable, but advanced features such as smart reconnection, message queueing, and heartbeat are still under development.

---

## Features

* Persistent WebSocket connection (`ws://` / `wss://`) with SSL support
* Event-driven architecture with dynamic handler binding
* Built-in JSON parser (customizable via `set_parser`)
* Support for custom headers (Authorization, Cookies, etc.)
* Decorator-based event system: `@client.on("event_type")`
* Multiple handlers per event supported
* Send messages using `client.connection.send(...)`

---

## 📥 Installation

```bash
pip install websocket-client
pip install NexusWS
```

---

## Basic Usage

```python
import json
from NexusWS import Client

headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "User-Agent": "NexusWS/1.0"
}

client = Client(
    "wss://example.com",
    headers=headers
)

# Optional custom parser (default is JSON)
client.set_parser(lambda msg: json.loads(msg))

@client.on("0:0")
def handle_text(data):
    print("Text message received:", data)

@client.on("0:100")
def handle_image(data):
    print("Image message received:", data)

client.run()

client.connection.send(json.dumps({
    "type": "0:0",
    "data": "Hello"
}))
```

---

## Main Methods

| Method                                  | Description                               |
| --------------------------------------- | ----------------------------------------- |
| `WebSocketClient(url, headers=None)`    | Initialize a client with optional headers |
| `set_parser(func)`                      | Override the default message parser       |
| `register_handler(event_type, handler)` | Bind handler manually                     |
| `on(event_type)`                        | Decorator-based handler registration      |
| `run()`                                 | Start the WebSocket connection            |
| `connection.send(message)`              | Send data to the server                   |
| `connection.reconnect()`                | Manually reconnect (basic)                |

---

## Architecture Overview

```
Raw Message
   ↓
Parser (default: JSON)
   ↓
Event Dispatcher
   ↓
Handlers
```

---

## Limitations (Alpha)

* Handlers execute synchronously (blocking)
* No internal message queue (may cause delays under high load)
* Basic reconnect logic (no retry strategy or backoff)
* No heartbeat (ping/pong) mechanism yet
* Parser is not fault-tolerant (invalid data may raise exceptions)
* Limited error handling (errors are printed only)

---

## Roadmap

Planned improvements for upcoming versions:

* Non-blocking handler execution (thread pool)
* Internal message queue system
* Smart reconnect with exponential backoff
* Heartbeat (ping/pong) support
* Improved error handling and logging system
* Middleware support (pre/post processing)

---

## Disclaimer

This library is currently in **Alpha stage**.
It is recommended for testing, learning, and prototyping only.
Avoid using it in production environments until stability improvements are released.
