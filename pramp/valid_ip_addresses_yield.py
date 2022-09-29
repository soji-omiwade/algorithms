def tokens(ip):
    loc = 0
    while loc < len(ip):
        token = []
        for idx in range(loc, len(ip)):
            if ip[idx] == '.':
                break
            else:
               token.append(ip[idx]) 
        loc = idx + 1
        yield token

def isvalid(token):
    val = 0
    for ch in token:
        if '0' <= ch <= '9':
            val = 10 * val + ord(ch) - ord('0')
            if val > 255:
                break
        else:
            break
    else:
        return bool(token)
    return False

def validateIP(ip):
    """
    @param ip: str
    @return: bool
    valid tokens: 
        is a number: &*
        can't be empty: 12..12 
    """
    count = 0
    for token in tokens(ip):
        if isvalid(token):
            count += 1
        else:
            break # invalid token
    else:
        return count == 4
    return False

ip = '192.168.0.1'
print(validateIP(ip))

ip = '0.0.0.0'
print(validateIP(ip))

ip = '123.24.59.99'
print(validateIP(ip))

ip = '192.168.123.456'
print(validateIP(ip))

