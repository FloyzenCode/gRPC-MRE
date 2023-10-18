from __future__ import print_function

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def run():
    print(bcolors.BOLD + "============================")
    print("Will try to greet world ...")
    print("============================")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print(bcolors.OKGREEN + "Greeter client received: " + response.message)
        response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you again'))
        print(bcolors.OKGREEN + "Greeter client received: " + response.message)

if __name__ == "__main__":
    logging.basicConfig()
    run()
