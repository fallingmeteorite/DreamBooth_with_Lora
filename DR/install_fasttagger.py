import zipfile
import os
print("开始解压fastTagger.zip")
with zipfile.ZipFile(r"fastTagger.zip") as zf:
    zf.extractall()
print("解压完成")
os.remove("fastTagger.zip")
print("源文件删除完成")
print(r'安装依赖')
os.system(r'pip install basicsr==1.4.2')
os.system(r'pip install GitPython==3.1.31')
os.system(r'pip install piexif==1.1.3')
os.system(r'pip install fonts==0.0.3')
os.system(r'pip install omegaconf==2.3.0')
os.system(r'pip install open_clip_torch==2.16.0')
os.system(r'pip install lark==1.1.5')
os.system(r'pip install blendmodes==2022')
os.system(r'pip install jsonmerge==1.9.0')
os.system(r'pip install clean_fid==0.1.35')
os.system(r'pip install clip==0.2.0')
os.system(r'pip install resize_right==0.0.2')
os.system(r'pip install torchdiffeq==0.2.3')
os.system(r'pip install torchsde==0.2.5')
print(r'完成')
