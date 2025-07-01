import math
from typing import Dict

def estimate_ice_thickness(weather_data: Dict[str, float], duration_hours: int = 24) -> float:
    """
    Оценка толщины льда на проводе через интегральную модель намерзания.
    
    Формула:
    IceThickness = k * ∫(V_wind * RH * f(T)) dt
    
    :param weather_data: Словарь с метеоданными
    :param duration_hours: Длительность намерзания (часы)
    :return: Толщина льда (мм)
    """
    # Коэффициенты модели
    k = 0.05  # Эмпирический коэффициент
    temp = weather_data.get("temperature", -5)
    rh = weather_data.get("humidity", 80)
    wind_speed = weather_data.get("wind_speed", 10)
    
    # Функция зависимости скорости намерзания от температуры
    def f_temp(temp):
        if temp >= 0:
            return 0  # Нет намерзания при положительной температуре
        return max(0, 1 - abs(temp)/10)  # Уменьшение скорости намерзания с ростом температуры
    
    # Расчёт толщины льда
    ice_thickness = k * wind_speed * rh * f_temp(temp) * duration_hours
    return round(ice_thickness, 2)

# Пример использования:
if __name__ == "__main__":
    sample_weather = {
        "temperature": -5,
        "wind_speed": 12,
        "humidity": 90,
        "precipitation": 0.5
    }
    
    thickness = estimate_ice_thickness(sample_weather, duration_hours=48)
    print(f"Оценённая толщина льда: {thickness} мм")
