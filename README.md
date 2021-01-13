# Regex Organizer
A quick utility to help you organize your files (move/copy to directories according to your criteria).
It also supports custom regular expressions, so you can create whatever criteria you want to customize the organization of your files.


![demo](/demo/demo.png)
# Install
Install requirements from requirements.txt using pip
`pip install -r requirements.txt`
(check out https://pip.pypa.io/en/stable/reference/pip_install/ for more info)

Run RegexOrganizer.pyw in the main directory to run the program

# Parameters

## Search subfolders
Choose wheteher the search should be limited to the files contained only directly under the root folder, or all subfolders should be searched as well

## Move/Copy
Choose whether you want to move/copy the selected files 

## Filename
Choose whether the full absolute path should be used or only the filename

## Regular Expression
There are some commonly used presets that are already builtin (both in python and the program itself) so you don't have to write regex for those:
* Starts with
Uses python's startswith() function of strings (more info https://docs.python.org/3/library/stdtypes.html#str.startswith)
* Ends with
Uses python's endswith() function of strings (more info https://docs.python.org/3/library/stdtypes.html#str.endswith)
* Contains
Uses python's in operator for strings
* Equals
Simple string comparison
* Custom Regex
Uses python's match() function for regular expressions, can be changed in the backend/CopyFiles.py file to use the search() function there:
```
        # executing custom regex
        # if preset == "custom" and pattern.search(to_check): #use pattern.search()
        if preset == "custom" and pattern.match(to_check): #use pattern.match()
            regex_checked.append(file)
```
Find more about the differences between match and search there: https://docs.python.org/2/library/re.html?highlight=matching%20searching#search-vs-match and https://stackoverflow.com/questions/180986/what-is-the-difference-between-re-search-and-re-match
