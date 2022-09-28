def __scan_directories(dir_path, ext):
  
    file_list = []
    for path, directories, files in os.walk(dir_path):
        
        for file in files:
        
            if ext in file:
                file_list.append(os.path.join(path, file))
    
    return file_list

    print("file_list")