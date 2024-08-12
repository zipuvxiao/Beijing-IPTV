import shutil

def replace_in_file(file_path, old_string, new_string):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace(old_string, new_string)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    # 原文件路径
    original_file_path = 'IPTV-Unicom.m3u'
    
    # 创建并修改 IPTV-UDPXY.m3u
    new_file_path_udpxy = 'IPTV-UDPXY.m3u'
    shutil.copyfile(original_file_path, new_file_path_udpxy)
    replace_in_file(new_file_path_udpxy, '192.168.123.1:23234', 'gfsg.bj.cn.ikunchina.com:2112')
    
    # 创建并修改 IPTV-MSDLITE.m3u
    new_file_path_msdlite = 'IPTV-MSDLITE.m3u'
    shutil.copyfile(original_file_path, new_file_path_msdlite)
    replace_in_file(new_file_path_msdlite, '192.168.123.1:23234', 'gfsg.bj.cn.ikunchina.com:7088')
