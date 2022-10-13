'''
Validate an IP address (IPv4). An address is valid if and only if it is in the form "X.X.X.X", where each X is a number from 0 to 255.

For example, "12.34.5.6", "0.23.25.0", and "255.255.255.255" are valid IP addresses, while "12.34.56.oops", "1.2.3.4.5", and "123.235.153.425" are invalid IP addresses.

Examples:

    ip = '192.168.0.1'
    output: true

    ip = '0.0.0.0'
    output: true

    ip = '123.24.59.99'
    output: true

    ip = '192.168.123.456'
    output: false
    Constraints:

        [time limit] 5000ms
        [input] string ip
        [output] boolean

parse it into its pieces
validate each piece
'''
def toint(string):
    val = 0
    for ch in string:
        val = 10 * val + (ord(ch) - ord('0'))
    return val

def getnext(ip, sloc):
    token = []
    idx = sloc
    while idx < len(ip) and ip[idx] != '.':
        token.append(ip[idx])
        idx += 1
    return token, idx + 1

def isvalid(token):
    for ch in token:
        if not '0' <= ch <= '9':
            return False
    return len(token) < 4 and toint(token) < 256

def validateIP(ip: str) -> bool:
    count = 0
    sloc = 0
    while True:
       token, sloc = getnext(ip, sloc)
       if not token:
           break
       else:
           if not isvalid(token):
               break
           else:
               count += 1
    return count == 4

ip = '12.34.56.78'
print(validateIP(ip))

ip = '2.2.'
print(validateIP(ip))

ip = '12.3.5.78'
print(validateIP(ip))

ip = '12.34..78'
print(validateIP(ip))
