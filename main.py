from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads
import sys

#saving list of ip addresses
ips = ip_file_valid()

try:
    ip_addr_valid(ips)
except KeyboardInterrupt:
    print("\n Program aborted by user. Exiting...\n")
    sys.exit()

#are ips reachable
try:
    ip_reach(ips)
except KeyboardInterrupt:
    print("\n Program aborted by user. Exiting...\n")
    sys.exit()

#create threads
create_threads(ips, ssh_connection)
