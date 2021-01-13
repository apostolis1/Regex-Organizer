from shutil import copyfile, move
import os
import re
import ntpath


def copy_or_move_file(src, dest, context)->None: #Copies or moves the file from src to dest, depending on context["type"]
    if context["type"] == "copy":
        copyfile(src, dest)
    elif context["type"] == "move":
        move(src, dest)
    return


def find_files(root, regex, context)->list:

    preset = context["preset"]# Used for preset common operations, such as endswith etc

    if context["search_subfolders"]: #If the user wants to look at the subfolders as well, recursive search
        print(f"Searching directory {root} and all subfolders")
        final_files = []
        for path, subdirs, files in os.walk(root):
            for name in files:
                final_files.append(os.path.join(path, name))
    else: #Search only in current dir
        print(f"Searching directory {root}, not including the subfolders")
        final_files = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]

    try:
        pattern = re.compile(regex)
    except Exception as e:
        print("Error in compiling the regex, please make sure that it's a valid regex")
        print(e)

    regex_checked = []
    for file in final_files:
        if not context["use_filename_only"]: #Check the relative path
            to_check = os.path.relpath(file, root)
        else:
            to_check = ntpath.basename(file)

        if preset == "endswith" and to_check.endswith(regex): #looking if string endswith param
            regex_checked.append(file)

        if preset == "startswith" and to_check.startswith(regex): #looking if string startswith param
            regex_checked.append(file)

        if preset == "equals" and to_check == regex: #looking if string equals param
            regex_checked.append(file)

        if preset == "contains" and regex in to_check: #looking if string contains param
            regex_checked.append(file)

        # executing custom regex
        # if preset == "custom" and pattern.search(to_check): #use pattern.search()
        if preset == "custom" and pattern.match(to_check): #use pattern.match()
            regex_checked.append(file)


    regex_checked = [f for f in regex_checked if os.path.isfile(f)] #Filter only for files
    return regex_checked


def organize_files(src, dest_folder, regex, context)->str: #input: root folder, destination folder , regex to check, context
    files = find_files(src, regex, context)
    if len(files) == 0: #nothing to copy/move
        return "No files were found matching your parameters"
    for file in files:
        print(file)
    for file_to_copy in files:
        copy_or_move_file(file_to_copy, os.path.join(dest_folder, ntpath.basename(file_to_copy)), context)
    print(f"Finished, {len(files)} were copied/moved successfully")
    if context["type"] == "move":
        return (f"{len(files)} files were moved successfully")
    else:
        return (f"{len(files)} files were copied successfully")
