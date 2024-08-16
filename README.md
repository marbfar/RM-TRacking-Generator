# RM-Tracking-Generator

### Purpose

This tool was created to address a specific challenge when sending signed-for letters via Royal Mail. In situations where our client sends out large mailings—sometimes up to 10,000 letters—they need a reliable way to track which letters have been delivered. For instance, if a customer claims they did not receive a letter about their debt, the client would need the tracking number to verify the delivery status. Without a system to manage these tracking numbers, verifying deliveries becomes difficult.

The RM-Tracking-Generator provides a solution by batch generating tracking label references. These references can then be integrated back into the customer data file, enabling our client to quickly and easily check the delivery status of each letter.

### How to Use

1. **Enter the total number of tracking labels you need to generate.**
2. **Enter the 8-digit reference number of the first label.**  
   For example, if your first label is `KL111122229GB`, enter `11112222` (excluding the prefix `KL` and suffix `GB`). 

This process will generate all the necessary tracking references for your mailing list, making it easier to manage and verify deliveries.
