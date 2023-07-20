import os

# __file__就是constant所在路径/os.pardir上一层路径conmmon/os.pardir上一层路径基于百年党史~/
BASE_DIR = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
DATA_DIR = os.path.join(BASE_DIR, "data")

