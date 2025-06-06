"""
Interview session management tools for conducting mock interviews.
"""

import json
import random
from typing import Dict, Any, Optional
from pathlib import Path
from datetime import datetime

from ..utils import generate_session_id, save_session_data, load_session_data


def start_interview_session(
    interview_type: str,
    role: str,
    difficulty_level: str,
    company: str,
    focus_areas: str,
    session_duration: int
) -> Dict[str, Any]:
    """
    Start a new interview session with specified parameters.

    Args:
        interview_type: Type of interview (behavioral, technical, system_design, case_study)
        role: Job role being interviewed for
        difficulty_level: Difficulty level (easy, medium, hard)
        company: Company name (optional)
        focus_areas: Comma-separated focus areas (optional)
        session_duration: Session duration in minutes

    Returns:
        Dictionary with session details and first interaction
    """
    try:
        # Handle default values
        if not difficulty_level:
            difficulty_level = "medium"
        if not company:
            company = ""
        if not focus_areas:
            focus_areas = ""
        if not session_duration:
            session_duration = 60

        # Generate unique session ID
        session_id = generate_session_id()

        # Parse focus areas
        focus_list = [area.strip()
                      for area in focus_areas.split(",")] if focus_areas else []

        # Initialize session data
        session_data = {
            "session_id": session_id,
            "interview_type": interview_type,
            "role": role,
            "difficulty_level": difficulty_level,
            "company": company,
            "focus_areas": focus_list,
            "session_duration": session_duration,
            "start_time": datetime.now().isoformat(),
            "current_question": 0,
            "questions_asked": [],
            "answers_given": [],
            "scores": [],
            "feedback_given": [],
            "session_status": "active"
        }

        # Save session data
        save_success = save_session_data(session_id, session_data)
        if not save_success:
            return {
                "status": "error",
                "message": "Failed to save session data."
            }

        # Create opening message based on interview type
        opening_messages = {
            "behavioral": f"""
🎭 **Behavioral Interview Session Started**

Hello! I'm your interviewer today. I'll be conducting a behavioral interview focusing on your past experiences and how you've handled various work situations.

**Session Details:**
- Role: {role}
- Company: {company if company else "Generic"}
- Duration: {session_duration} minutes
- Focus Areas: {', '.join(focus_list) if focus_list else 'General behavioral competencies'}

**Format:** I'll ask you behavioral questions using the STAR method (Situation, Task, Action, Result). Please provide specific examples from your experience.

Let's begin! Please take a moment to get comfortable, and let me know when you're ready for the first question.
            """,

            "technical": f"""
💻 **Technical Interview Session Started**

Welcome! I'll be your technical interviewer today. This session will assess your technical knowledge, problem-solving skills, and coding abilities.

**Session Details:**
- Role: {role}
- Company: {company if company else "Generic"}
- Duration: {session_duration} minutes
- Difficulty: {difficulty_level.title()}
- Focus Areas: {', '.join(focus_list) if focus_list else 'General technical skills'}

**Format:** I'll present technical problems and questions. Please think out loud, ask clarifying questions, and explain your reasoning as you work through solutions.

Are you ready to begin? Let me know when you'd like the first technical challenge.
            """,

            "system_design": f"""
🏗️ **System Design Interview Session Started**

Hello! I'm here to conduct your system design interview. We'll work together to design a large-scale distributed system.

**Session Details:**
- Role: {role}
- Company: {company if company else "Generic"}
- Duration: {session_duration} minutes
- Focus Areas: {', '.join(focus_list) if focus_list else 'Scalable system architecture'}

**Format:** I'll present a system design problem. Please start with clarifying questions, then work through the design systematically. Think about scalability, reliability, and trade-offs.

Ready to design some systems? Let me know when you'd like to start.
            """,

            "case_study": f"""
📊 **Case Study Interview Session Started**

Greetings! I'll be leading your case study interview today. We'll work through business scenarios that test your analytical and strategic thinking.

**Session Details:**
- Role: {role}
- Company: {company if company else "Generic"}
- Duration: {session_duration} minutes
- Focus Areas: {', '.join(focus_list) if focus_list else 'Business analysis and strategy'}

**Format:** I'll present a business case or scenario. Please structure your approach, ask clarifying questions, and walk me through your analysis and recommendations.

Shall we dive into our first case study? Let me know when you're ready.
            """
        }

        opening_message = opening_messages.get(
            interview_type,
            "Welcome to your interview session! Let me know when you're ready to begin."
        )

        return {
            "status": "success",
            "message": opening_message,
            "session_details": {
                "session_id": session_id,
                "interview_type": interview_type,
                "role": role,
                "difficulty_level": difficulty_level,
                "company": company,
                "focus_areas": focus_list,
                "duration": session_duration
            },
            "next_action": "Wait for candidate confirmation to begin questioning"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error starting interview session: {str(e)}"
        }


