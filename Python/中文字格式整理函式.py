import re
def strQ2B(ustring):  # 營業地址用
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:                            # 全形空格直接轉換
            inside_code = 32
        elif inside_code == 65288:                            # 全形開括號直接轉換
            inside_code = 40
        elif inside_code == 65289:                            # 全形關括號直接轉換
            inside_code = 41
        # 長-(dash)換短-(dash)
        elif inside_code == 8213 or inside_code == 126 or inside_code == 65374:
            inside_code = 45
        elif 65281 <= inside_code <= 65373:   				# 全形字元（除空格）根據關係轉化原65374
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring
    

def strQ2B2(ustring):  # 營業人名稱用
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:                            # 全形空格直接轉換
            inside_code = 32
        elif inside_code == 59972:                            # 全形開括號直接轉換
            inside_code = 19968
        elif inside_code == 65288:                            # 全形開括號直接轉換
            inside_code = 40
        elif inside_code == 65289:                            # 全形關括號直接轉換
            inside_code = 41
        elif inside_code == 8213:                            # 長-(dash)換成「一」
            inside_code = 19968
        elif 65281 <= inside_code <= 65374:   				# 全形字元（除空格）根據關係轉化
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring

def strQ2B3(adr):  # 營業人名稱用
    str11 = re.sub(r"\d+F", '', str11)  # 刪除結尾的樓層(英數)
    str11 = re.sub("&", '', str11)  # 刪除結尾的樓層(英數)
    str11 = re.sub(r"[\d]、[\d]樓", '', str11)  # 刪除結尾的樓層(數字)
    str11 = re.sub(r"\d+樓", '', str11)  # 刪除結尾的樓層(數字)
    str11 = re.sub("-樓", '', str11)  # 刪除結尾的樓層(-短dash)
    str11 = re.sub("1段", "一段", str11)
    str11 = re.sub("2段", "二段", str11)
    str11 = re.sub("3段", "三段", str11)
    str11 = re.sub("4段", "四段", str11)
    str11 = re.sub("5段", "五段", str11)
    str11 = re.sub("6段", "六段", str11)
    str11 = re.sub("7段", "七段", str11)
    str11 = re.sub("8段", "八段", str11)
    str11 = re.sub("9段", "九段", str11)
    str11 = re.sub(r"[^u4E00-u9FA5]樓", '', str11)  # 刪除結尾的樓層(中文)
    str11 = re.sub(r"[^u4E00-u9FA5][^u4E00-u9FA5]里",
                   '', str11)  # 刪除里
    str11 = re.sub(r"[^u4E00-u9FA5]里", '', str11)  # 刪除里
    str11 = re.sub(r"[^u4E00-u9FA5][^u4E00-u9FA5]村",
                   '', str11)  # 刪除結尾的樓層(中文)
    str11 = re.sub(r"[^u4E00-u9FA5]村", '', str11)  # 刪除村
    str11 = re.sub(r"\d+鄰", '', str11)  # 刪除鄰
    str11 = re.sub(
                    r"[^u4E00-u9FA5]、[^u4E00-u9FA5]樓", '', str11)  # 刪除多層樓層(中文)