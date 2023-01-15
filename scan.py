import subprocess
import xmltodict
from graphviz import Digraph

def scan_network():
    nmap_output = subprocess.run(["nmap", "-oX", "-", "-sP", "192.168.12.0/24"], capture_output=True)
    print(nmap_output.stdout.decode())
    nmap_data = xmltodict.parse(nmap_output.stdout.decode())
    graph = Digraph()

    for host in nmap_data['nmaprun']['host']:
        hostname = host['hostnames']['hostname']['@name'] if host['hostnames'] is not None else host['address']['@addr']
        graph.node(hostname)

    graph.render('network_graph', view=True)

scan_network()
