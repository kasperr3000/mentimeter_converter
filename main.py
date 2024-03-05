import sys
import subprocess

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QRadioButton, \
        QFileDialog
except ImportError:
    print("PyQt5 is not installed. Installing PyQt5 now...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5"])
        print("PyQt5 has been successfully installed.")
    except subprocess.CalledProcessError:
        print("Failed to install PyQt5. Please install PyQt5 manually.")
        sys.exit(1)


def convert_text():
    input_text = input_entry.text()
    output_direction = output_direction_var
    output_location, _ = QFileDialog.getSaveFileName(None, "Save HTML File", "", "HTML Files (*.html)")

    if output_location:
        with open(output_location, "w") as file:
            if output_direction == "Reverse":
                input_text = input_text[::-1]
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Embedded Script</title>
            </head>
            <body>
                {input_text}
            </body>
            </html>
            """
            file.write(html_content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the main window
    window = QWidget()
    window.setWindowTitle("HTML File Creator")

    # Create input label and entry
    input_label = QLabel("Enter Embedded Script:")
    input_entry = QLineEdit()
    input_layout = QVBoxLayout()
    input_layout.addWidget(input_label)
    input_layout.addWidget(input_entry)

    # Create output direction radio buttons
    normal_radio = QRadioButton("Normal")
    reverse_radio = QRadioButton("Reverse")
    output_direction_var = "Normal"


    def on_radio_button_clicked():
        global output_direction_var
        radio_button = window.sender()
        if radio_button.isChecked():
            output_direction_var = radio_button.text()


    normal_radio.clicked.connect(on_radio_button_clicked)
    reverse_radio.clicked.connect(on_radio_button_clicked)

    # Create convert button
    convert_button = QPushButton("Create HTML File")
    convert_button.clicked.connect(convert_text)

    # Arrange widgets in layout
    layout = QVBoxLayout()
    layout.addLayout(input_layout)
    layout.addWidget(normal_radio)
    layout.addWidget(reverse_radio)
    layout.addWidget(convert_button)

    # Set the layout for the main window
    window.setLayout(layout)

    # Show the main window
    window.show()

    # Start the application event loop
    sys.exit(app.exec_())
