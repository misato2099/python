clear all
use "folder_path\\data.dta"
*縣改市
replace county = subinstr(county, "縣", "市", .)
*鄉鎮市改區
replace 鄉鎮市區 = subinstr(鄉鎮市區, "鄉", "區", .) if regexm(鄉鎮市區, ".*鄉$")
replace 鄉鎮市區 = subinstr(鄉鎮市區, "鎮", "區", .) if regexm(鄉鎮市區, ".*鎮$")
replace 鄉鎮市區 = subinstr(鄉鎮市區, "市", "區", .) if regexm(鄉鎮市區, ".*市$")
*村改里
replace 村里 = subinstr(村里, "村", "里", .)
egen 完整地區_2 = concat(county 鄉鎮市區 村里)
drop 完整地區
rename 完整地區_2 完整地區
order countycode 完整地區
merge 1:1 完整地區 using "folder_path\\data_r.dta", update
// sort 完整地區_2
// by 完整地區_2: gen count = _N
// order count countycode 完整地區 完整地區_2
// codebook count