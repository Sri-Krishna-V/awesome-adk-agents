"""
Utility functions for the Job Interview Roleplay Agent.
"""

import datetime
from typing import Dict, Any, List
import json
import os
from pathlib import Path


def get_current_time() -> str:
    """Get current date and time formatted for display."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S (%A)")


def format_interview_duration(minutes: int) -> str:
    """Format interview duration in human-readable format."""
    if minutes < 60:
        return f"{minutes} minutes"
    else:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        if remaining_minutes == 0:
            return f"{hours} hour{'s' if hours > 1 else ''}"
        else:
            return f"{hours} hour{'s' if hours > 1 else ''} {remaining_minutes} minutes"


def calculate_interview_score(answers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate interview performance score based on answers.
    
    Args:
        answers: List of answer dictionaries with scores and feedback
    
    Returns:
        Dictionary with overall score and breakdown
    """
    if not answers:
        return {
            "overall_score": 0,
            "breakdown": {},
            "total_questions": 0
        }
    
    scores = []
    categories = {
        "technical": [],
        "behavioral": [],
        "communication": [],
        "problem_solving": []
    }
    
    for answer in answers:
        if "score" in answer:
            scores.append(answer["score"])
            
            # Categorize the score
            question_type = answer.get("type", "general")
            if question_type in categories:
                categories[question_type].append(answer["score"])
    
    overall_score = sum(scores) / len(scores) if scores else 0
    
    breakdown = {}
    for category, category_scores in categories.items():
        if category_scores:
            breakdown[category] = sum(category_scores) / len(category_scores)
        else:
            breakdown[category] = 0
    
    return {
        "overall_score": round(overall_score, 1),
        "breakdown": breakdown,
        "total_questions": len(answers),
        "max_score": 10.0
    }


def save_session_data(session_id: str, data: Dict[str, Any]) -> bool:
    """
    Save interview session data to file.
    
    Args:
        session_id: Unique session identifier
        data: Session data to save
    
    Returns:
        True if successful, False otherwise
    """
    try:
        sessions_dir = Path("interview_sessions")
        sessions_dir.mkdir(exist_ok=True)
        
        file_path = sessions_dir / f"{session_id}.json"
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        return True
    except Exception as e:
        print(f"Error saving session data: {e}")
        return False


def load_session_data(session_id: str) -> Dict[str, Any]:
    """
    Load interview session data from file.
    
    Args:
        session_id: Unique session identifier
    
    Returns:
        Session data dictionary or empty dict if not found
    """
    try:
        sessions_dir = Path("interview_sessions")
        file_path = sessions_dir / f"{session_id}.json"
        
        if file_path.exists():
            with open(file_path, 'r') as f:
                return json.load(f)
        else:
            return {}
    except Exception as e:
        print(f"Error loading session data: {e}")
        return {}


def generate_session_id() -> str:
    """Generate a unique session ID."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"interview_{timestamp}"


def validate_email(email: str) -> bool:
    """Simple email validation."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def parse_datetime_string(date_str: str) -> datetime.datetime:
    """
    Parse various datetime string formats.
    
    Args:
        date_str: Date/time string in various formats
    
    Returns:
        Parsed datetime object
    """
    formats = [
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d %H:%M:%S", 
        "%m/%d/%Y %H:%M",
        "%d/%m/%Y %H:%M",
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d/%m/%Y"
    ]
    
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    raise ValueError(f"Unable to parse datetime string: {date_str}")
