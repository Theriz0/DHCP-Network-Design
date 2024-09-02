# DHCP Server and Switch Design
The Goal of this project is to Utilize how servers in specified cities can communicate and send data through many offices in one location to another through a DHCP protocol. In order to acomplish this, I will be virtualizing this via Cisco Packet Tracer where I would need 4 Cisco 3560 Multi-Layer Switches for this Project. 

Next would be to install 2 PC's per switch where all my PC's will be in a DHCP configuration with leased IP addresses to mimic how a user in a particular office can connect to someone in a different server zone via DHCP protocol. Each switch will be configured to have port security in order to protect dropped packets from unknown MAC addresses but does not log the violation, restrict the port from dropping packets from unknown MAC addresses and logs the violation and to automatically shutdown a port if a violation has been made in that specific port.

Then, IP addresses are going to be subnetted where I have obtained leased IP addresses to be used for this project and I will be able to calculate via subnetting the required Vlans needed for each switch.
