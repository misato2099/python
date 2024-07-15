egen missarray = anycount(var1 - var_N),values(-99)
tab missarray //計無MISSING(0)有多少筆，然後再用總區數減此數獲得缺失區數
// drop missarray
