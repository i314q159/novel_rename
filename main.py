import os
import shutil


def extract_text_from_brackets(filename):
    start_index = filename.find("《")
    end_index = filename.find("》")

    if start_index != -1 and end_index != -1:
        # 提取《》之间的文本，并添加.txt后缀
        text_between_brackets = filename[start_index + 1 : end_index] + ".txt"
        return text_between_brackets
    else:
        # 如果没有找到《》则返回原文件名
        return filename + ".txt"


def copy_and_move_files(src_directory, dest_directory):
    # 确保源目录存在
    if not os.path.exists(src_directory):
        print(f"The source directory {src_directory} does not exist.")
        return

    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    # 获取源目录中的所有文件名
    filenames = os.listdir(src_directory)

    # 复制并移动文件
    for filename in filenames:
        new_filename = extract_text_from_brackets(filename)
        src_file_path = os.path.join(src_directory, filename)
        dest_file_path = os.path.join(dest_directory, new_filename)

        # 复制文件到目标目录
        shutil.copy2(src_file_path, dest_file_path)
        print(f"Copied '{filename}' to '{dest_file_path}'")


# 使用函数
src_directory = "./txt"  # 源文件夹路径
dest_directory = "./result"  # 目标文件夹路径
copy_and_move_files(src_directory, dest_directory)
