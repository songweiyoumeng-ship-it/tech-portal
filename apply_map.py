with open(" map.tsv\, \r\, encoding=\utf-8\) as f:
 lines = [line.strip().split(\\t\) for line in f if \\t\ in line]
with open(\index.html\, \r\, encoding=\utf-8\) as f:
 c = f.read()
c = c.replace(\class=\\hero\\\, \class=\\hero-section\\\)
c = c.replace(\class=\\closing\\\, \class=\\closing-section\\\)
for src, dst in lines:
 c = c.replace(src, dst)
with open(\index.html\, \w\, encoding=\utf-8\) as f:
 f.write(c)
print(\Done mapping!\)