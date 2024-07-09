clear all
cd "folder_path"
local f: dir "folder_path" files "*.csv"
foreach file of local f{
	insheet using `file'
	save `file'.dta, replace
	clear all	
}
local g: dir "folder_path" files "*.dta"
foreach file of local g{
	unicode analyze `file'
	unicode encoding set utf-8
	unicode translate `file'
}
use originfile.csv.dta
foreach file of local g{
	merge 1:1 column_var using `file', force
	drop _merge
}
drop var
order var
*export delimited using "combine_tax.csv", replace
save "combinefile.dta", replace
clear
