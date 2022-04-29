import warnings
# import sys 
warnings.filterwarnings('ignore')


import numpy as np
from keras.models import load_model
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from PyQt5.Qt import Qt
import cv2


threshold = 0.90
font = cv2.FONT_HERSHEY_COMPLEX
model = load_model('asl_model')
predictDict={}

predictSentence=""
alphabet = "abcdefghiklmnopqrstuvwxy"
dictionary = {}
for i in range(24):
    dictionary[i] = alphabet[i]


def resetDict():
    for i in alphabet:
        predictDict[i]=0

resetDict()
def preprocessing(img):
        img = img.astype("uint8")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.equalizeHist(img)
        img = img/255
        return img


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._radius = 0

        self._animation = QVariantAnimation(startValue=0.0)
        self._animation.valueChanged.connect(self._handle_valueChanged)
        self._animation.finished.connect(self._handle_finished)
        self._animation.setDuration(300)
        self.pressed.connect(self._start_animation)

    def _start_animation(self):
        self._animation.setEndValue(self.width() / 2.0)
        self._animation.start()

    def _handle_valueChanged(self, value):
        self._radius = value
        self.update()

    def _handle_finished(self):
        self._radius = 0
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self._radius:
            qp = QPainter(self)
            qp.setBrush(QColor(255, 255, 255, 127))
            qp.setPen(Qt.NoPen)
            qp.drawEllipse(self.rect().center(), self._radius, self._radius)


class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        
        # self.leftlist = QListWidget()
        # self.leftlist.insertItem (0, 'HOME' )
        # self.leftlist.insertItem (1, 'Recognise' )
        # self.leftlist.insertItem (2, 'Keyboard' )
            
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
            
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.stack4UI()
            
        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.stack1)        
        self.Stack.addWidget (self.stack2)
        self.Stack.addWidget (self.stack3)
        self.Stack.addWidget (self.stack4)
            
        hbox = QHBoxLayout(self)
        # hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        # self.leftlist.currentRowChanged.connect(lambda: self.Stack.setCurrentIndex(1))
        # self.setGeometry(300, 50, 10,10)
        self.setWindowTitle("Sign Language Recogniser")
        self.show()
            
    def stack1UI(self):
        self.VBL=QVBoxLayout()
        self.BTN1 = Button("Learn")
        
        self.BTN1.clicked.connect(self.StartFeed1)
        self.VBL.addWidget(self.BTN1)

        self.BTN2 = Button("Recognise")
        self.BTN2.clicked.connect(self.StartFeed2)
        self.VBL.addWidget(self.BTN2)

        self.BTN3 = Button("Keyboard")
        self.BTN3.clicked.connect(self.StartFeed3)
        self.VBL.addWidget(self.BTN3)
        self.stack1.setLayout(self.VBL)
        
    def stack2UI(self):
        self.VBL=QVBoxLayout()    
        self.setFixedWidth(650)
        self.setFixedHeight(600)

        self.title=QLabel()
        self.title.setText("LEARN")
        self.title.setAlignment(Qt.AlignCenter)
  
        self.VBL.addWidget(self.title)
        
        self.FeedLabel1 = QLabel()
        self.VBL.addWidget(self.FeedLabel1)
        
        self.CancelBTN = Button("Back")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()
            
        self.stack2.setLayout(self.VBL)

    def stack3UI(self):
        self.VBL=QVBoxLayout()    
        self.setFixedWidth(650)
        self.setFixedHeight(600)

        self.title=QLabel()
        self.title.setText("RECOGNISE")
        self.title.setAlignment(Qt.AlignCenter)
  
        self.VBL.addWidget(self.title)
        
        self.FeedLabel2 = QLabel()
        self.VBL.addWidget(self.FeedLabel2)

        self.CancelBTN = Button("Back")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker2 = Worker1()
            
        self.stack3.setLayout(self.VBL)

    def stack4UI(self):
        self.VBL=QVBoxLayout()    
        self.setFixedWidth(650)
        self.setFixedHeight(600)

        self.title=QLabel()
        self.title.setText("KEYBOARD")
        self.title.setAlignment(Qt.AlignCenter)
  
        self.VBL.addWidget(self.title)
        
        self.FeedLabel3 = QLabel()
        self.VBL.addWidget(self.FeedLabel3)
        
        self.CancelBTN = Button("Back")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker3 = Worker1()
            
        self.stack4.setLayout(self.VBL)


    def ImageUpdateSlot1(self,Image):
        self.FeedLabel1.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot2(self,Image):
        self.FeedLabel2.setPixmap(QPixmap.fromImage(Image))

    def ImageUpdateSlot3(self,Image):
        self.FeedLabel3.setPixmap(QPixmap.fromImage(Image))    

    def StartFeed1(self):    
        self.Stack.setCurrentIndex(1)
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot1)

    def StartFeed2(self):
        self.Stack.setCurrentIndex(2)
        self.Worker2.start()
        self.Worker2.ImageUpdate.connect(self.ImageUpdateSlot2)

    def StartFeed3(self):
        self.Stack.setCurrentIndex(3)
        self.Worker3.start()
        self.Worker3.ImageUpdate.connect(self.ImageUpdateSlot3)

    def CancelFeed(self):
        self.Worker1.stop()
        self.Worker2.stop()
        self.Worker3.stop()
        self.Stack.setCurrentIndex(0)
        global predictSentence
        predictSentence=""

    # def onKeyPressed(self,event):
    #     print("this:",event.text())


        
