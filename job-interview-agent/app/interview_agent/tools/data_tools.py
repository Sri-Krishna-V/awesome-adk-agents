"""
Data management and reporting tools for interview sessions.
"""

import json
from typing import Dict, Any, List, Optional
from pathlib import Path
from datetime import datetime, timedelta

from ..utils import load_session_data, save_session_data, calculate_interview_score


def generate_interview_report(session_id: str, include_full_transcript: bool = False) -> Dict[str, Any]:
    """
    Generate a comprehensive interview performance report.

    Args:
        session_id: Session identifier to generate report for
        include_full_transcript: Whether to include full question/answer transcript

    Returns:
        Dictionary with detailed interview report
    """
    try:
        # Load session data
        session_data = load_session_data(session_id)
        if not session_data:
            return {
                "status": "error",
                "message": "Session not found."
            }

        # Calculate performance metrics
        questions_asked = session_data.get("questions_asked", [])
        answers_given = session_data.get("answers_given", [])
        scores = session_data.get("scores", [])
        feedback_given = session_data.get("feedback_given", [])

        # Overall performance calculation
        overall_metrics = calculate_interview_score(scores)

        # Session summary
        start_time = datetime.fromisoformat(session_data.get("start_time", ""))
        session_summary = {
            "session_id": session_id,
            "interview_type": session_data.get("interview_type", ""),
            "role": session_data.get("role", ""),
            "company": session_data.get("company", ""),
            "difficulty_level": session_data.get("difficulty_level", ""),
            "focus_areas": session_data.get("focus_areas", []),
            "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "duration_planned": session_data.get("session_duration", 60),
            "questions_asked": len(questions_asked),
            "questions_answered": len(answers_given),
            "completion_rate": (len(answers_given) / len(questions_asked) * 100) if questions_asked else 0
        }

        # Performance analysis
        performance_analysis = {
            "overall_score": overall_metrics["overall_score"],
            "max_possible_score": overall_metrics["max_score"],
            "performance_level": _get_performance_level(overall_metrics["overall_score"]),
            "category_breakdown": overall_metrics["breakdown"],
            "total_questions": overall_metrics["total_questions"]
        }

        # Strengths and areas for improvement
        strengths = []
        areas_for_improvement = []

        if overall_metrics["breakdown"].get("content_quality", 0) >= 7:
            strengths.append("Strong content quality with relevant examples")
        elif overall_metrics["breakdown"].get("content_quality", 0) < 5:
            areas_for_improvement.append(
                "Need more relevant and detailed content in answers")

        if overall_metrics["breakdown"].get("structure_clarity", 0) >= 7:
            strengths.append("Well-structured and clear communication")
        elif overall_metrics["breakdown"].get("structure_clarity", 0) < 5:
            areas_for_improvement.append(
                "Improve answer structure and clarity")

        if overall_metrics["breakdown"].get("specificity", 0) >= 7:
            strengths.append("Good use of specific examples and details")
        elif overall_metrics["breakdown"].get("specificity", 0) < 5:
            areas_for_improvement.append(
                "Include more specific examples and metrics")

        # Recommendations based on performance
        recommendations = _generate_recommendations(
            overall_metrics, session_data.get("interview_type", ""))

        # Question-by-question breakdown
        question_breakdown = []
        for i, question in enumerate(questions_asked):
            answer = next((a for a in answers_given if a.get(
                "question_number") == question.get("question_number")), {})
            score = next((s for s in scores if s.get(
                "question_number") == question.get("question_number")), {})
            feedback = next((f for f in feedback_given if f.get(
                "question_number") == question.get("question_number")), {})

            breakdown_item = {
                "question_number": question.get("question_number", i + 1),
                "category": question.get("category", question.get("domain", "general")),
                "question_type": question.get("type", "behavioral"),
                "difficulty": question.get("difficulty", "medium"),
                "score": score.get("overall_score", 0) if score else 0,
                "has_answer": bool(answer),
                "has_feedback": bool(feedback)
            }

            if include_full_transcript:
                breakdown_item.update({
                    "question_text": question.get("question", ""),
                    "answer_text": answer.get("answer", ""),
                    "feedback_summary": {
                        "strengths": feedback.get("strengths", ""),
                        "improvements": feedback.get("areas_for_improvement", ""),
                        "suggestions": feedback.get("specific_suggestions", "")
                    }
                })

            question_breakdown.append(breakdown_item)

        # Create final report
        report = {
            "status": "success",
            "report_generated_at": datetime.now().isoformat(),
            "session_summary": session_summary,
            "performance_analysis": performance_analysis,
            "strengths_identified": strengths,
            "areas_for_improvement": areas_for_improvement,
            "recommendations": recommendations,
            "question_breakdown": question_breakdown
        }

        if include_full_transcript:
            report["full_transcript"] = True

        # Format report text
        report_text = f"""
# Interview Performance Report

## Session Overview
- **Session ID:** {session_id}
- **Interview Type:** {session_summary['interview_type'].title()}
- **Role:** {session_summary['role']}
- **Company:** {session_summary['company'] or 'Generic'}
- **Date:** {session_summary['start_time']}
- **Questions Asked:** {session_summary['questions_asked']}
- **Completion Rate:** {session_summary['completion_rate']:.1f}%

## Performance Summary
**Overall Score: {performance_analysis['overall_score']:.1f}/10** ({performance_analysis['performance_level']})

### Category Breakdown:
{chr(10).join([f"• {cat.replace('_', ' ').title()}: {score:.1f}/10" for cat, score in performance_analysis['category_breakdown'].items()])}

## Key Strengths
{chr(10).join([f"✅ {strength}" for strength in strengths]) if strengths else "• Areas of strength to be developed through practice"}

## Areas for Improvement  
{chr(10).join([f"🔄 {area}" for area in areas_for_improvement]) if areas_for_improvement else "• Continue building on current strong performance"}

## Recommendations
{chr(10).join([f"💡 {rec}" for rec in recommendations])}

---
*This report was generated automatically. For personalized coaching, consider booking a follow-up session.*
        """

        report["formatted_report"] = report_text

        return report

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error generating report: {str(e)}"
        }