def ask_behavioral_question(
    session_id: str,
    category: str,
    custom_question: str
) -> Dict[str, Any]:
    """
    Ask a behavioral interview question from the question bank.

    Args:
        session_id: Active session identifier
        category: Question category (leadership, teamwork, problem_solving, communication, adaptability, random)
        custom_question: Custom question to ask instead of bank question
          Returns:
        Dictionary with question details and follow-up information
    """
    try:
        # Handle default values
        if not category:
            category = "random"
        if not custom_question:
            custom_question = ""

        # Load session data
        session_data = load_session_data(session_id)
        if not session_data:
            return {
                "status": "error",
                "message": "Session not found. Please start a new interview session."
            }

        if session_data.get("session_status") != "active":
            return {
                "status": "error",
                "message": "Session is not active."
            }

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

        if custom_question:
            # Use custom question
            question_data = {
                "question": custom_question,
                "follow_ups": [
                    "Can you provide more details about the situation?",
                    "What was the outcome?",
                    "What would you do differently next time?"
                ],
                "key_points": ["Specific example", "Clear action taken", "Measurable result", "Learning/reflection"]
            }
            category_used = "custom"
        else:
            # Select from question bank
            behavioral_questions = question_bank.get(
                "behavioral_questions", {})

            if category == "random" or category not in behavioral_questions:
                # Pick random category
                available_categories = list(behavioral_questions.keys())
                if not available_categories:
                    return {
                        "status": "error",
                        "message": "No behavioral questions available in question bank."
                    }
                category_used = random.choice(available_categories)
            else:
                category_used = category

            # Get questions from selected category
            category_questions = behavioral_questions.get(category_used, [])
            if not category_questions:
                return {
                    "status": "error",
                    "message": f"No questions available for category: {category_used}"
                }

            # Select a question we haven't asked yet in this session
            asked_questions = {q.get("question", "")
                               for q in session_data.get("questions_asked", [])}
            available_questions = [
                q for q in category_questions if q["question"] not in asked_questions]

            if not available_questions:
                # If all questions in category have been asked, pick any from category
                available_questions = category_questions

            question_data = random.choice(available_questions)

        # Update session data
        question_number = len(session_data.get("questions_asked", [])) + 1
        question_entry = {
            "question_number": question_number,
            "category": category_used,
            "question": question_data["question"],
            "follow_ups": question_data.get("follow_ups", []),
            "key_points": question_data.get("key_points", []),
            "asked_at": datetime.now().isoformat()
        }

        session_data.setdefault("questions_asked", []).append(question_entry)
        session_data["current_question"] = question_number

        # Save updated session
        save_session_data(session_id, session_data)

        # Format the question presentation
        question_text = f"""
**Question {question_number} - {category_used.replace('_', ' ').title()}**

{question_data['question']}

*Please provide a specific example using the STAR method (Situation, Task, Action, Result). Take your time to think of a relevant experience.*

**Key areas to address:**
{chr(10).join([f"• {point}" for point in question_data.get('key_points', [])])}
        """

        return {
            "status": "success",
            "message": question_text,
            "question_details": question_entry,
            "session_progress": {
                "current_question": question_number,
                "total_questions_asked": len(session_data["questions_asked"])
            },
            "follow_up_questions": question_data.get("follow_ups", [])
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error asking behavioral question: {str(e)}"
        }


