def getFileList(dir, xrootPrefix='', histname='', maxN=-1):
  import os, subprocess
  filelist = []
  edir = os.path.expandvars(dir)
  p = subprocess.Popen(["ls "+ edir], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  for line in p.stdout.readlines():
    if not (histname=="" or line.count(histname)):continue
    try:
      fname = line[:-1].split()[-1]
      filelist.append(fname)
    except:
      print "Could not read", line
  filelist = [xrootPrefix+edir+'/'+f for f in filelist]
  if maxN>=0:
    filelist = filelist[:maxN]
  return filelist
