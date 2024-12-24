import asyncio
import json
import os
import subprocess
import sys
import unittest

import aiohttp
from aiohttp import web

PORT = int(os.environ.get("PORT", "3000"))
RPCNODE = sys.argv[1] if len(sys.argv)>1 else "https://sepolia.base.org/"

# @method
# async def ping():
#     return 'pong'
# @method
# async def web3_clientVersion():
#     return Success({"done": '3.4'})


class RPCd(dict):
    def json(self):
        return json.dumps(self)


RPCc = lambda method, id, params=[]: RPCd({"jsonrpc": "2.0", "method": method, "params": params, "id": id})
RPCr = lambda result, id: RPCd({"jsonrpc": "2.0", "result": result, "id": id})
RPCerror = lambda err_code, err_msg, id: RPCd(
    {"jsonrpc": "2.0", "error": {"code": err_code, "message": err_msg}, "id": id})
RPCe_NotExistingMethod = lambda id: RPCerror(err_code=-32601, err_msg="Method not found")


class Client:
    def __init__(self, base_url, ssl=None):
        self.ssl = ssl if not (ssl is None) else base_url.lower().startswith('https://')
        self.base_url = base_url
        self._client = None

    @property
    def client(self):
        if self._client is None:
            self._client = aiohttp.ClientSession()
        return self._client

    async def get(self, method, *params, **data):
        rpc = RPCc(method, data['id'], params)
        return await self.client.post(self.base_url, json=rpc, ssl=self.ssl)

    async def dispatch(self, data):
        r = await self.get(data['method'], *data['params'], id=data['id'])
        ret = await (r.text() if r.headers['Content-Type'] == 'text/plain' else r.json())
        return ret


def handle():
    client = Client(RPCNODE)

    async def _handle(request):
        data = await request.text()
        orig = json.loads(data.strip())
        print("<-", orig)
        oret = await client.dispatch(orig)
        print("->", oret)
        return web.Response(text=RPCr(oret['result'], oret['id']).json(),
                            content_type="application/json")

    return _handle


app = web.Application()
app.router.add_post('/', handle())

# >>> import subprocess
# >>> result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
# >>> result.stdout

CMD1 = '{"jsonrpc":"2.0","method":"web3_sha3","params":["0x68656c6c6f20776f726c64"],"id":64}'
CMD1_RET = '{"jsonrpc": "2.0", "result": "0x47173285a8d7341e5e972fc677286384f802f8ef42a5ec5f03bbfa254cb01fad", "id": 64}'


class RunServer:
    @staticmethod
    async def run(app):
        web.run_app(app, port=PORT)


class BasicTests(unittest.TestCase):
    SERVER = f"http://localhost:{PORT}"

    @classmethod
    def setUpClass(cls):
        async def quit(req):
            await app.shutdown()
            return web.Response(text="bye!", content_type="text/plain")

        app.router.add_post('/quit', quit)
        cls.task = asyncio.create_task(RunServer.run(app))
        # web.run_app(app, port=PORT)

    @classmethod
    def tearDownClass(cls):
        app.shutdown()
        # client = aiohttp.ClientSession(cls.SERVER)
        # client.post('/quit')

    def run(self, cmd):
        return subprocess.run(
            ['curl', '-X', 'POST', '--data', cmd, self.SERVER],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def test_basic1(self):
        ret = self.run(CMD1)
        self.assertEqual(ret.stdout, CMD1_RET)


if __name__ == '__main__':
    print(f"jrpc-proxy - listen at port {PORT}. RPCNODE: {RPCNODE}")
    web.run_app(app, port=PORT)
    # r=subprocess.run(ll
    #     ['curl', '-X', 'POST', '--data', CMD1, 'https://sepolia.base.org'],
    #     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # print(r.stdout)
