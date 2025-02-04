import os
import shutil
import glob

def copy_files_from_actors_folders(root_dir, target_dir):
    # 创建目标目录，如果不存在的话
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 使用glob模块来查找所有名为 .actors 的文件夹
    actors_folders = glob.glob(os.path.join(root_dir, '**', '.actors'), recursive=True)
    
    for folder in actors_folders:
        print(f"Copying files from {folder} to {target_dir}")
        # 遍历每个 .actors 文件夹中的文件
        for file_name in os.listdir(folder):
            full_file_path = os.path.join(folder, file_name)
            if os.path.isfile(full_file_path):
                # 构建目标文件路径
                target_file_path = os.path.join(target_dir, file_name)
                # 复制文件
                shutil.copy2(full_file_path, target_file_path)
                print(f" - Copied {file_name} to {target_file_path}")

def organize_images(root_dir):
    # 遍历根目录中的所有文件
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                # 获取图片的全名和扩展名
                image_full_name, ext = os.path.splitext(filename)
                # 替换下划线为空格
                image_full_name = image_full_name.replace('_', ' ')
                # 获取图片的第一个字符（如果是英文则大写）
                first_char = image_full_name[0].upper() if image_full_name[0].isalpha() else image_full_name[0]
                # 创建第一层文件夹
                first_level_dir = os.path.join(root_dir, first_char)
                os.makedirs(first_level_dir, exist_ok=True)
                
                # 创建第二层文件夹
                second_level_dir = os.path.join(first_level_dir, image_full_name)
                os.makedirs(second_level_dir, exist_ok=True)
                
                # 构建源文件路径和目标文件路径
                source_path = os.path.join(dirpath, filename)
                target_filename = f"poster{ext}"
                target_path = os.path.join(second_level_dir, target_filename)
                
                # 剪切并重命名文件
                shutil.move(source_path, target_path)
                print(f"Moved and renamed: {source_path} -> {target_path}")

def main():
    # 指定目标目录
    storage_directory = input("请输入临时存放People图片路径 (完成后请剪贴至Jellyfin\\ServerData\\metadata\\People): ")

    while True:
        print("请选择要执行的操作:")
        print("0. 退出")
        print("1. 选择需要提取图片的路径 (会遍历此路径下所有.actors文件夹)")
        print("2. 重命名图片并整理成文件夹")
        
        choice = input("请输入选项 (0/1/2): ")
        
        if choice == '0':
            print("退出程序")
            break
        elif choice == '1':
            while True:
                print("\n退出请输入 (0)")
                # 指定要搜索的目录
                search_directory = input("请输入要提取的目录路径: ")

                if search_directory == '0':
                    break
                else:
                    copy_files_from_actors_folders(search_directory, storage_directory)
        elif choice == '2':
            organize_images(storage_directory)
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()