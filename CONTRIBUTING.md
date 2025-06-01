# Contributing to Awesome ADK Agents

First off, thank you for considering contributing to Awesome ADK Agents! This repository thrives on community contributions, and your help is essential for making it a valuable resource for ADK developers worldwide.

## Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the repository maintainers.

## How Can I Contribute?

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
5. **Commit Changes** - Use clear commit messages

   ```bash
   git commit -m 'Add amazing agent for [specific purpose]'
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

If you have any questions about contributing, please open an issue or reach out to the repository maintainers.

Thank you for your contributions!
