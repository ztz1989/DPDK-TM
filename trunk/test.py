#!/usr/bin/python
# The script to test the RX functionality
# sudo ./build/FlowMon-DPDK -l 0,2,4,6,8 -- -P -p 8 --rx="(3,0,2,0)(3,1,4,1)" --tx="(6,0)(8,1)"
# sudo ./build/FlowMon-DPDK --lcores="0,(1,3)@1,(2,4)@2" -c 1F -n 4 -- -P -p 4 --rx="(2,0,1,0)(2,1,2,1)" --tx="(3,0)(4,1)"

import subprocess, time, signal, random

for _ in range(10):
	p = subprocess.Popen(["./build/FlowMon-DPDK", "-l", "1,2,4,6,8", "--", "-P", "-p", "4", '--rx="(2,0,2,0)(2,1,4,1)"', '--tx="(6,0)(8,1)"', "--write-file"])
	time.sleep(140)
	p.send_signal(signal.SIGINT)
	time.sleep(6)
