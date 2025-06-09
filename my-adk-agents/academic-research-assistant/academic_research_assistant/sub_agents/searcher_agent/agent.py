"""Searcher Agent for finding relevant academic papers.

This module defines the Searcher Agent, which is responsible for finding relevant
academic papers based on a research topic and keywords. It uses both SerpAPI and
web browsing capabilities to search academic databases and extract paper information.

The agent serves as the second step in the Academic Research Assistant workflow,
taking inputs from the Profiler Agent and providing results to the Comparison Agent.

Key components:
- SerpAPI integration for reliable Google Scholar access
- Web browsing tools as fallback for navigating academic search engines
- Screenshot capabilities for visual inspection of search results
- Page analysis tools to determine next actions in the search process
- Text extraction and processing for obtaining paper information

The agent is designed to handle various academic search interfaces and adapt its
behavior based on the content it encounters.
"""

import time
import warnings
import random
from typing import Optional

import selenium
from google.adk.agents.llm_agent import Agent
from google.adk.tools.load_artifacts_tool import load_artifacts_tool
from google.adk.tools.tool_context import ToolContext
from google.genai import types
from PIL import Image
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from ...shared_libraries import constants
from ...tools import serpapi_tools
from . import prompt

warnings.filterwarnings("ignore", category=UserWarning)

if not constants.DISABLE_WEB_DRIVER:
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    options.add_argument("user-data-dir=/tmp/selenium")

    # Add user agent to avoid detection
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
    ]
    options.add_argument(f"user-agent={random.choice(user_agents)}")

    driver = selenium.webdriver.Chrome(options=options)


def go_to_url(url: str) -> str:
    """Navigates the browser to the given URL.

    Args:
        url (str): The complete URL to navigate to, including protocol (http/https).

    Returns:
        str: Confirmation message that navigation was attempted.

    Note:
        This function uses the global Selenium driver instance to navigate to the URL.
        The function prints a log message to the console for debugging purposes.
    """
    print(f"🌐 Navigating to URL: {url}")  # Added print statement

    # Maximum number of retry attempts
    max_retries = 3
    retry_count = 0

    while retry_count < max_retries:
        try:
            # Add a delay between requests to avoid rate limiting
            if retry_count > 0:
                # Random delay between 2-5 seconds
                time.sleep(2 + random.random() * 3)

            driver.get(url.strip())
            return f"Navigated to URL: {url}"

        except Exception as e:
            retry_count += 1
            if retry_count >= max_retries:
                return f"Error: Could not navigate to URL after {max_retries} attempts. {e}"
            # Wait before retrying
            time.sleep(2 + random.random() * 3)


async def take_screenshot(tool_context: ToolContext) -> dict:
    """Takes a screenshot of the current browser view and saves it as an artifact.

    This function captures the current state of the browser window, saves it as a PNG file,
    and registers it as an artifact that can be referenced later in the conversation.

    Args:
        tool_context (ToolContext): Context object providing access to artifact storage.

    Returns:
        dict: A dictionary containing status information and the filename of the saved screenshot.

    Note:
        The screenshot is saved with a timestamped filename to ensure uniqueness.
        This function requires an async context as it interacts with the artifact storage system.
    """
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    print(f"📸 Taking screenshot and saving as: {filename}")
    driver.save_screenshot(filename)

    # Open the file in binary mode and read the bytes directly
    with open(filename, "rb") as f:
        image_bytes = f.read()

    await tool_context.save_artifact(
        filename,
        types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
    )

    return {"status": "ok", "filename": filename}


def click_at_coordinates(x: int, y: int) -> str:
    """Clicks at the specified coordinates on the screen.

    Args:
        x (int): The x-coordinate (horizontal position) to click at.
        y (int): The y-coordinate (vertical position) to click at.

    Returns:
        None: This function does not return a value.

    Note:
        This function first scrolls to the specified coordinates to ensure
        the target area is visible before attempting the click.
    """
    driver.execute_script(f"window.scrollTo({x}, {y});")
    driver.find_element(By.TAG_NAME, "body").click()


