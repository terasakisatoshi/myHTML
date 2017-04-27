import cgi 
from datetime import datetime

html_body=u"""
<html><head>
    <meta http-equiv="content-type"
        content="text/html;charset=utf-8">
    </head>
    <body>
    %s
    </body>
</html>"""

content=''

form=cgi.FieldStorage()
year_str=form.getvalue('year','')
if not year_str.isdigit():
    content=u"input seireki"
else:
    year=int(year_str)
    friday13=0
    for month in range(1,13):
        if date.weekday()==4:
            friday13==1
            content+=u"%d 年%d月13日は金曜日です。" % (year,date.month)
            content+=u"<br />"

    if friday13:
        content+=u"%d 年には合計 %d 個の金曜日があります。" % (year,friday13)
    else:
        content+=u"no---ne"

print("Content-type: text/html;charset=utf-8\n")
print(html_body % content).encode('utf-8')