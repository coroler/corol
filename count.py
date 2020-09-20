#!/usr/bin/python2.7
# -*- coding: utf-8 -*-


class Solution_permuteUnique(object):
    """
    给定一个可包含重复数字的序列，返回所有不重复的全排列。
    输入: [1,1,2]
    输出: [[1,1,2],
           [1,2,1],
           [2,1,1]]
    """

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_dict = dict()
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        nums_info_list = sorted(nums_dict.items(), key=lambda x: (-x[1], x[0]))

        #  序列中出现的数字按出现次数归类排序
        nums_list = list()
        for nums_info in nums_info_list:
            if not nums_list:
                num_list = list()
                for _ in range(nums_info[1]):
                    num_list.append(nums_info[0])
                nums_list.append(num_list)
                continue

            new_nums_list = list()
            for num_list in nums_list:
                new_nums_list += self.num_list_create(num_list, nums_info)
                nums_list = new_nums_list

        return nums_list

    def num_list_create(self, nums_list, nums_info):
        """
        :param nums_list: 已完成排列的
        :param nums_info: 下一步要插入排列中的新数字
               nums_info[0]: 新数字
               nums_info[1]：新数字在序列中出现的次数
        :return: 新数字插入nums_list中得到的新排列list
        """
        num_for_insert_create_list = self.num_for_insert_create_list(nums_info[1], len(nums_list) + 1)

        new_nums_list = list()
        for num_for_insert_create in num_for_insert_create_list:
            num_list = list()
            for i in range(len(num_for_insert_create)):
                if num_for_insert_create[i]:
                    for _ in range(num_for_insert_create[i]):
                        num_list.append(nums_info[0])
                if i != len(num_for_insert_create) - 1:
                    num_list.append(nums_list[i])
            new_nums_list.append(num_list)

        return new_nums_list

    def num_for_insert_create_list(self, count, empty_count):
        """
        :param count: 要插入序列中的新数字出现的次数
        :param empty_count: 需要分配的序列存在可插入的间隔数，
                            序列中每个数的两端，即【序列长 + 1】个间隔数
                            如：[1, 1, 2, 2] 存在5个间隔数
        :return: 间隔数中插入新数字的不重复list，长度为间隔数
                 填写每个间隔处插入该数字的次数，未在该间隔处插入数字填写None
                 如：[1, 1, 1]中插入两个2，即为4个间隔处插入两个2
                 结果：[[2, None, None, None],
                        [None, 2, None, None],
                        [None, None, 2, None],
                        [None, None, None, 2],
                        [1, 1, None, None],
                        [1, None, 1, None],
                        [1, None, None, 1],
                        [None, 1, 1, None],
                        [None, 1, None, 1],
                        [None, None, 1, 1]]
        """
        num_for_insert_create_list = list()
        for pieces in range(1, count + 1):
            num_for_insert_create_list += self.insert_create_list(count, pieces, empty_count)

        return num_for_insert_create_list

    def insert_create_list(self, num_count, pieces, need_insert_count):
        """
        :param num_count: 要插入序列中的新数字出现的次数
        :param pieces: 需要将新数字分成的份数，整理成list，list中存放该数字每份的次数
                       如：将7个数字分成3分
                       结果：[[1, 1, 5], [1, 2, 4], [1, 3, 3], [2, 2, 3]]
                             需要求出每份的数据，返回所有不重复的全排列
                             如结果中的[1, 1, 5]需要返回的全排列为[[1, 1, 5], [1, 5, 1], [5, 1, 1]]，
                             与本次处理的目的性一致，可直接递归直到求出最终结果
        :param need_insert_count:
        :return: 间隔数中插入新数字的不重复list，长度为间隔数
                 填写每个间隔处插入该数字的次数，未在该间隔处插入数字填写None
                 如：[1, 1, 1]中插入两个2，即为4个间隔处插入两个2
                 结果：[[2, None, None, None],
                        [None, 2, None, None],
                        [None, None, 2, None],
                        [None, None, None, 2],
                        [1, 1, None, None],
                        [1, None, 1, None],
                        [1, None, None, 1],
                        [None, 1, 1, None],
                        [None, 1, None, 1],
                        [None, None, 1, 1]]
        """
        insert_create_list = list()
        create_list = list()
        create_list.append(num_count - pieces + 1)
        for i in range(pieces - 1):
            create_list.append(1)

        flg = True
        while(flg):
            # 对每次分组的结果求全排列，可直接递归求出结果
            new_create_list = self.permuteUnique(create_list)
            for mini_create_list in new_create_list:
                insert_create_list += self.insert_list(mini_create_list, need_insert_count - len(mini_create_list))

            if len(create_list) == 1:
                flg = False
            for i in range(0, len(create_list) - 1):
                if create_list[i] - create_list[i + 1] >= 2:
                    create_list[i] -= 1
                    create_list[i + 1] += 1
                    break
                if i + 2 == len(create_list):
                    flg = False

        return insert_create_list

    def insert_list(self, create_list, need_insert_count):
        """
        :param create_list: 数据排序的结果，如insert_create_list()中求出的结果[1, 1, 5]，顺序固定
        :param need_insert_count: 需要插入的间隔数
        :return: 间隔数中插入新数字的不重复list，长度为间隔数
                 填写每个间隔处插入该数字的次数，未在该间隔处插入数字填写None
                 例处理：长度为3的结果[1, 1, 5]，插入间隔数为5，则None的个数为2
                         第一步：锁定第一位为[1]，则剩余[1, 5]与2个None排序，[1, 5]的顺序固定
                         第二步：锁定前两位为[None, 1], 则剩余[1, 5]与1个None排序，[1, 5]的顺序固定
                         第三步：锁定前三位为[None, None, 1], 则剩余[1, 5]且位置固定，为唯一解
                         第四步：没有None可插入最前方作为固定值，处理结束
                         第五步：第一步与第二步的的剩余结果，与例处理一致，可重复按照顺序处理，最后与锁定的位置合并
                 最终结果：[[1, 1, 5, None, None],
                           [1, 1, None, 5, None],
                           [1, 1, None, None, 5],
                           [1, None, 1, 5, None],
                           [1, None, 1, None, 5],
                           [1, None, None, 1, 5],
                           [None, 1, 1, 5, None],
                           [None, 1, 1, None, 5],
                           [None, 1, None, 1, 5],
                           [None, None, 1, 1, 5]]
        """
        if len(create_list) > 1:
            result_list = list()
            for i in range(need_insert_count + 1):
                default_list = list()
                default_list.append(create_list[-1])
                for j in range(i):
                    default_list.append(None)
                # 锁定后的结果做递归处理后与锁定的值合并
                samll_list = self.insert_list(create_list[0:-1], need_insert_count - i)
                for mini_list in samll_list:
                    mini_list += default_list
                    result_list.append(mini_list)
        else:
            result_list = list()
            for count in range(need_insert_count + 1):
                mini_list = [None for _ in range(need_insert_count)]
                mini_list.insert(count, create_list[0])
                result_list.append(mini_list)

        return result_list


class Solution_subsets(object):
    """
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    输入: nums = [1,2,3]
    输出: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
    """

    def __init__(self):
        self.nums_list = [[]]

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def subsets(nums):
            if not nums:
                return
            else:
                new_nums_list = list()
                for num_list in self.nums_list:
                    new_nums_list.append([num for num in num_list])
                    new_nums_list.append([nums[-1]] + [num for num in num_list])
                self.nums_list = new_nums_list
                subsets(nums[0:-1])

        subsets(nums)

        return self.nums_list
