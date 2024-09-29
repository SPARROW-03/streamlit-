import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# Function to check if the number is even or odd
def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is Even."
    else:
        return f"{number} is Odd."

# Create the PyQt5 application class
class EvenOddCheckerApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set up the UI components
        self.initUI()

    # Initialize UI elements
    def initUI(self):
        # Window title and dimensions
        self.setWindowTitle('Even or Odd Number Checker')
        self.setGeometry(100, 100, 300, 150)

        # Label for instructions
        self.label = QLabel('Enter a number:', self)

        # Input field to enter the number
        self.input_field = QLineEdit(self)

        # Button to check whether the number is even or odd
        self.check_button = QPushButton('Check', self)
        self.check_button.clicked.connect(self.check_number)  # Connect button to the function

        # Label to display the result
        self.result_label = QLabel('', self)

        # Layout for vertical arrangement
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.check_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    # Method to check if the number is even or odd
    def check_number(self):
        try:
            # Get the number from the input field
            number = int(self.input_field.text())

            # Call the function to check if the number is even or odd
            result = check_odd_even(number)

            # Display the result in the result_label
            self.result_label.setText(result)

        except ValueError:
            # Handle invalid input (non-integer)
            self.result_label.setText("Please enter a valid integer.")

# Main function to run the PyQt5 application
def main():
    app = QApplication(sys.argv)
    window = EvenOddCheckerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
