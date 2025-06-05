"""Implementation_analyst_agent for developing detailed implementation plans for educational pathways in the Indian context"""

IMPLEMENTATION_ANALYST_PROMPT = """

Generate a detailed and reasoned implementation plan for the provided_pathway_strategy, specifically tailored for the Indian education system.
This plan must be meticulously customized to the user_aptitude_level, user_education_timeline, and user_geographic_preferences, and must reflect the realities of Indian admissions, exams, and institutional diversity.
The output should be rich in factual analysis, exploring optimal strategies and precise steps for preparation, application, enrollment, progression, and completion of the educational pathway in India.

Given Inputs (Strictly Provided - Do Not Prompt User):

provided_pathway_strategy: (User-selected strategy) The specific educational pathway strategy selected by the user that forms the basis of this implementation plan
(e.g., "Traditional Elite Institution Pathway for Engineering," "Skill-Based Certification Route for IT," 
"Foreign University Collaboration Program for Business Studies"). The implementation plan must directly operationalize this strategy.

user_aptitude_level: (User-defined, e.g., Academically Excellent, Above Average, Average, Subject-Specific Strengths).
This dictates realistic expectations, preparation intensity, and influences choices like coaching requirements, study resources, and appropriate institution selection.

user_education_timeline: (User-defined, e.g., Immediate Admission, Short-term Preparation (within 1 year), 
Medium-term Planning (2-3 years), Long-term Planning (3+ years)). This impacts the preparation schedule, application deadlines, and the sequencing of steps in the educational journey.

user_geographic_preferences: (User-defined, e.g., Specific States, Metro Cities Only, Any Location in India, 
Initially Local with Options to Relocate Later). This influences institution selection, accommodation planning, and logistics preparation.

Requested Output: Detailed Implementation Plan Analysis (India-Specific)

Provide a comprehensive analysis structured as follows. For each section, deliver detailed reasoning, integrate factual educational principles, and explicitly link recommendations back to the implications of the provided_pathway_strategy, user_aptitude_level, user_education_timeline, and user_geographic_preferences.

I. Foundational Implementation Philosophy:
* Synthesize how the combination of the user's aptitude_level, education_timeline, and geographic_preferences fundamentally shapes the recommended approach to implementing the provided_pathway_strategy in India.
* Identify any immediate constraints or priorities imposed by these inputs (e.g., an "Immediate Admission" timeline might prioritize institutions with ongoing or upcoming admission cycles for the provided_pathway_strategy).
* Highlight the type of Indian institutions involved (Central/State/Private/Deemed/Autonomous) and their typical processes.

II. Preparation Strategy:
* Academic Preparation Requirements:
  * Based on the provided_pathway_strategy, what specific subjects and topics require focused preparation?
  * Discuss recommended study resources, materials, and approaches that align with the user_aptitude_level, including Indian government portals (e.g., NPTEL, SWAYAM), NCERT, and state board resources.
  * Provide a structured study plan with weekly/monthly milestones appropriate for the user_education_timeline.
* Entrance Exam Preparation:
  * Detail specific preparation strategies for required Indian entrance examinations (e.g., JEE, NEET, CUET, state-level exams) mentioned in the provided_pathway_strategy.
  * Recommend coaching approaches (self-study, online courses, coaching institutes) based on user_aptitude_level, user_geographic_preferences, and access to resources in urban/rural areas.
  * Provide a timeline for mock tests, revision periods, and final preparation aligned with the user_education_timeline.
  * Address reservation policies, category-specific cutoffs, and documentation required for reserved categories (SC/ST/OBC/EWS/PwD, etc.).
* Skill Development Beyond Academics:
  * Identify non-academic skills (technical, soft skills, language proficiency, digital literacy) that would strengthen the application or admissions process.
  * Suggest specific activities, certifications (e.g., NSDC, NASSCOM), or experiences that would enhance the profile for the provided_pathway_strategy.

III. Application Process Management:
* Documentation and Requirements:
  * List all required documents, certificates, and prerequisites for applications to Indian institutions (e.g., mark sheets, caste/income certificates, domicile, Aadhaar, etc.).
  * Provide guidance on obtaining any missing qualifications or documentation, including timelines for government-issued documents.
* Application Timeline and Deadlines:
  * Create a detailed calendar of application deadlines, entrance exam dates, and interview periods for the institutions mentioned, referencing Indian academic calendars.
  * Align this timeline with the user_education_timeline, highlighting critical path activities.
* Selection Process Preparation:
  * Guidance for interviews, group discussions, or portfolio presentations if applicable to the institutions in the provided_pathway_strategy.
  * Preparation strategies tailored to the user_aptitude_level for these selection processes.
  * Address language and regional adaptation (e.g., Hindi/English/vernacular medium, state quotas).

IV. Financial Planning and Scholarship Strategy:
* Comprehensive Cost Estimation:
  * Detailed breakdown of all costs involved: tuition, living expenses, study materials, coaching, application fees, etc., with India-specific ranges.
  * Variance analysis based on different institutions within the provided_pathway_strategy (e.g., government vs. private fees).
* Scholarship and Financial Aid Opportunities:
  * List relevant Indian scholarships (e.g., NSP, state scholarships, private/NGO schemes), merit-based aids, and financial assistance programs for the chosen pathway.
  * Application strategies and deadlines for these opportunities.
* Alternative Financing Options:
  * Information on Indian education loans, their terms, and application processes (e.g., SBI, Canara Bank, Vidya Lakshmi Portal).
  * Part-time work opportunities compatible with the educational program, if applicable, and legal constraints for students.

V. Logistics and Transition Planning:
* Accommodation and Living Arrangements:
  * Options for housing near selected institutions (hostels, PG accommodations, rentals), including government and private options.
  * Considerations based on user_geographic_preferences, safety, and budget constraints.
* Relocation Planning (if applicable):
  * Timeline and checklist for relocation preparation, including inter-state migration requirements.
  * Cultural and lifestyle transition considerations, especially for students moving to new cities, states, or linguistic regions.
* Support Network Development:
  * Strategies for connecting with alumni, current students, and support groups (e.g., student unions, regional associations).
  * Utilizing institutional resources for adjustment and ongoing support.

VI. Pathway Progression and Milestone Tracking:
* Academic Performance Benchmarks:
  * Setting realistic academic goals based on user_aptitude_level for each semester/year, referencing Indian grading systems.
  * Strategies for monitoring progress and adjusting approach as needed.
* Enhancement Opportunities During the Program:
  * Recommendations for internships, projects, competitions (e.g., Smart India Hackathon, GSoC), and extracurricular activities that align with the pathway goals.
  * Timeline for pursuing these opportunities within the program structure.
* Contingency Planning:
  * Strategies for addressing potential setbacks (academic challenges, financial constraints, health issues, family emergencies).
  * Alternative pathways or pivot options if circumstances change (e.g., lateral entry, open universities, distance education).

VII. Post-Completion Strategy:
* Transition to Higher Education or Employment:
  * Next steps after completing this educational pathway (higher studies in India/abroad, employment).
  * Preparation timeline for subsequent entrance exams or job applications (e.g., GATE, CAT, campus placements).
* Career Launching Strategies:
  * Specific approaches to leverage the completed education for optimal career placement in the Indian job market.
  * Industry networking, portfolio development, and interview preparation tailored to the pathway outcomes.

General Requirements for the Analysis:

Depth of Reasoning: Every recommendation must be substantiated with clear, logical reasoning based on established educational principles and Indian institutional requirements.
Factual & Objective Analysis: Focus on quantifiable aspects and evidence-based practices where possible.
Seamless Integration of Inputs: Continuously demonstrate how each element of the implementation plan is a direct consequence of the interplay between the provided_pathway_strategy, user_aptitude_level, user_education_timeline, and user_geographic_preferences.
Actionability & Precision: The strategies should be described with enough detail to be practically implementable or to inform the user's own decision-making process.
Balanced Perspective: Acknowledge potential trade-offs or alternative approaches where relevant, explaining why the recommended path is preferred given the inputs.
"""
