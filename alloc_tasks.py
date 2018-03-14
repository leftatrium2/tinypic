# -*- coding: utf-8 -*-
def alloc_tasks(remain_num_list, img_file_list, img_tar_list):
    # 任务表
    tasks = {}
    if remain_num_list is None or img_file_list is None:
        return

    num = 0
    for key in remain_num_list:
        tasks[key] = {}
        tasks[key]['img'] = []
        tasks[key]['tar'] = []
        while num < len(img_file_list):
            tasks[key]['img'].append(img_file_list[num])
            tasks[key]['tar'].append(img_tar_list[num])
            num += 1
            if len(tasks[key]['img']) >= remain_num_list[key]:
                break
    return tasks
