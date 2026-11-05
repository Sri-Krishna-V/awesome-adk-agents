# Contributing to Awesome ADK Agents

First off, thank you for considering contributing to Awesome ADK Agents! This repository thrives on community contributions, and your help is essential for making it a valuable resource for ADK developers worldwide.

## Code of Conduct

This project follows the [Contributor Covenant 3.0](CODE_OF_CONDUCT.md). It says how to report a problem.

## How Can I Contribute?

### Suggesting a List Entry

Most contributions add one project, tutorial, or article to `README.md`. Open a PR that adds one line to the matching section.

```text
- <level> [<label>](<url>) <🏭 if production-ready> - <Description.>
```

For example:

```text
- 🟢 [kkdai/linebot-adk](https://github.com/kkdai/linebot-adk) 🏭 - LINE Bot template with Docker, Cloud Run deployment, and security configurations.
```

**Your entry must meet all of these:**

1. It uses Google ADK: `google-adk`, `google.adk`, adk-go, adk-java or adk-js appears in its dependencies or imports (for articles and tutorials: it teaches ADK).
2. It was updated within the last 6 months and is not archived.
3. Its README has setup steps.
4. It adds something no existing entry covers.

No fork? Use the [Suggest an entry](https://github.com/Sri-Krishna-V/awesome-adk-agents/issues/new?template=1-suggest-entry.yml) issue form instead: the maintainer checks the suggestion and writes the line.

Not sure your project meets these rules yet? Post it in [Show your ADK project](https://github.com/Sri-Krishna-V/awesome-adk-agents/discussions/new?category=show-your-adk-project) first. A project post is not an entry.

**Label:** `owner/repo` when the link points to a repository's root. Use the project's name for a folder inside a repository, and the title for an article, video or course.

**Description:** about 15–20 words of technical fact: what it does, key technologies, what sets it apart. Start with a capital letter, end with a period, and do not start with the project's name. Plain wording, no marketing.

**Level and marks** (see the legend under "Contents" in the README):

- 🟢 Beginner, 🟡 Intermediate, 🔴 Advanced: one dot at the start of the line, matching the real technical complexity. Official SDK repositories and community spaces have no dot; hackathon winners keep their award emoji.
- 🏭 Production-ready: after the link, only when the project ships deployment code and docs (Dockerfile, Cloud Run, Agent Runtime, Helm).

**One link, one place:** each URL appears once in the list. If your project is already listed, update its line instead of adding a new one.

**Before you open the PR:** run `npx awesome-lint@2.3.0 README.md`. It must report no errors.

**Removal:** maintainers remove entries whose links 404, archived repos, and projects with no commits in 12+ months that are broken or built on pre-1.0 ADK.

### Adding a New Agent

The most valuable contribution is adding new, well-documented agent implementations:

1. **Decide on an agent concept** that isn't already covered
2. **Follow the standard agent structure**:

   ```   
   agent-name/
   ├── README.md                 # Description, usage, examples
   ├── agent_name/               # Main agent code
      ├── __init__.py
      ├── agent.py              # Core agent definition
      ├── tools/                # Custom tools
      ├── sub_agents/           # (If applicable)
      └── shared_libraries/     # Utilities and shared code
   ```

3. **Create thorough documentation** including:
   - What the agent does
   - Prerequisites and setup
   - Usage examples
   - Configuration options
   - Expected outputs

### Improving Existing Agents

If you'd like to enhance an existing agent:

1. **Fix bugs** - Repair any non-working functionality
2. **Add features** - Expand the agent's capabilities
3. **Improve performance** - Optimize the agent's operation
4. **Enhance documentation** - Make the agent easier to understand and use
5. **Add Callbacks** - Add before and after callbacks to the agent's lifecycle for better control

### Documentation Contributions

Documentation is crucial for this project:

1. **Update READMEs** - Keep descriptions and usage instructions current
2. **Add examples** - Create sample code showing how to use agents
3. **Write tutorials** - Create step-by-step guides for building or extending agents
4. **Improve main documentation** - Enhance the repository's primary documentation

### Testing

Quality testing helps ensure agents work as expected:

1. **Write unit tests** - Test individual agent components
2. **Create integration tests** - Test complete agent functionality
3. **Build evaluation datasets** - Create standard datasets for testing agent performance
4. **Document testing procedures** - Help others understand how to test agents

## Submission Process

1. **Fork the Repository** - Create your own fork of the project
2. **Create a Branch** - Make a new branch for your contribution

   ```bash
   git checkout -b feature/amazing-agent
   ```

3. **Make Changes** - Implement your contribution following the structure guidelines
4. **Test Your Changes** - Ensure your agent works as expected
5. **Commit Changes** - Use [Conventional Commits](https://www.conventionalcommits.org/), as the history does

   ```bash
   git commit -m 'docs: add amazing-agent to Domain-Specific Applications'
   ```

6. **Push to Your Fork** - Upload your changes

   ```bash
   git push origin feature/amazing-agent
   ```

7. **Submit a Pull Request** - Open a PR against the main repository

## Pull Request Guidelines

When submitting a pull request, please:

1. **Explain your changes** - Describe what your agent does and why it's valuable
2. **Reference issues** - Link to any related issues
3. **Follow coding standards** - Match the style of the existing codebase(atleast try to)
4. **Update documentation** - Ensure documentation reflects your changes

## Style Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use clear, descriptive variable and function names
- Include docstrings for all functions, classes, and modules
- Comment complex logic

### Documentation Style

- Use clear, concise language
- Include code examples
- Structure with Markdown headings
- Add screenshots or diagrams where helpful

## Questions?

Ask in [Discussions](https://github.com/Sri-Krishna-V/awesome-adk-agents/discussions): Q&A for questions about the list, a listed project or `my-adk-agents/`, and Ideas for changes to the list. Questions about ADK itself go to [google/adk-python Discussions](https://github.com/google/adk-python/discussions). Use an [issue](https://github.com/Sri-Krishna-V/awesome-adk-agents/issues/new/choose) for a broken or outdated entry or a bug in an agent.

Thank you for your contributions!
