
from autogenstudio.teammanager import TeamManager
import asyncio

from dotenv import load_dotenv
load_dotenv()

# Initialize the TeamManager
manager = TeamManager()

# Run a task with a specific team configuration
result = asyncio.run(manager.run(
task="what is 24243*234234",
team_config="team.json"
))
print(result)