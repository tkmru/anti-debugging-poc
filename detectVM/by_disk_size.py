# coding: UTF-8

import os

def GetDiskSpaceForWin(drive):
    from ctypes import c_ulonglong, windll, byref

    free_bytes_available       = c_ulonglong()
    total_number_of_bytes      = c_ulonglong()
    total_number_of_free_bytes = c_ulonglong()
    
    windll.kernel32.GetDiskFreeSpaceExA(
        drive,
        byref(free_bytes_available),
        byref(total_number_of_bytes),
        byref(total_number_of_free_bytes)
    )

    total_number_of_gigabytes = total_number_of_bytes.value / (1024 ** 3)

    return total_number_of_gigabytes


if __name__ == '__main__':
    disk_space = 0

    if os.name == 'nt':
        disk_space = GetDiskSpaceForWin('C:')

    elif os.name == 'posix':
        statvfs = os.statvfs('/')
        disk_space = statvfs.f_frsize * statvfs.f_blocks / (1024 ** 3)

    if disk_space < 100:
        print 'maybe VM'
    else:
        print 'real machine?'
