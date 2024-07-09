*========================================================================================================================
*==========================================================10806=========================================================
*========================================================================================================================
cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數"
*mkdir "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result10806"

//insheet using `file', comma clear ///;
/* do your stuff here */
import delimited "10806.csv", delimiter(",") clear 
gen 人口數 = v9[_n-1] if v8 == "男"
*gen female = v9[_n+1] if v8 == "男"
keep if v8 =="男"

rename v1 區域代碼
rename v2 區域別
rename v3 村里數_現有門牌
rename v4 村里數_戶籍登記
rename v5 鄰數_現有門牌
rename v6 鄰數_戶籍登記
rename v7 戶數
destring 村里數_現有門牌, replace
destring 村里數_戶籍登記, replace
destring 鄰數_現有門牌, replace
destring 鄰數_戶籍登記, replace
destring 戶數, replace
drop v8
drop v9
drop if 區域別 == "總  計"|區域別 == "總 計"|區域別 == "總計"|區域別 == "總　計"
drop if strmatch(區域別, "*宜蘭縣*")|strmatch(區域別, "*新竹縣*")|strmatch(區域別, "*苗栗縣*")|strmatch(區域別, "*彰化縣*") ///
	|strmatch(區域別, "*南投縣*")|strmatch(區域別, "*雲林縣*")|strmatch(區域別, "*嘉義縣*")|strmatch(區域別, "*屏東縣*") ///
	|strmatch(區域別, "*臺東縣*")|strmatch(區域別, "*花蓮縣*")|strmatch(區域別, "*澎湖縣*")|strmatch(區域別, "*基隆市*") ///
	|strmatch(區域別, "*新竹市*")|strmatch(區域別, "*嘉義市*")|strmatch(區域別, "*臺北市*")|strmatch(區域別, "*高雄市*") ///
	|strmatch(區域別, "*高雄縣*")|strmatch(區域別, "*新北市*")|strmatch(區域別, "*臺北縣*")|strmatch(區域別, "*臺中市*") ///
	|strmatch(區域別, "*臺中縣*")|strmatch(區域別, "*臺南市*")|strmatch(區域別, "*臺南縣*")|strmatch(區域別, "*桃園市*") ///
	|strmatch(區域別, "*桃園縣*")|strmatch(區域別, "*臺閩地區*")|strmatch(區域別, "*臺灣地區*")|strmatch(區域別, "*總　計*") ///
	|strmatch(區域別, "*總 計*")|strmatch(區域別,"*臺灣省*")|strmatch(區域別, "*福建省*")|strmatch(區域別, "*金門縣*") ///
	|strmatch(區域別, "*連江縣*")|strmatch(區域別, "*金門縣*")|strmatch(區域別, "*連江縣*")
// 	drop if 村里數_現有門牌 > 1
gen countycode = ustrleft(區域代碼,5)
gen county = "."

replace	county="宜蘭縣"	if	countycode=="10002"
replace	county="新竹縣"	if	countycode=="10004"
replace	county="苗栗縣"	if	countycode=="10005"
replace	county="彰化縣"	if	countycode=="10007"
replace	county="南投縣"	if	countycode=="10008"
replace	county="雲林縣"	if	countycode=="10009"
replace	county="嘉義縣"	if	countycode=="10010"
replace	county="屏東縣"	if	countycode=="10013"
replace	county="臺東縣"	if	countycode=="10014"
replace	county="花蓮縣"	if	countycode=="10015"
replace	county="澎湖縣"	if	countycode=="10016"
replace	county="基隆市"	if	countycode=="10017"
replace	county="新竹市"	if	countycode=="10018"
replace	county="嘉義市"	if	countycode=="10020"
replace	county="臺北市"	if	countycode=="63000"
replace	county="高雄市"	if	countycode=="64000"
replace	county="新北市"	if	countycode=="65000"
replace	county="臺中市"	if	countycode=="66000"
replace	county="臺南市"	if	countycode=="67000"
replace	county="桃園市"	if	countycode=="68000"
replace	county="金門縣"	if	countycode=="90200"
replace	county="連江縣" if	countycode=="90070"

gen date = 10806
order 區域代碼 區域別 人口數 村里數_現有門牌 村里數_戶籍登記 鄰數_現有門牌 鄰數_戶籍登記 戶數 county countycode date

cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result10806"
save "household_pop_10806.dta",replace
*========================================================================================================================
*==========================================================10812=========================================================
*========================================================================================================================
cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數"
mkdir "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result10812"

//insheet using `file', comma clear ///;
/* do your stuff here */
import delimited "10812.csv", delimiter(",") clear 
gen 人口數 = v9[_n-1] if v8 == "男"
*gen female = v9[_n+1] if v8 == "男"
keep if v8 =="男"

rename v1 區域代碼
rename v2 區域別
rename v3 村里數_現有門牌
rename v4 村里數_戶籍登記
rename v5 鄰數_現有門牌
rename v6 鄰數_戶籍登記
rename v7 戶數
destring 村里數_現有門牌, replace
destring 村里數_戶籍登記, replace
destring 鄰數_現有門牌, replace
destring 鄰數_戶籍登記, replace
destring 戶數, replace
drop v8
drop v9
drop if 區域別 == "總  計"|區域別 == "總 計"|區域別 == "總計"|區域別 == "總　計"
drop if strmatch(區域別, "*宜蘭縣*")|strmatch(區域別, "*新竹縣*")|strmatch(區域別, "*苗栗縣*")|strmatch(區域別, "*彰化縣*") ///
	|strmatch(區域別, "*南投縣*")|strmatch(區域別, "*雲林縣*")|strmatch(區域別, "*嘉義縣*")|strmatch(區域別, "*屏東縣*") ///
	|strmatch(區域別, "*臺東縣*")|strmatch(區域別, "*花蓮縣*")|strmatch(區域別, "*澎湖縣*")|strmatch(區域別, "*基隆市*") ///
	|strmatch(區域別, "*新竹市*")|strmatch(區域別, "*嘉義市*")|strmatch(區域別, "*臺北市*")|strmatch(區域別, "*高雄市*") ///
	|strmatch(區域別, "*高雄縣*")|strmatch(區域別, "*新北市*")|strmatch(區域別, "*臺北縣*")|strmatch(區域別, "*臺中市*") ///
	|strmatch(區域別, "*臺中縣*")|strmatch(區域別, "*臺南市*")|strmatch(區域別, "*臺南縣*")|strmatch(區域別, "*桃園市*") ///
	|strmatch(區域別, "*桃園縣*")|strmatch(區域別, "*臺閩地區*")|strmatch(區域別, "*臺灣地區*")|strmatch(區域別, "*總　計*") ///
	|strmatch(區域別, "*總 計*")|strmatch(區域別,"*臺灣省*")|strmatch(區域別, "*福建省*")|strmatch(區域別, "*金門縣*") ///
	|strmatch(區域別, "*連江縣*")|strmatch(區域別, "*金門縣*")|strmatch(區域別, "*連江縣*")
// 	drop if 村里數_現有門牌 > 1
gen countycode = ustrleft(區域代碼,5)
gen county = "."

replace	county="宜蘭縣"	if	countycode=="10002"
replace	county="新竹縣"	if	countycode=="10004"
replace	county="苗栗縣"	if	countycode=="10005"
replace	county="彰化縣"	if	countycode=="10007"
replace	county="南投縣"	if	countycode=="10008"
replace	county="雲林縣"	if	countycode=="10009"
replace	county="嘉義縣"	if	countycode=="10010"
replace	county="屏東縣"	if	countycode=="10013"
replace	county="臺東縣"	if	countycode=="10014"
replace	county="花蓮縣"	if	countycode=="10015"
replace	county="澎湖縣"	if	countycode=="10016"
replace	county="基隆市"	if	countycode=="10017"
replace	county="新竹市"	if	countycode=="10018"
replace	county="嘉義市"	if	countycode=="10020"
replace	county="臺北市"	if	countycode=="63000"
replace	county="高雄市"	if	countycode=="64000"
replace	county="新北市"	if	countycode=="65000"
replace	county="臺中市"	if	countycode=="66000"
replace	county="臺南市"	if	countycode=="67000"
replace	county="桃園市"	if	countycode=="68000"
replace	county="金門縣"	if	countycode=="90200"
replace	county="連江縣" if	countycode=="90070"

gen date = 10812
order 區域代碼 區域別 人口數 村里數_現有門牌 村里數_戶籍登記 鄰數_現有門牌 鄰數_戶籍登記 戶數 county countycode date

cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result10812"
save "household_pop_10812.dta",replace
*========================================================================================================================
*==========================================================10906=========================================================
*========================================================================================================================
cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數"
mkdir "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result10906"

//insheet using `file', comma clear ///;
/* do your stuff here */
import delimited "10906.csv", delimiter(",") clear 
gen 人口數 = v9[_n-1] if v8 == "男"
*gen female = v9[_n+1] if v8 == "男"
keep if v8 =="男"

rename v1 區域代碼
rename v2 區域別
rename v3 村里數_現有門牌
rename v4 村里數_戶籍登記
rename v5 鄰數_現有門牌
rename v6 鄰數_戶籍登記
rename v7 戶數
destring 村里數_現有門牌, replace
destring 村里數_戶籍登記, replace
destring 鄰數_現有門牌, replace
destring 鄰數_戶籍登記, replace
destring 戶數, replace
drop v8
drop v9
drop if 區域別 == "總  計"|區域別 == "總 計"|區域別 == "總計"|區域別 == "總　計"
drop if strmatch(區域別, "*宜蘭縣*")|strmatch(區域別, "*新竹縣*")|strmatch(區域別, "*苗栗縣*")|strmatch(區域別, "*彰化縣*") ///
	|strmatch(區域別, "*南投縣*")|strmatch(區域別, "*雲林縣*")|strmatch(區域別, "*嘉義縣*")|strmatch(區域別, "*屏東縣*") ///
	|strmatch(區域別, "*臺東縣*")|strmatch(區域別, "*花蓮縣*")|strmatch(區域別, "*澎湖縣*")|strmatch(區域別, "*基隆市*") ///
	|strmatch(區域別, "*新竹市*")|strmatch(區域別, "*嘉義市*")|strmatch(區域別, "*臺北市*")|strmatch(區域別, "*高雄市*") ///
	|strmatch(區域別, "*高雄縣*")|strmatch(區域別, "*新北市*")|strmatch(區域別, "*臺北縣*")|strmatch(區域別, "*臺中市*") ///
	|strmatch(區域別, "*臺中縣*")|strmatch(區域別, "*臺南市*")|strmatch(區域別, "*臺南縣*")|strmatch(區域別, "*桃園市*") ///
	|strmatch(區域別, "*桃園縣*")|strmatch(區域別, "*臺閩地區*")|strmatch(區域別, "*臺灣地區*")|strmatch(區域別, "*總　計*") ///
	|strmatch(區域別, "*總 計*")|strmatch(區域別,"*臺灣省*")|strmatch(區域別, "*福建省*")|strmatch(區域別, "*金門縣*") ///
	|strmatch(區域別, "*連江縣*")|strmatch(區域別, "*金門縣*")|strmatch(區域別, "*連江縣*")
// 	drop if 村里數_現有門牌 > 1
gen countycode = ustrleft(區域代碼,5)
gen county = "."

replace	county="宜蘭縣"	if	countycode=="10002"
replace	county="新竹縣"	if	countycode=="10004"
replace	county="苗栗縣"	if	countycode=="10005"
replace	county="彰化縣"	if	countycode=="10007"
replace	county="南投縣"	if	countycode=="10008"
replace	county="雲林縣"	if	countycode=="10009"
replace	county="嘉義縣"	if	countycode=="10010"
replace	county="屏東縣"	if	countycode=="10013"
replace	county="臺東縣"	if	countycode=="10014"
replace	county="花蓮縣"	if	countycode=="10015"
replace	county="澎湖縣"	if	countycode=="10016"
replace	county="基隆市"	if	countycode=="10017"
replace	county="新竹市"	if	countycode=="10018"
replace	county="嘉義市"	if	countycode=="10020"
replace	county="臺北市"	if	countycode=="63000"
replace	county="高雄市"	if	countycode=="64000"
replace	county="新北市"	if	countycode=="65000"
replace	county="臺中市"	if	countycode=="66000"
replace	county="臺南市"	if	countycode=="67000"
replace	county="桃園市"	if	countycode=="68000"
replace	county="金門縣"	if	countycode=="90200"
replace	county="連江縣" if	countycode=="90070"

gen date = 10906
order 區域代碼 區域別 人口數 村里數_現有門牌 村里數_戶籍登記 鄰數_現有門牌 鄰數_戶籍登記 戶數 county countycode date

cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result10906"
save "household_pop_10906.dta",replace
*========================================================================================================================
*==========================================================10912=========================================================
*========================================================================================================================
cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數"
mkdir "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result10912"

