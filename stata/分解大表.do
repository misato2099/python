clear all
// Load the consolidated table
use "XXXXXX\\file_name.dta"

// Sort the data by the "countycode" column
sort county

// Generate a list of all unique "countycode" values
levelsof county, local(county_list)

// Loop through each "countycode" value and save the corresponding subtable to a separate file
foreach county of local county_list {
    // Subset the data for the current "county" value using "if"
    use "XXXXXX\\file_name.dta" if county == "`county'" // 文字要再加"",變成"`'"格式
    
    // Save the subsetted data to a separate file
    save "XXXXXXXXX\\`county'_data.dta", replace
}