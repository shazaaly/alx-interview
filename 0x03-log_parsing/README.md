0x03. Log Parsing
ALXSE Task
#### Description
This script is designed to parse log files, specifically focusing on web server access logs. It reads input line by line from standard input (stdin) and computes various metrics based on the log data. The script is particularly useful for analyzing and summarizing HTTP request data in real-time.

#### Input Format
The script expects each line of input in the following format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

Lines that do not match this format will be skipped.

#### Features
- **Real-Time Data Processing**: The script reads from stdin, allowing for real-time log processing.
- **File Size Computation**: It calculates the total file size of all processed requests.
- **Status Code Summary**: The script aggregates the number of occurrences for each HTTP status code.

#### Output
After processing every 10 lines or upon receiving a keyboard interruption (CTRL + C), the script outputs the following:
1. **Total File Size**: Displays the cumulative file size of all requests.
2. **Status Code Count**: Lists the count of each HTTP status code encountered. The possible status codes are 200, 301, 400, 401, 403, 404, 405, and 500. Status codes are displayed in ascending order.

#### Example Usage
To use this script, pipe the output of a log generator (like `0-generator.py`) into `0-stats.py`:

```bash
./0-generator.py | ./0-stats.py
```

#### Sample Output
```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
...
```

#### Requirements
- Python 3.x
- Standard Python libraries: `sys`, `datetime`

#### Installation
No special installation is required. Ensure that Python 3.x is installed on your system.

#### Usage
To run the script, use the command line to execute it with Python. For real-time log parsing, pipe the output of your log generator into this script.

