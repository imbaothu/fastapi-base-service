### Why we built fastapi-base-service 
I want this repository to be able to create a server that can handle HTTP requests, WebSocket requests, and gRPC in less than one day. This codebase should be available for immediate use whenever I have ideas related to AI or GPT. I have a funny example, check it out



## Welcome to Python-Base-Service
A clear and fast Python codebase for building services that handle HTTP, SSE, and WS requests. In the fastapi-base-service, I have developed the following features, with ongoing features in the pipeline using the FastAPI framework. This framework provides robust features that enable developers to create web/apps quickly, within 1-2 days:

- [x] Support for working with configurations (Dev, Production, Default Values) with TOML. 
- [x] Support for managing logs (Format, Output, Level).
- [x] Support for database operations (RDBMS like Postgres, MongoDB).
- [x] Support for Authentication with JWT (Sample Payload, Create, GetClaims).
- [x] Support for Redis operations (Connect, Get, Set, Invalidate).
- [x] Support for AWS S3 operations (Connect, Get, Upload).
- [x] Support for Elasticsearch (Connect, Insert, Search).
- [x] Support for middleware (Rate Limit, Blocking).
- [x] Easy integration with HTTP request handling (Status, Response, graceful shutdown).
- [x] Support common utility features with datetime, async, sync, loop.
- [x] Helpful documentation for learning Python clearly.
- [x] Support for GRPC.
- [x] Support for WebSocket.

## Demo of a Basic System
I will demonstrate a project with this structure, featuring an MVP: Custom ChatGPT for everyone. This idea is inspired by typingmind. Users can store, search, and save chat messages with ChatGPT:

When user chat with AI endpoint like GPT, user must have enter API key, product don't store API key and only saved messages to serve functions to users.
- [x] Support standard authentication functions (Sign In, Sign Up, Change Password, Get Profile, Change API Key).
- [x] Support full-text search using Elasticsearch's API to search messages for users.
- [x] Support note-saving of chat messages with ChatGPT.
- [x] API documentation.
- [x] Python and FastAPI documentation (configurations, conventions, HTTP).

#### Frontend add on project here > Check it out ...

---


This version improves readability and maintains your original format and intent.

## How to run this project
```
# must run
Python 3.11.4
python3 -m venv venv
source venv/bin/active

# For dev
make install
make run

# for deploy

```

---

## Question for myself 
1. What generator run ? async generator run ?
2. what is block in asyncio ? bestpractice with even-loop ?
3. Should we create connection pool like session in endpoints ?
4. Why something openAPI docs not works ?




## Docs to support about Python, Async, Project 
1. Why I not used env file 
2. Python AsyncIO, a dificult things !

I was inspired by the repository : [fastapi-best-practices]("https://github.com/zhanymkanov/fastapi-best-practices")

#### Thanks for visting me, If you think this is helpful repo, give me a star :3