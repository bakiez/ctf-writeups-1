import itertools as it
import re

c = '11313221111241132131614122141231311261112124131111132131623212141221322111131312141321222141621211124114212162114241131222211121623122211112211112133162321214121211135321221412121112112113221221111221416231242121613111131222211121124163221214216352123221111241132212211121621322141311322111216241121322214163111113221221112163113211422111216213222111131321623212141221322111231131721142123213221142312262131221112222221111222212411222322132221221322111123222311221112211421322312211423122111112312231222143212221322221135111211111321142411213221112132221126111215112123211211232122111'

d = ''.join(str(n) * int(c) for n,c in zip(it.cycle([0,1]), c))
print ''.join(chr(int(x,2)) for x in re.findall('.{8}', d)) 
