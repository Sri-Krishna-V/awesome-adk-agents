"""
Calendar tools for interview scheduling and management.
"""

from typing import Dict, Any
from datetime import datetime, timedelta

from ..utils.calendar_utils import (
    get_calendar_service,
    parse_datetime,
    create_interview_description,
    find_free_time_slots
)


def schedule_interview(
    interview_type: str,
    role: str,
    start_time: str,
    duration_minutes: int,
    company: str,
    focus_areas: str,
    preparation_notes: str,
    interviewer_email: str
) -> Dict[str, Any]:
    """
    Schedule a new interview session in Google Calendar.

    Args:
        interview_type: Type of interview (behavioral, technical, system_design, case_study, panel)
        role: Job role being interviewed for
        start_time: Start time in format "YYYY-MM-DD HH:MM"
        duration_minutes: Interview duration in minutes
        company: Company name
        focus_areas: Comma-separated focus areas
        preparation_notes: Additional preparation notes
        interviewer_email: Email to invite

    Returns:
        Dictionary with scheduling result and event details
    """
    try:
        # Handle default values
        if not duration_minutes:
            duration_minutes = 60
        if not company:
            company = ""
        if not focus_areas:
            focus_areas = ""
        if not preparation_notes:
            preparation_notes = ""
        if not interviewer_email:
            interviewer_email = ""

        # Get calendar service
        service = get_calendar_service()
        if not service:
            return {
                "status": "error",
                "message": "Failed to authenticate with Google Calendar. Please check credentials."
            }

        # Parse start time
        start_dt = parse_datetime(start_time)
        if not start_dt:
            return {
                "status": "error",
                "message": "Invalid start time format. Please use YYYY-MM-DD HH:MM format."
            }

        # Calculate end time
        end_dt = start_dt + timedelta(minutes=duration_minutes)

        # Get timezone from calendar settings
        timezone_id = "America/New_York"  # Default
        try:
            settings = service.settings().list().execute()
            for setting in settings.get("items", []):
                if setting.get("id") == "timezone":
                    timezone_id = setting.get("value")
                    break
        except Exception:
            pass

        # Parse focus areas
        focus_list = [area.strip()
                      for area in focus_areas.split(",")] if focus_areas else []

        # Create event summary
        summary = f"Mock {interview_type.title()} Interview - {role}"
        if company:
            summary += f" ({company})"

        # Create detailed description
        description = create_interview_description(
            interview_type=interview_type,
            role=role,
            company=company,
            focus_areas=focus_list,
            preparation_notes=preparation_notes
        )

        # Create event body
        event_body = {
            "summary": summary,
            "description": description,
            "start": {
                "dateTime": start_dt.isoformat(),
                "timeZone": timezone_id
            },
            "end": {
                "dateTime": end_dt.isoformat(),
                "timeZone": timezone_id
            },
            "location": "Virtual Interview Session",
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "email", "minutes": 24 * 60},  # 1 day before
                    {"method": "popup", "minutes": 30}       # 30 minutes before
                ]
            }
        }

        # Add attendee if email provided
        if interviewer_email:
            event_body["attendees"] = [{"email": interviewer_email}]

        # Create the event
        event = service.events().insert(calendarId="primary", body=event_body).execute()

        return {
            "status": "success",
            "message": f"Interview scheduled successfully for {start_dt.strftime('%A, %B %d at %I:%M %p')}",
            "event_id": event["id"],
            "event_link": event.get("htmlLink", ""),
            "details": {
                "type": interview_type,
                "role": role,
                "company": company,
                "start_time": start_dt.strftime("%Y-%m-%d %H:%M"),
                "duration": duration_minutes,
                "focus_areas": focus_list
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error scheduling interview: {str(e)}"
        }


def list_scheduled_interviews(
    start_date: str,
    days_ahead: int
) -> Dict[str, Any]:
    """
    List upcoming scheduled interview sessions.

    Args:
        start_date: Start date for search (YYYY-MM-DD format, empty string defaults to today)
        days_ahead: Number of days to look ahead

    Returns:
        Dictionary with list of scheduled interviews
    """
    try:
        # Handle default values
        if not start_date:
            start_date = ""
        if not days_ahead:
            days_ahead = 30
        service = get_calendar_service()
        if not service:
            return {
                "status": "error",
                "message": "Failed to authenticate with Google Calendar."
            }

        # Parse start date or use today
        if start_date:
            start_dt = parse_datetime(start_date)
            if not start_dt:
                return {
                    "status": "error",
                    "message": "Invalid date format. Please use YYYY-MM-DD format."
                }
        else:
            start_dt = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

        # Calculate end date
        end_dt = start_dt + timedelta(days=days_ahead)

        # Search for interview events
        events_result = service.events().list(
            calendarId="primary",
            timeMin=start_dt.isoformat() + "Z",
            timeMax=end_dt.isoformat() + "Z",
            singleEvents=True,
            orderBy="startTime",
            q="Mock Interview"
        ).execute()

        events = events_result.get("items", [])

        interviews = []
        for event in events:
            start = event.get("start", {})
            start_time = start.get("dateTime", start.get("date", ""))

            if start_time:
                try:
                    # Parse the start time
                    start_dt_parsed = datetime.fromisoformat(
                        start_time.replace("Z", "+00:00"))
                    formatted_time = start_dt_parsed.strftime(
                        "%A, %B %d at %I:%M %p")
                except:
                    formatted_time = start_time

                interviews.append({
                    "event_id": event["id"],
                    "title": event.get("summary", ""),
                    "start_time": formatted_time,
                    "raw_start": start_time,
                    "location": event.get("location", ""),
                    "description": event.get("description", "")[:200] + "..." if len(event.get("description", "")) > 200 else event.get("description", ""),
                    "event_link": event.get("htmlLink", "")
                })

        return {
            "status": "success",
            "message": f"Found {len(interviews)} scheduled interview(s)",
            "interviews": interviews,
            "search_period": f"{start_dt.strftime('%Y-%m-%d')} to {end_dt.strftime('%Y-%m-%d')}"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error listing interviews: {str(e)}"
        }


def cancel_interview(event_id: str, reason: str) -> Dict[str, Any]:
    """
    Cancel a scheduled interview session.

    Args:
        event_id: Calendar event ID to cancel
        reason: Reason for cancellation (can be empty string)

    Returns:
        Dictionary with cancellation result
    """
    try:
        # Handle default values
        if not reason:
            reason = ""
        service = get_calendar_service()
        if not service:
            return {
                "status": "error",
                "message": "Failed to authenticate with Google Calendar."
            }

        # Get event details first
        try:
            event = service.events().get(calendarId="primary", eventId=event_id).execute()
            event_title = event.get("summary", "Unknown Event")
            start_time = event.get("start", {}).get("dateTime", "Unknown Time")
        except:
            return {
                "status": "error",
                "message": "Event not found or access denied."
            }

        # Delete the event
        service.events().delete(calendarId="primary", eventId=event_id).execute()

        return {
            "status": "success",
            "message": f"Interview '{event_title}' has been cancelled successfully.",
            "cancelled_event": {
                "title": event_title,
                "start_time": start_time,
                "reason": reason if reason else "No reason provided"
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error cancelling interview: {str(e)}"
        }


def update_interview(
    event_id: str,
    new_start_time: str,
    new_duration: int,
    new_focus_areas: str,
    additional_notes: str
) -> Dict[str, Any]:
    """
    Update an existing interview session.

    Args:
        event_id: Calendar event ID to update
        new_start_time: New start time (YYYY-MM-DD HH:MM format, empty string if no change)
        new_duration: New duration in minutes (0 if no change)
        new_focus_areas: Updated focus areas (empty string if no change)
        additional_notes: Additional preparation notes (empty string if none)

    Returns:
        Dictionary with update result
    """
    try:
        # Handle default values
        if not new_start_time:
            new_start_time = ""
        if not new_duration:
            new_duration = 0
        if not new_focus_areas:
            new_focus_areas = ""
        if not additional_notes:
            additional_notes = ""
        service = get_calendar_service()
        if not service:
            return {
                "status": "error",
                "message": "Failed to authenticate with Google Calendar."
            }

        # Get existing event
        try:
            event = service.events().get(calendarId="primary", eventId=event_id).execute()
        except:
            return {
                "status": "error",
                "message": "Event not found or access denied."
            }

        # Update start time if provided
        if new_start_time:
            start_dt = parse_datetime(new_start_time)
            if not start_dt:
                return {
                    "status": "error",
                    "message": "Invalid start time format. Please use YYYY-MM-DD HH:MM format."
                }

            # Get timezone
            timezone_id = event.get("start", {}).get(
                "timeZone", "America/New_York")

            # Update duration if provided, otherwise keep existing
            if new_duration > 0:
                end_dt = start_dt + timedelta(minutes=new_duration)
            else:
                # Calculate existing duration
                existing_start = datetime.fromisoformat(
                    event["start"]["dateTime"].replace("Z", "+00:00"))
                existing_end = datetime.fromisoformat(
                    event["end"]["dateTime"].replace("Z", "+00:00"))
                existing_duration = existing_end - existing_start
                end_dt = start_dt + existing_duration

            event["start"] = {
                "dateTime": start_dt.isoformat(),
                "timeZone": timezone_id
            }
            event["end"] = {
                "dateTime": end_dt.isoformat(),
                "timeZone": timezone_id
            }

        # Update description if new focus areas or notes provided
        if new_focus_areas or additional_notes:
            current_description = event.get("description", "")

            if new_focus_areas:
                # Update focus areas in description
                focus_list = [area.strip()
                              for area in new_focus_areas.split(",")]
                focus_section = f"Focus Areas: {', '.join(focus_list)}"

                # Replace existing focus areas or add new section
                if "Focus Areas:" in current_description:
                    lines = current_description.split("\n")
                    for i, line in enumerate(lines):
                        if "Focus Areas:" in line:
                            lines[i] = focus_section
                            break
                    current_description = "\n".join(lines)
                else:
                    current_description += f"\n{focus_section}"

            if additional_notes:
                current_description += f"\n\n Updated Notes:\n{additional_notes}"

            event["description"] = current_description

        # Update the event
        updated_event = service.events().update(
            calendarId="primary",
            eventId=event_id,
            body=event
        ).execute()

        return {
            "status": "success",
            "message": "Interview updated successfully.",
            "updated_event": {
                "title": updated_event.get("summary", ""),
                "start_time": updated_event.get("start", {}).get("dateTime", ""),
                "end_time": updated_event.get("end", {}).get("dateTime", ""),
                "event_link": updated_event.get("htmlLink", "")
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error updating interview: {str(e)}"
        }


def suggest_interview_times(
    duration_minutes: int,
    days_ahead: int,
    preferred_times: str
) -> Dict[str, Any]:
    """
    Suggest available time slots for interview scheduling.

    Args:
        duration_minutes: Required interview duration
        days_ahead: Number of days to look ahead
        preferred_times: Time preference ("business_hours", "morning", "afternoon", "evening")

    Returns:
        Dictionary with suggested time slots
    """
    try:
        # Handle default values
        if not duration_minutes:
            duration_minutes = 60
        if not days_ahead:
            days_ahead = 14
        if not preferred_times:
            preferred_times = "business_hours"
        # Calculate search period
        start_date = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
        end_date = start_date + timedelta(days=days_ahead)

        # Find free time slots
        service = get_calendar_service()
        free_slots = find_free_time_slots(
            start_date=start_date,
            end_date=end_date,
            duration_minutes=duration_minutes,
            service=service
        )

        # Filter by preferred times if specified
        if preferred_times != "business_hours":
            filtered_slots = []
            for slot in free_slots:
                slot_time = datetime.strptime(slot["start"], "%Y-%m-%d %H:%M")
                hour = slot_time.hour

                if preferred_times == "morning" and 9 <= hour < 12:
                    filtered_slots.append(slot)
                elif preferred_times == "afternoon" and 12 <= hour < 17:
                    filtered_slots.append(slot)
                elif preferred_times == "evening" and 17 <= hour < 20:
                    filtered_slots.append(slot)

            free_slots = filtered_slots

        return {
            "status": "success",
            "message": f"Found {len(free_slots)} available time slots",
            "suggested_times": free_slots[:8],  # Limit to 8 suggestions
            "search_criteria": {
                "duration": duration_minutes,
                "days_ahead": days_ahead,
                "preferred_times": preferred_times
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error finding available times: {str(e)}"
        }
