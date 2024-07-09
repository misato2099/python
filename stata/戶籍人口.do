cd "folder_path"
/*108-110年*/
forvalues y=108(1)110{
foreach m in 06 12{
import delimited "`y'`m'.csv", clear varnames(6) encoding(big5)
drop if 人口數==.
destring (村里數_現有門牌),replace
destring ( 村里數_戶籍登記 ),replace

foreach i in 村里數_現有門牌 村里數_戶籍登記 鄰數_現有門牌 鄰數_戶籍登記 戶數{
bysort 區域代碼:egen `i'_test=mean(`i')
drop `i'
ren `i'_test `i'
}

drop if 村里數_現有門牌>1

keep if 性別=="計"
drop 性別

gen countycode=usubstr( 區域代碼,1,5)
*gen villagecode=substr(區域代碼, -5, .)

gen     county= "宜蘭縣" if countycode=="10002"
replace county= "新竹縣" if countycode=="10004"
replace	county=	"苗栗縣" if countycode=="10005"
replace	county=	"彰化縣" if countycode=="10007"
replace	county=	"南投縣" if countycode=="10008"
replace	county=	"雲林縣" if countycode=="10009"
replace	county=	"嘉義縣" if countycode=="10010"
replace	county=	"屏東縣" if countycode=="10013"
replace	county=	"臺東縣" if countycode=="10014"
replace	county=	"花蓮縣" if countycode=="10015"
replace	county=	"澎湖縣" if countycode=="10016"
replace	county=	"基隆市" if countycode=="10017"
replace	county=	"新竹市" if countycode=="10018"
replace	county=	"嘉義市" if countycode=="10020"
replace	county=	"連江縣" if countycode=="90070"
replace	county=	"金門縣" if countycode=="90200"
replace	county=	"臺北市" if countycode=="63000"
replace	county=	"高雄市" if countycode=="64000"
replace	county=	"新北市" if countycode=="65000"
replace	county=	"臺中市" if countycode=="66000"
replace	county=	"臺南市" if countycode=="67000"
replace	county=	"桃園市" if countycode=="68000"

gen date=`y'`m'
save "data\household_pop_`y'`m'.dta",replace

}
}

/*10406-6都*/
foreach c in 01臺北市 02新北市 03桃園市 04臺中市 05臺南市 06高雄市 07宜蘭縣 08新竹縣 09苗栗縣 10彰化縣 11南投縣 12雲林縣 13嘉義縣 14屏東縣/*
*/          15臺東縣 16花蓮縣 17澎湖縣 18基隆市 19新竹市 20嘉義市 21金門縣 22連江縣{
import delimited "10406-6都/`c'.csv", clear varnames(6) encoding(big5)
drop if 人口數==.
destring (村里數_現有門牌),replace
destring ( 村里數_戶籍登記 ),replace

foreach i in 村里數_現有門牌 村里數_戶籍登記 鄰數_現有門牌 鄰數_戶籍登記 戶數{
bysort 區域代碼 區域別:egen `i'_test=mean(`i')
drop `i'
ren `i'_test `i'
}

drop if 村里數_現有門牌>1

keep if 性別=="計"
drop 性別
gen county="`c'"
save "10406-6都/`c'.dta",replace
}

use "10406-6都/01臺北市.dta", clear
foreach c in 02新北市 03桃園市 04臺中市 05臺南市 06高雄市 07宜蘭縣 08新竹縣 09苗栗縣 10彰化縣 11南投縣 12雲林縣 13嘉義縣 14屏東縣/*
*/          15臺東縣 16花蓮縣 17澎湖縣 18基隆市 19新竹市 20嘉義市 21金門縣 22連江縣{
append using "10406-6都/`c'.dta"
}
gen countycode=usubstr( 區域代碼,1,5)
replace     county= "宜蘭縣" if countycode=="10002"
replace county= "新竹縣" if countycode=="10004"
replace county=	"苗栗縣" if countycode=="10005"
replace	county=	"彰化縣" if countycode=="10007"
replace	county=	"南投縣" if countycode=="10008"
replace	county=	"雲林縣" if countycode=="10009"
replace	county=	"嘉義縣" if countycode=="10010"
replace	county=	"屏東縣" if countycode=="10013"
replace	county=	"臺東縣" if countycode=="10014"
replace	county=	"花蓮縣" if countycode=="10015"
replace	county=	"澎湖縣" if countycode=="10016"
replace	county=	"基隆市" if countycode=="10017"
replace	county=	"新竹市" if countycode=="10018"
replace	county=	"嘉義市" if countycode=="10020"
replace	county=	"連江縣" if countycode=="90070"
replace	county=	"金門縣" if countycode=="90200"
replace	county=	"臺北市" if countycode=="63000"
replace	county=	"高雄市" if countycode=="64000"
replace	county=	"新北市" if countycode=="65000"
replace	county=	"臺中市" if countycode=="66000"
replace	county=	"臺南市" if countycode=="67000"
replace	county=	"桃園市" if countycode=="68000"

