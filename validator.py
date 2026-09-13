from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QLineEdit, QLabel, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout
from PySide6.QtGui import QColor
from core import is_valid_asset_name as validate_name
import sys
import os

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Naming Convention Validator")
        self.setFixedSize(375, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Simply type in your custom prefixes and extensions \nbelow then click Browse Folders\n")
        layout.addWidget(self.label)

        self.prefix_input = QLineEdit()
        self.prefix_input.setPlaceholderText("Prefixes: train_, test_, val_, SM_")
        layout.addWidget(self.prefix_input)

        self.extension_input = QLineEdit()
        self.extension_input.setPlaceholderText("Extensions: .png, .jpg, .fbx")
        layout.addWidget(self.extension_input)

        self.label2 = QLabel("\nYour files:")
        layout.addWidget(self.label2)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        button = QPushButton("Browse Folders")
        button.clicked.connect(self.run_validator)
        layout.addWidget(button)

        button2 = QPushButton("Export Log")
        button2.clicked.connect(self.export_log)
        layout.addWidget(button2)

        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-family: Arial;
                font-size: 13px;
            }
            QLineEdit {
                background-color: #2d2d2d;
                color: white;
                border: 1px solid #3d3d3d;
                border-radius: 4px;
                padding: 2px;
            }
            QListWidget {
                background-color: black;
                border: none;
            }
            QPushButton {
                background-color: #0078d4;
                color: white;
                border-radius: 4px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
        """)

        self.files = []
        self.valid_counter = 0
        self.invalid_counter = 0

    def is_valid_asset_name(self, file_name):
        prefix_text = self.prefix_input.text().strip()
        extension_text = self.extension_input.text().strip()

        if not prefix_text or not extension_text:
            return False

        prefixes = tuple(p.strip() for p in prefix_text.split(","))
        extensions = tuple(e.strip() for e in extension_text.split(","))

        return validate_name(file_name, prefixes, extensions)

    def run_validator(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Asset Folder")

        if not folder:
            self.list_widget.clear()
            self.label.setText("No folder selected.\n")
            print('[INFO] No folder selected.')
            return

        self.files = os.listdir(folder)
        self.valid_counter = 0
        self.invalid_counter = 0
        assets = []

        for file in self.files:
            item = QListWidgetItem(file)
            assets.append(item)
            if self.is_valid_asset_name(file):
                item.setForeground(QColor("#4ec94e"))
                self.valid_counter += 1
            else:
                item.setForeground(QColor("red"))
                self.invalid_counter += 1

        self.label.setText(f"{self.valid_counter} valid, {self.invalid_counter} invalid.\n")
        print(f'[INFO] Selected "{folder}" directory.')

        self.list_widget.clear()
        for asset in assets:
            self.list_widget.addItem(asset)

    def export_log(self):
        if not self.files:
            self.label.setText("Error: Run validation first.\n")
            print('[WARN] Run validation first.')
            return

        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Log File",
            "validation_log.txt",
            "Text Files (*.txt)"
        )

        if path:
            try:
                with open(path, "w") as f:
                    f.write("Asset Validation Report\n")
                    f.write("=======================\n")
                    for file in self.files:
                        if self.is_valid_asset_name(file):
                            f.write(f"{file} - VALID\n")
                        else:
                            f.write(f"{file} - INVALID\n")
                    f.write(f"\nSummary: {self.valid_counter} valid, {self.invalid_counter} invalid.")
                print('[INFO] Asset Validation Report has been created.')
            except Exception as e:
                self.label.setText(f"Error: {e}\n")
                print(f"[ERROR] {e}")
        else:
            print(f'[INFO] Asset Validation Report has been cancelled.')


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()