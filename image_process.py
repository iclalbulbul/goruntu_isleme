import cv2
import numpy as np
from logger import logger

def process_frame(frame):
    try:
        logger.debug("görüntü işleme başlatıldı.")

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        logger.debug("görüntü HSV formatına dönüştürüldü.")

        colors = {
            "red": ([0, 120, 70], [10, 255, 255]),
            "green": ([36, 100, 100], [70, 255, 255]),
            "yellow": ([25, 50,70], [35,255,255]),
        }

        for color, (lower, upper) in colors.items():
            mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
            if cv2.countNonZero(mask) > 0:
                logger.info(f"{color} renk algılandı")
                break

        else:
            logger.debug("herhangi bir renk algılanamadı.")

    except Exception as e:
        logger.error(f"görüntü işleme sırasında hata oluştu: {e}")