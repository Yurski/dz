import os 
import shutil 
import re 
import zipfile 

 

def normalize(filename): 
    translit_filename = filename.encode('translit').decode('utf-8') 
    normalized_filename = re.sub(r'[^a-zA-Z0-9.]+', '_', translit_filename) 
    return normalized_filename 

 

def process_folder(folder_path): 
    for root, dirs, files in os.walk(folder_path): 
        for file in files: 
            file_path = os.path.join(root, file) 
            extension = file.split('.')[-1].upper() 

 

            if extension in {'ZIP', 'GZ', 'TAR'}: 
                try: 
                    with zipfile.ZipFile(file_path, 'r') as zip_ref: 
                        zip_ref.extractall(os.path.join(root, 'archives', file.split('.')[0])) 
                    os.remove(file_path) 
                except zipfile.BadZipFile: 
                    os.remove(file_path) 
                continue 

 

            # Обробка файлів 
            if extension in {'JPEG', 'PNG', 'JPG', 'SVG'}: 
                dest_folder = 'images' 
            elif extension in {'AVI', 'MP4', 'MOV', 'MKV'}: 
                dest_folder = 'video' 
            elif extension in {'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'}: 
                dest_folder = 'documents' 
            elif extension in {'MP3', 'OGG', 'WAV', 'AMR'}: 
                dest_folder = 'audio' 
            else: 
                dest_folder = 'other' 

 

            # Перейменування та переміщення файлу 
            normalized_filename = normalize(file) 
            new_path = os.path.join(root, dest_folder, normalized_filename) 
            shutil.move(file_path, new_path) 

 

    # Видалення порожніх папок 

    for root, dirs, files in os.walk(folder_path, topdown=False): 
        for folder in dirs: 
            folder_path = os.path.join(root, folder) 
            if not os.listdir(folder_path): 
                os.rmdir(folder_path) 

 

if __name__ == "__main__": 
    target_folder = input("C:\Users\Юрій\Desktop\Мотлох") # Папка яку слід перевірити
    process_folder(target_folder) 
    print("Сортування завершено.") 