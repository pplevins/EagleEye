import mysql.connector

from Models import Agent, AgentStatus


class AgentDAL:
    """Class to represent Agent's Data Layer, and implementing CRUD operations for agent."""

    def __init__(self, conn_str=None):
        """Constructor"""
        self.conn_str = conn_str or {
            'host': '127.0.0.1',
            'user': 'root',
            'password': '',
            'database': 'eagleEyeDB'
        }

    def connect(self):
        """Connect to database."""
        return mysql.connector.connect(**self.conn_str)

    def add_agent(self, agent: Agent):
        """Add agent to the database."""
        with self.connect() as conn:
            cursor = conn.cursor()
            query = """
                    INSERT INTO agents (codeName, realName, location, status, missionsCompleted)
                    VALUES (%s, %s, %s, %s, %s) \
                    """
            cursor.execute(query, (agent.code_name, agent.real_name, agent.location, agent.status.value,
                                   agent.missions_completed))
            conn.commit()

    def get_all_agents(self):
        """Get all agents from the database."""
        agents = []
        with self.connect() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM agents")
            for row in cursor:
                status = AgentStatus(row['status'])
                agents.append(Agent(
                    agent_id=row['id'],
                    code_name=row['codeName'],
                    real_name=row['realName'],
                    location=row['location'],
                    status=status,
                    missions_completed=row['missionsCompleted']
                ))
        return agents

    def update_agent_location(self, agent_id, new_location):
        """Update agent location."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE agents SET location = %s WHERE id = %s", (new_location, agent_id))
            conn.commit()

    def delete_agent(self, agent_id):
        """Deletes agent from the database."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM agents WHERE id = %s", (agent_id,))
            conn.commit()

    def reset_agents_table(self):
        """Reset agents table."""
        drop_sql = "DROP TABLE IF EXISTS agents;"
        create_sql = """
                     CREATE TABLE agents
                     (
                         id                INT AUTO_INCREMENT PRIMARY KEY,
                         codeName          VARCHAR(50),
                         realName          VARCHAR(50),
                         location          VARCHAR(100),
                         status            ENUM('Active', 'Injured', 'Missing', 'Retired'),
                         missionsCompleted INT
                     ); \
                     """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(drop_sql)
            cursor.execute(create_sql)
            conn.commit()
            print("Table 'agents' was successfully recreated.")
