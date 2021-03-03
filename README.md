# Scripts
This is a repository of various scripts that I've found helpful while pentesting. Descriptions of each can be found below.


## copyrand.sh
Copy a number of random characters from /dev/random using pbcopy<br>
Usage: `./copyrand.sh N` where N is the number of characters to copy

## portscan.sh
Find open ports using TCP<br>
Usage: `./portscan.sh [IP]`

## powershell_reverse_shell_tcp_generate.sh
Generate a PS command to create TCP reverse shell<br>
Usage: `./powershell_reverse_shell_tcp_generate.sh LHOST LPORT` where LHOST is the local host IP and LPORT is the listening local port

## testxss.py
Test all html tags and attributes to see which combinations are allowed by XSS filter. Tags and attributes are defined by PortSwigger on their XSS filter evasion cheatsheet.<br>
Usage: `./testxss.py -u <URL> [-t <tags> -a <attributes> -s <status>`