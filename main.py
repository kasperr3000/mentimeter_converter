import sys
import subprocess
import threading
# Check if PyQt5 is installed, if not, try to install it
try:
    from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
except ImportError:
    print("PyQt5 is not installed. Installing PyQt5 now...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt5"])
        print("PyQt5 has been successfully installed.")
        from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog
    except subprocess.CalledProcessError:
        print("Failed to install PyQt5. Please install PyQt5 manually.")
        sys.exit(1)

def convert_text():
    global input_entry, convert_button
    input_text = input_entry.text()
    output_location, _ = QFileDialog.getSaveFileName(None, "Save HTML File", "", "HTML Files (*.html)")

    if output_location:
        with open(output_location, "w") as file:
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

        # Provide visual feedback by changing button color to green and text to "Created!"
        convert_button.setStyleSheet("background-color: green;")
        convert_button.setText("Created!")

        # Start a separate thread to reset the button after 2 seconds
        threading.Thread(target=reset_button).start()

        # Clear the input field
        input_entry.clear()


def reset_button():
    global convert_button
    import time
    # Wait for 2 seconds
    time.sleep(2)
    # Reset button to its original state
    convert_button.setStyleSheet("")
    convert_button.setText("Create HTML File")


if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)

    # Create the window
    window = QWidget()
    window.setWindowTitle("HTML File Creator")

    # Create input label and entry
    input_label = QLabel("Enter Embedded Script:")
    input_entry = QLineEdit()
    input_layout = QVBoxLayout()
    input_layout.addWidget(input_label)
    input_layout.addWidget(input_entry)

    # Create convert button
    convert_button = QPushButton("Create HTML File")
    convert_button.clicked.connect(convert_text)

    # Arrange widgets in layout
    layout = QVBoxLayout()
    layout.addLayout(input_layout)
    layout.addWidget(convert_button)

    # Set the layout for the window
    window.setLayout(layout)

    # Show the window
    window.show()

    # Start the application event loop
    sys.exit(app.exec_())
