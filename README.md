# Simple DoS detect

This is a simple DoS attack detect Python scripts. I determine the attack condition based on network utilization and packet count.

Traditional IDS detects DoS attacks based on packet count. Therefore, if the packet count exceeds the threshold value, we consider the DoS attack to be detected.

The network utilization is used to determine the success rate of the attack. If it exceeds the defined threshold, it can be referred to as a successful attack.

Finally, I utilized the subprocess module to enable concurrent execution of two scripts, achieving an automated testing approach.
