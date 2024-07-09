clear         // 轉碼前務必先清空內存，否則會提示錯誤信息
cd "D:\data"  // 待轉換數據所在文件夾, 請務必事先備份一份數據
unicode encoding set big5
unicode retranslate *, invalid(ignore) transutf8 nodata replace