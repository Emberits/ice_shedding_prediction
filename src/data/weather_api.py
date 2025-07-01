import random
from typing import Dict

def get_weather_data(api_key: str, lat: float, lon: float) -> Dict[str, float]:
    """
    Заглушка для получения метеоданных через API.
    Возвращает синтетические данные для тестирования.
    
    :param api_key: API-ключ (не используется в заглушке)
    :param lat: Широта
    :param lon: Долгота
    :return: Словарь с метеоданными
    """
    # Симуляция случайных данных в диапазонах, характерных для зимних условий
    return {
        "temperature": round(random.uniform(-20, 5), 1),       # Температура, °C
        "wind_speed": round(random.uniform(0, 20), 1),         # Скорость ветра, м/с
        "humidity": round(random.uniform(60, 100), 1),         # Влажность, %
        "precipitation": round(random.uniform(0, 5), 1),       # Осадки, мм/час
        "lat": lat,
        "lon": lon
    }

# Пример использования:
if __name__ == "__main__":
    test_data = get_weather_data("fake_api_key", 55.7558, 37.6176)
    print("Полученные метеоданные:", test_data)
