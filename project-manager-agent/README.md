# Project Management Assistant with Persistent Storage

## Introduction

This example demonstrates a practical implementation of a Project Management Assistant built with Google's Agent Development Kit (ADK). This interactive agent helps users manage projects, tasks, and team members, with all data **persisting between sessions** - meaning your information is saved even when you close and restart the application.

### What is ADK?

The **Agent Development Kit (ADK)** is Google's toolkit for building AI agents powered by large language models (LLMs). ADK provides the infrastructure needed to:
- Create conversational agents with specialized capabilities
- Manage user interactions and conversations
- Store and retrieve information between sessions
- Organize complex functionality into modular tools

### What is Persistent Storage?

In the context of AI agents, **persistent storage** refers to the ability to save and retrieve information across multiple conversations and application restarts. This project uses ADK's `DatabaseSessionService` to store all your project management data in an SQLite database, ensuring nothing is lost when you exit the program.

## Quick Start

### 1. Environment Setup

If you haven't already, set up your Python environment:

```powershell
# Create virtual environment (if not already created in the parent directory)
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\Activate.ps1

# Install dependencies (from the main folder)
pip install -r ..\requirements.txt
```

### 2. API Key Configuration

Create a `.env` file in this directory with your Google API key:

```plaintext
GOOGLE_API_KEY=your_api_key_here
```

> **What is an API Key?** An API key is a unique identifier that authenticates requests to Google's AI services. It's required to access the Gemini models that power the agent.

### 3. Run the Application

```powershell
python main.py
```

That's it! You're now ready to interact with your Project Management Assistant.

## Learning Objectives

This project demonstrates several important concepts in AI agent development:

1. **Persistent Storage**: How to maintain information across sessions using database storage
2. **Tool-based Agents**: How to build specialized capabilities through well-defined tools
3. **State Management**: How to properly update and maintain user-specific information
4. **Session Handling**: How to manage ongoing conversations with users

## Features & Capabilities

### Project Management
- **Create Projects**: Add new projects with names, descriptions, and due dates
- **View Projects**: List all current projects and their details
- **Update Projects**: Modify project information as requirements change
- **Delete Projects**: Remove projects that are no longer needed
- **Status Tracking**: Monitor completion percentages and task distribution

> **Agent Tools Concept**: Each of these capabilities is implemented as a "tool" in ADK. Tools are specialized functions that the agent can call to perform specific actions, like retrieving or modifying data.

### Task Management
- **Add Tasks**: Create tasks within projects with specific requirements
- **Assign Team Members**: Connect tasks to specific people responsible for completion
- **Track Status**: Monitor if tasks are "not started," "in progress," or "completed"
- **Set Deadlines**: Manage timelines for individual task completion
- **Cross-Project Search**: Find tasks across all projects based on keywords

### Team Member Management
- **Add Team Members**: Record team member information including roles and contact details
- **Track Assignments**: See which team members are handling which tasks
- **Update Information**: Modify team member details as needed
- **Role Management**: Organize team members by their roles and responsibilities

### Persistent Storage System
- **Database Backend**: All information is stored in a SQLite database file
- **Session Persistence**: Your data remains available between different conversations
- **State Management**: Changes to projects, tasks, and team members are automatically saved
- **Extensible Storage**: Can be easily adapted to use other database systems

## Example Interactions & Commands

Here are some example interactions to try with the assistant. These demonstrate how to use natural language to control the agent's capabilities:

