# CTF Lab

Personal cybersecurity and CTF practice environment.

## Environment

- Host OS: Windows 11
- WSL2: Ubuntu 24.04
- Virtualization: VirtualBox
- Attacker VM: Kali Linux 2026.2
- Target VM: Ubuntu Server 24.04

## Network

The lab uses two separate private networks and supports two operating modes.

### Network Configuration

| Network | Type | Purpose |
|---|---|---|
| `ctf-lab` | Internal Network | Communication between attacker and target VMs |
| Host-only Network | Host-only Adapter | SSH administration from Windows |
| NAT | NAT | Internet access for Kali Linux when required |

### IP Addresses

| Machine | Interface | IP Address |
|---|---|---|
| Kali Linux | Internal | `192.168.56.10/24` |
| Ubuntu Server | Internal | `192.168.56.20/24` |
| Ubuntu Server | Host-only | `192.168.57.21/24` |
| Windows Host | Host-only | `192.168.57.1/24` |

### Normal Mode

Used for development, software installation, and general CTF practice.

- Kali Linux: NAT + Internal Network
- Ubuntu Server: Internal Network + Host-only Network
- Windows can administer Ubuntu Server over SSH.
- Kali Linux can access the internet through NAT.

### Isolated Mode

Used for testing intentionally vulnerable applications, including PHP2Shell.

- Kali Linux: Internal Network only
- Ubuntu Server: Internal Network only
- Kali NAT: Disabled
- Ubuntu Server Host-only: Disabled
- Shared folders, shared clipboard, and drag-and-drop: Disabled
- No default gateway configured on the isolated lab interfaces

In this mode, the two VMs communicate over `ctf-lab` without ordinary network connectivity to Windows or the internet.

### Network Management

- Kali Linux: NetworkManager (`nmcli`)
- Ubuntu Server: Netplan
- Kali's `ctf-lab` connection is bound to the internal adapter's MAC address to reduce interface-renaming issues when NAT is toggled.

## Tools

### Windows

- Ghidra
- Wireshark
- Burp Suite

### WSL2 Ubuntu

- Python
- pwntools
- SageMath
- Foundry (forge, cast, anvil, chisel)

### Kali Linux

- Nmap
- ffuf
- SQLmap
- Metasploit
- Burp Suite

### Ubuntu Server

- Docker
- Nginx
- OpenSSH
- Apache / PHP (isolated vulnerability labs)

## Lab Applications

- OWASP Juice Shop
- PHP2Shell

## CTF Categories

- Pwn
- Reverse Engineering
- Cryptography
- Web Exploitation
- Digital Forensics
- OSINT
- Blockchain
- Misc
- Penetration Testing

## Security

All intentionally vulnerable services are intended to run only in authorized local lab environments.

Security precautions include:

- Disabling external and host-only network adapters during high-risk experiments
- Disabling host–guest file sharing and clipboard integration
- Binding vulnerable services to designated lab interfaces
- Taking VirtualBox snapshots before experiments
- Reverting target VMs to trusted snapshots after experiments
- Keeping real credentials and production data outside the lab

Network isolation reduces exposure but does not provide an absolute security guarantee.

No real credentials, private keys, or production systems are intentionally included in this repository.
