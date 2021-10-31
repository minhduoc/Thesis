str = '''
Interactive SSH session established

-------------------------------------------

Product name       : AMO-10000-LT-S
MAC base address   : 00:15:AD:39:FF:00
Unit identifier    : C403-9125
Firmware version   : dev_AMO-10000-LT_7.9.2_24136
Serial number      : C403-9125
Assembly           : 500-090-03:22:25:00
Hardware options   : Dry-contact Input
Manufacture config : 0000

Executing command:    port edit PORT-1 state Enable
Executing command:    port edit PORT-2 state Enable
Executing command:    port edit PORT-3 state Enable
Executing command:    port edit PORT-4 state Enable
Executing command:    port edit PORT-5 state Enable
Executing command:    port edit PORT-6 state Enable
Executing command:    port edit PORT-7 state Enable
Executing command:    port edit PORT-8 state Enable
Executing command:    port edit PORT-9 state Enable
Executing command:    port edit PORT-10 state Enable
Executing command:    port edit PORT-11 state Enable
Executing command:    port edit PORT-12 state Enable
-------------------------------------------------------------------
		Executing Testcase: Test_disable_one_port
-------------------------------------------------------------------
Executing command:    port edit PORT-3 state Disable
Status  Connector  Port name                       State    Speed     MDI 
------- ---------- ------------------------------- -------- --------- ----
Up      SFP-1      PORT-1                          Enabled  1G-FD     --- 
Up      SFP-2      PORT-2                          Enabled  1G-FD     --- 
Down    SFP-3      PORT-3                          Disabled No-link   --- 
Up      SFP-4      PORT-4                          Enabled  1G-FD     --- 
Up      SFP-5      PORT-5                          Enabled  10G-FD    --- 
Up      SFP-6      PORT-6                          Enabled  10G-FD    --- 
Up      SFP-7      PORT-7                          Enabled  10G-FD    --- 
Up      SFP-8      PORT-8                          Enabled  10G-FD    --- 
Up      RJ45-9     PORT-9                          Enabled  1G-FD     MDI 
Up      RJ45-10    PORT-10                         Enabled  1G-FD     MDI 
Up      RJ45-11    PORT-11                         Enabled  1G-FD     MDIX
Up      RJ45-12    PORT-12                         Enabled  1G-FD     MDI 
Up      Management Management                      Enabled  100M-FD   MDI 
Down    ---        LAG-1                           Enabled  ---       --- 
Down    ---        LAG-2                           Enabled  ---       --- 
Down    ---        LAG-3                           Enabled  ---       --- 
Down    ---        LAG-4                           Enabled  ---       --- 
Down    ---        LAG-5                           Enabled  ---       --- 
Down    ---        LAG-6                           Enabled  ---       --- 

Port name : PORT-3
   Connector : SFP-3
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 
      State         : Configuring


-------------------------------------------------------------------
		Test_disable_one_port		FAILED
-------------------------------------------------------------------
Executing command:    port edit PORT-1 state Enable
Executing command:    port edit PORT-2 state Enable
Executing command:    port edit PORT-3 state Enable
Executing command:    port edit PORT-4 state Enable
Executing command:    port edit PORT-5 state Enable
Executing command:    port edit PORT-6 state Enable
Executing command:    port edit PORT-7 state Enable
Executing command:    port edit PORT-8 state Enable
Executing command:    port edit PORT-9 state Enable
Executing command:    port edit PORT-10 state Enable
Executing command:    port edit PORT-11 state Enable
Executing command:    port edit PORT-12 state Enable
-------------------------------------------------------------------
		Executing Testcase: Test_disable_all_port
-------------------------------------------------------------------
Executing command:    port edit PORT-1 state Disable
Executing command:    port edit PORT-2 state Disable
Executing command:    port edit PORT-3 state Disable
Executing command:    port edit PORT-4 state Disable
Executing command:    port edit PORT-5 state Disable
Executing command:    port edit PORT-6 state Disable
Executing command:    port edit PORT-7 state Disable
Executing command:    port edit PORT-8 state Disable
Executing command:    port edit PORT-9 state Disable
Executing command:    port edit PORT-10 state Disable
Executing command:    port edit PORT-11 state Disable
Executing command:    port edit PORT-12 state Disable
Status  Connector  Port name                       State    Speed     MDI 
------- ---------- ------------------------------- -------- --------- ----
Down    SFP-1      PORT-1                          Disabled No-link   --- 
Down    SFP-2      PORT-2                          Disabled No-link   --- 
Down    SFP-3      PORT-3                          Disabled No-link   --- 
Down    SFP-4      PORT-4                          Disabled No-link   --- 
Down    SFP-5      PORT-5                          Disabled No-link   --- 
Down    SFP-6      PORT-6                          Disabled No-link   --- 
Down    SFP-7      PORT-7                          Disabled No-link   --- 
Down    SFP-8      PORT-8                          Disabled No-link   --- 
Down    RJ45-9     PORT-9                          Disabled No-link   --- 
Down    RJ45-10    PORT-10                         Disabled No-link   --- 
Down    RJ45-11    PORT-11                         Disabled No-link   --- 
Down    RJ45-12    PORT-12                         Disabled No-link   --- 
Up      Management Management                      Enabled  100M-FD   MDI 
Down    ---        LAG-1                           Enabled  ---       --- 
Down    ---        LAG-2                           Enabled  ---       --- 
Down    ---        LAG-3                           Enabled  ---       --- 
Down    ---        LAG-4                           Enabled  ---       --- 
Down    ---        LAG-5                           Enabled  ---       --- 
Down    ---        LAG-6                           Enabled  ---       --- 

Port name : PORT-1
   Connector : SFP-1
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 
      State         : Configuring


Port name : PORT-2
   Connector : SFP-2
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 
      State         : Configuring


Port name : PORT-3
   Connector : SFP-3
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 
      State         : Configuring


Port name : PORT-4
   Connector : SFP-4
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 
      State         : Configuring


Port name : PORT-5
   Connector : SFP-5
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 10G-FD
      Advertisements: 10G-FD
      Link partner  : 
      State         : Configuring



Port name : PORT-6
   Connector : SFP-6
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 10G-FD
      Advertisements: 10G-FD
      Link partner  : 
      State         : Configuring


Port name : PORT-7
   Connector : SFP-7
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 10G-FD
      Advertisements: 10G-FD
      Link partner  : 
      State         : Configuring


Port name : PORT-8
   Connector : SFP-8
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 10G-FD
      Advertisements: 10G-FD
      Link partner  : 
      State         : Configuring


Port name : PORT-9
   Connector : RJ45-9
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 10M-FD,100M-FD,1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 10M-HD
      State         : Configuring



Port name : PORT-10
   Connector : RJ45-10
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 10M-FD,100M-FD,1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 10M-HD
      State         : Configuring


Port name : PORT-11
   Connector : RJ45-11
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 10M-FD,100M-FD,1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 10M-HD
      State         : Configuring



Port name : PORT-12
   Connector : RJ45-12
   State     : Disabled
   Status     : Down
   Speed      : ---
   Duplex     : ---
   MDI        : ---
   Pauses     : ---
   Protection : ---
   Auto-nego        : Enabled
      Capabilities  : 10M-FD,100M-FD,1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 10M-HD
      State         : Configuring


-------------------------------------------------------------------
		Test_disable_all_port		PASSED
-------------------------------------------------------------------
Executing command:    port edit PORT-1 state Enable
Executing command:    port edit PORT-2 state Enable
Executing command:    port edit PORT-3 state Enable
Executing command:    port edit PORT-4 state Enable
Executing command:    port edit PORT-5 state Enable
Executing command:    port edit PORT-6 state Enable
Executing command:    port edit PORT-7 state Enable
Executing command:    port edit PORT-8 state Enable
Executing command:    port edit PORT-9 state Enable
Executing command:    port edit PORT-10 state Enable
Executing command:    port edit PORT-11 state Enable
Executing command:    port edit PORT-12 state Enable
-------------------------------------------------------------------
		Executing Testcase: Test_enable_one_port
-------------------------------------------------------------------
Executing command:    port edit PORT-5 state enable
Status  Connector  Port name                       State    Speed     MDI 
------- ---------- ------------------------------- -------- --------- ----
Up      SFP-1      PORT-1                          Enabled  1G-FD     --- 
Up      SFP-2      PORT-2                          Enabled  1G-FD     --- 
Up      SFP-3      PORT-3                          Enabled  1G-FD     --- 
Up      SFP-4      PORT-4                          Enabled  1G-FD     --- 
Up      SFP-5      PORT-5                          Enabled  10G-FD    --- 
Up      SFP-6      PORT-6                          Enabled  10G-FD    --- 
Up      SFP-7      PORT-7                          Enabled  10G-FD    --- 
Up      SFP-8      PORT-8                          Enabled  10G-FD    --- 
Down    RJ45-9     PORT-9                          Enabled  No-link   --- 
Down    RJ45-10    PORT-10                         Enabled  No-link   --- 
Down    RJ45-11    PORT-11                         Enabled  No-link   --- 
Down    RJ45-12    PORT-12                         Enabled  No-link   --- 
Up      Management Management                      Enabled  100M-FD   MDI 
Down    ---        LAG-1                           Enabled  ---       --- 
Down    ---        LAG-2                           Enabled  ---       --- 
Down    ---        LAG-3                           Enabled  ---       --- 
Down    ---        LAG-4                           Enabled  ---       --- 
Down    ---        LAG-5                           Enabled  ---       --- 
Down    ---        LAG-6                           Enabled  ---       --- 

Port name : PORT-5
   Connector : SFP-5
   State     : Enabled
   Status    : Up
   Speed     : 10Gbps
   Duplex    : Full-Duplex
   MDI       : ---
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 10G-FD
      Advertisements: 10G-FD
      Link partner  : 
      State         : Disabled


-------------------------------------------------------------------
		Test_enable_one_port		FAILED
-------------------------------------------------------------------
Executing command:    port edit PORT-1 state Enable
Executing command:    port edit PORT-2 state Enable
Executing command:    port edit PORT-3 state Enable
Executing command:    port edit PORT-4 state Enable
Executing command:    port edit PORT-5 state Enable
Executing command:    port edit PORT-6 state Enable
Executing command:    port edit PORT-7 state Enable
Executing command:    port edit PORT-8 state Enable
Executing command:    port edit PORT-9 state Enable
Executing command:    port edit PORT-10 state Enable
Executing command:    port edit PORT-11 state Enable
Executing command:    port edit PORT-12 state Enable
-------------------------------------------------------------------
		Executing Testcase: Test_enable_all_port
-------------------------------------------------------------------
Executing command:    port edit PORT-1 state Ensable
Executing command:    port edit PORT-2 state Ensable
Executing command:    port edit PORT-3 state Ensable
Executing command:    port edit PORT-4 state Ensable
Executing command:    port edit PORT-5 state Ensable
Executing command:    port edit PORT-6 state Ensable
Executing command:    port edit PORT-7 state Ensable
Executing command:    port edit PORT-8 state Ensable
Executing command:    port edit PORT-9 state Ensable
Executing command:    port edit PORT-10 state Ensable
Executing command:    port edit PORT-11 state Ensable
Executing command:    port edit PORT-12 state Ensable
Status  Connector  Port name                       State    Speed     MDI 
------- ---------- ------------------------------- -------- --------- ----
Up      SFP-1      PORT-1                          Enabled  1G-FD     --- 
Up      SFP-2      PORT-2                          Enabled  1G-FD     --- 
Up      SFP-3      PORT-3                          Enabled  1G-FD     --- 
Up      SFP-4      PORT-4                          Enabled  1G-FD     --- 
Up      SFP-5      PORT-5                          Enabled  10G-FD    --- 
Up      SFP-6      PORT-6                          Enabled  10G-FD    --- 
Up      SFP-7      PORT-7                          Enabled  10G-FD    --- 
Up      SFP-8      PORT-8                          Enabled  10G-FD    --- 
Down    RJ45-9     PORT-9                          Enabled  No-link   --- 
Down    RJ45-10    PORT-10                         Enabled  No-link   --- 
Down    RJ45-11    PORT-11                         Enabled  No-link   --- 
Down    RJ45-12    PORT-12                         Enabled  No-link   --- 
Up      Management Management                      Enabled  100M-FD   MDI 
Down    ---        LAG-1                           Enabled  ---       --- 
Down    ---        LAG-2                           Enabled  ---       --- 
Down    ---        LAG-3                           Enabled  ---       --- 
Down    ---        LAG-4                           Enabled  ---       --- 
Down    ---        LAG-5                           Enabled  ---       --- 
Down    ---        LAG-6                           Enabled  ---       --- 

Port name : PORT-1
   Connector : SFP-1
   State     : Enabled
   Status    : Up
   Speed     : 1Gbps
   Duplex    : Full-Duplex
   MDI       : ---
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 1G-FD
      State         : Complete, link partner has auto-negotiation


Port name : PORT-2
   Connector : SFP-2
   State     : Enabled
   Status    : Up
   Speed     : 1Gbps
   Duplex    : Full-Duplex
   MDI       : ---
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 1G-FD
      State         : Complete, link partner has auto-negotiation



Port name : PORT-3
   Connector : SFP-3
   State     : Enabled
   Status    : Up
   Speed     : 1Gbps
   Duplex    : Full-Duplex
   MDI       : ---
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 1G-FD
      State         : Complete, link partner has auto-negotiation


Port name : PORT-4
   Connector : SFP-4
   State     : Enabled
   Status    : Up
   Speed     : 1Gbps
   Duplex    : Full-Duplex
   MDI       : ---
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 1G-FD
      State         : Complete, link partner has auto-negotiation


Port name : PORT-5
   Connector : SFP-5
   State     : Enabled
   Status    : Up
   Speed     : 10Gbps
   Duplex    : Full-Duplex
   MDI       : ---
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 10G-FD
      Advertisements: 10G-FD
      Link partner  : 
      State         : Disabled


Port name : PORT-6
   Connector : SFP-6
   State     : Enabled
   Status    : Up
   Speed     : 10Gbps
   Duplex    : Full-Duplex
   MDI       : ---
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 10G-FD
      Advertisements: 10G-FD
      Link partner  : 
      State         : Disabled


Port name : PORT-7
   Connector : SFP-7
   State     : Enabled
   Status    : Up
   Speed     : 10Gbps
   Duplex    : Full-Duplex
   MDI       : ---
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 10G-FD
      Advertisements: 10G-FD
      Link partner  : 
      State         : Disabled


Port name : PORT-8
   Connector : SFP-8
   State     : Enabled
   Status    : Up
   Speed     : 10Gbps
   Duplex    : Full-Duplex
   MDI       : ---
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 10G-FD
      Advertisements: 10G-FD
      Link partner  : 
      State         : Disabled


Port name : PORT-9
   Connector : RJ45-9
   State     : Enabled
   Status    : Up
   Speed     : 1Gbps
   Duplex    : Full-Duplex
   MDI       : MDI
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 10M-FD,100M-FD,1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 10M-HD,10M-FD,100M-HD,100M-FD,1G-HD,1G-FD,pause,asym-pause
      State         : Complete, link partner has auto-negotiation
      Mastership    : Auto


Port name : PORT-10
   Connector : RJ45-10
   State     : Enabled
   Status    : Up
   Speed     : 1Gbps
   Duplex    : Full-Duplex
   MDI       : MDI
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 10M-FD,100M-FD,1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 10M-HD,10M-FD,100M-HD,100M-FD,1G-HD,1G-FD,pause,asym-pause
      State         : Complete, link partner has auto-negotiation
      Mastership    : Auto


Port name : PORT-11
   Connector : RJ45-11
   State     : Enabled
   Status    : Up
   Speed     : 1Gbps
   Duplex    : Full-Duplex
   MDI       : MDIX
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 10M-FD,100M-FD,1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 10M-HD,10M-FD,100M-HD,100M-FD,1G-HD,1G-FD,pause,asym-pause
      State         : Complete, link partner has auto-negotiation
      Mastership    : Auto

Port name : PORT-12
   Connector : RJ45-12
   State     : Enabled
   Status    : Up
   Speed     : 1Gbps
   Duplex    : Full-Duplex
   MDI       : MDIX
   Pauses    : Do not send pauses, Receive pauses
   Protection: ---
   Auto-nego        : Enabled
      Capabilities  : 10M-FD,100M-FD,1G-FD,pause,asym-pause
      Advertisements: 1G-FD,pause,asym-pause
      Link partner  : 10M-HD,10M-FD,100M-HD,100M-FD,1G-HD,1G-FD,pause,asym-pause
      State         : Complete, link partner has auto-negotiation
      Mastership    : Auto

-------------------------------------------------------------------
		Test_enable_all_port		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_show_port_statistics_all_port
-------------------------------------------------------------------
Port name                       Tx packets         Tx errors          Rx packets  Rx errors         
------------------------------- ------------------ ------------------ ----------- ------------------
PORT-1                          0                  0                  0           0                 
PORT-2                          0                  0                  0           0                 
PORT-3                          0                  0                  0           0                 
PORT-4                          0                  0                  0           0                 
PORT-5                          790,200            0                  790,200     0                 
PORT-6                          0                  0                  0           0                 
PORT-7                          0                  0                  0           0                 
PORT-8                          0                  0                  0           0                 
PORT-9                          0                  0                  0           0                 
PORT-10                         0                  0                  0           0                 
PORT-11                         0                  0                  0           0                 
PORT-12                         0                  0                  0           0                 
Management                      2,414,274          0                  3,858,191   0                 
LAG-1                           0                  0                  0           0                 
LAG-2                           0                  0                  0           0                 
LAG-3                           0                  0                  0           0                 
LAG-4                           0                  0                  0           0                 
LAG-5                           0                  0                  0           0                 
LAG-6                           0                  0                  0           0                 

-------------------------------------------------------------------
		Test_show_port_statistics_all_port		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_show_port_statistics
-------------------------------------------------------------------
PORT-5 port statistics
Transmit statistics :
 Bytes good     :           2,920,449,528 Bytes total    :           2,920,449,528
 Unicast pkts   :                 790,200 Multicast pkts :                       0
 Broadcast pkts :                       0 Pause frames   :                       0
 Tagged frames  :                 790,200 CRC errors     :                       0
 Deferred       :                       0 Exces. defer.  :                       0
 Single coll.   :                       0 Multiple coll. :                       0
 Excessive coll.:                       0 Late coll.     :                       0
 Normal coll.   :                       0 FIFO errors    :                       0
 Pkts 64        :                       0 Pkts 65-127    :                       0
 Pkts 128-255   :                       0 Pkts 256-511   :                       0
 Pkts 512-1023  :                  43,020 Pkts 1024-1518 :                  82,862
 Pkts 1519-2047 :                 136,797 Pkts 2048-4095 :                 301,081
 Pkts 4096-8191 :                  99,143 Pkts 8192-more :                 127,297
 Large packets  :                 527,521 L1 BW util.    :                    0.00 %
 L1 rate (Mbps) :                    0.00 L2 rate (Mbps) :                    0.00

Receive statistics :
 Bytes good     :           2,920,449,528 Bytes total    :           2,920,449,528
 Short ok       :                       0 Short bad      :                       0
 Long ok        :                       0 Long bad       :                       0
 Unicast pkts   :                 790,200 Multicast pkts :                       0
 Broadcast pkts :                       0 Pause frames   :                       0
 Tagged frames  :                 790,200 CRC errors     :                       0
 Align errors   :                       0 Runt frames    :                       0
 Length errors  :                       0 False CRS      :                       0
 PHY errors     :                       0 FIFO errors    :                       0
 Ignored        :                       0 Bad opcode     :                       0
 Pkts 64        :                       0 Pkts 65-127    :                       0
 Pkts 128-255   :                       0 Pkts 256-511   :                       0
 Pkts 512-1023  :                  43,020 Pkts 1024-1518 :                  82,862
 Pkts 1519-2047 :                 136,797 Pkts 2048-4095 :                 301,081
 Pkts 4096-8191 :                  99,143 Pkts 8192-more :                 127,297
 Large packets  :                 527,521 L1 BW util.    :                    0.00 %
 L1 rate (Mbps) :                    0.00 L2 rate (Mbps) :                    0.00

-------------------------------------------------------------------
		Test_show_port_statistics		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_add_filter
-------------------------------------------------------------------
Executing command:    filter add l2 FilterVLAN100  vlan1-id 100 enable
Filter name                     MAC destination   MAC source        Etype  VLAN1 VLAN2
------------------------------- ----------------- ----------------- ------ ----- -----
*default                        ---               ---                  ---   ---   ---
PAA-Discovery                   FF:FF:FF:FF:FF:FF ---               0x88FC   ---   ---
FilterVlan100                   ---               ---                  ---   100   ---
FilterVLAN100                   ---               ---                  ---   100   ---
catchAll                        ---               ---                  ---   ---   ---
ieeeBPDU                        01:80:C2:00:00:00 ---                  ---   ---   ---
ciscoBPDU                       01:00:0C:CC:CC:CD ---                  ---   ---   ---
macDst                          00:15:AD:01:01:01 ---                  ---   ---   ---
macSrc                          ---               00:15:AD:01:01:01    ---   ---   ---
frameType                       ---               ---               0x9000   ---   ---
firstVlanId                     ---               ---                  ---   100   ---
firstVlanPrior                  ---               ---                  ---   ---   ---
firstVlanCfi                    ---               ---                  ---   ---   ---
secondVlanId                    ---               ---                  ---   ---   200
secondVlanPrior                 ---               ---                  ---   ---   ---
secondVlanCfi                   ---               ---                  ---   ---   ---

-------------------------------------------------------------------
		Test_add_filter		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_edit_filter
-------------------------------------------------------------------
Executing command:    filter edit l2 FilterVLAN100  vlan1-id 200 enable
Filter name                     MAC destination   MAC source        Etype  VLAN1 VLAN2
------------------------------- ----------------- ----------------- ------ ----- -----
*default                        ---               ---                  ---   ---   ---
PAA-Discovery                   FF:FF:FF:FF:FF:FF ---               0x88FC   ---   ---
FilterVlan100                   ---               ---                  ---   100   ---
FilterVLAN100                   ---               ---                  ---   200   ---
catchAll                        ---               ---                  ---   ---   ---
ieeeBPDU                        01:80:C2:00:00:00 ---                  ---   ---   ---
ciscoBPDU                       01:00:0C:CC:CC:CD ---                  ---   ---   ---
macDst                          00:15:AD:01:01:01 ---                  ---   ---   ---
macSrc                          ---               00:15:AD:01:01:01    ---   ---   ---
frameType                       ---               ---               0x9000   ---   ---
firstVlanId                     ---               ---                  ---   100   ---
firstVlanPrior                  ---               ---                  ---   ---   ---
firstVlanCfi                    ---               ---                  ---   ---   ---
secondVlanId                    ---               ---                  ---   ---   200
secondVlanPrior                 ---               ---                  ---   ---   ---
secondVlanCfi                   ---               ---                  ---   ---   ---

-------------------------------------------------------------------
		Test_edit_filter		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_detete_filter
-------------------------------------------------------------------
Executing command:    filter delete l2 FilterVLAN100
Filter name                     MAC destination   MAC source        Etype  VLAN1 VLAN2
------------------------------- ----------------- ----------------- ------ ----- -----
*default                        ---               ---                  ---   ---   ---
PAA-Discovery                   FF:FF:FF:FF:FF:FF ---               0x88FC   ---   ---
FilterVlan100                   ---               ---                  ---   100   ---
catchAll                        ---               ---                  ---   ---   ---
ieeeBPDU                        01:80:C2:00:00:00 ---                  ---   ---   ---
ciscoBPDU                       01:00:0C:CC:CC:CD ---                  ---   ---   ---
macDst                          00:15:AD:01:01:01 ---                  ---   ---   ---
macSrc                          ---               00:15:AD:01:01:01    ---   ---   ---
frameType                       ---               ---               0x9000   ---   ---
firstVlanId                     ---               ---                  ---   100   ---
firstVlanPrior                  ---               ---                  ---   ---   ---
firstVlanCfi                    ---               ---                  ---   ---   ---
secondVlanId                    ---               ---                  ---   ---   200
secondVlanPrior                 ---               ---                  ---   ---   ---
secondVlanCfi                   ---               ---                  ---   ---   ---

-------------------------------------------------------------------
		Test_detete_filter		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_policy_show_configuration
-------------------------------------------------------------------
Executing command:    policy show configuration Traffic-10 10
policy show configuration Traffic-10 10

Policy 10 on PORT-10
   State             : Disabled
   Action            : Permit
   Filter type       : L2
   Filter name       : 
   Monitoring        : Disabled
   Monitor           : ---
   Out-port          : PORT-5          
   EVC mapping       : 
      Encapsulation  : None
      Ethertype1     : C-VLAN (0x8100)
      VLAN1 ID       : 0   
      Ethertype2     : C-VLAN (0x8100)
      VLAN2 ID       : 0   
   CoS mapping       : 
      PCP action     : Preserve
      1-State        : Disabled
      1-Type         : PCP VLAN
      1-Cos profile  : ---
      1-Regulator set: ---
      2-State        : Disabled
      2-Type         : PCP VLAN
      2-Cos profile  : ---
      2-Regulator set: ---
   Default mapping   : 
      Pre-marking    : Green
      Green CFI      : 0
      Green PCP      : 0
      Yellow CFI     : 0
      Yellow PCP     : 0
      Regulator name : ---
      Regulation     : Disabled
   Queuing Profile   :
      Name           : default-queuing-profile

C403-9125: 
-------------------------------------------------------------------
		Test_policy_show_configuration		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_policy_add
-------------------------------------------------------------------
Executing command:    filter add l2 FilterVlan100  vlan1-id 100 enable
Executing command:    policy edit Traffic-1 5 out-port PORT-8 filter l2 FilterVlan100 action Permit state Enable
Executing command:    policy show configuration Traffic-1 5
policy show configuration Traffic-1 5

Policy 5 on PORT-1
   State             : Enabled
   Action            : Permit
   Filter type       : L2
   Filter name       : FilterVlan100
   Monitoring        : Disabled
   Monitor           : Monitor-1
   Out-port          : PORT-8          
   EVC mapping       : 
      Encapsulation  : None
      Ethertype1     : C-VLAN (0x8100)
      VLAN1 ID       : 0   
      Ethertype2     : C-VLAN (0x8100)
      VLAN2 ID       : 0   
   CoS mapping       : 
      PCP action     : Preserve
      1-State        : Disabled
      1-Type         : PCP VLAN
      1-Cos profile  : ---
      1-Regulator set: ---
      2-State        : Disabled
      2-Type         : PCP VLAN
      2-Cos profile  : ---
      2-Regulator set: ---
   Default mapping   : 
      Pre-marking    : Green
      Green CFI      : 0
      Green PCP      : 0
      Yellow CFI     : 0
      Yellow PCP     : 0
      Regulator name : ---
      Regulation     : Disabled
   Queuing Profile   :
      Name           : default-queuing-profile

C403-9125: 
-------------------------------------------------------------------
		Test_policy_add		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_policy_show_statistic
-------------------------------------------------------------------
Executing command:    policy show statistics Traffic-3 1
policy show statistics Traffic-3 1

Codes : E - Enable, P - Permit

Policies statistics for Traffic-3 on port PORT-3
Index E P Filter name       Packets good      Bytes good            Packets bad
----- - - ----------------- ----------------- --------------------- ------------
1     N Y                   0                 0                     0           

C403-9125: 
-------------------------------------------------------------------
		Test_policy_show_statistic		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_user_add
-------------------------------------------------------------------
Executing command:    user add user1
User name  First name   Last name    Phone number   E-mail
---------- ------------ ------------ -------------- -----------------------------
admin                                               
user1                                               

-------------------------------------------------------------------
		Test_user_add		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_user_permission
-------------------------------------------------------------------
Executing command:    user permissions edit user1 add-group Admin
User user1 is a member of the following groups

Group              Member
------------------ ------
Admin              Yes 

-------------------------------------------------------------------
		Test_user_permission		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_user_edit
-------------------------------------------------------------------
Executing command:    user edit user1 email abc@gmail.com
User name    : user1
First name   : 
Last name    : 
Phone number : 
E-mail       : abc@gmail.com

-------------------------------------------------------------------
		Test_user_edit		PASSED
-------------------------------------------------------------------
-------------------------------------------------------------------
		Executing Testcase: Test_user_delete
-------------------------------------------------------------------
Executing command:    user delete user1
User name  First name   Last name    Phone number   E-mail
---------- ------------ ------------ -------------- -----------------------------
admin                                               

-------------------------------------------------------------------
		Test_user_delete		PASSED
-------------------------------------------------------------------

 
 
Test Result!!!
==================================================================
	Test_disable_one_port                             FAILED
	Test_disable_all_port                             PASSED
	Test_enable_one_port                              FAILED
	Test_enable_all_port                              PASSED
	Test_show_port_statistics_all_port                PASSED
	Test_show_port_statistics                         PASSED
	Test_add_filter                                   PASSED
	Test_edit_filter                                  PASSED
	Test_detete_filter                                PASSED
	Test_policy_show_configuration                    PASSED
	Test_policy_add                                   PASSED
	Test_policy_show_statistic                        PASSED
	Test_user_add                                     PASSED
	Test_user_permission                              PASSED
	Test_user_edit                                    PASSED
	Test_user_delete                                  PASSED

'''
print(str)