"""
Data models for Learning Content Creation System
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from enum import Enum


class ContentType(Enum):
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    PRESENTATION = "presentation"
    QUIZ = "quiz"


class QualityLevel(Enum):
    DRAFT = "draft"
    REVIEW = "review"
    GOOD = "good"
    EXCELLENT = "excellent"


@dataclass
class LearningObjective:
    """Represents a learning objective"""
    objective: str
    level: str  # beginner, intermediate, advanced
    time_estimate: int  # in minutes


@dataclass
class ContentElement:
    """Represents a piece of content"""
    content_type: ContentType
    title: str
    content: str
    metadata: Dict[str, Any]
    quality_score: float = 0.0
    file_path: Optional[str] = None


@dataclass
class LearningModule:
    """Represents a complete learning module"""
    title: str
    description: str
    objectives: List[LearningObjective]
    content_elements: List[ContentElement]
    duration_minutes: int
    difficulty_level: str
    quality_assessment: Dict[str, Any] = None


@dataclass
class ContentAnalysis:
    """Results from content analysis"""
    key_concepts: List[str]
    learning_objectives: List[LearningObjective]
    difficulty_level: str
    estimated_duration: int
    recommended_formats: List[ContentType]
    quality_metrics: Dict[str, float]


@dataclass
class GenerationRequest:
    """Request for content generation"""
    source_content: str
    target_formats: List[ContentType]
    learning_objectives: List[LearningObjective]
    preferences: Dict[str, Any]
    context: Dict[str, Any] = None
