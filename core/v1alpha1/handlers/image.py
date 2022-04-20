from utils import *


class ImageHandler(object):
    def __init__(self):
        pass

    @staticmethod
    def serve_dummy_image():
        im = cv2.imread('dummy.tif', -1)
        res, im_png = cv2.imencode(".png", im)
        return io.BytesIO(im_png.tobytes()), "image/png"
