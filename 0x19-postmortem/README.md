*Project instructions:*  
  
*"Using one of the web stack debugging projects issue*
*or an outage you have personally faced, write a postmortem. Most*
*of you never have faced an outage, so just get creative and invent your own."*
  
*I decided to base the postmortem loosely on a 2017 AWS outage.*  
  
# Postmortem  
  
• Outage **start** time: Monday, September 27 at 3:06 PM Eastern Standard Time.  
• Outage **end** time: Monday, September 27 at 7:27 PM Eastern Standard Time.   
    
• What occurred: A large number of our servers were shut down from our US-EAST-1 region.  
• What clients and users experienced: Affected users were complety unavailable to access our client's websites or had degraded website performances. We ourselves experoenced an outage as these servers were also used to monitor the health of our cloud service.    
• Percentage of users affected: About 45% - 55% clients had their websites down.  
• Root cause of the problem: Engineer executed wrong comamnd which shut down a significant amount of servers.  
  
## Timeline  
• When was issue detected: Early afternoon at 3:06 PM EST.  
• How was issue detected: A large portion of our clients started calling customer service.  
• Actions taken: Unable to access our own dashboard because of the outage, we had to rely on Twitter to communicate withour customers.  
• Debugging path taken:  
• Who was the issue escalated to:  
• How was the incident resolved:  
  
## Root cause and resolution
• Deatiled explination of what caused the problem: An engineer was debugging an issue with our billing system when he accidentally mistyped a command. 
• Detailed explination of how the problem was fixed:  
  
## Corrective and preventative measures:  
Things that can be improved/fixed:  
•  
•  
•  
•  
•  
•  
