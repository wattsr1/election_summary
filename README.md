# Election Summary Using PyPoll

## Overview

This project was developed to create the PyPoll tool using Python script to automate the process of auditing the votes and provide a summary that can be submitted to the Election Commission.  The data for each polling location is stored in a comma seperated values(CSV) file which identifies each unique vote, the county that it was cast and the candidate that was selected.  These files are large and is as challenge to summarize quickly to allow the Elections Commission to present the results in a quick manner. To help with this process an example of an automated script using Python was developed to present a summary of the results, which included the total votes cast, list of the candidates and the votes that they received, and identify the winner and the votes that they received.  In addition, the number of votes cast by county was also included to show the turnout in each county and identify the county with the highest voter turnout.  The results were stored in a text file containing a summary of the results that could be provided to the Elections Commission.
---
## Election - Audit Results

Using the script that was developed we could provide a quick summary of the election results.  These results are available in the [text file](analysis/election_analysis.txt) that we provided the Election Commission.

* Using the data collected in the CSV file we could determine that there were 369, 711 votes cast
  -The was calculated by calculating the total entries contained in the file which represented a single vote
  -The code ran a loop reading each row of the file individually
  code image
* Based on the audit the following results for each county are as follows:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
* From this we can observe that Denver county had the greatest voter turnout at 306,055 making up 82.8% of the total vote
* From the candidates in the election the following results were collected:
  - Charles Casper Stockham recieved 23.0% of the vote with a total of 85,213 votes.
  - Diana DeGette received 73.8% of the vote with a total of 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with a total of 11,606 votes.
* Based on the results the winner of the congressional election was:
  - Diana DeGette with a total of 272,892 votes with a total of 73.8% of the vote.

The results of the congressional election were calculated using loops to idenfiy the candidate and the county that each vote was cast. The results were collected and written into the election analysis document that summerized the votes for each candidate and the counties that the votes were cast.  This automated audit of the results rapidly provides a summary that can be submitted for the Election Commission.  A summary of the coding used to collect this data is summaried below:

coding image.
---
## Election - Audit Summary

### Expansion of use

The use of this script to automate the audit and analysis of the voting results give the Election Commission a tool to provide quickly gather the results of the election which can be presented and shared using the summary provide with the election analysis summary text file. This file can be used to share the results in a timely manner.  This code can be used across other election to complete the audit of the results and analyze the results to provide the winner and the distribution of the votes between the candidates and the counties where the votes were cast.  This can be expanded across other elections and provide the summary of results for each.  The data can be used to track voter turnout over time and provide information that can be used by election commission to share the findings.

### Added Features

To facilitate the expanded use of the PyPoll for other elections and providing the election commission with and analysis and audit of the results.  To share with the election commission some other functions that could be incorperated into PyPoll to expand its use.  

1. Customize the file naming to allow for expanded use of the data being collected

Including this functionality will help organize the file containing the analysis of the results allowing them to be stored and easily referenced for future use. The format can include the date of the election result analysis.  An example of the code used to create this functionally is seen below: 




2. Include the breakdown of voting results per county based on the results.  This will show the votes for each candidate as seen in each county in the election. An example of the code used to introduce this to the analysis is seen below.