gen date=10406
save "data\household_pop_10406.dta",replace


/*10412*/
foreach c in 01臺北市 02新北市 03桃園市 04臺中市 05臺南市 06高雄市 07宜蘭縣 08新竹縣 09苗栗縣 10彰化縣 11南投縣 12雲林縣 13嘉義縣 14屏東縣/*
*/          15臺東縣 16花蓮縣 17澎湖縣 18基隆市 19新竹市 20嘉義市 21金門縣 22連江縣{
import delimited "10412/`c'.csv", clear varnames(6) encoding(big5)
drop if 人口數==.
destring (村里數_現有門牌),replace
destring ( 村里數_戶籍登記 ),replace

foreach i in 村里數_現有門牌 村里數_戶籍登記 鄰數_現有門牌 鄰數_戶籍登記 戶數{
bysort 區域代碼 區域別:egen `i'_test=mean(`i')
drop `i'
ren `i'_test `i'
}

drop if 村里數_現有門牌>1

keep if 性別=="計"
drop 性別
gen county="`c'"
save "10412/`c'.dta",replace
}

use "10412/01臺北市.dta", clear
foreach c in 02新北市 03桃園市 04臺中市 05臺南市 06高雄市 07宜蘭縣 08新竹縣 09苗栗縣 10彰化縣 11南投縣 12雲林縣 13嘉義縣 14屏東縣/*
*/          15臺東縣 16花蓮縣 17澎湖縣 18基隆市 19新竹市 20嘉義市 21金門縣 22連江縣{
append using "10412/`c'.dta"
}
gen countycode=usubstr( 區域代碼,1,5)
replace     county= "宜蘭縣" if countycode=="10002"
replace county= "新竹縣" if countycode=="10004"
replace	county=	"苗栗縣" if countycode=="10005"
replace	county=	"彰化縣" if countycode=="10007"
replace	county=	"南投縣" if countycode=="10008"
replace	county=	"雲林縣" if countycode=="10009"
replace	county=	"嘉義縣" if countycode=="10010"
replace	county=	"屏東縣" if countycode=="10013"
replace	county=	"臺東縣" if countycode=="10014"
replace	county=	"花蓮縣" if countycode=="10015"
replace	county=	"澎湖縣" if countycode=="10016"
replace	county=	"基隆市" if countycode=="10017"
replace	county=	"新竹市" if countycode=="10018"
replace	county=	"嘉義市" if countycode=="10020"
replace	county=	"連江縣" if countycode=="90070"
replace	county=	"金門縣" if countycode=="90200"
replace	county=	"臺北市" if countycode=="63000"
replace	county=	"高雄市" if countycode=="64000"
replace	county=	"新北市" if countycode=="65000"
replace	county=	"臺中市" if countycode=="66000"
replace	county=	"臺南市" if countycode=="67000"
replace	county=	"桃園市" if countycode=="68000"
gen date=10412
save "data\household_pop_10412.dta",replace

