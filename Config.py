import toml
from dataclasses import dataclass
from logger import logger

@dataclass
class ColorConfig:
    red_lower: list
    red_upper: list
    green_lower: list
    green_upper: list
    yellow_lower: list
    yellow_upper: list


def load_config(file_path="config/config.toml"):
    try:
        logger.debug(f"{file_path} dosyasını yüklemeye çalışıyorum.")
        config = toml.load(file_path)
        logger.info(f"{file_path} dosyası başarıyla yüklendi.")
        return ColorConfig(**config["colors"])
    except FileNotFoundError:
        logger.error(f"Konfigürasyon dosyası bulunamadı: {file_path}")
        raise
    except KeyError as e:
        logger.error(f"Konfigürasyon dosyasında eksik anahtar: {e}")
        raise
    except Exception as e:
        logger.error(f"Konfigürasyon yüklenirken beklenmeyen bir hata oluştu: {e}")
        raise
