# Prompt Engineering Explorer

## Project Overview

Prompt Engineering Explorer is an AI-powered web application that helps users explore different prompt engineering techniques and generate AI responses.

Users can select a prompting technique, enter a task, and receive a response generated using an AI language model. The application is developed using Python and Streamlit.

## Objectives

* Understand different prompt engineering techniques.
* Generate AI responses using structured prompts.
* Compare how different prompting methods work.
* Provide a simple and interactive user interface.
* Learn how to integrate an AI model with a Python application.

## Features

* **Zero-shot Prompting:** Generates responses without providing examples.
* **Few-shot Prompting:** Uses examples to guide the AI response.
* **Role-based Prompting:** Assigns a specific role to the AI.
* **Step-by-step Prompting:** Organizes responses into clear steps.
* **Output-format Prompting:** Structures responses in a requested format.
* **Constraint-based Prompting:** Guides responses using specific instructions.
* **AI Response Generation:** Generates answers using an AI language model.
* **Prompt Preview:** Allows users to view the generated prompt.

## Technologies Used

* Python
* Streamlit
* Groq API
* Large Language Models (LLMs)
* Prompt Engineering

## Project Structure

```text
Prompt-Engineering-Explorer/
│
├── app.py
├── llm.py
├── prompt_templates.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml
```

Note: The `.streamlit/secrets.toml` file contains the API key and must not be uploaded to GitHub.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Prompt-Engineering-Explorer
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.streamlit/secrets.toml` file and add your Groq API key:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Replace `your_groq_api_key` with your actual API key. Never publish your API key.

### 5. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## How to Use

1. Launch the application.
2. Select a prompting technique from the dropdown menu.
3. Enter your task in the text area.
4. Click Generate Response.
5. View the AI-generated response.
6. Expand the prompt preview to inspect the prompt sent to the model.

## Prompt Engineering Techniques

| Technique                  | Purpose                              |
| -------------------------- | ------------------------------------ |
| Zero-shot Prompting        | Answers without examples             |
| Few-shot Prompting         | Uses examples to guide responses     |
| Role-based Prompting       | Responds from a specified role       |
| Step-by-step Prompting     | Organizes the answer into steps      |
| Output-format Prompting    | Follows a requested output structure |
| Constraint-based Prompting | Follows specified requirements       |

## Applications

* AI-assisted learning
* Educational content generation
* Prompt experimentation
* Text generation
* Understanding Large Language Models
* Improving AI interaction

## Future Enhancements

* Compare responses from multiple AI models.
* Add more advanced prompting techniques.
* Save and download generated responses.
* Add prompt history.
* Improve the user interface.
* Deploy the application online.

## Conclusion

Prompt Engineering Explorer provides a simple way to understand and experiment with different prompt engineering techniques. By combining Python, Streamlit, and an AI language model, the project demonstrates how well-structured prompts can guide AI-generated responses.

