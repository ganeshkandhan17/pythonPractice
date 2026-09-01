import modules

modules.otp()
modules.greet('ganesh')



from modules import otp, greet

otp()
greet()

import modules as m

m.otp()
m.greet('ganesh')

from modules import *
otp()
greet()
