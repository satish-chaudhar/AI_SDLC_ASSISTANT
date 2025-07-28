def generate_architecture_prompt(project_description):
    return f"""
You are a GenAI SDLC Architect Assistant.

Given the following project description:
---
{project_description}
---

Provide the following:
1. Suggested SDLC phase to begin with
2. Recommended Architecture Style (e.g., Microservices, Monolith, Serverless)
3. Suggested Tech Stack (Frontend, Backend, DB, Infra)
4. Reasoning for each recommendation
5. Best practices for current SDLC stage
"""
