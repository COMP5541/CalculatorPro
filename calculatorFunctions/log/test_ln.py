import math
from CalculatorPro import ln

#X is Zero
assert ln.loge(0)==float('-Inf'),"X=0 Fail"

#X is less than Zero
assert math.isnan(ln.loge(-1)),"X=-1 Fail"

#0 < X < 1
assert round(math.log(0.5),10) == ln.loge(0.5),"X=0.5 Fail"

#X is larger than One
assert round(math.log(2),10) == ln.loge(2),"X=2 Fail"
