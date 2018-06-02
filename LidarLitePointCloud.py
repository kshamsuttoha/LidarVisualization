import time
import serial
import math as m
import VtkPointCloud as v
import sys
import vtk
import csv
from numpy import random,genfromtxt,size
from PyQt4 import QtCore, QtGui
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import display
import threading
import time
from PyQt4.QtCore import QThread
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot


class ScanThread(QtCore.QThread):
    top = 0
    def __init__(self, main_gui):
        QtCore.QThread.__init__(self)
        self.top = main_gui
		
    def run(self):
        #Create and initialize variables
        i = 0
        pan_angle = 0
        tilt_angle = 0
        distance = 0
        
		#Setup VTK for plots
        self.top.need_pointcloud_setup.emit()
		#13500
        while i<2500:
            s = self.top.ser.readline().split()
            if(len(s) == 3):
                pan_angle = float(s[0])
                tilt_angle = float(s[1])
                distance = float(s[2])
            point = ConvertToCartesian(distance, pan_angle, 90-tilt_angle)
            if(abs(point[0])<1000 and abs(point[1])<1000 and abs(point[2])<1000):
                self.top.write.emit(pan_angle,tilt_angle,distance, point)            
                QtGui.QApplication.processEvents()
                self.top.pointcloud_changed.emit(point)
            i = i+1
	
        #Disable signal for scanning
        self.top.stop_scanning(self.top.ser)
        time.sleep(2)
		#Start interactions on the widget
        #self.top.vtkWidget.Start()
        self.top.vtkWidget.Initialize()


class MainWindow(QtGui.QMainWindow, display.Ui_MainWindow):
	
    write = pyqtSignal(float, float, int, list)
    pointcloud_changed = pyqtSignal(list)
    need_pointcloud_setup = pyqtSignal()
     
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        
        #Instance Variables
        self.point_array = []
        self.vl = QtGui.QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)
        self.frame.setLayout(self.vl)
        print(self.frame.height, self.frame.width) 
        self.renderer = vtk.vtkRenderer()
        self.pointCloud = v.VtkPointCloud()
        self.renderWindowInteractor = vtk.vtkRenderWindowInteractor()
        self.setup_vtk
        self.ser = 0
        
        #Signal slots of buttons
        self.startButton.clicked.connect(lambda: self.start_scanning(self.ser))
        self.stopButton.clicked.connect(lambda: self.stop_scanning(self.ser))
        
        #Actions for menu bar
        self.actionSave_CSV.triggered.connect(lambda: write_CSV(self.point_array))
        self.actionSave_STL.triggered.connect(lambda: write_STL(self.pointCloud))
        self.actionClear.triggered.connect(lambda: self.clear_pointcloud())
        
        #Scan thread
        self.scan_thread = ScanThread(self)
        self.write.connect(self.write_to_browser)
        self.pointcloud_changed.connect(self.update_pointcloud)
        self.need_pointcloud_setup.connect(self.setup_vtk)
        
    def write_something(self, x):
		self.textBrowser.append(x)

    def setup_vtk(self):
        # Renderer
        self.renderer.AddActor(self.pointCloud.vtkActor)
        self.renderer.SetBackground(0.0, 0.0, 0.0)
        self.renderer.ResetCamera()
        
        self.vtkWidget.GetRenderWindow().AddRenderer(self.renderer)
        self.vtkWidget.GetRenderWindow().Render()
        #self.vtkWidget.GetRenderWindow().SetSize(732,487)
        self.vtkWidget.Initialize()

	
    def update_vtk(self):
        # Renderer
        self.renderer.ResetCamera()		
        # Render Window
        self.vtkWidget.GetRenderWindow().Render()	
			
    def start_scanning(self, ser):
        #This is the enable signal to start scanning
        self.textBrowser.append("Start Scanning \n")
        QtGui.QApplication.processEvents()
        self.serial_setup()
        #Set the correct speed
        if(self.radioButton_slow.isChecked()):
            self.ser.write('2')
            self.textBrowser.append("Speed set to slow \n")
        elif(self.radioButton_medium.isChecked()):
            self.ser.write('3')
            self.textBrowser.append("Speed set to medium \n")
        elif(self.radioButton_fast.isChecked()):
            self.textBrowser.append("Speed set to fast \n")
            self.ser.write('4')
        #Send enable setting
        self.ser.write('1')
        #self.generate_pointcloud()
        if not self.scan_thread.isRunning():
			self.scan_thread.start()
		
    def stop_scanning(self, ser):
        if self.scan_thread.isRunning():
            self.scan_thread.terminate()
		#Disable signal for scanning
        self.textBrowser.append("Stop Scanning \n")
        QtGui.QApplication.processEvents()
        ser.write('0')
        #self.vtkWidget.Start()
    
    def serial_setup(self):
        if self.ser == 0:
            self.ser = serial.Serial('COM3', 9600)
            #On windows, starting the serial port takes sometime. According to the arduino website, sleeping for 2 seconds kis a way of getting around it.  
            time.sleep(2)
     
    def write_to_browser(self, pan_angle, tilt_angle, distance, point):
        self.textBrowser.append("pan: %f tilt: %f distance:%f \n" %(pan_angle,tilt_angle,distance))
        self.textBrowser.append("x: %f y: %f z: %f \n" %(point[0],point[1],point[2]))
        
    def update_pointcloud(self, point):
        self.point_array.append(point)
        self.pointCloud.addPoint(point)
        self.update_vtk()
    
    def clear_pointcloud(self):
		del self.point_array[:]
		self.textBrowser.setText("")
		self.pointCloud.clearPoints()
		self.update_vtk()			

def ConvertToCartesian(r, theta, phi):
    x = r * m.sin(m.radians(phi)) * m.cos(m.radians(theta))
    y = r * m.sin(m.radians(phi)) * m.sin(m.radians(theta))
    z = r * m.cos(m.radians(phi))
    return [x, y, z]
    
def write_STL(pointCloud):
    # Write the stl file to disk
    filename = "DataPoints.stl"
    stlWriter = vtk.vtkSTLWriter()
    stlWriter.SetFileName(filename)
    stlWriter.SetInputData(pointCloud.vtkPolyData)
    stlWriter.Write()
	
def write_CSV(point_array):
    with open('DataPoints.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(point_array)

	
if __name__ == "__main__":
 
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    sys.exit(app.exec_())
