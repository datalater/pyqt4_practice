import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("HUFS_GRADE")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        
        
         #-------------------시작_메뉴바(위젯)-------------------#
         
        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()  

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        
        #-------------------끝_메뉴바(위젯)-------------------#

        self.home()

    def home(self):
    
        #-------------------시작_버튼(위젯)-------------------#
        
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
        
        #-------------------끝_버튼(위젯)-------------------#
        
        
        #-------------------시작_툴바(위젯)-------------------#

        extractAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)
        
        #-------------------끝_툴바(위젯)-------------------#
        
        
        #-------------------시작_폰트위젯(위젯)-------------------#
        
        fontChoice = QtGui.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
                #self.toolBar = self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)
        
        
        
        #-------------------시작_체크박스(위젯)-------------------#

        checkBox = QtGui.QCheckBox('Shrink Window', self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)
        
        #-------------------끝_체크박스(위젯)-------------------#
        
        
        #-------------------시작_프로그레스바(위젯)-------------------#
        
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)
        
        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)
        
        #-------------------끝_프로그레스바(위젯)-------------------#
        
        
        #-------------------시작_드랍다운(위젯)-------------------#
        
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("Windows Vista", self)
        
        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowvista")
        
        comboBox.move(50, 250)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)
        
        #-------------------끝_드랍다운(위젯)-------------------#
        
        self.show()
        
        #-------------------시작_폰트위젯(함수)-------------------#
        
    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)
        
        #-------------------끝_폰트위젯(함수)-------------------#
        
        
        #-------------------시작_드랍다운(함수)-------------------#
        
    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
        
        
        #-------------------끝_드랍다운(함수)-------------------#
        
        
        #-------------------시작_프로그레스바(함수)-------------------#
        
    def download(self):
        self.completed = 0
        
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
            
        #-------------------끝_프로그레스바(함수)-------------------#
        
        
        #-------------------시작_체크박스(함수)-------------------#

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
            
        #-------------------끝_체크박스(함수)-------------------#
        
        
        #-------------------시작_메뉴바(함수)-------------------#

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
            
        #-------------------끝_메뉴바(함수)-------------------#
        
        

    
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()