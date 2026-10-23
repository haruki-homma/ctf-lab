# CTF Lab

Personal repository for cybersecurity research, CTF challenges, and hands-on security practice.

## Environment

- **Host:** Windows 11
- **Development:** WSL2 (Ubuntu 24.04)
- **Virtualization:** VirtualBox
- **Attacker VM:** Kali Linux
- **Target VM:** Ubuntu Server 24.04

## Network

The lab uses an internal VirtualBox network for security testing.

- **Normal Mode:** NAT and host-only networking enabled when needed
- **Isolated Mode:** Internal network only, without external network access

Intentionally vulnerable applications are tested in isolated environments.

## Tools

| Environment | Tools |
|---|---|
| Windows | Ghidra, Wireshark, Burp Suite |
| WSL2 Ubuntu | Python, pwntools, SageMath, Foundry |
| Kali Linux | Nmap, ffuf, SQLmap, Metasploit |
| Ubuntu Server | Docker, Nginx, OpenSSH, Apache/PHP |

## Practice Labs

- OWASP Juice Shop
- PHP2Shell
- Solidity / Foundry security experiments

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

All vulnerability testing is performed in authorized lab or CTF environments. Credentials and private keys are excluded from this repository.