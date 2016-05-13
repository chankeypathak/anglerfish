#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Multiprocessing helper."""


import logging as log
import sys

from concurrent import futures


class __MultiProcessed():

    def __init__(self, cpu_num, thread_num):
        self.cpu_num, self.thread_num = cpu_num, thread_num

    def __multi_cpu(self, func, job_queue, timeout):
        if __getLen(job_queue) == 0:
            return []
        index = __get_index(job_queue, self.cpu_num)
        cpu_pool = multiprocessing.Pool(processes=self.cpu_num)
        mgr = multiprocessing.Manager()
        process_bar = mgr.list()
        for i in range(self.cpu_num):
            process_bar.append(0)
        result_queue = cpu_pool.map(
            __multi_thread,
            [[func, self.cpu_num, self.thread_num, job_queue[index[i][0]:
            index[i][1] + 1], timeout, process_bar, i]
                for i in range(len(index))])
        result = []
        for rl in result_queue:
            for r in rl:
                result.append(r)
        return result

def __func(argv):
    argv[2][argv[3]] = round((argv[4] * 100.0 / argv[5]), 2)
    sys.stdout.write(str(argv[2]) + ' ||' + '->' + "\r")
    sys.stdout.flush()
    return argv[0](argv[1])


def __multi_thread(argv):
    thread_num = argv[2]
    if __getLen(argv[3]) < thread_num:
        thread_num = argv[3]
    func_argvs = [[argv[0], argv[3][i], argv[5], argv[6], i, len(argv[3]) ]
                      for i in range(len(argv[3]))]
    result = []
    if thread_num == 1:
        for func_argv in func_argvs:
            result.append(__func(func_argv))
        return result
    thread_pool = futures.ThreadPoolExecutor(max_workers=thread_num)
    result = thread_pool.map(__func, func_argvs, timeout=argv[4])
    return [r for r in result]


def __get_index(job_queue, split_num):
    job_num = __getLen(job_queue)
    if job_num < split_num:
        split_num = job_num
    each_num = job_num / split_num
    index = [[i * each_num, i * each_num + each_num - 1]
                 for i in range(split_num)]
    residual_num = job_num % split_num
    for i in range(residual_num):
        index[split_num - residual_num + i][0] += i
        index[split_num - residual_num + i][1] += i + 1
    return index


def __getLen(_list):
    return 0 if _list == None else len(_list)


def multiprocessed(func, job_queue, cpu_num=1, thread_num=1, timeout=None):
    multicpu_instance = __MultiProcessed(cpu_num, thread_num)
    return multicpu_instance.__multi_cpu(func, job_queue, timeout)