def ask_technical_question(
    session_id: str,
    domain: str,
    difficulty: str,
    custom_question: str
) -> Dict[str, Any]:
    """
    Ask a technical interview question based on domain and difficulty.

    Args:
        session_id: Active session identifier
        domain: Technical domain (software_engineering, data_science, product_management)
        difficulty: Difficulty level (easy, medium, hard)
        custom_question: Custom question to ask instead of bank question

    Returns:
        Dictionary with question details and evaluation criteria
    """
    try:
        # Handle default values
        if not domain:
            domain = "software_engineering"
        if not difficulty:
            difficulty = "medium"
        if not custom_question:
            custom_question = ""

        # Load session data
        # Load session data
        session_data = load_session_data(session_id)
        if not session_data:
            return {
                "status": "error",
                "message": "Session not found. Please start a new interview session."
            }

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

        if custom_question:
            # Use custom question
            question_data = {
                "question": custom_question,
                "difficulty": difficulty,
                "key_points": ["Technical accuracy", "Problem-solving approach", "Communication clarity"],
                "follow_ups": ["Can you explain your reasoning?", "Are there alternative approaches?", "What are the trade-offs?"]
            }
        else:
            # Get technical questions for domain
            technical_questions = question_bank.get("technical_questions", {})
            domain_questions = technical_questions.get(domain, [])

            if not domain_questions:
                return {
                    "status": "error",
                    "message": f"No technical questions available for domain: {domain}"
                }

            # Filter by difficulty if specified
            if difficulty != "medium":
                filtered_questions = [
                    q for q in domain_questions if q.get("difficulty") == difficulty]
                if filtered_questions:
                    domain_questions = filtered_questions

            # Select question not asked in this session
            asked_questions = {q.get("question", "")
                               for q in session_data.get("questions_asked", [])}
            available_questions = [
                q for q in domain_questions if q["question"] not in asked_questions]

            if not available_questions:
                available_questions = domain_questions

            question_data = random.choice(available_questions)

        # Update session data
        question_number = len(session_data.get("questions_asked", [])) + 1
        question_entry = {
            "question_number": question_number,
            "type": "technical",
            "domain": domain,
            "difficulty": question_data.get("difficulty", difficulty),
            "question": question_data["question"],
            "key_points": question_data.get("key_points", []),
            "follow_ups": question_data.get("follow_ups", []),
            "asked_at": datetime.now().isoformat()
        }

        session_data.setdefault("questions_asked", []).append(question_entry)
        session_data["current_question"] = question_number
        save_session_data(session_id, session_data)

        # Format technical question
        question_text = f"""


**Technical Question {question_number} - {domain.replace('_', ' ').title()}**
*Difficulty: {question_data.get('difficulty', difficulty).title()}*

{question_data['question']}

**Please think through this step by step and explain your reasoning out loud.**

**Evaluation criteria: **
{chr(10).join([f"• {point}" for point in question_data.get('key_points', [])])}

Take your time and feel free to ask clarifying questions.
        """

        return {
            "status": "success",
            "message": question_text,
            "question_details": question_entry,
            "session_progress": {
                "current_question": question_number,
                "total_questions_asked": len(session_data["questions_asked"])
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error asking technical question: {str(e)}"
        }


def provide_feedback(
    session_id: str,
    answer_text: str,
    strengths: Optional[str] = None,
    areas_for_improvement: Optional[str] = None,
    specific_suggestions: Optional[str] = None
) -> Dict[str, Any]:
    """
    Provide detailed feedback on the candidate's answer.

    Args:
        session_id: Active session identifier
        answer_text: The candidate's answer to evaluate
        strengths: Optional; What the candidate did well (default: None)
        areas_for_improvement: Optional; Areas that need work (default: None)
        specific_suggestions: Optional; Specific actionable suggestions (default: None)

    Returns:
        Dictionary with structured feedback
    """
    try:
        # Handle defaults for optional parameters
        strengths = strengths or ""
        areas_for_improvement = areas_for_improvement or ""
        specific_suggestions = specific_suggestions or ""

        # Load session data
        session_data = load_session_data(session_id)
        if not session_data:
            return {
                "status": "error",
                "message": "Session not found."
            }

        current_question = session_data.get("current_question", 0)
        if current_question == 0:
            return {
                "status": "error",
                "message": "No active question to provide feedback for."
            }

        # Get current question details for better context
        question_details = None
        for q in session_data.get("questions_asked", []):
            if q.get("question_number") == current_question:
                question_details = q
                break

        # Auto-generate feedback if not provided
        if not strengths and not areas_for_improvement:
            # Generate feedback based on question type if available
            question_type = question_details.get("type", "") if question_details else ""
            category = question_details.get("category", "") if question_details else ""
            
            feedback_text = f"""
**Feedback for Question {current_question}**

Thank you for your response. Here's my feedback:

**What went well:**
• You provided a specific example from your experience
• Your answer had a clear structure
• You demonstrated relevant skills for the role

**Areas for improvement:**
• Consider adding more quantifiable results or metrics
• Expand on the specific actions you took
• Reflect more on what you learned from the experience

**Suggestions for next time:**
• Use the STAR method more explicitly (Situation, Task, Action, Result)
• Prepare 2-3 variations of each story for different question angles
• Practice timing - aim for 2-3 minutes per response

Overall, this was a solid response that demonstrates relevant experience!
            """
        else:
            # Use provided feedback
            feedback_parts = [f"**Feedback for Question {current_question}**\n"]

            if strengths:
                feedback_parts.append(f"**What went well:**\n{strengths}\n")

            if areas_for_improvement:
                feedback_parts.append(
                    f"**Areas for improvement:**\n{areas_for_improvement}\n")

            if specific_suggestions:
                feedback_parts.append(
                    f"**Specific suggestions:**\n{specific_suggestions}\n")

            feedback_text = "\n".join(feedback_parts)

        # Store feedback in session
        feedback_entry = {
            "question_number": current_question,
            "answer_text": answer_text[:500] + "..." if len(answer_text) > 500 else answer_text,
            "strengths": strengths,
            "areas_for_improvement": areas_for_improvement,
            "specific_suggestions": specific_suggestions,
            "feedback_given_at": datetime.now().isoformat()
        }

        # Store answer with timestamp
        answer_entry = {
            "question_number": current_question,
            "answer": answer_text,
            "answered_at": datetime.now().isoformat()
        }

        session_data.setdefault("feedback_given", []).append(feedback_entry)
        session_data.setdefault("answers_given", []).append(answer_entry)

        save_session_data(session_id, session_data)

        return {
            "status": "success",
            "message": feedback_text,
            "feedback_summary": {
                "strengths_provided": bool(strengths),
                "improvements_provided": bool(areas_for_improvement),
                "suggestions_provided": bool(specific_suggestions)
            },
            "question_number": current_question,
            "next_steps": "Ready for next question or would you like to practice this question again?"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error providing feedback: {str(e)}"
        }


def evaluate_answer(
    session_id: str,
    answer_text: str,
    question_type: str = "behavioral"
) -> Dict[str, Any]:
    """
    Evaluate and score a candidate's answer using predefined criteria.

    Args:
        session_id: Active session identifier
        answer_text: The candidate's answer
        question_type: Type of question (behavioral, technical, case_study)

    Returns:
        Dictionary with evaluation scores and detailed assessment
    """
    try:
        # Load session data
        session_data = load_session_data(session_id)
        if not session_data:
            return {
                "status": "error",
                "message": "Session not found."
            }

        # Load feedback criteria
        data_dir = Path(__file__).parent.parent / "data"
        config_path = data_dir / "interview_config.json"

        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            criteria = config.get("feedback_criteria", {})
        except FileNotFoundError:
            # Use default criteria
            criteria = {
                "content_quality": {"weight": 0.3},
                "structure_clarity": {"weight": 0.25},
                "specificity": {"weight": 0.2},
                "impact_results": {"weight": 0.15},
                "self_awareness": {"weight": 0.1}
            }

        # Simple scoring algorithm (in real implementation, this could use ML)
        scores = {}

        # Content Quality (1-10)
        content_score = 5  # Base score
        if len(answer_text) > 100:
            content_score += 1
        if any(keyword in answer_text.lower() for keyword in ["result", "outcome", "achievement", "impact"]):
            content_score += 1
        if any(keyword in answer_text.lower() for keyword in ["challenge", "problem", "difficult", "complex"]):
            content_score += 1
        scores["content_quality"] = min(content_score, 10)

        # Structure & Clarity
        structure_score = 5
        if any(keyword in answer_text.lower() for keyword in ["situation", "task", "action", "result"]):
            structure_score += 2
        if len(answer_text.split('.')) > 3:  # Multiple sentences
            structure_score += 1
        scores["structure_clarity"] = min(structure_score, 10)

        # Specificity
        specificity_score = 5
        if any(char.isdigit() for char in answer_text):  # Contains numbers/metrics
            specificity_score += 2
        if len(answer_text.split()) > 50:  # Detailed response
            specificity_score += 1
        scores["specificity"] = min(specificity_score, 10)

        # Impact & Results
        impact_score = 4
        impact_keywords = ["increased", "decreased", "improved",
                           "saved", "revenue", "efficiency", "success"]
        if any(keyword in answer_text.lower() for keyword in impact_keywords):
            impact_score += 3
        scores["impact_results"] = min(impact_score, 10)

        # Self-awareness
        awareness_score = 5
        awareness_keywords = ["learned", "realize",
                              "mistake", "improve", "feedback", "next time"]
        if any(keyword in answer_text.lower() for keyword in awareness_keywords):
            awareness_score += 2
        scores["self_awareness"] = min(awareness_score, 10)

        # Calculate weighted overall score
        overall_score = sum(
            scores[criterion] * criteria[criterion]["weight"] for criterion in scores)

        # Store evaluation
        evaluation = {
            "question_number": session_data.get("current_question", 0),
            "answer_length": len(answer_text),
            "scores": scores,
            "overall_score": round(overall_score, 1),
            "evaluation_time": datetime.now().isoformat()
        }

        session_data.setdefault("scores", []).append(evaluation)
        save_session_data(session_id, session_data)

        # Create evaluation summary
        score_interpretation = ""
        if overall_score >= 8:
            score_interpretation = "Excellent response! Strong across all criteria."
        elif overall_score >= 6:
            score_interpretation = "Good response with room for improvement in some areas."
        elif overall_score >= 4:
            score_interpretation = "Adequate response, but several areas need strengthening."
        else:
            score_interpretation = "Response needs significant improvement across multiple areas."

        evaluation_text = f"""
**Answer Evaluation**

**Overall Score: {overall_score:.1f}/10** - {score_interpretation}

**Detailed Breakdown:**
• Content Quality: {scores['content_quality']}/10
• Structure & Clarity: {scores['structure_clarity']}/10  
• Specificity: {scores['specificity']}/10
• Impact & Results: {scores['impact_results']}/10
• Self-awareness: {scores['self_awareness']}/10

**Scoring based on:** Answer depth, structure, specific examples, measurable results, and reflection on learning.
        """

        return {
            "status": "success",
            "message": evaluation_text,
            "evaluation": evaluation,
            "overall_score": overall_score,
            "detailed_scores": scores
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Error evaluating answer: {str(e)}"
        }
