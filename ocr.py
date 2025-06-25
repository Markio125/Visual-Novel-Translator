from paddleocr import PaddleOCR
import logging

def jpn_ocr(file_path):
    logging.getLogger('ppocr').setLevel(logging.WARNING)
    ocr = PaddleOCR(use_angle_cls=True, lang='japan')
    result = ocr.ocr(file_path, det=True, cls=True)
    final = ''
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            final += str(line[1][0]) + ' '
    return final