from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QLabel, QDialogButtonBox

from Models import AgentStatus


class AgentForm(QDialog):
    def __init__(self, parent=None, agent=None):
        super().__init__(parent)
        self.setWindowTitle("Agent Form")
        self.setMinimumWidth(300)

        self.agent = agent
        layout = QVBoxLayout()

        self.code_input = QLineEdit()
        self.real_input = QLineEdit()
        self.loc_input = QLineEdit()
        self.status_input = QComboBox()
        self.status_input.addItems([status.name for status in AgentStatus])
        self.missions_input = QLineEdit()

        layout.addWidget(QLabel("Code Name"))
        layout.addWidget(self.code_input)
        layout.addWidget(QLabel("Real Name"))
        layout.addWidget(self.real_input)
        layout.addWidget(QLabel("Location"))
        layout.addWidget(self.loc_input)
        layout.addWidget(QLabel("Status"))
        layout.addWidget(self.status_input)
        layout.addWidget(QLabel("Missions Completed"))
        layout.addWidget(self.missions_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.setLayout(layout)

        if agent:
            self.code_input.setText(agent.code_name)
            self.real_input.setText(agent.real_name)
            self.loc_input.setText(agent.location)
            self.status_input.setCurrentText(agent.status.name)
            self.missions_input.setText(str(agent.missions_completed))

    def get_data(self):
        return {
            "code_name": self.code_input.text(),
            "real_name": self.real_input.text(),
            "location": self.loc_input.text(),
            "status": AgentStatus[self.status_input.currentText()],
            "missions_completed": int(self.missions_input.text())
        }
