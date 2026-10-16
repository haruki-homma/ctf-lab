# CTF Lab

Personal cybersecurity and CTF practice environment.

## Environment

- Host OS: Windows 11
- WSL2: Ubuntu 24.04
- Virtualization: VirtualBox
- Attacker VM: Kali Linux
- Target VM: Ubuntu Server 24.04

## Network

- Internal network: ctf-lab
- Kali Linux: 192.168.56.10
- Ubuntu Server: 192.168.56.20
- Kali: NAT + Internal Network
- Ubuntu Server: Internal Network only

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

All intentionally vulnerable services are operated in an isolated
local lab environment. No real credentials or production systems
are included in this repository.
