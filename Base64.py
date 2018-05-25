#Base64是一种用64个字符来表示任意二进制数据的方法
#二进制-->字符串 3Byte的二进制数据编码-->4字节的文本数据

# PIL:Python平台事实上的图像处理标准库 Pillow第三方图像处理库
'''
from PIL import Image
from PIL import _imaging as core
#打开一个jpg文件,
im = Image.open('/home/jesee/project/3691336-44a632b55f207ef5.jpg')
w,h = im.size

print('Original image size: %sx%s' %(w,h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('/home/jesee/project/thumbnail.jpg', 'jpeg')

'''