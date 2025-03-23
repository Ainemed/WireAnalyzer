from subprocess import *

def open_sys_file():
    call("python", "sniffer.py","en0")

open_sys_file()