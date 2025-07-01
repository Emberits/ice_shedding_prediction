import pandas as pd
import numpy as np
from typing import Dict

def normalize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Нормализация данных: приведение к диапазону [0, 1].
    
    :param df: Исходный DataFrame
    :return: Нормализованный DataFrame
    """
    return (df - df.min()) / (df.max() - df.min())

def generate_shedding_potential(weather_data: Dict[str, float]) -> float:
    """
    Расчёт потенциала сброса льда на основе метеоданных.
    
    Формула: 
    Potential = ΔT_6h + P_rain + V_wind
    
    :param weather_data: Словарь с метеоданными
    :return: Потенциал сброса (0–1)
    """
    delta_temp = abs(weather_data.get("temperature_change_6h", 0))
    precipitation = weather_data.get("precipitation", 0)
    wind_speed = weather_data.get("wind_speed", 0)
    
    # Нормализация факторов
    max_delta_temp = 10  # Максимальный перепад температур за 6 часов
    max_precipitation = 5  # Максимальные осадки (мм/час)
    max_wind_speed = 20  # Максимальная скорость ветра (м/с)
    
    normalized_delta = delta_temp / max_delta_temp
    normalized_precip = precipitation / max_precipitation
    normalized_wind = wind_speed / max_wind_speed
    
    # Комбинированный потенциал
    potential = (normalized_delta + normalized_precip + normalized_wind) / 3
    return round(min(potential, 1.0), 2)

# Пример использования:
if __name__ == "__main__":
    sample_weather = {
        "temperature": -5,
        "wind_speed": 12,
        "humidity": 90,
        "precipitation": 0.5,
        "temperature_change_6h": 3.2
    }
    
    print("Потенциал сброса льда:", generate_shedding_potential(sample_weather))