//insheet using `file', comma clear ///;
/* do your stuff here */
import delimited "10912.csv", delimiter(",") clear 
gen 人口數 = v9[_n-1] if v8 == "男"
*gen female = v9[_n+1] if v8 == "男"
keep if v8 =="男"

rename v1 區域代碼
rename v2 區域別
rename v3 村里數_現有門牌
rename v4 村里數_戶籍登記
rename v5 鄰數_現有門牌
rename v6 鄰數_戶籍登記
rename v7 戶數
destring 村里數_現有門牌, replace
destring 村里數_戶籍登記, replace
destring 鄰數_現有門牌, replace
destring 鄰數_戶籍登記, replace
destring 戶數, replace
drop v8
drop v9
drop if 區域別 == "總  計"|區域別 == "總 計"|區域別 == "總計"|區域別 == "總　計"
drop if strmatch(區域別, "*宜蘭縣*")|strmatch(區域別, "*新竹縣*")|strmatch(區域別, "*苗栗縣*")|strmatch(區域別, "*彰化縣*") ///
	|strmatch(區域別, "*南投縣*")|strmatch(區域別, "*雲林縣*")|strmatch(區域別, "*嘉義縣*")|strmatch(區域別, "*屏東縣*") ///
	|strmatch(區域別, "*臺東縣*")|strmatch(區域別, "*花蓮縣*")|strmatch(區域別, "*澎湖縣*")|strmatch(區域別, "*基隆市*") ///
	|strmatch(區域別, "*新竹市*")|strmatch(區域別, "*嘉義市*")|strmatch(區域別, "*臺北市*")|strmatch(區域別, "*高雄市*") ///
	|strmatch(區域別, "*高雄縣*")|strmatch(區域別, "*新北市*")|strmatch(區域別, "*臺北縣*")|strmatch(區域別, "*臺中市*") ///
	|strmatch(區域別, "*臺中縣*")|strmatch(區域別, "*臺南市*")|strmatch(區域別, "*臺南縣*")|strmatch(區域別, "*桃園市*") ///
	|strmatch(區域別, "*桃園縣*")|strmatch(區域別, "*臺閩地區*")|strmatch(區域別, "*臺灣地區*")|strmatch(區域別, "*總　計*") ///
	|strmatch(區域別, "*總 計*")|strmatch(區域別,"*臺灣省*")|strmatch(區域別, "*福建省*")|strmatch(區域別, "*金門縣*") ///
	|strmatch(區域別, "*連江縣*")|strmatch(區域別, "*金門縣*")|strmatch(區域別, "*連江縣*")
// 	drop if 村里數_現有門牌 > 1
gen countycode = ustrleft(區域代碼,5)
gen county = "."

replace	county="宜蘭縣"	if	countycode=="10002"
replace	county="新竹縣"	if	countycode=="10004"
replace	county="苗栗縣"	if	countycode=="10005"
replace	county="彰化縣"	if	countycode=="10007"
replace	county="南投縣"	if	countycode=="10008"
replace	county="雲林縣"	if	countycode=="10009"
replace	county="嘉義縣"	if	countycode=="10010"
replace	county="屏東縣"	if	countycode=="10013"
replace	county="臺東縣"	if	countycode=="10014"
replace	county="花蓮縣"	if	countycode=="10015"
replace	county="澎湖縣"	if	countycode=="10016"
replace	county="基隆市"	if	countycode=="10017"
replace	county="新竹市"	if	countycode=="10018"
replace	county="嘉義市"	if	countycode=="10020"
replace	county="臺北市"	if	countycode=="63000"
replace	county="高雄市"	if	countycode=="64000"
replace	county="新北市"	if	countycode=="65000"
replace	county="臺中市"	if	countycode=="66000"
replace	county="臺南市"	if	countycode=="67000"
replace	county="桃園市"	if	countycode=="68000"
replace	county="金門縣"	if	countycode=="90200"
replace	county="連江縣" if	countycode=="90070"

gen date = 10912
order 區域代碼 區域別 人口數 村里數_現有門牌 村里數_戶籍登記 鄰數_現有門牌 鄰數_戶籍登記 戶數 county countycode date

cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result10912"
save "household_pop_10912.dta",replace
*========================================================================================================================
*==========================================================11006=========================================================
*========================================================================================================================
cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數"
*mkdir "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result11006"

