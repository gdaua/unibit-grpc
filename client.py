import sys

import grpc
from pb import whoami_pb2_grpc, whoami_pb2

host = "localhost"
if len(sys.argv) > 1:
    host = sys.argv[1]

remote = "{}:9080".format(host)
print("Remote: {}".format(remote))

channel = grpc.insecure_channel(remote)
stub = whoami_pb2_grpc.WhoamiStub(channel)
req = whoami_pb2.Request()
resp = stub.Whoami(req)

print(resp)

# print(resp.server_name)
# print(resp.client_conn)
# print(resp.server_ip)
# print(resp.env)