def get_question_bank(
    question_type: str = "all",
    category: str = "all",
    difficulty: str = "all"
) -> Dict[str, Any]:
    """
    Retrieve questions from the question bank with optional filtering.

    Args:
        question_type: Type of questions (behavioral, technical, case_study, all)
        category: Question category (varies by type)
        difficulty: Difficulty level (easy, medium, hard, all)

    Returns:
        Dictionary with filtered question bank
    """
    try:
        # Load question bank
        data_dir = Path(__file__).parent.parent / "data"
        question_bank_path = data_dir / "question_bank.json"

        try:
            with open(question_bank_path, 'r') as f:
                question_bank = json.load(f)
        except FileNotFoundError:
            return {
                "status": "error",
                "message": "Question bank not found."
            }

        # Filter by question type
        if question_type == "all":
            filtered_bank = question_bank
        elif question_type in question_bank:
            filtered_bank = {question_type: question_bank[question_type]}
        else:
            return {
                "status": "error",
                "message": f"Question type '{question_type}' not found."
            }

        # Apply category and difficulty filters
        if category != "all" or difficulty != "all":
            final_bank = {}
            for q_type, categories in filtered_bank.items():
                final_bank[q_type] = {}

                for cat_name, questions in categories.items():
                    if category != "all" and cat_name != category:
                        continue

                    if difficulty != "all":
                        # Filter questions by difficulty
                        filtered_questions = []
                        for q in questions:
                            if isinstance(q, dict) and q.get("difficulty") == difficulty:
                                filtered_questions.append(q)
                            elif difficulty == "medium" and isinstance(q, dict) and "difficulty" not in q:
                                # Include questions without difficulty as medium
                                filtered_questions.append(q)

                        if filtered_questions:
                            final_bank[q_type][cat_name] = filtered_questions
                    else:
                        final_bank[q_type][cat_name] = questions

            filtered_bank = final_bank

        # Count questions
        total_questions = 0
        question_summary = {}

        for q_type, categories in filtered_bank.items():
            type_count = 0
            for cat_name, questions in categories.items():
                cat_count = len(questions) if isinstance(
                    questions, list) else 0
                type_count += cat_count
                question_summary[f"{q_type}_{cat_name}"] = cat_count

            question_summary[q_type] = type_count
            total_questions += type_count

        return {
            "status": "success",
            "message": f"Retrieved {total_questions} questions matching criteria",
            "filters_applied": {
                "question_type": question_type,
                "category": category,
                "difficulty": difficulty
            },
            "question_summary": question_summary,
            "question_bank": filtered_bank
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error retrieving question bank: {str(e)}"
        }


