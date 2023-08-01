Node Red Dashboard Automation Tool

Installation Requirements:

To use the Node Red Dashboard Automation Tool, you need the following:

1. Python: Make sure you have Python installed on your computer. You can download the latest version of Python from the official website: https://www.python.org/downloads/
1. PyQt5: The program uses the PyQt5 library for building the graphical user interface. You can install PyQt5 using pip by running the following command in your terminal or command prompt:

pip install pyqt5

How the Program Works:

The Node Red Dashboard Automation Tool is a Python-based desktop application that allows you to automate certain tasks related to Node-RED dashboard JSON files. It provides a graphical user interface (GUI) to import a JSON file, perform automation on the data, and save the modified JSON back to a file.

Here's how the program works:

1. Launch the Application: After installing the required dependencies, run the Python script to launch the application.
1. GUI Layout: The application opens a window with the title "Node Red Dashboard Automation." The window contains the following components:
- `	`A large text area (QTextEdit) where you can paste the content of your JSON file or view the modified JSON data.
- `	`Two input fields (QLineEdit) labeled "Find" and "Replace." These fields allow you to specify the text you want to find and replace in the JSON data.
- `	`Three buttons (QPushButton) labeled "Import JSON," "Perform Automation," and "Save JSON." These buttons trigger specific actions.

3\. Import JSON: Click on the "Import JSON" button to open a file dialog. Select the JSON file you want to work with, and its content will be displayed in the large text area.

4\. Perform Automation: After importing the JSON, enter the text you want to find and replace in the "Find" and "Replace" input fields, respectively. Click on the "Perform Automation" button to apply the automation process. The following actions are performed:

- `	`Replace "ui\_tab" ID with "1" and update all occurrences in the JSON.
- `	`Replace "tab" ID with "100" and update all occurrences in the JSON.
- `	 `Replace "ui\_group" ID with "1+i" (where i is an incremental number) and update all occurrences in the JSON.
- `	`Find and replace "branch plant" values with the specified text.

Additionally, the program finds and replaces all occurrences of the specified "Find" text with the specified "Replace" text. The modified JSON will be displayed in the text area.

5\. Save JSON: If you are satisfied with the modifications, click on the "Save JSON" button. A file dialog will open, allowing you to specify the file path and save the modified JSON to a new file.

Notes

- The application uses PyQt5 for the graphical user interface, making it easy to interact with the program.
- Be cautious when performing automation, as it may modify the JSON in unexpected ways if not used properly.
- Make sure to back up your original JSON files before applying any modifications with this tool.


