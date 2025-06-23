# Airline Data Cleaning Script

This project contains a Python script to clean and transform a raw airline dataset provided in a stringified table format.
The original data uses semicolon (`;`) delimiters and newline (`\n`) as row separators.

## Description

The script:

- Parses the input data using `pandas`
- Clean inconsistent formatting in the `Airline Code` column
- Fills missing `FlightCodes` by incrementing the pervious value by 10
- Splits the `To_From` column into two columns: `From` and `To`
- Standardizes capitalization for better readability

## Libraries Used

- **pandas**: for table (DataFrame) operations, parsing, and transformations
- **re**: Python's regex module, used to clean nad normalize the `Airline Code` column
- **io**: to treat the stringified data as a file-like object so `pandas.read_csv()` can parse it

## Notes

- Missing `FlightCodes` are filled by adding 10 to the previous value and cast to integer
- `To_From` is split on `_`, and both resulting columns are title-cased (`"london"` -> `"London"`)
- `Airline Code`is cleaned of all punctuation and excess whitespace, and normalized to title case
