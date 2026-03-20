# Dev Activity Live Dashboard

Real-time dashboard that tracks active developers and displays who is currently coding, using live WebSocket data.

---

## Overview

This project connects to a real-time WebSocket stream from Git City and processes developer activity events. It captures live heartbeat signals to determine which developers are actively coding and exposes this data through a web interface.

## Features

- Real-time data ingestion via WebSocket
- Live updates of active developers
- In-memory state management using Python
- REST API built with FastAPI
- Dynamic frontend with auto-refresh (JavaScript)
- Modular architecture (collector + main + API)

## Architecture

| Layer | Responsibility |
|---|---|
| Collector | Connects to WebSocket and listens for live events |
| Processor (`main.py`) | Parses messages and maintains active users |
| API (FastAPI) | Exposes `/online` endpoint with live data |
| Frontend | Fetches data periodically and renders users in real time |

## Tech Stack

- Python
- FastAPI
- WebSockets
- Asyncio
- JavaScript (Vanilla)

## What I Learned

- Working with real-time data streams
- WebSocket communication and event handling
- Async programming in Python
- Building APIs with FastAPI
- Structuring scalable backend architecture
