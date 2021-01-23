#!/usr/bin/python3
import requests
import json
from sys import argv


def serverZones_List(scheme, domain, port, path):
    response = requests.get(str(scheme)+ "://" + str(domain) + ":" + str(port) + "/" + str(path) + "/control?cmd=status&group=server&zone=*")
    serverZonesList = json.loads(response.text)["serverZones"].keys()
    serverZonesDict = []
    for zone in serverZonesList:
        serverZonesDict.append({"Zone":zone})
    return json.dumps(serverZonesDict)


def upStreamZones_List(scheme, domain, port, path):
    response = requests.get(str(scheme)+ "://" + str(domain) + ":" + str(port) + "/" + str(path) + "/control?cmd=status&group=upstream@group&zone=*")
    upStreamZones = json.loads(response.text)["upstreamZones"]
    serverZonesList = upStreamZones.keys()
    upstreams_list = []
    for key in serverZonesList:
        upstreams = upStreamZones[key]
        for upstream in upstreams:
            upstreams_list.append({"Zone":upstream["server"]})
    return json.dumps(upstreams_list)


def cacheZones_List(scheme, domain, port, path):
    response = requests.get(str(scheme)+ "://" + str(domain) + ":" + str(port) + "/" + str(path) + "/control?cmd=status&group=cache&zone=*")
    serverZonesList = json.loads(response.text)["cacheZones"].keys()
    serverZonesDict = []
    for zone in serverZonesList:
        serverZonesDict.append({"Zone":zone})
    return json.dumps(serverZonesDict)


def serverZones_Info(scheme, domain, port, path, zone_name):
    response = requests.get(str(scheme)+ "://" + str(domain) + ":" + str(port) + "/" + str(path) + "/control?cmd=status&group=server&zone="+str(zone_name))
    serverZonesInfo = json.loads(response.text)[str(zone_name)]
    return json.dumps(serverZonesInfo)


def cacheZones_Info(scheme, domain, port, path, zone_name):
    response = requests.get(str(scheme)+ "://" + str(domain) + ":" + str(port) + "/" + str(path) + "/control?cmd=status&group=cache&zone="+str(zone_name))
    cacheZonesInfo = json.loads(response.text)[str(zone_name)]
    return json.dumps(cacheZonesInfo)


def upstream_Info(scheme, domain, port, path, upstream_IP):
    response = requests.get(str(scheme)+ "://" + str(domain) + ":" + str(port) + "/" + str(path) + "/control?cmd=status&group=upstream@group&zone=*")
    upStreamZones = json.loads(response.text)["upstreamZones"]
    serverZonesList = upStreamZones.keys()
    for key in serverZonesList:
        upstreams = upStreamZones[key]
        for upstream in upstreams:
            if upstream["server"]==upstream_IP:
                return json.dumps(upstream)




if __name__ == '__main__':
    scheme = argv[1]
    domain = argv[2]
    port = argv[3]
    path = argv[4]
    type = argv[5]
    if type == "serverZones_List":
        print(serverZones_List(scheme, domain, port, path))
    elif type == "upStreamZones_List":
        print(upStreamZones_List(scheme, domain, port, path))
    elif type == "cacheZones_List":
        print(cacheZones_List(scheme, domain, port, path))
    elif type == "serverZones_Info":
        zone_name = argv[6]
        print(serverZones_Info(scheme, domain, port, path,zone_name))
    elif type == "cacheZones_Info":
        zone_name = argv[6]
        print(cacheZones_Info(scheme, domain, port, path,zone_name))
    elif type == "upstream_Info":
        upstream_IP = argv[6]
        print(upstream_Info(scheme, domain, port, path,upstream_IP))











