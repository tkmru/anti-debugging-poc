# coding: UTF-8

import _winreg

handle = _winreg.OpenKey(
        _winreg.HKEY_LOCAL_MACHINE,
        'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum'
        )

try:
    reg_val = _winreg.QueryValueEx(handle, '0')[0]

    if "VMware" in reg_val:
        print "Vmware Detected"
    elif "VBOX" in reg_val:
        print "Virtualbox Detected"

finally:
    _winreg.CloseKey(handle)