def find_element_with_text(text: str) -> str:
    """Finds an element on the page with the given text.

    This function searches the current page for any element containing the exact
    text specified and returns information about whether it was found.

    Args:
        text (str): The exact text to search for in the page elements.

    Returns:
        str: A message indicating whether the element was found.

    Note:
        This function uses XPath to locate elements by their exact text content.
        It handles common Selenium exceptions and returns appropriate messages.
    """
    print(f"🔍 Finding element with text: '{text}'")  # Added print statement

    try:
        element = driver.find_element(By.XPATH, f"//*[text()='{text}']")
        if element:
            return "Element found."
        else:
            return "Element not found."
    except selenium.common.exceptions.NoSuchElementException:
        return "Element not found."
    except selenium.common.exceptions.ElementNotInteractableException:
        return "Element not interactable, cannot click."


def click_element_with_text(text: str) -> str:
    """Clicks on an element on the page with the given text.

    This function searches for and attempts to click on any element containing
    the exact text specified.

    Args:
        text (str): The exact text of the element to click.

    Returns:
        str: A message indicating the result of the click attempt.

    Note:
        This function handles various Selenium exceptions that might occur during
        the click operation and returns appropriate error messages.
    """
    print(f"🖱️ Clicking element with text: '{text}'")  # Added print statement

    try:
        element = driver.find_element(By.XPATH, f"//*[text()='{text}']")
        element.click()
        return f"Clicked element with text: {text}"
    except selenium.common.exceptions.NoSuchElementException:
        return "Element not found, cannot click."
    except selenium.common.exceptions.ElementNotInteractableException:
        return "Element not interactable, cannot click."
    except selenium.common.exceptions.ElementClickInterceptedException:
        return "Element click intercepted, cannot click."


def enter_text_into_element(text_to_enter: str, element_id: str) -> str:
    """Enters text into an element with the given ID.

    This function locates an input element by its ID attribute and enters
    the specified text into it.

    Args:
        text_to_enter (str): The text to type into the input element.
        element_id (str): The HTML ID attribute of the target input element.

    Returns:
        str: A message indicating the result of the text entry operation.

    Note:
        This function handles common Selenium exceptions related to finding
        and interacting with elements, returning appropriate error messages.
    """
    print(
        f"📝 Entering text '{text_to_enter}' into element with ID: {element_id}"
    )  # Added print statement

    try:
        input_element = driver.find_element(By.ID, element_id)
        input_element.send_keys(text_to_enter)
        return (
            f"Entered text '{text_to_enter}' into element with ID: {element_id}"
        )
    except selenium.common.exceptions.NoSuchElementException:
        return "Element with given ID not found."
    except selenium.common.exceptions.ElementNotInteractableException:
        return "Element not interactable, cannot click."


def scroll_down_screen() -> str:
    """Scrolls down the screen by a moderate amount.

    This function scrolls the current browser view downward by a fixed amount
    (500 pixels) to reveal more content.

    Returns:
        str: A confirmation message that scrolling was performed.

    Note:
        The scroll amount is fixed at 500 pixels, which is typically enough
        to reveal new content without skipping too much of the page.
    """
    print("⬇️ scroll the screen")  # Added print statement
    driver.execute_script("window.scrollBy(0, 500)")
    return "Scrolled down the screen."


def get_page_source() -> str:
    """Returns the current page source HTML.

    This function retrieves the HTML source code of the current page, limited
    to a maximum size to prevent overwhelming the model.

    Returns:
        str: The HTML source code of the current page, truncated if necessary.

    Note:
        The function limits the returned HTML to 1,000,000 characters to avoid
        exceeding context limits when processing the source.
    """
    LIMIT = 1000000
    print("📄 Getting page source...")  # Added print statement
    return driver.page_source[0:LIMIT]


