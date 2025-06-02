# 📋 Project Manager Agent

> 🚀 **Smart project management made simple!** An AI-powered assistant that helps you organize projects, track tasks, and manage teams - with everything automatically saved between sessions.

## 🤖 What is ADK?

The **Agent Development Kit (ADK)** is Google's powerful framework for building AI agents that can:

- 🗣️ Understand natural language conversations
- 🛠️ Use specialized tools and capabilities  
- 💾 Remember information across sessions
- 🔧 Integrate with other systems and APIs

## 💡 What's Special About Persistent Storage?

Unlike simple chatbots that forget everything when you close them, this agent **remembers everything**! Using ADK's `DatabaseSessionService`, all your projects, tasks, and team data is automatically saved to an SQLite database. Close the app, restart your computer, come back next week - your agent will remember exactly where you left off! 🧠✨

## 🚀 Quick Start

Ready to get your projects organized? Let's get you up and running in just a few minutes!

### 1. 🛠️ Environment Setup

```powershell
# Create virtual environment (if not already created)
python -m venv .venv

# Activate the virtual environment (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate the virtual environment (Linux/Mac)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. 🔑 API Key Configuration

Create a `.env` file in this directory with your Google API key:

```plaintext
GOOGLE_API_KEY=your_api_key_here
```

**Need an API key?** Get yours from the [Google AI Studio](https://makersuite.google.com/app/apikey) - it's free to get started! 🎉

### 3. 🎯 Run the Application

```powershell
python main.py
```

That's it! Your Project Manager Agent is ready to help you stay organized! 🎊

## 📚 What You'll Learn

This agent is perfect for learning key ADK concepts while building something actually useful! 🎓

### 🔑 Key Concepts Covered

- **💾 Persistent Storage**: Keep your data safe across sessions using database storage
- **🛠️ Tool-based Agents**: Build specialized capabilities through well-defined tools  
- **📊 State Management**: Properly update and maintain user-specific information
- **💬 Session Handling**: Manage ongoing conversations with users like a pro

### 🌟 Why This Matters

Unlike simple demos, this agent shows you how to build **real-world applications** that people can actually use every day!

## ✨ Features & Capabilities

### 📁 Project Management

- **➕ Create Projects**: Add new projects with names, descriptions, and due dates
- **👀 View Projects**: List all current projects and their details  
- **✏️ Update Projects**: Modify project information as requirements change
- **🗑️ Delete Projects**: Remove projects that are no longer needed
- **📊 Status Tracking**: Monitor completion percentages and task distribution

**🛠️ Agent Tools Concept**: Each capability is implemented as a "tool" in ADK - specialized functions that the agent can call to perform specific actions!

### ✅ Task Management  

- **📝 Add Tasks**: Create tasks within projects with specific requirements
- **👤 Assign Team Members**: Connect tasks to specific people responsible for completion
- **🔄 Track Status**: Monitor if tasks are "not started," "in progress," or "completed"
- **⏰ Set Deadlines**: Manage timelines for individual task completion  
- **🔍 Cross-Project Search**: Find tasks across all projects based on keywords

### 👥 Team Member Management

- **👋 Add Team Members**: Record team member information including roles and contact details
- **📋 Track Assignments**: See which team members are handling which tasks
- **✏️ Update Information**: Modify team member details as needed
- **🎯 Role Management**: Organize team members by their roles and responsibilities

### 💾 Persistent Storage System

- **🗄️ Database Backend**: All information is stored in a SQLite database file
- **🔄 Session Persistence**: Your data remains available between different conversations  
- **📊 State Management**: Changes to projects, tasks, and team members are automatically saved
- **🔧 Extensible Storage**: Can be easily adapted to use other database systems

## 💬 Example Interactions & Commands

Ready to see what this agent can do? Here are some fun interactions to try! Just talk to your agent naturally - it understands what you mean! 🗣️

### 🆔 Getting Started

- My name is {Your Name}, I am a student at {University Name}

### 📁 Academic Projects and Tasks

- Create a new project called 'Operating Systems Assignment' due on 2025-06-10
- Create another project called 'Final Year Capstone' due on 2025-12-15
- Add a task to Operating Systems Assignment: 'Implement round-robin scheduler' due 2025-06-03
- Add another task to Operating Systems Assignment: 'Write report and documentation' due 2025-06-08

### 👥 Group Work and Collaboration

- Add Alice as a team member for Capstone, role: Backend Developer, email <alice@university.edu>
- Add Raj as a team member, role: Research Lead, email <raj@university.edu>
- Add a task to Final Year Capstone: 'Design project architecture' due 2025-07-01, assigned to Alice
- Add a task to Final Year Capstone: 'Conduct literature review' due 2025-06-20, assigned to Raj

### ✅ Task and Role Updates

- Update the task 'Conduct literature review' to in progress
- Change Raj’s role to AI Research Lead
- Mark the task 'Implement round-robin scheduler' as completed
- Add another task to Capstone: 'Build prototype API' due 2025-08-10, assigned to Alice

### 📦 Project and Task Cleanup

- Rename the project 'Operating Systems Assignment' to 'OS Scheduler Assignment'
- Delete the task 'Write report and documentation' from OS Scheduler Assignment
- Remove Alice from the Final Year Capstone team

### 📊 Progress Review and Tracking

- What is the current status of the OS Scheduler Assignment project?
- Show me all tasks still in progress
- List all tasks assigned to Raj
- List all completed tasks across my projects
- Show me a summary of all my active projects and deadlines

**🧠 Pro Tip**: The agent understands natural language, so feel free to phrase things your own way! It's designed to understand your intent, not just specific commands.

---

## 🏗️ Project Architecture & Structure

Want to understand how this magic works? Let's dive into the architecture! This application uses ADK's `DatabaseSessionService` to maintain state between sessions.

```text
project-manager-agent/
├── main.py                      # 🚀 Entry point - sets up sessions and conversation loop
├── project_management_data.db   # 💾 SQLite database (created automatically on first run)
├── utils.py                     # 🛠️ Utility functions for conversation management  
└── project_management_agent/    # 🤖 Agent code directory
    ├── __init__.py              # 📦 Package initialization
    └── agent.py                 # 🧠 Defines the agent and all its tools