```plaintext
# User identity
"My name is John"

# Basic Project Management
"Create a new project called Website Redesign due on 2025-08-15"
"Show me all my projects"
"What's the status of the Website Redesign project?"
"Update the Website Redesign project deadline to 2025-09-30"
"Rename the project Website Redesign to Corporate Website Redesign"
"Delete the Website Redesign project"

# Team Management
"Add John to the team as a Developer, email: john@example.com"
"Add Mary to the team as a Designer, email: mary@example.com" 
"Show me all team members"
"Update Mary's role to Lead Designer"
"Remove Mary from the team"
"Remind me who's working on that project"

# Task Management
"Add a task to Website Redesign: Create homepage wireframes due 2025-06-01, assigned to Mary"
"Add another task to Website Redesign: Develop homepage layout due 2025-06-10, assigned to John"
"Update the task Develop homepage layout to in progress"
"Change the due date of Develop homepage layout to 2025-06-12"
"Mark the task Create homepage wireframes in Website Redesign as completed"
"Delete the task Test layout responsiveness from Corporate Website Redesign"

# Advanced Queries
"What tasks are still in progress for Website Redesign?"
"Show me all completed tasks in Corporate Website Redesign"
"List all tasks assigned to John"
"What are the upcoming due dates in my projects?"
"Do I still have the project Corporate Website Redesign saved?"

# Multi-Project Management
"Create a new project: Mobile App Release due 2025-12-01"
"Add a task: Design app icon to Mobile App Release due 2025-09-01, assigned to John"
"What are all my current projects?"
"Show project details for Mobile App Release"
```

> **Natural Language Understanding**: The agent is designed to understand natural language instructions, not just specific commands. You can phrase your requests in different ways, and the agent will attempt to understand your intent.

> **Continuous Memory**: Try running through the sequence of commands above in order. You'll see how the agent remembers everything you've told it previously, making for a natural conversation flow.

## Project Architecture & Structure

This application uses the ADK's `DatabaseSessionService` to maintain state between sessions. Let's explore how it's structured:

```
13-proj-management-asstnt/
├── main.py                      # Sets up the session and conversation loop
├── project_management_data.db   # SQLite database (created on first run)
├── utils.py                     # Utility functions for conversation management
└── project_management_agent/    # Agent code directory
    ├── __init__.py              # Package initialization
    └── agent.py                 # Defines the agent and all its tools
```

### Key Components Explained

#### 1. Main Application (`main.py`)
This file serves as the entry point and handles:
- **Database Connection**: Initializes the SQLite database connection
- **Session Management**: Finds existing sessions or creates new ones
- **Conversation Loop**: Manages the back-and-forth interaction with the user
- **State Persistence**: Ensures all data is saved properly

#### 2. Agent Definition (`agent.py`)
This file defines:
- **Agent Configuration**: Sets up the language model and instructions
- **Tool Functions**: Implements all the specialized capabilities
- **State Updates**: Handles how data is stored and retrieved

#### 3. Database File (`project_management_data.db`)
This SQLite file:
- **Stores All Data**: Contains tables for sessions and state information
- **Persists Between Runs**: Maintains information even when the application is closed
- **Manages Multiple Users**: Can store data for different users separately

#### 4. Utilities (`utils.py`)
This file provides:
- **Display Functions**: Formats data for terminal output
- **Helper Methods**: Simplifies common operations
- **Error Handling**: Manages exceptions and edge cases

## Extending & Customizing the Assistant

This project provides a foundation that can be extended in several ways to add more capabilities:

### Advanced Project Management Features
- **Metrics & Analytics**: Add more sophisticated reporting on project progress
- **Gantt Charts**: Implement timeline visualization for projects
- **Critical Path Analysis**: Identify the sequence of tasks that determine project duration
- **Resource Allocation**: Track and optimize how team members are assigned to tasks

### Integration Possibilities
- **Calendar Integration**: Connect with calendar APIs to set reminders for deadlines
- **Email Notifications**: Send updates when tasks are assigned or deadlines approach
- **File Attachments**: Allow documents to be associated with projects and tasks
- **External APIs**: Pull in data from other project management tools

### Technical Enhancements
- **Web Interface**: Create a browser-based UI instead of terminal interaction
- **Multi-User Support**: Enhance to support concurrent users with access controls
- **Advanced Search**: Implement full-text search across all project data
- **Data Export**: Add capabilities to export reports in various formats

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
