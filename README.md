This is a sample nginx reverse proxy demo



+---------+          +----------------+          +-------------------+
|  Client | -------> |  NGINX Proxy   | -------> |  Backend Service  |
|         |          | (Port 80)      |          | (FastAPI, Port 8000) |
+---------+          +----------------+          +-------------------+
