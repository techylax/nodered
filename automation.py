import json
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QFileDialog

class AutomationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Node Red Dashboard Automation')
        self.setGeometry(100, 100, 500, 400)

        self.json_textedit = QTextEdit()
        self.find_label = QLabel('Find:')
        self.find_lineedit = QLineEdit()
        self.replace_label = QLabel('Replace:')
        self.replace_lineedit = QLineEdit()
        self.import_button = QPushButton('Import JSON')
        self.process_button = QPushButton('Perform Automation')
        self.save_button = QPushButton('Save JSON')

     # Python script to create Ui using PyQt5


        layout = QVBoxLayout()
        layout.addWidget(self.json_textedit)
        layout.addWidget(self.find_label)
        layout.addWidget(self.find_lineedit)
        layout.addWidget(self.replace_label)
        layout.addWidget(self.replace_lineedit)
        layout.addWidget(self.import_button)
        layout.addWidget(self.process_button)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

        self.import_button.clicked.connect(self.import_json)
        self.process_button.clicked.connect(self.perform_automation)
        self.save_button.clicked.connect(self.save_json)

        self.modified_json = None
    

    def import_json(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Import JSON', '', 'JSON Files (*.json)')
        if file_path:
            with open(file_path, 'r') as file:
                self.json_textedit.setPlainText(file.read())

    def perform_automation(self):
        json_data = self.json_textedit.toPlainText()
        find_text = self.find_lineedit.text()
        replace_text = self.replace_lineedit.text()

        try:
            data = json.loads(json_data)
            ui_group_counter = 2
            ui_group_mapping = {}


# Replace ui_tab ID with "1" and update all occurrences
            for node in data:
                if node.get('type') == 'ui_tab':
                    old_id = node.get('id')
                    node['id'] = '1'
                    for other_node in data:
                        for key, value in other_node.items():
                            if key != 'id' and value == old_id:
                                other_node[key] = '1'


# Replace tab ID with "100" and update all occurrences
            for node in data:
                if node.get('type') == 'tab':
                    old_id = node.get('id')
                    node['id'] = '100'
                    for other_node in data:
                        for key, value in other_node.items():
                            if key != 'id' and value == old_id:
                                other_node[key] = '100'

            # Replace ui_group ID with "1+i" and update all occurrences
            for node in data:
                if node.get('type') == 'ui_group':
                    old_id = node.get('id')
                    new_id = str(ui_group_mapping.get(old_id, ui_group_counter))
                    node['id'] = new_id
                    ui_group_mapping[old_id] = new_id
                    ui_group_counter += 1
                    for other_node in data:
                        for key, value in other_node.items():
                            if key != 'id' and value == old_id:
                                other_node[key] = new_id

            # Find and replace branch plant if needed
            for node in data:
                if node.get('type') == 'branch_plant':
                    if node.get('value') == find_text:
                        node['value'] = replace_text

            # Find and replace all occurrences
            modified_json = json.dumps(data, indent=4)
            modified_json = modified_json.replace(find_text, replace_text)

            # Save the modified JSON
            self.modified_json = modified_json
            self.json_textedit.setPlainText(self.modified_json)
        except Exception as e:
            print('Error:', str(e))

    def save_json(self):
        if self.modified_json:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self, 'Save JSON', '', 'JSON Files (*.json)')
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(self.modified_json)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutomationWindow()
    window.show()
    sys.exit(app.exec_())
