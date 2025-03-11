import os
import random
import re


def print_file_content(filename, content, id):
    # 使用正则表达式找到所有的 RANDOM，并替换为新的随机数
    def replace_random(match):
        return str(random.randint(1, 1000000))

    content = content.replace("TAG_HEAD", "rcg")
    content = content.replace("TAG_TAIL", str(id))
    content = re.sub(r"RANDOM", replace_random, content)
    print(f"文件: {id}\n内容:\n{content}\n")

    # 写入文件
    with open(
        "./gen/" + filename + "_" + str(id) + ".c", "w", encoding="utf-8"
    ) as file:
        file.write(content)


def read_c_files(directory, cnt):
    # 检查目录是否存在
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在")
        return

    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查是否是.c文件
        if not filename.endswith(".c"):
            continue

        id = 0

        file_path = os.path.join(directory, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                filename = filename.replace(".c", "")
                print(f"正在处理文件: {filename}")

                while id < cnt:
                    print_file_content(filename, content, id)
                    id += 1

        except Exception as e:
            print(f"读取文件 {file_path} 时发生错误: {e}")


# 使用当前目录下的template文件夹
read_c_files("template", 3)
