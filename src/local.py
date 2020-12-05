import kopf
import asyncio


@kopf.on.login(errors=kopf.ErrorsMode.PERMANENT)
async def login_fn(**kwargs):
    await asyncio.sleep(2.0)
    return kopf.ConnectionInfo(
        server='http://localhost:8001',
        insecure=True)

