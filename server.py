import time
from concurrent import futures
import socket
import os

import grpc
from pb import whoami_pb2_grpc, whoami_pb2

import netifaces

def get_ips():
    ip_list=[]
    ips=""
    for iface in netifaces.interfaces():
        iface_details = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in iface_details:
            for ip_interfaces in iface_details[netifaces.AF_INET]:
                for key, ip_add in ip_interfaces.items():
                    if key == 'addr' and ip_add != '127.0.0.1':
                        ips += "{} ".format(ip_add)
                        ip_list.append(whoami_pb2.Ip(ip=ip_add))
    return ip_list


class WhoamiServicer(whoami_pb2_grpc.WhoamiServicer):
    def Whoami(self, request, context):
        return whoami_pb2.Response(server_name=socket.gethostname(), server_ip=get_ips(), client_conn=context.peer())

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    whoami_pb2_grpc.add_WhoamiServicer_to_server(WhoamiServicer(), server)
    print('Starting server on port 9080.')
    server.add_insecure_port('0.0.0.0:9080')
    server.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
