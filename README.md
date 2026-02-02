# SaaS Onboarding FAQ Bot

## Overview
This project is a SaaS onboarding FAQ chatbot designed to help new users
quickly understand product features, integrations, billing, API access,
and best practices using documentation-based question answering.

## Problem Statement
New SaaS users often struggle during onboarding due to scattered
documentation and delayed support responses. This project addresses
that problem by providing an interactive FAQ chatbot that delivers
instant answers from onboarding documentation.

## Solution
The chatbot follows a RAG-style design using onboarding documentation
as its knowledge base. User questions are matched against documented
content to provide accurate and helpful responses.

The system is designed to integrate with the ScaleDown API for compressed
document-based AI responses and includes a fallback mechanism to ensure
reliability if AI services are unavailable.

## Features
- SaaS onboarding FAQ chatbot
- Covers account setup, API access, integrations, billing, and best practices
- Simple command-line interface
- Offline fallback logic for stability
- Extensible architecture for AI integration

## Tech Stack
- Python
- Documentation-based Q&A
- ScaleDown API (intended integration)

## How to Run
```bash
python app.py
