clear all
cd "folder_path"
use "data_new.dta"

* 建立縣市別名稱
gen county_name = substr(Add, 1, 9) 

* 抽取縣市別唯一值
levelsof county_name, local(unique_values_str)

* Loop through each unique county value
foreach value of local unique_values_str {
	
    * Create a subset of data for the current county
    keep if county_name == "`value'"
    
    * Sort the data by county
    sort county_name
    
    * Export the data for the current county to a single file
    save "data_`value'.dta", replace
    
    * Restore the original data
    use "data_new.dta", clear
	
	* Regenerate countycode variable after restoring the original data
	gen county_name = substr(Add, 1, 9)
}