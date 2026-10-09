
import streamlit as st
from llm import generate_response
from prompt_templates import build_prompt

st.set_page_config(
    page_title="Prompt Engineering Explorer",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Prompt Engineering Explorer")
st.caption("Explore. Experiment. Generate.")

st.write(
    "Select a prompting technique, enter your task, "
    "and generate an AI response using Qwen."
)

st.divider()

techniques = [
    "Zero-shot Prompting",
    "Few-shot Prompting",
    "Role-based Prompting",
    "Step-by-step Prompting",
    "Output-format Prompting",
    "Constraint-based Prompting"
]

technique = st.selectbox(
    "Choose a Prompting Technique",
    techniques
)

task = st.text_area(
    "Enter Your Task",
    placeholder=(
        "Example: Explain Artificial Intelligence "
        "in simple English with an example."
    ),
    height=150
)

if st.button("🚀 Generate Response", use_container_width=True):
    if not task.strip():
        st.warning("Please enter a task before generating.")
    else:
        prompt = build_prompt(technique, task)

        with st.spinner("Qwen is generating your response..."):
            try:
                answer = generate_response(prompt)

                st.success("Response generated successfully!")

                st.subheader("📝 Generated Response")
                st.write(answer)

                with st.expander("🔍 View the Generated Prompt"):
                    st.code(prompt, language="text")

            except Exception as error:
                st.error(str(error))

st.divider()
st.caption("Powered by Qwen and Hugging Face Inference API.")
