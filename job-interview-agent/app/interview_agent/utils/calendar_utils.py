"""
Calendar utilities for interview scheduling, adapted from Jarvis calendar tools.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, Any, List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define scopes needed for Google Calendar
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Path for token storage
TOKEN_PATH = Path(os.path.expanduser("~/.credentials/interview_calendar_token.json"))
CREDENTIALS_PATH = Path("credentials.json")


def get_calendar_service():
    """
    Authenticate and create a Google Calendar service object.

    Returns:
        A Google Calendar service object or None if authentication fails
    """
    creds = None

    # Check if token exists and is valid
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_info(
            json.loads(TOKEN_PATH.read_text()), SCOPES
        )

    # If credentials don't exist or are invalid, refresh or get new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # If credentials.json doesn't exist, we can't proceed with OAuth flow
            if not CREDENTIALS_PATH.exists():
                print(
                    f"Error: {CREDENTIALS_PATH} not found. Please follow setup instructions."
                )
                return None

            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        TOKEN_PATH.parent.mkdir(exist_ok=True)
        TOKEN_PATH.write_text(creds.to_json())

    # Build and return the Calendar service
    try:
        service = build("calendar", "v3", credentials=creds)
        return service
    except Exception as e:
        print(f"Error building calendar service: {e}")
        return None


def parse_datetime(datetime_str: str) -> Optional[datetime]:
    """
    Parse datetime string in format "YYYY-MM-DD HH:MM".
    
    Args:
        datetime_str: String in format "YYYY-MM-DD HH:MM"
    
    Returns:
        Parsed datetime object or None if invalid
    """
    try:
        return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
    except ValueError:
        try:
            # Try without time (assume start of day)
            return datetime.strptime(datetime_str, "%Y-%m-%d")
        except ValueError:
            return None


def format_event_details(event: Dict[str, Any]) -> str:
    """Format calendar event details for display."""
    title = event.get("summary", "No title")
    start = event.get("start", {})
    end = event.get("end", {})
    
    # Handle different datetime formats
    start_time = start.get("dateTime", start.get("date", ""))
    end_time = end.get("dateTime", end.get("date", ""))
    
    if start_time and end_time:
        try:
            # Parse and format times
            start_dt = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
            end_dt = datetime.fromisoformat(end_time.replace("Z", "+00:00"))
            
            time_str = f"{start_dt.strftime('%Y-%m-%d %H:%M')} - {end_dt.strftime('%H:%M')}"
        except:
            time_str = f"{start_time} - {end_time}"
    else:
        time_str = "Time not specified"
    
    location = event.get("location", "")
    description = event.get("description", "")
    
    result = f"📅 {title}\n🕒 {time_str}"
    if location:
        result += f"\n📍 {location}"
    if description:
        result += f"\n📝 {description[:100]}{'...' if len(description) > 100 else ''}"
    
    return result


def create_interview_description(
    interview_type: str,
    role: str,
    company: str = "",
    focus_areas: List[str] = None,
    preparation_notes: str = ""
) -> str:
    """
    Create a comprehensive description for interview calendar events.
    
    Args:
        interview_type: Type of interview (behavioral, technical, etc.)
        role: Job role being interviewed for
        company: Company name (optional)
        focus_areas: List of specific focus areas
        preparation_notes: Additional preparation notes
    
    Returns:
        Formatted description string
    """
    description_parts = [
        f"🎯 Interview Type: {interview_type.title()}",
        f"💼 Role: {role}",
    ]
    
    if company:
        description_parts.append(f"🏢 Company: {company}")
    
    if focus_areas:
        description_parts.append(f"📋 Focus Areas: {', '.join(focus_areas)}")
    
    description_parts.extend([
        "",
        "📚 Preparation Tips:",
        "• Review the job description and company background",
        "• Prepare STAR method examples for behavioral questions",
        "• Practice technical concepts relevant to the role",
        "• Prepare thoughtful questions about the role and company",
        "",
        "🎭 This is a practice interview session with AI roleplay",
    ])
    
    if preparation_notes:
        description_parts.extend([
            "",
            "📝 Additional Notes:",
            preparation_notes
        ])
    
    return "\n".join(description_parts)


def find_free_time_slots(
    start_date: datetime,
    end_date: datetime,
    duration_minutes: int = 60,
    service=None
) -> List[Dict[str, str]]:
    """
    Find available time slots for interview scheduling.
    
    Args:
        start_date: Start of search period
        end_date: End of search period
        duration_minutes: Required duration in minutes
        service: Calendar service object
    
    Returns:
        List of available time slots
    """
    if not service:
        service = get_calendar_service()
        if not service:
            return []
    
    try:
        # Get busy times from calendar
        body = {
            "timeMin": start_date.isoformat() + "Z",
            "timeMax": end_date.isoformat() + "Z",
            "items": [{"id": "primary"}]
        }
        
        response = service.freebusy().query(body=body).execute()
        busy_times = response.get("calendars", {}).get("primary", {}).get("busy", [])
        
        # Generate potential time slots (9 AM to 6 PM, weekdays only)
        free_slots = []
        current = start_date.replace(hour=9, minute=0, second=0, microsecond=0)
        
        while current < end_date:
            # Skip weekends
            if current.weekday() >= 5:
                current += timedelta(days=1)
                current = current.replace(hour=9, minute=0, second=0, microsecond=0)
                continue
            
            # Skip outside business hours
            if current.hour < 9 or current.hour >= 18:
                if current.hour >= 18:
                    current += timedelta(days=1)
                    current = current.replace(hour=9, minute=0, second=0, microsecond=0)
                else:
                    current = current.replace(hour=9, minute=0, second=0, microsecond=0)
                continue
            
            slot_end = current + timedelta(minutes=duration_minutes)
            
            # Check if this slot conflicts with any busy time
            is_free = True
            for busy in busy_times:
                busy_start = datetime.fromisoformat(busy["start"].replace("Z", "+00:00"))
                busy_end = datetime.fromisoformat(busy["end"].replace("Z", "+00:00"))
                
                if (current < busy_end and slot_end > busy_start):
                    is_free = False
                    break
            
            if is_free:
                free_slots.append({
                    "start": current.strftime("%Y-%m-%d %H:%M"),
                    "end": slot_end.strftime("%Y-%m-%d %H:%M"),
                    "formatted": f"{current.strftime('%A, %B %d at %I:%M %p')} - {slot_end.strftime('%I:%M %p')}"
                })
            
            # Move to next 30-minute slot
            current += timedelta(minutes=30)
            
            # Limit to reasonable number of suggestions
            if len(free_slots) >= 10:
                break
        
        return free_slots
        
    except Exception as e:
        print(f"Error finding free time slots: {e}")
        return []
