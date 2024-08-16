import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QPlainTextEdit, QLabel, QLineEdit, \
    QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
import pyperclip


class App(QWidget):
    IMAGE_PATH = r"W:\RoyalMail_Tracking_Number_Generator\Royal_Mail_logo2.png"
    EXAMPLE_IMAGE_PATH = r"W:\RoyalMail_Tracking_Number_Generator\example2.png"
    WINDOW_TITLE = 'Royal Mail Tracking Number Generator'
    WINDOW_DIMENSIONS = (150, 150, 900, 700)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setGeometry(*self.WINDOW_DIMENSIONS)

        # Main layout
        main_layout = QVBoxLayout()

        # Image layout
        image_layout = QHBoxLayout()
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap(self.IMAGE_PATH))
        image_layout.addWidget(self.image)

        # Input layout
        input_layout = QGridLayout()

        self.total_tracking_numbers_label = QLabel("Total tracking numbers to generate:")
        self.total_tracking_numbers = QLineEdit()
        input_layout.addWidget(self.total_tracking_numbers_label, 0, 0)
        input_layout.addWidget(self.total_tracking_numbers, 0, 1)

        self.first_number_label = QLabel("First number on tracking label reel:")
        self.first_number = QLineEdit()
        input_layout.addWidget(self.first_number_label, 1, 0)
        input_layout.addWidget(self.first_number, 1, 1)

        self.first_number_label2 = QLabel("Enter the 2, 4-chunk digits without spaces")
        input_layout.addWidget(self.first_number_label2, 2, 0, 1, 2)

        # Text area for output
        self.textHR = QPlainTextEdit(self)
        self.textHR.setReadOnly(True)
        main_layout.addWidget(self.textHR)

        # Buttons layout
        buttons_layout = QHBoxLayout()
        self.generate_tracking_numbers = QPushButton('Generate Tracking Numbers')
        self.generate_tracking_numbers.clicked.connect(self.tracking_numbers)
        buttons_layout.addWidget(self.generate_tracking_numbers)

        self.button_Clear = QPushButton('Clear Form')
        self.button_Clear.clicked.connect(self.clear_form)
        buttons_layout.addWidget(self.button_Clear)

        self.copy_button = QPushButton('Copy Numbers')
        self.copy_button.clicked.connect(self.copy_numbers)
        buttons_layout.addWidget(self.copy_button)

        # Assemble main layout
        main_layout.addLayout(image_layout)
        main_layout.addLayout(input_layout)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)
        self.show()

    def clear_form(self):
        """Clears all input and output fields."""
        self.textHR.clear()
        self.first_number.clear()
        self.total_tracking_numbers.clear()

    def copy_numbers(self):
        """Copies the generated tracking numbers to the clipboard."""
        pyperclip.copy(self.textHR.toPlainText())

    def tracking_numbers(self):
        """Generates tracking numbers based on input."""
        try:
            starting_number = int(self.first_number.text())
            total_numbers = int(self.total_tracking_numbers.text())

            for _ in range(total_numbers):
                digits = [int(x) for x in str(starting_number).zfill(8)]

                multipliers = [8, 6, 4, 2, 3, 5, 9, 7]
                total = sum(d * m for d, m in zip(digits, multipliers))
                checksum = (11 - (total % 11)) % 11
                checksum = 0 if checksum == 10 else checksum

                self.text_update(
                    f'KL {digits[0]}{digits[1]}{digits[2]}{digits[3]} {digits[4]}{digits[5]}{digits[6]}{digits[7]} {checksum}GB')
                starting_number += 1

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers for the total and first number.")

    def text_update(self, message):
        """Updates the output text area with a new message."""
        self.textHR.appendPlainText(message)
        self.textHR.verticalScrollBar().setValue(self.textHR.verticalScrollBar().maximum())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
