import os
import json

from dotenv import load_dotenv


load_dotenv()


class SettingsFile(object):
    def __init__(self) -> None:
        # Формирование пути файла
        file_path = os.path.join(os.getcwd(), os.getenv("SETTINGS_FILE_NAME"))
        print(file_path)
        self.file_path = file_path
    
    
    def read_settings(self) -> dict: 
        '''
        Функция для чтения файла конфигурации
        '''       
        with open(self.file_path, "r") as file:
            settings_dict = json.load(file)
        
        return settings_dict
    
    
    def write_settings(self, settings_dict: dict) -> None:
        '''
        Функция для записи файла конфигурации
        '''       
        with open(self.file_path, "w") as file:
            json.dump(settings_dict, file)
    


# def get_settings_file_path() -> str:
#     # Формирование пути файла
#     current_dir = os.getcwd()
#     file_name = os.getenv("SETTINGS_FILE_NAME")
#     # file_path = os.path.join(current_dir, file_name)
#     # print(file_path)
    
#     return ''
    

# # Функция для чтения файла конфигурации
# def read_settings() -> dict:
#     file_path = get_settings_file_path()
    
#     with open("E:\\R\\js_projects\\learn_js_main\\dca_test\\dca_bot\\settings.json", "r") as file:
#         settings_dict = json.load(file)
    
#     return settings_dict


# # Функция для записи файла конфигурации
# def write_settings(settings_dict: dict) -> None:
#     file_path = get_settings_file_path()
    
#     with open("E:\\R\\js_projects\\learn_js_main\\dca_test\\dca_bot\\settings.json", "w") as file:
#         json.dump(settings_dict, file)
