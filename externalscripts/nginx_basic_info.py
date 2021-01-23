#!/usr/bin/python3
import requests
import json
from sys import argv


def nginx_monitoring(scheme, domain, port, path):
    response = requests.get(str(scheme)+ "://" + str(domain) + ":" + str(port) + "/" + str(path) + "/format/json")
    Full_Info = json.loads(response.text)
    basic_info = {
        "HostName": Full_Info["hostName"],
        "nginxVersion": Full_Info["nginxVersion"],
        "Uptime": uptime(Full_Info["nowMsec"], Full_Info["loadMsec"]),
        "ActiveConnections": str(Full_Info["connections"]["active"]),
        "ReadingConnections": str(Full_Info["connections"]["reading"]),
        "WritingConnections": str(Full_Info["connections"]["writing"]),
        "WaitingConnections": str(Full_Info["connections"]["waiting"]),
        "AcceptedConnections": str(Full_Info["connections"]["accepted"]),
        "HandledConnections": str(Full_Info["connections"]["handled"]),
        "RequestsConnections": str(Full_Info["connections"]["requests"]),
    }
    return basic_info


def uptime(now, start):
    time = (int(now)-int(start))/1000
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    return str(int(day))+"d "+str(int(hour))+"h "+ str(int(minutes))+"m "+str(int(seconds))+"s"


if __name__ == '__main__':
    scheme = argv[1]
    domain = argv[2]
    port = argv[3]
    path = argv[4]
    basic_info = nginx_monitoring(scheme, domain, port, path)
    print(json.dumps(basic_info))
