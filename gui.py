"""GUI for the Folder Creator."""
import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
from PyQt6.QtWidgets import QComboBox, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout
import workspace_parser

# jade-spector - Subclass QMainQindow to customize Application's main window
class MainWindow(QMainWindow):
    """ Controls the createion of th window and collects the data to
    be sent to folder creator method."""
    def create_dir(self,p_name,dem_sel,type_sel):
        """ Atempts to create the folder based on the provided information.
        If the folder is created returns a success messege. If it does not
        create the folder an error messege is returned."""
        result = workspace_parser.fc_start(p_name,dem_sel,type_sel)
        if result == "exists":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Folder Already Exists.")
            msg.setWindowTitle("Warning")
            msg.exec()
        elif result == "Invalid":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Invalid Folder Chosen.")
            msg.setWindowTitle("Warning")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Project Structure Has Been Created.")
            msg.setWindowTitle("Success")
            msg.exec()

    def btn_clicked(self):
        """When the 'Create Workspace' button is clicked collects the data that
        has been collected. """
        p_name = self.project_name_entry.text()
        dem_sel = self.dem_widget.currentText()
        type_sel = self.type_widget.currentText()
        self.create_dir(p_name,dem_sel,type_sel)

    def __init__(self):
        """Sets up the layout for the window."""
        super().__init__()
        self.setWindowTitle("Ghostly Project Organizer")
        # jade-spector:  Project name section
        proj_widget = QLabel()
        proj_widget.setText("Project Name: ")
        self.project_name_entry = QLineEdit(parent=self)


        # jade-spector: Demnsion combobox section
        self.dem_widget = QComboBox()
        self.dem_widget.addItems(["2D","3D"])

        # jade-spector: Project Type combobox section
        self.type_widget = QComboBox()
        self.type_widget.addItems(["Static","Animated"])

        # jade-spector: Folder Creator Button
        btn_create = QPushButton("Create Workspace")
        btn_create.setCheckable(True)
        btn_create.clicked.connect(self.btn_clicked)

        # jade-spector: Layout for the GUI
        h_layout = QHBoxLayout()
        layout = QVBoxLayout()
        h_layout.addWidget(proj_widget)
        h_layout.addWidget(self.project_name_entry)
        layout.addLayout(h_layout)
        layout.addWidget(self.dem_widget)
        layout.addWidget(self.type_widget)
        layout.addWidget(btn_create)
        container = QWidget()
        container.setLayout(layout)
        self.setFixedSize(QSize(400, 200))
        # Set the central widget of the Window.
        self.setCentralWidget(container)

def gui_start():
    """ Starting point for the gui program"""
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()
