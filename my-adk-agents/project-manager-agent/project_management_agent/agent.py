from google.adk.agents import Agent
from google.adk.tools.tool_context import ToolContext
from datetime import datetime
from typing import Optional


# ===== PROJECT MANAGEMENT TOOLS =====

def add_project(name: str, tool_context: ToolContext, description: Optional[str] = None, due_date: Optional[str] = None) -> dict:
    """Add a new project to the project list.

    Args:
        name: The name of the project
        tool_context: Context for accessing and updating session state
        description: A description of the project (optional)
        due_date: The due date for the project (YYYY-MM-DD) (optional)

    Returns:
        A confirmation message
    """
    print(f"--- Tool: add_project called for '{name}' ---")

    # Handle default values inside the function
    if description is None:
        description = "No description provided"
    if due_date is None:
        due_date = "2025-12-31"

    # Validate date format (YYYY-MM-DD)
    try:
        if due_date:
            datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        return {
            "action": "add_project",
            "status": "error",
            "message": f"Invalid date format: {due_date}. Please use YYYY-MM-DD format."
        }

    # Get current projects from state
    projects = tool_context.state.get("projects", [])

    # Create a new project
    new_project = {
        "name": name,
        "description": description,
        "due_date": due_date,
        "tasks": [],
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

    # Add the new project
    projects.append(new_project)

    # Update state with the new list of projects
    tool_context.state["projects"] = projects

    return {
        "action": "add_project",
        "project": name,
        "message": f"Added project: {name} with due date {due_date}"
    }


def view_projects(tool_context: ToolContext) -> dict:
    """View all current projects.

    Args:
        tool_context: Context for accessing session state

    Returns:
        The list of projects
    """
    print("--- Tool: view_projects called ---")

    # Get projects from state
    projects = tool_context.state.get("projects", [])

    return {
        "action": "view_projects",
        "projects": projects,
        "count": len(projects)
    }


def update_project(index: int, tool_context: ToolContext, name: Optional[str] = None, description: Optional[str] = None, due_date: Optional[str] = None) -> dict:
    """Update an existing project.

    Args:
        index: The 1-based index of the project to update
        tool_context: Context for accessing and updating session state
        name: The new name for the project (optional)
        description: The new description for the project (optional)
        due_date: The new due date for the project (optional)

    Returns:
        A confirmation message
    """
    print(f"--- Tool: update_project called for index {index} ---")

    # Get current projects from state
    projects = tool_context.state.get("projects", [])

    # Check if the index is valid
    if not projects or index < 1 or index > len(projects):
        return {
            "action": "update_project",
            "status": "error",
            "message": f"Could not find project at position {index}. Currently there are {len(projects)} projects."
        }

    # Get the project to update (adjusting for 0-based indices)
    project = projects[index - 1]
    old_project = project.copy()    # Update the project fields if provided
    if name:
        project["name"] = name
    if description:
        project["description"] = description
    if due_date:
        # Validate date format
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            project["due_date"] = due_date
        except ValueError:
            return {
                "action": "update_project",
                "status": "error",
                "message": f"Invalid date format: {due_date}. Please use YYYY-MM-DD format."
            }

    # Update state with the modified list
    tool_context.state["projects"] = projects

    return {
        "action": "update_project",
        "index": index,
        "old_project": old_project,
        "updated_project": project,
        "message": f"Updated project {index}: '{project['name']}'"
    }


def delete_project(index: int, tool_context: ToolContext) -> dict:
    """Delete a project.

    Args:
        index: The 1-based index of the project to delete
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(f"--- Tool: delete_project called for index {index} ---")

    # Get current projects from state
    projects = tool_context.state.get("projects", [])

    # Check if the index is valid
    if not projects or index < 1 or index > len(projects):
        return {
            "action": "delete_project",
            "status": "error",
            "message": f"Could not find project at position {index}. Currently there are {len(projects)} projects."
        }

    # Remove the project (adjusting for 0-based indices)
    deleted_project = projects.pop(index - 1)

    # Update state with the modified list
    tool_context.state["projects"] = projects

    return {
        "action": "delete_project",
        "index": index,
        "deleted_project": deleted_project,
        "message": f"Deleted project {index}: '{deleted_project['name']}'"
    }


# ===== TASK MANAGEMENT TOOLS =====

def add_task(project_index: int, tool_context: ToolContext, name: Optional[str] = None,
             assigned_to: Optional[str] = None, due_date: Optional[str] = None,
             status: Optional[str] = None) -> dict:
    """Add a new task to a project.

    Args:
        project_index: The 1-based index of the project to add the task to
        tool_context: Context for accessing and updating session state
        name: The name of the task (optional)
        assigned_to: The team member assigned to the task (optional)
        due_date: The due date for the task (YYYY-MM-DD) (optional)
        status: The status of the task (e.g., "not started", "in progress", "completed") (optional)

    Returns:
        A confirmation message
    """
    print(
        f"--- Tool: add_task called for project {project_index}, task '{name}' ---")

    # Handle default values inside the function
    if name is None:
        name = "New Task"
    if assigned_to is None:
        assigned_to = "Unassigned"
    if due_date is None:
        due_date = "2025-12-31"
    if status is None:
        status = "not started"

    # Validate date format
    try:
        if due_date:
            datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        return {
            "action": "add_task",
            "status": "error",
            "message": f"Invalid date format: {due_date}. Please use YYYY-MM-DD format."
        }

    # Validate status
    valid_statuses = ["not started", "in progress", "completed"]
    if status.lower() not in valid_statuses:
        return {
            "action": "add_task",
            "status": "error",
            "message": f"Invalid status: {status}. Please use one of: {', '.join(valid_statuses)}."
        }

    # Get current projects from state
    projects = tool_context.state.get("projects", [])

    # Check if the project index is valid
    if not projects or project_index < 1 or project_index > len(projects):
        return {
            "action": "add_task",
            "status": "error",
            "message": f"Could not find project at position {project_index}. Currently there are {len(projects)} projects."
        }

    # Create a new task
    new_task = {
        "name": name,
        "assigned_to": assigned_to,
        "due_date": due_date,
        "status": status,
        "created_at": datetime.now().strftime("%Y-%m-%d")
    }

    # Add the task to the project
    project = projects[project_index - 1]
    project["tasks"].append(new_task)

    # Update state with the modified project list
    tool_context.state["projects"] = projects

    return {
        "action": "add_task",
        "project": project["name"],
        "task": name,
        "message": f"Added task '{name}' to project '{project['name']}', assigned to {assigned_to}"
    }


def update_task(project_index: int, task_index: int, tool_context: ToolContext,
                name: Optional[str] = None, assigned_to: Optional[str] = None,
                due_date: Optional[str] = None, status: Optional[str] = None) -> dict:
    """Update an existing task.

    Args:
        project_index: The 1-based index of the project
        task_index: The 1-based index of the task within the project
        tool_context: Context for accessing and updating session state
        name: The new name for the task (optional)
        assigned_to: The new team member assigned to the task (optional)
        due_date: The new due date for the task (optional)
        status: The new status of the task (optional)

    Returns:
        A confirmation message
    """
    print(
        f"--- Tool: update_task called for project {project_index}, task {task_index} ---")

    # Get current projects from state
    projects = tool_context.state.get("projects", [])

    # Check if the project index is valid
    if not projects or project_index < 1 or project_index > len(projects):
        return {
            "action": "update_task",
            "status": "error",
            "message": f"Could not find project at position {project_index}. Currently there are {len(projects)} projects."
        }

    # Get the project and check if the task index is valid
    project = projects[project_index - 1]
    tasks = project.get("tasks", [])

    if not tasks or task_index < 1 or task_index > len(tasks):
        return {
            "action": "update_task",
            "status": "error",
            "message": f"Could not find task at position {task_index} in project '{project['name']}'. Currently there are {len(tasks)} tasks."
        }

    # Get the task to update
    task = tasks[task_index - 1]
    old_task = task.copy()    # Update the task fields if provided
    if name:
        task["name"] = name
    if assigned_to:
        task["assigned_to"] = assigned_to
    if due_date:
        # Validate date format
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            task["due_date"] = due_date
        except ValueError:
            return {
                "action": "update_task",
                "status": "error",
                "message": f"Invalid date format: {due_date}. Please use YYYY-MM-DD format."
            }
    if status:
        # Validate status
        valid_statuses = ["not started", "in progress", "completed"]
        if status.lower() not in valid_statuses:
            return {
                "action": "update_task",
                "status": "error",
                "message": f"Invalid status: {status}. Please use one of: {', '.join(valid_statuses)}."
            }
        task["status"] = status

    # Update state with the modified project list
    tool_context.state["projects"] = projects

    return {
        "action": "update_task",
        "project": project["name"],
        "task": task["name"],
        "old_task": old_task,
        "updated_task": task,
        "message": f"Updated task '{task['name']}' in project '{project['name']}'"
    }


def delete_task(project_index: int, task_index: int, tool_context: ToolContext) -> dict:
    """Delete a task from a project.

    Args:
        project_index: The 1-based index of the project
        task_index: The 1-based index of the task within the project
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(
        f"--- Tool: delete_task called for project {project_index}, task {task_index} ---")

    # Get current projects from state
    projects = tool_context.state.get("projects", [])

    # Check if the project index is valid
    if not projects or project_index < 1 or project_index > len(projects):
        return {
            "action": "delete_task",
            "status": "error",
            "message": f"Could not find project at position {project_index}. Currently there are {len(projects)} projects."
        }

    # Get the project and check if the task index is valid
    project = projects[project_index - 1]
    tasks = project.get("tasks", [])

    if not tasks or task_index < 1 or task_index > len(tasks):
        return {
            "action": "delete_task",
            "status": "error",
            "message": f"Could not find task at position {task_index} in project '{project['name']}'. Currently there are {len(tasks)} tasks."
        }

    # Remove the task
    deleted_task = tasks.pop(task_index - 1)

    # Update state with the modified project list
    tool_context.state["projects"] = projects

    return {
        "action": "delete_task",
        "project": project["name"],
        "deleted_task": deleted_task,
        "message": f"Deleted task '{deleted_task['name']}' from project '{project['name']}'"
    }


# ===== TEAM MEMBER MANAGEMENT TOOLS =====

def add_team_member(name: str, role: str, email: str, tool_context: ToolContext) -> dict:
    """Add a new team member.

    Args:
        name: The name of the team member
        role: The role of the team member
        email: The email of the team member
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(f"--- Tool: add_team_member called for '{name}' ---")

    # Get current team members from state
    team_members = tool_context.state.get("team_members", [])

    # Create a new team member
    new_member = {
        "name": name,
        "role": role,
        "email": email
    }

    # Add the new team member
    team_members.append(new_member)

    # Update state with the new list of team members
    tool_context.state["team_members"] = team_members

    return {
        "action": "add_team_member",
        "member": name,
        "message": f"Added team member: {name} ({role})"
    }


def view_team_members(tool_context: ToolContext) -> dict:
    """View all current team members.

    Args:
        tool_context: Context for accessing session state

    Returns:
        The list of team members
    """
    print("--- Tool: view_team_members called ---")

    # Get team members from state
    team_members = tool_context.state.get("team_members", [])

    return {
        "action": "view_team_members",
        "team_members": team_members,
        "count": len(team_members)
    }


def update_team_member(index: int, tool_context: ToolContext, name: Optional[str] = None, role: Optional[str] = None, email: Optional[str] = None) -> dict:
    """Update an existing team member.

    Args:
        index: The 1-based index of the team member to update
        tool_context: Context for accessing and updating session state
        name: The new name for the team member (optional)
        role: The new role for the team member (optional)
        email: The new email for the team member (optional)

    Returns:
        A confirmation message
    """
    print(f"--- Tool: update_team_member called for index {index} ---")

    # Get current team members from state
    team_members = tool_context.state.get("team_members", [])

    # Check if the index is valid
    if not team_members or index < 1 or index > len(team_members):
        return {
            "action": "update_team_member",
            "status": "error",
            "message": f"Could not find team member at position {index}. Currently there are {len(team_members)} team members."
        }

    # Get the team member to update
    member = team_members[index - 1]
    old_member = member.copy()

    # Update the team member fields if provided
    if name:
        member["name"] = name
    if role:
        member["role"] = role
    if email:
        member["email"] = email

    # Update state with the modified list
    tool_context.state["team_members"] = team_members

    return {
        "action": "update_team_member",
        "index": index,
        "old_member": old_member,
        "updated_member": member,
        "message": f"Updated team member {index}: '{member['name']}' ({member['role']})"
    }


def delete_team_member(index: int, tool_context: ToolContext) -> dict:
    """Delete a team member.

    Args:
        index: The 1-based index of the team member to delete
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(f"--- Tool: delete_team_member called for index {index} ---")

    # Get current team members from state
    team_members = tool_context.state.get("team_members", [])

    # Check if the index is valid
    if not team_members or index < 1 or index > len(team_members):
        return {
            "action": "delete_team_member",
            "status": "error",
            "message": f"Could not find team member at position {index}. Currently there are {len(team_members)} team members."
        }

    # Remove the team member
    deleted_member = team_members.pop(index - 1)

    # Update state with the modified list
    tool_context.state["team_members"] = team_members

    return {
        "action": "delete_team_member",
        "index": index,
        "deleted_member": deleted_member,
        "message": f"Deleted team member {index}: '{deleted_member['name']}' ({deleted_member['role']})"
    }


def search_projects(query: str, tool_context: ToolContext) -> dict:
    """Search for projects by name or description.

    Args:
        query: The search query to match against project names or descriptions
        tool_context: Context for accessing session state

    Returns:
        Matching projects with their indices
    """
    print(f"--- Tool: search_projects called with query '{query}' ---")

    # Get projects from state
    projects = tool_context.state.get("projects", [])

    # Search for matches
    matches = []
    for idx, project in enumerate(projects, 1):
        if (query.lower() in project["name"].lower() or
                query.lower() in project["description"].lower()):
            matches.append({"index": idx, "project": project})

    return {
        "action": "search_projects",
        "query": query,
        "matches": matches,
        "count": len(matches),
        "message": f"Found {len(matches)} projects matching '{query}'"
    }


def update_user_name(name: str, tool_context: ToolContext) -> dict:
    """Update the user's name.

    Args:
        name: The new name for the user
        tool_context: Context for accessing and updating session state

    Returns:
        A confirmation message
    """
    print(f"--- Tool: update_user_name called with '{name}' ---")

    # Get current name from state
    old_name = tool_context.state.get("user_name", "")

    # Update the name in state
    tool_context.state["user_name"] = name

    return {
        "action": "update_user_name",
        "old_name": old_name,
        "new_name": name,
        "message": f"Updated your name to: {name}"
    }


def search_tasks(query: str, tool_context: ToolContext) -> dict:
    """Search for tasks by name across all projects.

    Args:
        query: The search query to match against task names
        tool_context: Context for accessing session state

    Returns:
        Matching tasks with their project and task indices
    """
    print(f"--- Tool: search_tasks called with query '{query}' ---")

    # Get projects from state
    projects = tool_context.state.get("projects", [])

    # Search for matching tasks across all projects
    matches = []
    for proj_idx, project in enumerate(projects, 1):
        for task_idx, task in enumerate(project.get("tasks", []), 1):
            if query.lower() in task["name"].lower():
                matches.append({
                    "project_index": proj_idx,
                    "project_name": project["name"],
                    "task_index": task_idx,
                    "task": task
                })

    return {
        "action": "search_tasks",
        "query": query,
        "matches": matches,
        "count": len(matches),
        "message": f"Found {len(matches)} tasks matching '{query}'",
        "tasks": matches
    }


def find_project_by_name(name: str, tool_context: ToolContext) -> dict:
    """Find a project by name.

    Args:
        name: The name of the project to find (case-insensitive partial match)
        tool_context: Context for accessing session state

    Returns:
        The found project and its index, or an error message
    """
    print(f"--- Tool: find_project_by_name called for '{name}' ---")

    # Get projects from state
    projects = tool_context.state.get("projects", [])

    # Search for matches (case-insensitive)
    matches = []
    for idx, project in enumerate(projects, 1):
        if name.lower() in project["name"].lower():
            matches.append({"index": idx, "project": project})

    if not matches:
        return {
            "action": "find_project_by_name",
            "status": "error",
            "query": name,
            "matches": [],
            "count": 0,
            "message": f"No projects found matching '{name}'"
        }
    elif len(matches) == 1:
        return {
            "action": "find_project_by_name",
            "status": "success",
            "query": name,
            "match": matches[0],
            "count": 1,
            "message": f"Found 1 project matching '{name}': '{matches[0]['project']['name']}' (index: {matches[0]['index']})"
        }
    else:
        return {
            "action": "find_project_by_name",
            "status": "multiple_matches",
            "query": name,
            "matches": matches,
            "count": len(matches),
            "message": f"Found {len(matches)} projects matching '{name}'"
        }


def find_tasks_by_status(status: str, project_index: Optional[int], tool_context: ToolContext) -> dict:
    """Find tasks by status, optionally within a specific project.

    Args:
        status: The status to filter by ("not started", "in progress", "completed")
        project_index: The 1-based index of the project to search in (optional)
        tool_context: Context for accessing session state

    Returns:
        The found task(s) and its/their index/indices, or an error message
    """
    print(f"--- Tool: find_tasks_by_status called for '{status}' ---")

    # Validate status
    status = status.lower()
    valid_statuses = ["not started", "in progress", "completed"]
    if status not in valid_statuses:
        return {
            "action": "find_tasks_by_status",
            "status": "error",
            "message": f"Invalid status: {status}. Please use one of: {', '.join(valid_statuses)}."
        }

    # Get projects from state
    projects = tool_context.state.get("projects", [])

    # Search for matches by status
    matches = []

    # If project_index is provided, only search in that project
    if project_index is not None:
        if not projects or project_index < 1 or project_index > len(projects):
            return {
                "action": "find_tasks_by_status",
                "status": "error",
                "message": f"Could not find project at position {project_index}. Currently there are {len(projects)} projects."
            }

        project = projects[project_index - 1]
        for task_idx, task in enumerate(project.get("tasks", []), 1):
            if task["status"].lower() == status:
                matches.append({
                    "project_index": project_index,
                    "project_name": project["name"],
                    "task_index": task_idx,
                    "task": task
                })
    else:
        # Search across all projects
        for proj_idx, project in enumerate(projects, 1):
            for task_idx, task in enumerate(project.get("tasks", []), 1):
                if task["status"].lower() == status:
                    matches.append({
                        "project_index": proj_idx,
                        "project_name": project["name"],
                        "task_index": task_idx,
                        "task": task
                    })

    project_scope = f"in project {project_index}" if project_index else "across all projects"

    if not matches:
        return {
            "action": "find_tasks_by_status",
            "status": "error",
            "query": status,
            "matches": [],
            "count": 0,
            "message": f"No tasks with status '{status}' found {project_scope}"
        }
    else:
        return {
            "action": "find_tasks_by_status",
            "status": "success",
            "query": status,
            "matches": matches,
            "count": len(matches),
            "message": f"Found {len(matches)} tasks with status '{status}' {project_scope}"
        }


def find_task_by_name(name: str, project_index: Optional[int], tool_context: ToolContext) -> dict:
    """Find a task by name, optionally within a specific project.

    Args:
        name: The name of the task to find (case-insensitive partial match)
        project_index: The 1-based index of the project to search in (optional)
        tool_context: Context for accessing session state

    Returns:
        The found task(s) and its/their index/indices, or an error message
    """
    print(f"--- Tool: find_task_by_name called for '{name}' ---")

    # Get projects from state
    projects = tool_context.state.get("projects", [])

    # Search for matches (case-insensitive)
    matches = []

    # If project_index is provided, only search in that project
    if project_index is not None:
        if not projects or project_index < 1 or project_index > len(projects):
            return {
                "action": "find_task_by_name",
                "status": "error",
                "query": name,
                "message": f"Could not find project at position {project_index}. Currently there are {len(projects)} projects."
            }

        project = projects[project_index - 1]
        for task_idx, task in enumerate(project.get("tasks", []), 1):
            if name.lower() in task["name"].lower():
                matches.append({
                    "project_index": project_index,
                    "project_name": project["name"],
                    "task_index": task_idx,
                    "task": task
                })
    else:
        # Search across all projects
        for proj_idx, project in enumerate(projects, 1):
            for task_idx, task in enumerate(project.get("tasks", []), 1):
                if name.lower() in task["name"].lower():
                    matches.append({
                        "project_index": proj_idx,
                        "project_name": project["name"],
                        "task_index": task_idx,
                        "task": task
                    })

    if not matches:
        project_scope = f"in project {project_index}" if project_index else "across all projects"
        return {
            "action": "find_task_by_name",
            "status": "error",
            "query": name,
            "matches": [],
            "count": 0,
            "message": f"No tasks found matching '{name}' {project_scope}"
        }
    else:
        project_scope = f"in project {project_index}" if project_index else "across all projects"
        return {
            "action": "find_task_by_name",
            "status": "success",
            "query": name,
            "matches": matches,
            "count": len(matches),
            "message": f"Found {len(matches)} tasks matching '{name}' {project_scope}"
        }


def get_project_status(project_index: int, tool_context: ToolContext) -> dict:
    """Get the status of a project, including task completion percentages.

    Args:
        project_index: The 1-based index of the project
        tool_context: Context for accessing session state

    Returns:
        Project status information
    """
    print(f"--- Tool: get_project_status called for index {project_index} ---")

    # Get current projects from state
    projects = tool_context.state.get("projects", [])

    # Check if the project index is valid
    if not projects or project_index < 1 or project_index > len(projects):
        return {
            "action": "get_project_status",
            "status": "error",
            "message": f"Could not find project at position {project_index}. Currently there are {len(projects)} projects."
        }

    # Get the project
    project = projects[project_index - 1]
    tasks = project.get("tasks", [])

    # Calculate completion status
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["status"] == "completed")
    completion_percentage = 0 if total_tasks == 0 else (
        completed_tasks / total_tasks) * 100

    # Organize tasks by status
    tasks_by_status = {
        "not started": [],
        "in progress": [],
        "completed": []
    }

    for task in tasks:
        status = task["status"].lower()
        if status in tasks_by_status:
            tasks_by_status[status].append(task)
        else:
            # Handle unknown status types
            if "not started" in tasks_by_status:
                tasks_by_status["not started"].append(task)

    # Calculate days to deadline
    try:
        due_date = datetime.strptime(project["due_date"], "%Y-%m-%d")
        today = datetime.now()
        days_remaining = (due_date - today).days
        deadline_status = "overdue" if days_remaining < 0 else f"{days_remaining} days remaining"
    except ValueError:
        deadline_status = "unknown"

    return {
        "action": "get_project_status",
        "project_name": project["name"],
        "due_date": project["due_date"],
        "deadline_status": deadline_status,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "completion_percentage": f"{completion_percentage:.1f}%",
        "tasks_by_status": tasks_by_status,
        "message": f"Project '{project['name']}' is {completion_percentage:.1f}% complete ({completed_tasks}/{total_tasks} tasks completed)"
    }


