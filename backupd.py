# -*- coding: utf-8 -*-
"""

@author: bwb0de
"""

from sys import platform
from os import sep, system, linesep
from modules.config.pathc import *
from modules.config.mail_e_whats import *
from modules.config.sps_var import *
from modules.config.unb_sigra import *
#from modules.db_functions import *
#from modules.sae2spsdb import *
from modules.var_translation import *
from modules.db_skell import *
#from modules.bwtools import *

fn = backup_to_sqlite(engine.connect())

print "* Backup concluído..."