```

### 🔧 Key Components Explained

#### 1. 🚀 Main Application (`main.py`)

The command center that handles:

- **🗄️ Database Connection**: Initializes the SQLite database connection
- **📋 Session Management**: Finds existing sessions or creates new ones  
- **💬 Conversation Loop**: Manages the back-and-forth interaction with you
- **💾 State Persistence**: Ensures all your data is saved properly

#### 2. 🧠 Agent Definition (`agent.py`)

Where the magic happens:

- **🤖 Agent Configuration**: Sets up the language model and instructions
- **🛠️ Tool Functions**: Implements all the specialized capabilities  
- **📊 State Updates**: Handles how data is stored and retrieved

#### 3. 💾 Database File (`project_management_data.db`)

Your data's safe home:

- **🗄️ Stores All Data**: Contains tables for sessions and state information
- **🔄 Persists Between Runs**: Maintains information even when the application is closed
- **👥 Manages Multiple Users**: Can store data for different users separately  

#### 4. 🛠️ Utilities (`utils.py`)

The helpful extras:

- **🎨 Display Functions**: Formats data for terminal output
- **🤝 Helper Methods**: Simplifies common operations
- **🛡️ Error Handling**: Manages exceptions and edge cases

## 🚀 Extending & Customizing the Assistant

This project is just the beginning! Here are some awesome ways you could take it further:

### 📊 Advanced Project Management Features

- **📈 Metrics & Analytics**: Add sophisticated reporting on project progress
- **📅 Gantt Charts**: Implement timeline visualization for projects
- **⚡ Critical Path Analysis**: Identify the sequence of tasks that determine project duration
- **🧩 Resource Allocation**: Track and optimize how team members are assigned to tasks

### 🔌 Integration Possibilities

- **📆 Calendar Integration**: Connect with calendar APIs to set reminders for deadlines
- **📧 Email Notifications**: Send updates when tasks are assigned or deadlines approach
- **📎 File Attachments**: Allow documents to be associated with projects and tasks
- **🔄 External APIs**: Pull in data from other project management tools

### 💻 Technical Enhancements

- **🌐 Web Interface**: Create a browser-based UI instead of terminal interaction
- **👥 Multi-User Support**: Enhance to support concurrent users with access controls
- **🔍 Advanced Search**: Implement full-text search across all project data
- **📤 Data Export**: Add capabilities to export reports in various formats

## Understanding Persistent Storage in ADK

This project demonstrates a key ADK concept: **persistent storage** using the `DatabaseSessionService`. Here's how it works:

### Database Session Service

```python
from google.adk.sessions import DatabaseSessionService

# Initialize with an SQLite database
db_url = "sqlite:///./project_management_data.db"
session_service = DatabaseSessionService(db_url=db_url)
```

The `DatabaseSessionService` connects to a database where all conversation and state information is stored. This is what allows the agent to "remember" information between different sessions.

### Session Management Process

```python
# Check for existing sessions for this user
existing_sessions = session_service.list_sessions(
    app_name=APP_NAME,
    user_id=USER_ID,
)

# If there's an existing session, use it, otherwise create a new one
if existing_sessions and len(existing_sessions.sessions) > 0:
    # Use the most recent session
    SESSION_ID = existing_sessions.sessions[0].id
    print(f"Continuing existing session: {SESSION_ID}")
else:
    # Create a new session with initial state
    new_session = session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state,
    )
    SESSION_ID = new_session.id
    print(f"Created new session: {SESSION_ID}")
```

This code demonstrates how the application finds existing sessions for a user or creates a new one if needed.

### State Updates with Tool Context

```python
def add_project(name: str, tool_context: ToolContext, description: Optional[str] = None, 
                due_date: Optional[str] = None) -> dict:
    # Handle default values inside the function
    if description is None:
        description = "No description provided"
    if due_date is None:
        due_date = "2025-12-31"
        
    # Get current projects from state
    projects = tool_context.state.get("projects", [])
    
    # Add the new project
    projects.append({
        "name": name,
        "description": description,
        "due_date": due_date,
        "tasks": [],
        "created_at": datetime.now().strftime("%Y-%m-%d")
    })
    
    # Update state with the new list of projects
    tool_context.state["projects"] = projects
    
    return {
        "action": "add_project",
        "project": name,
        "message": f"Added project: {name} with due date {due_date}"
    }
```

This example shows how tools update the state through `tool_context.state`. Any changes made to the state are automatically saved to the database.

### Production Database Options

For production use, you might want to switch to a more robust database like PostgreSQL:

```python
# Example of using PostgreSQL instead of SQLite
db_url = "postgresql://username:password@localhost:5432/project_management"
session_service = DatabaseSessionService(db_url=db_url)
```

The same code can work with different database backends by simply changing the connection string.

## Learning More About ADK

To learn more about Agent Development Kit concepts, explore these resources:

- [Google ADK Documentation](https://github.com/google/adk-docs) - Official documentation for the ADK
- [ADK Sessions Documentation](https://google.github.io/adk-docs/sessions/session/) - Details on session management
- [ADK Tools Documentation](https://google.github.io/adk-docs/agents/tools/) - Learn more about creating tools
- [ADK GitHub Repository](https://github.com/google/adk) - Source code and examples

Happy building with ADK!
