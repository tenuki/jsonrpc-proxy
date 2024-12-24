# json-rpc proxy

### Setup

0. checkout (or download and decompress) this project
1. prepare environment: `python3 -m venv env`
2. enter the environment: `. ./env/bin/activate`
3. install dependencies `pip install -r requirements.txt`

### Usage

0. enter the environment: `. ./env/bin/activate`
1. run proxy: `PORT=5000 RPCNODE=https://sepolia.base.org python jsonrpc-proxy.py` 


### Testing with curl

You can find a lot of examples here: https://ethereum.org/en/developers/docs/apis/json-rpc/ which you can run against this server, for example:

`curl -X POST --data '{"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":67}'  http://localhost:5000/ `


### Sample output

```
(.venv) aweil@T460p:~/Personal/jrpc-proxy$ PORT=5000 RPCNODE=https://sepolia.base.org python main.py 
jrpc-proxy - listen at port 5000. RPCNODE: https://sepolia.base.org/
======== Running on http://0.0.0.0:5000 ========
(Press CTRL+C to quit)
Error handling request
<- {'id': '1735047755524', 'jsonpc': '2.0', 'method': 'eth_chainId', 'params': []}
-> {'jsonrpc': '2.0', 'result': '0x14a34', 'id': '1735047755524'}
<- {'id': '1735048208229', 'jsonrpc': '2.0', 'method': 'eth_chainId', 'params': []}
-> {'jsonrpc': '2.0', 'result': '0x14a34', 'id': '1735048208229'}
<- {'id': '1735048320917', 'jsonrpc': '2.0', 'method': 'eth_chainId', 'params': []}
-> {'jsonrpc': '2.0', 'result': '0x14a34', 'id': '1735048320917'}
<- {'id': 3118554890175374, 'jsonrpc': '2.0', 'method': 'eth_blockNumber', 'params': []}
-> {'jsonrpc': '2.0', 'result': '0x12baed6', 'id': 3118554890175374}
<- {'id': 5866423429159558, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
<- {'id': 5866423429159559, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
<- {'id': 5866423429159560, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
<- {'id': 5866423429159561, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
<- {'id': 5866423429159562, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
<- {'id': 5866423429159563, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
-> {'jsonrpc': '2.0', 'result': '84532', 'id': 5866423429159558}
<- {'id': 5866423429159564, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
-> {'jsonrpc': '2.0', 'result': '84532', 'id': 5866423429159560}
-> {'jsonrpc': '2.0', 'result': '84532', 'id': 5866423429159559}
-> {'jsonrpc': '2.0', 'result': '84532', 'id': 5866423429159561}
-> {'jsonrpc': '2.0', 'result': '84532', 'id': 5866423429159563}
-> {'jsonrpc': '2.0', 'result': '84532', 'id': 5866423429159562}
<- {'id': 5866423429159565, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
<- {'id': 5866423429159566, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
<- {'id': 5866423429159567, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
<- {'id': 5866423429159568, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
<- {'id': 5866423429159569, 'jsonrpc': '2.0', 'method': 'net_version', 'params': []}
```
