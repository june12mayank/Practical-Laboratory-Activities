"""Standalone Gradio chatbot for Exercise 5.

Run from the project root:
    python Exercise5_app.py

Then open http://127.0.0.1:7860 in a browser.
"""

import re

import gradio as gr


def chatbot(message, history):
    """Return a rule-based reply for the supplied user message."""
    text = (message or "").lower().strip()

    if not text:
        return "Please type a question so I can help."

    if re.search(r"\b(hello|hi|hey|greetings)\b", text):
        return "Hello! Welcome to my AI chatbot. How can I help you today?"

    if "how are you" in text:
        return "I am doing well, thank you! What would you like to explore?"

    if "machine learning" in text or " ml " in f" {text} ":
        return (
            "Machine learning is a branch of AI in which models learn patterns "
            "from data and use them to make predictions or decisions."
        )

    if "python" in text:
        return (
            "Python is a popular, readable programming language used for data "
            "science, automation, web development, and AI."
        )

    if "gradio" in text:
        return (
            "Gradio is a Python library for quickly building interactive web "
            "interfaces for machine-learning models and data applications."
        )

    if "data science" in text or "pandas" in text:
        return (
            "Data science combines statistics, programming, and domain knowledge "
            "to turn data into useful insights. pandas is a key Python library "
            "for tabular data analysis."
        )

    if re.search(r"\b(bye|goodbye|thanks|thank you)\b", text):
        return "You're welcome! Thanks for trying the demo chatbot."

    return (
        "Thank you for your question! I am a demonstration chatbot. "
        "Try asking about Python, machine learning, Gradio, or data science."
    )


demo = gr.ChatInterface(
    fn=chatbot,
    title="My AI Chatbot",
    description=(
        "Welcome! Ask questions about Python, machine learning, Gradio, "
        "and general topics. This demo runs locally without an API key."
    ),
    examples=[
        "Hello!",
        "What is Python?",
        "Explain machine learning.",
        "What is Gradio?",
    ],
    cache_examples=False,
)

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        show_error=True,
        footer_links=[],
        theme=gr.themes.Soft(primary_hue="teal", neutral_hue="slate"),
        css="""
        .gradio-container {max-width: 1100px !important; margin: auto !important;}
        footer {display: none !important;}
        """,
    )