//insheet using `file', comma clear ///;
/* do your stuff here */
import delimited "11006_2.csv", delimiter(",") clear 
gen 人口數 = v9[_n-1] if v8 == "男"
*gen female = v9[_n+1] if v8 == "男"
keep if v8 =="男"

rename v1 區域代碼
rename v2 區域別
rename v3 村里數_現有門牌
rename v4 村里數_戶籍登記
rename v5 鄰數_現有門牌
rename v6 鄰數_戶籍登記
rename v7 戶數
destring 村里數_現有門牌, replace
destring 村里數_戶籍登記, replace
destring 鄰數_現有門牌, replace
destring 鄰數_戶籍登記, replace
destring 戶數, replace
drop v8
drop v9
drop if 區域別 == "總  計"|區域別 == "總 計"|區域別 == "總計"|區域別 == "總　計"
drop if strmatch(區域別, "*宜蘭縣*")|strmatch(區域別, "*新竹縣*")|strmatch(區域別, "*苗栗縣*")|strmatch(區域別, "*彰化縣*") ///
	|strmatch(區域別, "*南投縣*")|strmatch(區域別, "*雲林縣*")|strmatch(區域別, "*嘉義縣*")|strmatch(區域別, "*屏東縣*") ///
	|strmatch(區域別, "*臺東縣*")|strmatch(區域別, "*花蓮縣*")|strmatch(區域別, "*澎湖縣*")|strmatch(區域別, "*基隆市*") ///
	|strmatch(區域別, "*新竹市*")|strmatch(區域別, "*嘉義市*")|strmatch(區域別, "*臺北市*")|strmatch(區域別, "*高雄市*") ///
	|strmatch(區域別, "*高雄縣*")|strmatch(區域別, "*新北市*")|strmatch(區域別, "*臺北縣*")|strmatch(區域別, "*臺中市*") ///
	|strmatch(區域別, "*臺中縣*")|strmatch(區域別, "*臺南市*")|strmatch(區域別, "*臺南縣*")|strmatch(區域別, "*桃園市*") ///
	|strmatch(區域別, "*桃園縣*")|strmatch(區域別, "*臺閩地區*")|strmatch(區域別, "*臺灣地區*")|strmatch(區域別, "*總　計*") ///
	|strmatch(區域別, "*總 計*")|strmatch(區域別,"*臺灣省*")|strmatch(區域別, "*福建省*")|strmatch(區域別, "*金門縣*") ///
	|strmatch(區域別, "*連江縣*")|strmatch(區域別, "*金門縣*")|strmatch(區域別, "*連江縣*")
// 	drop if 村里數_現有門牌 > 1
gen countycode = ustrleft(區域代碼,5)
gen county = "."

replace	county="宜蘭縣"	if	countycode=="10002"
replace	county="新竹縣"	if	countycode=="10004"
replace	county="苗栗縣"	if	countycode=="10005"
replace	county="彰化縣"	if	countycode=="10007"
replace	county="南投縣"	if	countycode=="10008"
replace	county="雲林縣"	if	countycode=="10009"
replace	county="嘉義縣"	if	countycode=="10010"
replace	county="屏東縣"	if	countycode=="10013"
replace	county="臺東縣"	if	countycode=="10014"
replace	county="花蓮縣"	if	countycode=="10015"
replace	county="澎湖縣"	if	countycode=="10016"
replace	county="基隆市"	if	countycode=="10017"
replace	county="新竹市"	if	countycode=="10018"
replace	county="嘉義市"	if	countycode=="10020"
replace	county="臺北市"	if	countycode=="63000"
replace	county="高雄市"	if	countycode=="64000"
replace	county="新北市"	if	countycode=="65000"
replace	county="臺中市"	if	countycode=="66000"
replace	county="臺南市"	if	countycode=="67000"
replace	county="桃園市"	if	countycode=="68000"
replace	county="金門縣"	if	countycode=="90200"
replace	county="連江縣" if	countycode=="90070"

gen date = 11006
order 區域代碼 區域別 人口數 村里數_現有門牌 村里數_戶籍登記 鄰數_現有門牌 鄰數_戶籍登記 戶數 county countycode date

cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result11006"
save "household_pop_11006.dta",replace
*========================================================================================================================
*==========================================================11012=========================================================
*========================================================================================================================
cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數"
mkdir "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result11012"

