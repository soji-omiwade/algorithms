import re
idate = re.compile(r'INTERNALDATE "'
	r'(?P<day>[ 0123][\d])-(?P<month>\w{3})-(?P<year>\d{4})'
    r' (?P<hour>\d\d):(?P<min>\d\d):(?P<sec>\d\d)'
    r' (?P<zonem>[+-])(?P<zonen>\d{4})')