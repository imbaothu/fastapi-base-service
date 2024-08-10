1. aiohttp is simple, quick and async

Folow this link https://docs.aiohttp.org/en/stable/client_quickstart.html#make-a-request, don’t create a session per request. Most likely you need a session per application which performs all requests together. More complex cases may require a session per site, e.g. one for Github and other one for Facebook APIs. Anyway making a session for every request is a very bad idea.
A session contains a connection pool inside. Connection reusage and keep-alive (both are on by default) may speed up total performance.

But need use ClientSession with async with ClientSession() as session, else use 