//insheet using `file', comma clear ///;
/* do your stuff here */
import delimited "11012_2.csv", delimiter(",") clear 
gen 人口數 = v9[_n-1] if v8 == "男"
*gen female = v9[_n+1] if v8 == "男"
keep if v8 =="男"

rename v1 區域代碼
rename v2 區域別
rename v3 村里數_現有門牌
rename v4 村里數_戶籍登記
rename v5 鄰數_現有門牌
rename v6 鄰數_戶籍登記
rename v7 戶數
destring 村里數_現有門牌, replace
destring 村里數_戶籍登記, replace
destring 鄰數_現有門牌, replace
destring 鄰數_戶籍登記, replace
destring 戶數, replace
drop v8
drop v9
drop if 區域別 == "總  計"|區域別 == "總 計"|區域別 == "總計"|區域別 == "總　計"
drop if strmatch(區域別, "*宜蘭縣*")|strmatch(區域別, "*新竹縣*")|strmatch(區域別, "*苗栗縣*")|strmatch(區域別, "*彰化縣*") ///
	|strmatch(區域別, "*南投縣*")|strmatch(區域別, "*雲林縣*")|strmatch(區域別, "*嘉義縣*")|strmatch(區域別, "*屏東縣*") ///
	|strmatch(區域別, "*臺東縣*")|strmatch(區域別, "*花蓮縣*")|strmatch(區域別, "*澎湖縣*")|strmatch(區域別, "*基隆市*") ///
	|strmatch(區域別, "*新竹市*")|strmatch(區域別, "*嘉義市*")|strmatch(區域別, "*臺北市*")|strmatch(區域別, "*高雄市*") ///
	|strmatch(區域別, "*高雄縣*")|strmatch(區域別, "*新北市*")|strmatch(區域別, "*臺北縣*")|strmatch(區域別, "*臺中市*") ///
	|strmatch(區域別, "*臺中縣*")|strmatch(區域別, "*臺南市*")|strmatch(區域別, "*臺南縣*")|strmatch(區域別, "*桃園市*") ///
	|strmatch(區域別, "*桃園縣*")|strmatch(區域別, "*臺閩地區*")|strmatch(區域別, "*臺灣地區*")|strmatch(區域別, "*總　計*") ///
	|strmatch(區域別, "*總 計*")|strmatch(區域別,"*臺灣省*")|strmatch(區域別, "*福建省*")|strmatch(區域別, "*金門縣*") ///
	|strmatch(區域別, "*連江縣*")|strmatch(區域別, "*金門縣*")|strmatch(區域別, "*連江縣*")
// 	drop if 村里數_現有門牌 > 1
gen countycode = ustrleft(區域代碼,5)
gen county = "."

replace	county="宜蘭縣"	if	countycode=="10002"
replace	county="新竹縣"	if	countycode=="10004"
replace	county="苗栗縣"	if	countycode=="10005"
replace	county="彰化縣"	if	countycode=="10007"
replace	county="南投縣"	if	countycode=="10008"
replace	county="雲林縣"	if	countycode=="10009"
replace	county="嘉義縣"	if	countycode=="10010"
replace	county="屏東縣"	if	countycode=="10013"
replace	county="臺東縣"	if	countycode=="10014"
replace	county="花蓮縣"	if	countycode=="10015"
replace	county="澎湖縣"	if	countycode=="10016"
replace	county="基隆市"	if	countycode=="10017"
replace	county="新竹市"	if	countycode=="10018"
replace	county="嘉義市"	if	countycode=="10020"
replace	county="臺北市"	if	countycode=="63000"
replace	county="高雄市"	if	countycode=="64000"
replace	county="新北市"	if	countycode=="65000"
replace	county="臺中市"	if	countycode=="66000"
replace	county="臺南市"	if	countycode=="67000"
replace	county="桃園市"	if	countycode=="68000"
replace	county="金門縣"	if	countycode=="90200"
replace	county="連江縣" if	countycode=="90070"

gen date = 11012
order 區域代碼 區域別 人口數 村里數_現有門牌 村里數_戶籍登記 鄰數_現有門牌 鄰數_戶籍登記 戶數 county countycode date

cd "\\140.109.121.110\nas\92至110 每年6月及12月各鄉鎮市區（或村里）村里鄰戶數與人口數\result11012"
save "household_pop_11012.dta",replace


