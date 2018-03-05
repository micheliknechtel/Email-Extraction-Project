#  Nslookup.py
#  python
#
#  Created by Micheli Knechtel on 05/03/2018.
#  Copyright © 2018 Micheli Knechtel. All rights reserved.
# 
#   Description: class Nslookup() 
#   Query a Google's public DNS server to lookup IP address information

import os
import dns.resolver
from dns.exception import DNSException
from PrintManager import PrintManager

class Nslookup():

#   this method receives a list of domains, to each domain in the list, 
#   the function is going to perform a query and print IP addresses mapped 
    def DNSquery(self,domains):
        r = dns.resolver.Resolver()
        r.nameServers = ['8.8.8.8']
        for i in range(len(domains)):
            try:
                ips = r.query(domains[i], "A")
                PrintManager().nslookupTry(domains[i]);
                for ip in ips:
                    print(ip)
            except:
                PrintManager().nslookupExcept(domains[i]);