class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive=True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            # if keyboard.read_key() == 'backspace':
            #     print("You pressed "+keyboard.read_key())

            ret,imgOriginal = Capture.read()

            if ret:
                
                # Image = cv2.cvtColor(imgOriginal,cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(imgOriginal,1)
                # FlippedImage=imgOriginal                
                img = np.asarray(FlippedImage)
                cv2.putText(FlippedImage, "Alphabet", (20,35), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
                cv2.putText(FlippedImage, "Probability", (20,75), font, 0.75, (255,0,255), 2, cv2.LINE_AA)
                
                cv2.rectangle(img, (400, 100), (600,300), (50,50,255), 2)
                crop_img = img[100:300, 400:600]
                img = cv2.resize(crop_img, (28,28))
                img = preprocessing(img)
                img = img.reshape(1, 28, 28, 1)
                prediction = model.predict(img)
                predicted_letter = dictionary[np.argmax(prediction)]
                probabilityVal = np.amax(prediction)
                
                if probabilityVal>threshold:
                    cv2.putText(FlippedImage, predicted_letter, (150,35), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
                    cv2.putText(FlippedImage, str(round(probabilityVal*100,2))+"%", (180,75), font, 0.75, (255,0,255), 2, cv2.LINE_AA)                
                    predictDict[predicted_letter]+=1
                    if predictDict[predicted_letter]>10:
                        print(predicted_letter)
                        global predictSentence
                        predictSentence += predicted_letter
                        resetDict()
                cv2.putText(FlippedImage, "Sentence: "+predictSentence, (20,425), font, 0.75, (0,0,255), 2, cv2.LINE_AA)
        
                
                Image = cv2.cvtColor(FlippedImage,cv2.COLOR_BGR2RGB)
                ConvertToQtFormat = QImage(Image.data,Image.shape[1],Image.shape[0],QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640,480,Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()

   
	
if __name__ == "__main__":
   app = QApplication(sys.argv)
   ex = StackedExample()
   ex.setStyleSheet(
        """
    QPushButton {
    background-color: #2B5DD1;
    border-color: #2B5DD1;
    color: #FFFFFF;
    height:70px;
    width:200px;
    padding: 2px;
    font: bold 20px;
    border-width: 35px;
    border-radius: 35px;
    
}
QPushButton:hover {
    background-color: lightgreen;
    border-color: lightgreen;
}"""
    )
   
   sys.exit(app.exec()) 
   
    