from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QApplication, QMessageBox
)

from DAL import AgentDAL


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EagleEye Agent Manager")
        self.setMinimumSize(800, 400)

        self.agent_dal = AgentDAL()

        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Code Name", "Real Name", "Location", "Status", "Missions"])
        self.layout.addWidget(self.table)

        self.refresh_button = QPushButton("Refresh Agents")
        self.refresh_button.clicked.connect(self.load_agents)
        self.layout.addWidget(self.refresh_button)

        self.setLayout(self.layout)
        self.load_agents()

    def load_agents(self):
        try:
            agents = self.agent_dal.get_all_agents()
            self.table.setRowCount(len(agents))
            for row, agent in enumerate(agents):
                self.table.setItem(row, 0, QTableWidgetItem(str(agent.id)))
                self.table.setItem(row, 1, QTableWidgetItem(agent.code_name))
                self.table.setItem(row, 2, QTableWidgetItem(agent.real_name))
                self.table.setItem(row, 3, QTableWidgetItem(agent.location))
                self.table.setItem(row, 4, QTableWidgetItem(agent.status.name))
                self.table.setItem(row, 5, QTableWidgetItem(str(agent.missions_completed)))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load agents:\n{e}")
