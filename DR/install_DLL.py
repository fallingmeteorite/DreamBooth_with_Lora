import time
import zipfile
import shutil
import os
print("开始解压mwxKTEtelILoIbMbruuM.zip")
try:
    with zipfile.ZipFile(r"DR\mwxKTEtelILoIbMbruuM.zip") as zf:
        zf.extractall()
    print("解压完成")
    time.sleep(2)
    print("开始移动文件")
except:
    print(r'跳过')
    pass
origin_path_one=r'cudnn_windows\cudnn_adv_infer64_8.dll'
origin_path_two=r'cudnn_windows\cudnn_cnn_infer64_8.dll'
origin_path_three=r'cudnn_windows\cudnn_cnn_train64_8.dll'
origin_path_four=r'cudnn_windows\cudnn_ops_infer64_8.dll'
origin_path_five=r'cudnn_windows\cudnn_ops_train64_8.dll'
origin_path_six=r'cudnn_windows\cudnn64_8.dll'
origin_path_last=r'cudnn_windows\cudnn_adv_train64_8.dll'
new_file_name_one=r'DR\cudnn_windows'
try:
    shutil.move(origin_path_one, new_file_name_one)
    shutil.move(origin_path_two, new_file_name_one)
    shutil.move(origin_path_three, new_file_name_one)
    shutil.move(origin_path_four, new_file_name_one)
    shutil.move(origin_path_five, new_file_name_one)
    shutil.move(origin_path_six, new_file_name_one)
    shutil.move(origin_path_last, new_file_name_one)
except:
    print("已存在")
time.sleep(4)
print("删除源文件")
try:
    os.remove("DR\mwxKTEtelILoIbMbruuM.zip")
except:
    pass
print("源文件删除完成")

