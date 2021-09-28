*Project instructions:*  
  
*"Using one of the web stack debugging projects issue*
*or an outage you have personally faced, write a postmortem. Most*
*of you never have faced an outage, so just get creative and invent your own."*
  
*I decided to base the postmortem loosely on a 2017 AWS outage.*  
  
# Postmortem  
  
• Outage **start** time: Monday, September 27 at 3:06 PM Eastern Standard Time.  
• Outage **end** time: Monday, September 27 at 7:27 PM Eastern Standard Time.   
    
• What occurred: A large number of our servers were shut down from our US-EAST-1 region.  
• What clients and users experienced: Affected users were complety unavailable to access our client's websites or had degraded website performances. We ourselves experienced an outage as these servers were also used to monitor the health of our cloud service.    
• Percentage of users affected: About 45% - 55% of clients had their websites down.  
• Root cause of the problem: Engineer executed wrong command which shut down a significant amount of servers.  
  
## Timeline  
• When was issue detected: Early afternoon at 3:06 PM EST.  
• How was issue detected: A large portion of our clients started calling customer service.  
• Actions taken: Unable to access our own dashboard because of the outage, we had to rely on Twitter to communicate with our customers.  
• Debugging path taken: We immidietly restarted the systems and validated all metadata.  
• Who was the issue escalated to: Head of the AWS S3 Service Deparment.   
• How was the incident resolved: Servers were restarted.    
  
## Root cause and resolution
• Detailed explination of what caused the problem: An engineer was debugging an issue with our billing system when he accidentally mistyped a command. The engineer meant to execute a command intended to remove only a small number of servers running one of the S3 subsystems. Unfortunately, one of the inputs to the command was entered incorrectly resulting in a larger set of servers being removed. These servers supported other major systems that manage data resulting in catastrophic outages. Restarting these servers took much longer than anticipated resulting in other subsystems that rely on them to malfunction. AWS has experienced massive growth over the last several years and the process of restarting these services and running the necessary safety checks to validate the integrity of the metadata took longer than expected.  
• Detailed explination of how the problem was fixed: After validating all data and fully restarting the system, and taking care of all the backlogged requests, the issue was fixed
  
## Corrective and preventative measures:  
Things that can be improved/fixed:  
•  We will modify our server removing tool to prevent it from removing too much capacity too quickly and to prevent capacity from being removed when any subsystem reaches its minimum required capacity.  
• Reprioritize work to partition one of the affected subsystems into smaller “cells,” which was planned for later this year but we will now begin right away.  
• Status Health Dashboard now runs across multiple AWS regions so that customers don’t have to rely on Twitter to learn about the health of their cloud infrastructure in case of another outage  
