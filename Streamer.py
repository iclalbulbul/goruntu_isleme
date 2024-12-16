import cv2
from logger import logger

def get_frame():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        logger.error('Kamera açılamadı')
        raise Exception("Kamera açılamadı.")

    logger.info("Kamera başarıyla açıldı.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        logger.debug("yeni bir görüntü alındı.")
        yield frame

        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            logger.info("kamera kapatma isteği alındı 'q' tuşuna basıldı.")
            break


    cap.release()
    cv2.destroyAllWindows()
    logger.info("kamera kapatıldı ve tüm kaynaklar serbest bırakıldı.")