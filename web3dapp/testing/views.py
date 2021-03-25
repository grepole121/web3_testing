import json
from django.http.response import HttpResponse
from web3 import Web3
from web3.auto.infura import w3

from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages


from django.http import HttpResponse


def index(request):
    return HttpResponse(f"<h1>Current Ethereum Block: {w3.eth.block_number}</h1>")


# # ROPSTEN
# public_key = ""
# private_key = ""

# # Infura
# url = "https://ropsten.infura.io/v3/93418f48240b422ba2806bec82e66d2c"

# web3 = Web3(Web3.HTTPProvider(url))
# address = web3.toChecksumAddress("0xaddress")
# # abi = json.loads('''''')

# contract = web3.eth.contract(address=address, abi=abi)
