# coding: UTF-8

import multiprocessing

if multiprocessing.cpu_count() == 1:
    print 'maybe VM'
else:
    print 'real machine?'