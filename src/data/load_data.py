import pandas as pd
import os

def load_lep_data(file_path: str) -> pd.DataFrame:
    """
    Загрузка параметров ЛЭП из CSV-файла.
    
    :param file_path: Путь к CSV-файлу
    :return: DataFrame с данными о ЛЭП
    :raises FileNotFoundError: Если файл не найден
    :raises KeyError: Если отсутствуют необходимые колонки
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    
    required_columns = ['wire_diameter', 'span_length', 'temperature', 'wind_speed', 'humidity', 'precipitation']
    
    df = pd.read_csv(file_path)
    missing_cols = [col for col in required_columns if col not in df.columns]
    
    if missing_cols:
        raise KeyError(f"Отсутствуют необходимые колонки: {missing_cols}")
    
    return df[required_columns]

# Пример использования:
if __name__ == "__main__":
    # Создание тестового CSV-файла (для демонстрации)
    test_data = pd.DataFrame({
        'wire_diameter': [12.7, 15.2, 12.7],
        'span_length': [200, 300, 250],
        'temperature': [-3, -5, 0],
        'wind_speed': [10, 12, 5],
        'humidity': [85, 90, 60],
        'precipitation': [0.2, 0.5, 0.0]
    })
    
    test_data.to_csv("test_lep_data.csv", index=False)
    
    # Тестирование функции
    loaded_data = load_lep_data("test_lep_data.csv")
    print("Загруженные данные ЛЭП:")
    print(loaded_data.head())