def save_interview_progress(
    session_id: str,
    notes: str = "",
    bookmark: str = "",
    custom_data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Save additional progress and notes for an interview session.

    Args:
        session_id: Session identifier
        notes: Additional notes about the session
        bookmark: Bookmark for resuming later
        custom_data: Any additional custom data

    Returns:
        Dictionary with save result
    """
    try:
        session_data = load_session_data(session_id)
        if not session_data:
            return {
                "status": "error",
                "message": "Session not found."
            }

        # Add progress data
        progress_data = {
            "saved_at": datetime.now().isoformat(),
            "notes": notes,
            "bookmark": bookmark,
            "custom_data": custom_data or {}
        }

        session_data.setdefault("progress_saves", []).append(progress_data)

        # Save session
        success = save_session_data(session_id, session_data)

        if success:
            return {
                "status": "success",
                "message": "Interview progress saved successfully.",
                "save_timestamp": progress_data["saved_at"],
                "total_saves": len(session_data["progress_saves"])
            }
        else:
            return {
                "status": "error",
                "message": "Failed to save progress data."
            }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error saving progress: {str(e)}"
        }


def load_interview_progress(session_id: str) -> Dict[str, Any]:
    """
    Load saved progress for an interview session.

    Args:
        session_id: Session identifier

    Returns:
        Dictionary with session progress data
    """
    try:
        session_data = load_session_data(session_id)
        if not session_data:
            return {
                "status": "error",
                "message": "Session not found."
            }

        # Get session progress summary
        progress_summary = {
            "session_id": session_id,
            "session_status": session_data.get("session_status", "unknown"),
            "interview_type": session_data.get("interview_type", ""),
            "role": session_data.get("role", ""),
            "start_time": session_data.get("start_time", ""),
            "questions_asked": len(session_data.get("questions_asked", [])),
            "answers_given": len(session_data.get("answers_given", [])),
            "current_question": session_data.get("current_question", 0),
            "scores_recorded": len(session_data.get("scores", [])),
            "feedback_given": len(session_data.get("feedback_given", [])),
            "progress_saves": session_data.get("progress_saves", [])
        }

        # Get latest bookmark if available
        latest_bookmark = ""
        if progress_summary["progress_saves"]:
            latest_save = progress_summary["progress_saves"][-1]
            latest_bookmark = latest_save.get("bookmark", "")

        return {
            "status": "success",
            "message": f"Loaded progress for session {session_id}",
            "progress_summary": progress_summary,
            "latest_bookmark": latest_bookmark,
            "can_resume": progress_summary["session_status"] == "active",
            "completion_percentage": (progress_summary["answers_given"] / max(progress_summary["questions_asked"], 1)) * 100
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error loading progress: {str(e)}"
        }


def _get_performance_level(score: float) -> str:
    """Get performance level description based on score."""
    if score >= 8.5:
        return "Outstanding"
    elif score >= 7.5:
        return "Strong"
    elif score >= 6.5:
        return "Good"
    elif score >= 5.5:
        return "Satisfactory"
    elif score >= 4.0:
        return "Needs Improvement"
    else:
        return "Requires Significant Work"


def _generate_recommendations(metrics: Dict[str, Any], interview_type: str) -> List[str]:
    """Generate personalized recommendations based on performance metrics."""
    recommendations = []
    overall_score = metrics.get("overall_score", 0)
    breakdown = metrics.get("breakdown", {})

    # General recommendations based on overall score
    if overall_score < 5:
        recommendations.append(
            "Consider booking additional practice sessions to build confidence")
        recommendations.append(
            "Review common interview questions and practice your responses using the STAR method")
    elif overall_score < 7:
        recommendations.append(
            "Focus on providing more specific examples with quantifiable results")
        recommendations.append(
            "Practice structuring your answers more clearly")
    else:
        recommendations.append(
            "Excellent performance! Consider practicing with harder questions to further improve")

    # Specific recommendations based on category scores
    if breakdown.get("content_quality", 0) < 6:
        recommendations.append(
            "Prepare more detailed examples that directly relate to the job requirements")

    if breakdown.get("structure_clarity", 0) < 6:
        recommendations.append(
            "Practice the STAR method (Situation, Task, Action, Result) for behavioral questions")

    if breakdown.get("specificity", 0) < 6:
        recommendations.append(
            "Include specific metrics, numbers, and concrete details in your examples")

    if breakdown.get("impact_results", 0) < 6:
        recommendations.append(
            "Focus on highlighting the measurable impact and results of your actions")

    if breakdown.get("self_awareness", 0) < 6:
        recommendations.append(
            "Practice reflecting on what you learned from each experience you share")

    # Interview type specific recommendations
    if interview_type == "technical":
        recommendations.append(
            "Continue practicing coding problems and explaining your thought process aloud")
        recommendations.append(
            "Review system design concepts and practice drawing architecture diagrams")
    elif interview_type == "behavioral":
        recommendations.append(
            "Develop a portfolio of 7-10 strong STAR examples covering different competencies")
    elif interview_type == "case_study":
        recommendations.append(
            "Practice business case frameworks and structured problem-solving approaches")

    return recommendations[:6]  # Limit to 6 recommendations
