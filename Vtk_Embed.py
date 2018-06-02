import sys
import vtk
from PyQt4 import QtCore, QtGui
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import display
 
class MainWindow(QtGui.QMainWindow, display.Ui_MainWindow):
 
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        
        #QtGui.QMainWindow.__init__(self, parent)
 
        #self.frame = QtGui.QFrame()
 
        #self.vl = QtGui.QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        #self.vl.addWidget(self.vtkWidget)
 
        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()
 
        # Create source
        source = vtk.vtkSphereSource()
        source.SetCenter(0, 0, 0)
        source.SetRadius(5.0)
 
        # Create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())
 
        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
 
        self.ren.AddActor(actor)
 
        self.ren.ResetCamera()
 
        #self.frame.setLayout(self.vl)
        #self.setCentralWidget(self.frame)
 
        self.show()
        self.iren.Initialize()
        
 
 
if __name__ == "__main__":
 
    app = QtGui.QApplication(sys.argv)
 
    window = MainWindow()
    
    window.show() 
 
    sys.exit(app.exec_())