/*105-107*/
forvalues y=105(1)107{
foreach m in 06 12{
foreach c in 01臺北市 02新北市 03桃園市 04臺中市 05臺南市 06高雄市 07宜蘭縣 08新竹縣 09苗栗縣 10彰化縣 11南投縣 12雲林縣 13嘉義縣 14屏東縣/*
*/          15臺東縣 16花蓮縣 17澎湖縣 18基隆市 19新竹市 20嘉義市 21金門縣 22連江縣{
import delimited "`y'`m'/`c'.csv", clear varnames(6) encoding(big5)
drop if 人口數==.
destring (村里數_現有門牌),replace
destring ( 村里數_戶籍登記 ),replace

foreach i in 村里數_現有門牌 村里數_戶籍登記 鄰數_現有門牌 鄰數_戶籍登記 戶數{
bysort 區域代碼 區域別:egen `i'_test=mean(`i')
drop `i'
ren `i'_test `i'
}

drop if 村里數_現有門牌>1

keep if 性別=="計"
drop 性別
gen county="`c'"
save "`y'`m'/`c'.dta",replace
}
use "`y'`m'/01臺北市.dta", clear
foreach city in 02新北市 03桃園市 04臺中市 05臺南市 06高雄市 07宜蘭縣 08新竹縣 09苗栗縣 10彰化縣 11南投縣 12雲林縣 13嘉義縣 14屏東縣/*
*/          15臺東縣 16花蓮縣 17澎湖縣 18基隆市 19新竹市 20嘉義市 21金門縣 22連江縣{
append using "`y'`m'/`city'.dta"
}
gen countycode=usubstr( 區域代碼,1,5)
replace     county= "宜蘭縣" if countycode=="10002"
replace county= "新竹縣" if countycode=="10004"
replace	county=	"苗栗縣" if countycode=="10005"
replace	county=	"彰化縣" if countycode=="10007"
replace	county=	"南投縣" if countycode=="10008"
replace	county=	"雲林縣" if countycode=="10009"
replace	county=	"嘉義縣" if countycode=="10010"
replace	county=	"屏東縣" if countycode=="10013"
replace	county=	"臺東縣" if countycode=="10014"
replace	county=	"花蓮縣" if countycode=="10015"
replace	county=	"澎湖縣" if countycode=="10016"
replace	county=	"基隆市" if countycode=="10017"
replace	county=	"新竹市" if countycode=="10018"
replace	county=	"嘉義市" if countycode=="10020"
replace	county=	"連江縣" if countycode=="90070"
replace	county=	"金門縣" if countycode=="90200"
replace	county=	"臺北市" if countycode=="63000"
replace	county=	"高雄市" if countycode=="64000"
replace	county=	"新北市" if countycode=="65000"
replace	county=	"臺中市" if countycode=="66000"
replace	county=	"臺南市" if countycode=="67000"
replace	county=	"桃園市" if countycode=="68000"
save "data\household_pop_`y'`m'.dta",replace
gen date=`y'`m'
}
}

/*09912-5都*/
foreach c in 01臺北市 02新北市 03桃園縣 04臺中市 05臺南市 06高雄市 07宜蘭縣 08新竹縣 09苗栗縣 10彰化縣 11南投縣 12雲林縣 13嘉義縣 14屏東縣/*
*/          15臺東縣 16花蓮縣 17澎湖縣 18基隆市 19新竹市 20嘉義市 2122金門連江{
import delimited "09912-5都/`c'.csv", clear varnames(5) encoding(big5)
drop if 人口==.
destring (村),replace
destring (鄰),replace
destring (戶),replace


/*foreach i in 村 鄰 戶{
bysort 區域別:egen `i'_test=mean(`i')
drop `i'
ren `i'_test `i'
}

drop if 村>1

keep if 性別=="計"
drop 性別
gen county="`c'"*/
gen county="`c'"
gen date=09912
save "folder_name/`c'.dta",replace
}
use "folder_name/dta_name.dta", clear
foreach c in 02新北市 03桃園縣 04臺中市 05臺南市 06高雄市 07宜蘭縣 08新竹縣 09苗栗縣 10彰化縣 11南投縣 12雲林縣 13嘉義縣 14屏東縣/*
*/          15臺東縣 16花蓮縣 17澎湖縣 18基隆市 19新竹市 20嘉義市 2122金門連江{
append using "09912-5都/`c'.dta"
}
replace v43=v1 if v43==""
foreach i in 村 鄰 戶{
bysort v43:egen `i'_test=mean(`i')
drop `i'
ren `i'_test `i'
}
split v43, p(V)



