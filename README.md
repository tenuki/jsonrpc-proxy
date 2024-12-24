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
