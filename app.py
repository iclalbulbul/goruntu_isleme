from Streamer import get_frame
from image_process import process_frame
from Config import load_config
from logger import logger


if __name__ == '__main__':
    try:
        logger.info("uygulama başlatılıyor.")

        config = load_config()
        logger.info("konfigürasyon başarıyla yüklendi.")

        logger.info("kamera çerçeve yakalama işlemi başlatıldı.")
        for frame in get_frame():
            process_frame(frame)

    except Exception as e:
        logger.critical(f"uygulama çalışırken kritik bir hata oldu: {e}")

    finally:
        logger.info("uygulama sonlandırıldı.")