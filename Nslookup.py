import os
import dns.resolver
from dns.exception import DNSException
from PrintManager import PrintManager

class Nslookup():
    def DNSquery(self,domains):
        # 8.8.8.8 is Google's public DNS server
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
