import os
import re

import jieba

from common import file_util, constant


def load_train_data():
    # 训练一个标签里的所有问题问法
    train_x = []
    # 标签
    train_y = []
    file_path_list = file_util.get_file_list(os.path.join(constant.DATA_DIR, "question"))
    for file_item in file_path_list:
        # 获取文件名中的label
        label = re.sub(r'\D', "", file_item)
        if label.isnumeric():
            label_num = int(label)
            # 读取文件内容
            with (open(file_item, "r", encoding="utf-8")) as file:
                lines = file.readlines()
                for line in lines:
                    # 分词
                    word_list = list(jieba.cut(str(line).strip()))
                    # print(word_list)
                    train_x.append("".join(word_list))
                    train_y.append(label_num)
    for i in train_x:
        print(i)
    for j in train_y:
        print(j)


if __name__ == '__main__':
    load_train_data()
