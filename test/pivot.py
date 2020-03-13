fin = "/Users/steve/Downloads/log+death-rate.csv"
from tabl import Tabl as tbl
from tabl import *
from infixpy import *

def lmap(fn,x):  return list(map(fn,x))


def tp(msg,o=None):
  import datetime
  omsg = ": %s" %repr(o) if o is not None else ""
  dtf = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  print(f"[{dtf}] {msg}{omsg}")


t = read_tabl(fin)
tp(t)

def newCols(cols, grp):
  def cstname(grp):
    return '_'.join(grp['country'],grp['state'])
  def cname(grp,col):
    return '_'.join(cstname(grp),col)
  grp = sorted(grp,key=cname)
  # cols = g.columns
  # newcols = lmap(lambda g: [cname(grp,'confirmed'),cname(grp,'deaths')])
  # return newcols
  out = [grp[i]
  return grp

cols = ['country','state','confirmed','deaths']
t2 = t[:,cols]
def newCols1(grp):

for c in cols:
  t2 = t2.group_by('day',[(newCols,cols)])
tp(t2)