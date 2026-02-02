"""
SaaS Onboarding FAQ Bot

This chatbot helps new SaaS users by answering onboarding questions
such as account setup, API access, integrations, billing, and best practices.

The bot is designed as a documentation-driven FAQ assistant and can be
extended to use AI services like ScaleDown for RAG-based responses.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_PATH = os.path.join(BASE_DIR, "data", "faq.txt")

if not os.path.exists(FAQ_PATH):
    print("FAQ file not found. Please check data/faq.txt")
    exit()

with open(FAQ_PATH, "r", encoding="utf-8") as file:
    faq_text = file.read().lower()

print("\nSaaS Onboarding FAQ Bot")
print("Ask onboarding questions. Type 'exit' to quit.\n")
# Function to return answers based on onboarding keywords
def get_answer(question):
    q = question.lower()

    if "password" in q or "reset" in q:
        return (
            "You can reset your password using the 'Forgot Password' option on the login page. "
            "A reset link will be sent to your registered email."
        )

    if "api" in q:
        return (
            "API access is available by generating an API key from the developer settings page. "
            "The API allows you to manage projects, tasks, and analytics programmatically."
        )

    if "integration" in q or "github" in q or "slack" in q:
        return (
            "The product supports integrations with GitHub, Slack, and Google Drive. "
            "You can enable integrations from the settings panel."
        )

    if "billing" in q or "invoice" in q:
        return (
            "Billing details, plans, and invoices can be managed from the billing section "
            "in your account settings."
        )

    if "best practice" in q or "best practices" in q:
        return (
            "Best practices include organizing projects into workspaces, "
            "keeping tasks updated, and reviewing analytics regularly."
        )

    if "help" in q or "what can you do" in q:
        return (
            "I can help you with onboarding questions related to account setup, "
            "API access, integrations, billing, and best practices."
        )

    return (
        "This question is not covered in the onboarding documentation. "
        "Please check the help center or contact support."
    )

while True:
    user_input = input("Ask a question: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    print("\nAnswer:", get_answer(user_input), "\n")
