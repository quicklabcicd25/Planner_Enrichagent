# Planner_Enrichagent# Multi‑Agent AI System

## Overview
Multi‑agent system that uses GPT for intelligent planning and summarization, SpaceX & OpenWeatherMap APIs for data.

## Agents
- **LLMAgent**: Generates step-by-step plans and final summary.
- **SpaceXAgent**: Retrieves next launch and pad info.
- **WeatherAgent**: Gets weather at launch location.
- **SummaryAgent**: Refines final summary via GPT.

## Setup
1. Clone repo.
2. Copy `.env.example` to `.env` (or use Streamlit secrets).
3. Add your API keys.
4. Install deps:  