def analyze_webpage_and_determine_action(
    page_source: str, user_task: str, tool_context: ToolContext
) -> str:
    """Analyzes the webpage and determines the next action to take.

    This function generates a prompt for the LLM to analyze the current webpage
    and determine what action to take next (scroll, click, etc.) based on the
    user's task and the page content.

    Args:
        page_source (str): The HTML source of the current webpage.
        user_task (str): Description of what the user is trying to accomplish.
        tool_context (ToolContext): Context object for the tool execution.

    Returns:
        str: A prompt for the LLM to analyze the page and determine next actions.

    Note:
        This function doesn't perform the analysis itself; it constructs a detailed
        prompt for the LLM to perform the analysis and return an action plan.
        The returned prompt includes instructions for choosing from a set of
        predefined actions like scrolling, clicking, or entering text.
    """
    print(
        "🤔 Analyzing webpage and determining next action..."
    )  # Added print statement

    analysis_prompt = f"""
    You are an expert web page analyzer.
    You have been tasked with controlling a web browser to achieve a user's goal.
    The user's task is: {user_task}
    Here is the current HTML source code of the webpage:
    ```html
    {page_source}
    ```

    Based on the webpage content and the user's task, determine the next best action to take.
    Consider actions like: completing page source, scrolling down to see more content, clicking on links or buttons to navigate, or entering text into input fields.

    Think step-by-step:
    1. Briefly analyze the user's task and the webpage content.
    2. If source code appears to be incomplete, complete it to make it valid html. Keep the product titles as is. Only complete missing html syntax
    3. Identify potential interactive elements on the page (links, buttons, input fields, etc.).
    4. Determine if scrolling is necessary to reveal more content.
    5. Decide on the most logical next action to progress towards completing the user's task.

    Your response should be a concise action plan, choosing from these options:
    - "COMPLETE_PAGE_SOURCE": If source code appears to be incomplete, complte it to make it valid html
    - "SCROLL_DOWN": If more content needs to be loaded by scrolling.
    - "CLICK: <element_text>": If a specific element with text <element_text> should be clicked. Replace <element_text> with the actual text of the element.
    - "ENTER_TEXT: <element_id>, <text_to_enter>": If text needs to be entered into an input field. Replace <element_id> with the ID of the input element and <text_to_enter> with the text to enter.
    - "TASK_COMPLETED": If you believe the user's task is likely completed on this page.
    - "STUCK": If you are unsure what to do next or cannot progress further.
    - "ASK_USER": If you need clarification from the user on what to do next.

    If you choose "CLICK" or "ENTER_TEXT", ensure the element text or ID is clearly identifiable from the webpage source. If multiple similar elements exist, choose the most relevant one based on the user's task.
    If you are unsure, or if none of the above actions seem appropriate, default to "ASK_USER".

    Example Responses:
    - SCROLL_DOWN
    - CLICK: Learn more
    - ENTER_TEXT: search_box_id, Gemini API
    - TASK_COMPLETED
    - STUCK
    - ASK_USER

    What is your action plan?
    """
    return analysis_prompt


def search_papers(
    query: str, keywords: Optional[str]=None, year_from: Optional[int]=None
) -> str:
    """
    Searches for academic papers using SerpAPI or falls back to web browsing.

    This function serves as a unified interface for paper searches. It first tries
    to use SerpAPI if an API key is available, and falls back to web browsing
    instructions if not.

    Args:
        query (str): The main research topic to search for.
        keywords (str, optional): Comma-separated keywords to refine the search.
        year_from (int, optional): The earliest publication year to include.

    Returns:
        str: Search results or instructions for web-based searching.
    """
    print(f"🔍 Searching for papers on: {query}")

    # If SerpAPI key is available, use it
    if constants.SERPAPI_KEY:
        # Convert comma-separated keywords string to list if provided
        keyword_list = None
        if keywords:
            keyword_list = [k.strip() for k in keywords.split(',')]

        # Use SerpAPI to search
        return serpapi_tools.search_scholar_papers(query, keyword_list, year_from)

    # Otherwise, provide instructions for web-based searching
    else:
        return """
        No SerpAPI key found. Please use the web browsing tools to search for papers:
        
        1. Use `go_to_url` to navigate to Google Scholar: https://scholar.google.com/
        2. Use `enter_text_into_element` to search for your topic
        3. Use `click_element_with_text` to navigate through results
        4. Use `get_page_source` to extract paper information
        
        Follow the web browsing workflow to collect paper information.
        """


searcher_agent = Agent(
    model=constants.MODEL,
    name="searcher_agent",
    description="Searches academic databases for relevant papers using web browsing.",
    instruction=prompt.ACADEMIC_SEARCH_PROMPT,
    tools=[
        # SerpAPI-based search (preferred when API key is available)
        search_papers,

        # Web browsing fallback tools
        go_to_url,
        take_screenshot,
        find_element_with_text,
        click_element_with_text,
        enter_text_into_element,
        scroll_down_screen,
        get_page_source,
        load_artifacts_tool,
        analyze_webpage_and_determine_action,
    ],
)
