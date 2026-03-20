import json
import asyncio
from fastapi import FastAPI
from collector.websocket_client import listen
from fastapi.responses import HTMLResponse

app = FastAPI()
users = {}

def handle_message(message):
    data = json.loads(message)

    if len(data) > 4:
        event_data = data[4]

        if "payload" in event_data:
            payload = event_data["payload"]

            user = payload.get("githubLogin")
            status = payload.get("status")

            if user and status:
                users[user] = status
                print(users)

@app.get("/online")
def get_online_users():
    return users

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(listen(handle_message))

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Git City Live</title>
    </head>
    <body>
        <h1>Quem está codando agora</h1>
        <div id="users"></div>

        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 20px;
                color: #FFFFFF;
                display: flex;
                flex-direction: column;
                align-items: center;


            }
            #users div {
                margin-bottom: 10px;
                color: #00FF00;
            }
            body{
                background-color: #000000;
            }
        </style>

        <script>
            async function loadUsers() {
                const response = await fetch('/online');
                const users = await response.json();

                const container = document.getElementById('users');
                container.innerHTML = '';

                for (const [name, status] of Object.entries(users)) {
                    const div = document.createElement('div');
                    div.textContent = `${name} - ${status}`;
                    container.appendChild(div);
                }
            }

            loadUsers();
            setInterval(loadUsers, 2000);
        </script>
    </body>
    </html>
    """