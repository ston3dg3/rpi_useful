Connection / Network commands

man ip
man nmcli
man lshw

sudo lshw -class network -short                    check network interfaces and their paths
ip a                                               check ip adresses for each interface
ip a s [network interface] | grep state            check ip of that interface (and state)
ip route                                           check the route
nmcli dev wifi                                     check available wifi networks
wavemon                                            info of current wifi connection

Useful Command Line Tools:
- exa (better ls)
- bat (better code browsing)
- Ripgrep (better grep)
- FZF (fuzzy filename search)
- Zoxide (better cd)
- Entr (executes code changes on the press of Enter)
- Midnight Commander (file manager)