# Create the project management agent
project_management_agent = Agent(
    name="project_management_agent",
    model="gemini-2.0-flash-lite",
    description="A project management assistant with persistent memory for tracking projects, tasks, and team members",    
    instruction="""
    You are Dwight K. Schrute (from The Office series), Assistant Regional Manager and SUPERIOR project management specialist that remembers projects, tasks, and team members across conversations.
        
        The user's information is stored in state:
        - User's name: {user_name}
        - Projects: {projects}
        - Team Members: {team_members}
        
        You can help users manage their projects with the following capabilities:
        
        1. Project Management
        - Add new projects
        - View existing projects
        - Update projects
        - Delete projects
        - Get project status
        - Search for projects by name or description
        
        2. Task Management
        - Add tasks to projects
        - Update tasks
        - Delete tasks
        - Search for tasks across all projects
        
        3. Team Management
        - Add team members
        - View team members
        - Update team members
        - Delete team members
        
        Always be friendly and address the user by name. If you don't know their name yet,
        use the update_user_name tool to store it when they introduce themselves.
        
        **PROJECT MANAGEMENT GUIDELINES:**
        
        When dealing with projects and tasks:
        
        1. When the user asks to update or delete a project/task but doesn't provide an index:
        - First try to find the project or task by name using find_project_by_name or find_task_by_name
        - If they mention the name of the project or task, look through the list to find a match
        - If you find a match, use that index
        - If no match is found, list all projects/tasks and ask the user to specify
        
        2. When the user mentions a number or position:
        - Use that as the index (e.g., "delete project 2" means index=2)
        - Remember that indexing starts at 1 for the user
        
        3. For relative positions:
        - Handle "first", "last", "second", etc. appropriately
        - "First project" = index 1
        - "Last project" = the highest index
        
        4. For viewing:
        - Always use the view_projects or view_team_members tools when the user asks to see their information
        - Format the response in a numbered list for clarity
        - If there are no projects/members, suggest adding some
        
        5. For project status:
        - Use the get_project_status tool to provide detailed information about a project's progress
        - Include completion percentage and task breakdowns
        - Mention the deadline status (days remaining or if overdue)
        
        6. For task management:
        - Always specify both the project index and task index
        - When updating task status, use standardized statuses: "not started", "in progress", "completed"
        
        7. Due Dates:
        - Always use YYYY-MM-DD format for dates
        - Remind users of upcoming deadlines when they view projects
        - Warn users about overdue tasks or projects when relevant
        
        8. Search and Lookup Functionality:
        - Use search_projects tool when users want to find specific projects by name or description
        - Use search_tasks tool when users want to find specific tasks across all projects
        - Use find_project_by_name when you need to find a specific project by name
        - Use find_task_by_name when you need to find a specific task by name
        - Use find_tasks_by_status when users ask about tasks with a specific status
        - Present search results in a clear, numbered format
        - If no results are found, suggest alternative search terms or actions
        
        9. Error Handling:
        - Always validate user inputs before processing them
        - Provide clear, helpful error messages when things go wrong
        - Suggest corrections or alternatives when appropriate

        Remember to explain that you can remember their information across conversations like Dwight K. Schrute.

    """,    
    tools=[
        # Project management tools
        add_project,
        view_projects,
        update_project,
        delete_project,
        get_project_status,
        search_projects,
        find_project_by_name,

        # Task management tools
        add_task,
        update_task,
        delete_task,
        search_tasks,
        find_task_by_name,
        find_tasks_by_status,

        # Team management tools
        add_team_member,
        view_team_members,
        update_team_member,
        delete_team_member,

        # User tools
        update_user_name,
    ],
)
