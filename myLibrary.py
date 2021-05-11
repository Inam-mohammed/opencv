import cv2
img = cv2.imread('input_image.png', cv2.IMREAD_UNCHANGED)


class Checkerboard(object):
    def __init__(self):
        self.instruction = """Welcome to Checkerboard Game!!!.Read the instruction carefully given below.
                                        1. In which size you want your board to display .
        rk the boxes as per your wish and those value starts from ('a1'..'h1') 
                                        i                                2. Man a horizontal manner and ('a1'..'a8')..('h1'...'h8') in vertical manner."""

    def instuctions(self):
        print(self.instruction)

    def drawing(self, circle):
        global img
        if circle == 'a1':
            img = cv2.circle(img, (39, 590), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'b1':
            img = cv2.circle(img, (118, 590), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'c1':
            img = cv2.circle(img, (197, 590), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'd1':
            img = cv2.circle(img, (274, 590), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'e1':
            img = cv2.circle(img, (353, 590), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'f1':
            img = cv2.circle(img, (433, 590), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'g1':
            img = cv2.circle(img, (512, 590), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'h1':
            img = cv2.circle(img, (590, 590), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'a2':
            img = cv2.circle(img, (39, 511), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'b2':
            img = cv2.circle(img, (118, 511), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'c2':
            img = cv2.circle(img, (197, 511), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'd2':
            img = cv2.circle(img, (274, 511), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'e2':
            img = cv2.circle(img, (353, 511), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'f2':
            img = cv2.circle(img, (433, 511), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'g2':
            img = cv2.circle(img, (512, 511), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'h2':
            img = cv2.circle(img, (590, 511), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'a3':
            img = cv2.circle(img, (39, 432), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'b3':
            img = cv2.circle(img, (118, 432), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'c3':
            img = cv2.circle(img, (197, 432), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'd3':
            img = cv2.circle(img, (274, 432), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'e3':
            img = cv2.circle(img, (353, 432), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'f3':
            img = cv2.circle(img, (433, 432), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'g3':
            img = cv2.circle(img, (512, 432), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'h3':
            img = cv2.circle(img, (590, 432), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'a4':
            img = cv2.circle(img, (39, 353), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'b4':
            img = cv2.circle(img, (118, 353), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'c4':
            img = cv2.circle(img, (197, 353), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'd4':
            img = cv2.circle(img, (274, 353), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'e4':
            img = cv2.circle(img, (353, 353), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'f4':
            img = cv2.circle(img, (433, 353), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'g4':
            img = cv2.circle(img, (512, 353), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'h4':
            img = cv2.circle(img, (590, 353), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'a5':
            img = cv2.circle(img, (39, 274), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'b5':
            img = cv2.circle(img, (118, 274), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'c5':
            img = cv2.circle(img, (197, 274), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'd5':
            img = cv2.circle(img, (274, 274), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'e5':
            img = cv2.circle(img, (353, 274), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'f5':
            img = cv2.circle(img, (433, 274), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'g5':
            img = cv2.circle(img, (512, 274), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'h5':
            img = cv2.circle(img, (590, 274), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'a6':
            img = cv2.circle(img, (39, 197), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'b6':
            img = cv2.circle(img, (118, 197), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'c6':
            img = cv2.circle(img, (197, 197), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'd6':
            img = cv2.circle(img, (274, 197), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'e6':
            img = cv2.circle(img, (353, 197), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'f6':
            img = cv2.circle(img, (433, 197), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'g6':
            img = cv2.circle(img, (512, 197), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'h6':
            img = cv2.circle(img, (590, 197), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == "a7":
            img = cv2.circle(img, (39, 118), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'b7':
            img = cv2.circle(img, (118, 118), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'c7':
            img = cv2.circle(img, (197, 118), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'd7':
            img = cv2.circle(img, (274, 118), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'e7':
            img = cv2.circle(img, (353, 118), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'f7':
            img = cv2.circle(img, (433, 118), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'g7':
            img = cv2.circle(img, (512, 118), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'h7':
            img = cv2.circle(img, (590, 118), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'a8':
            img = cv2.circle(img, (39, 39), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'b8':
            img = cv2.circle(img, (118, 39), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'c8':
            img = cv2.circle(img, (197, 39), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'd8':
            img = cv2.circle(img, (274, 39), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'e8':
            img = cv2.circle(img, (353, 39), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'f8':
            img = cv2.circle(img, (433, 39), radius=39, color=[255, 255, 255], thickness=-1)
        elif circle == 'g8':
            img = cv2.circle(img, (512, 39), radius=39, color=[0, 0, 0], thickness=-1)
        elif circle == 'h8':
            img = cv2.circle(img, (590, 39), radius=39, color=[255, 255, 255], thickness=-1)

    def resize(self,size):
        global img
        width = int(size)
        height = int(size)
        img = cv2.resize(img, (width, height))
        return img

    def display(self):
        cv2.imwrite("static/saved_pics/yours_chess.jpeg", img)
        cv2.destroyAllWindows()
