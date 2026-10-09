def build_prompt(technique, task):
    """Build a prompt using the selected prompting technique."""

    task = task.strip()

    if technique == "Zero-shot Prompting":
        prompt = f"""
Answer the following task clearly and accurately.
Do not invent facts. If information is uncertain, say so.

Task:
{task}

Provide a clear and useful answer.
"""

    elif technique == "Few-shot Prompting":
        prompt = f"""
Learn the format from these examples.

Example 1:
Task: Explain Python.
Answer: Python is a beginner-friendly programming language.

Example 2:
Task: Explain AI.
Answer: Artificial Intelligence enables machines to perform tasks
that normally require human intelligence.

Now answer the user's task in a similar clear format.

Task:
{task}
"""

    elif technique == "Role-based Prompting":
        prompt = f"""
Act as a knowledgeable subject expert and teacher.
Explain concepts accurately using simple English.
Include a suitable example wherever useful.

Task:
{task}
"""

    elif technique == "Step-by-step Prompting":
        prompt = f"""
Solve the following task in a structured way.
Present the important steps and explain the result clearly.
Do not include unnecessary details.

Task:
{task}
"""

    elif technique == "Output-format Prompting":
        prompt = f"""
Answer the following task using this format:

1. Definition or Introduction
2. Key Points
3. Example
4. Conclusion

Keep the answer clear and easy to understand.
If a section is not relevant, adapt the format appropriately.

Task:
{task}
"""

    elif technique == "Constraint-based Prompting":
        prompt = f"""
Answer the following task using these constraints:
- Use simple English.
- Keep the answer concise.
- Focus only on relevant information.
- Include an example if useful.
- Do not invent facts.

Task:
{task}
"""

    else:
        prompt = f"Answer the following task clearly:\n{task}"

    return prompt.strip()
