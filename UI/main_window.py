from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout
)

from DAL import AgentDAL
from Models import Agent
from .agent_form import AgentForm


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EagleEye Agent Manager")
        self.setMinimumSize(900, 400)

        self.agent_dal = AgentDAL()

        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Code Name", "Real Name", "Location", "Status", "Missions"])
        self.layout.addWidget(self.table)

        button_layout = QHBoxLayout()
        self.refresh_button = QPushButton("Refresh")
        self.add_button = QPushButton("Add")
        self.edit_button = QPushButton("Edit")
        self.delete_button = QPushButton("Delete")

        self.refresh_button.clicked.connect(self.load_agents)
        self.add_button.clicked.connect(self.add_agent)
        self.edit_button.clicked.connect(self.edit_agent)
        self.delete_button.clicked.connect(self.delete_agent)

        for btn in [self.refresh_button, self.add_button, self.edit_button, self.delete_button]:
            button_layout.addWidget(btn)

        self.layout.addLayout(button_layout)
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

    def add_agent(self):
        form = AgentForm(self)
        if form.exec():
            data = form.get_data()
            new_agent = Agent(0, **data)  # ID will be auto-incremented in DB
            self.agent_dal.add_agent(new_agent)
            self.load_agents()

    def edit_agent(self):
        selected = self.table.currentRow()
        if selected == -1:
            QMessageBox.warning(self, "Warning", "Select a row to edit.")
            return

        agent_id = int(self.table.item(selected, 0).text())
        existing_agent = next((a for a in self.agent_dal.get_all_agents() if a.id == agent_id), None)
        if not existing_agent:
            QMessageBox.warning(self, "Error", "Agent not found.")
            return

        form = AgentForm(self, existing_agent)
        if form.exec():
            data = form.get_data()
            updated_agent = Agent(agent_id, **data)
            self.agent_dal.delete_agent(agent_id)  # Simplified: delete and re-add
            self.agent_dal.add_agent(updated_agent)
            self.load_agents()

    def delete_agent(self):
        selected = self.table.currentRow()
        if selected == -1:
            QMessageBox.warning(self, "Warning", "Select a row to delete.")
            return

        agent_id = int(self.table.item(selected, 0).text())
        confirm = QMessageBox.question(self, "Confirm", f"Delete agent #{agent_id}?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.agent_dal.delete_agent(agent_id)
            self.load_agents()
