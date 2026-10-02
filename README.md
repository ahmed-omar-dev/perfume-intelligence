# Perfume Intelligence

A Python CLI project for perfume management, search, recommendations, analytics, and automated testing.

## Project Overview

Perfume Intelligence is a command-line application built during Phase 1 of my learning roadmap.

The project was created to apply core Python and software engineering concepts in a practical way, including object-oriented programming, file handling, exception handling, testing, search, filtering, analytics, and rule-based recommendations.

## Features

- Add new perfumes
- View all perfumes
- Search perfumes by name
- Search perfumes by brand
- Filter perfumes by fragrance family
- Filter perfumes by season
- Filter perfumes by occasion
- Filter perfumes by notes
- Filter perfumes by maximum price
- Sort perfumes by price
- Sort perfumes by rating
- Delete perfumes
- Detect low-stock perfumes
- Rule-based perfume recommendations
- Perfume analytics
- JSON data persistence
- Input validation
- Custom exceptions
- Automated testing with pytest

## Project Structure

```text
perfume_intelligence/
│
├── main.py
│
├── models/
│   ├── perfume.py
│   ├── perfume_catalog.py
│   └── user_preference.py
│
├── services/
│   ├── perfume_service.py
│   ├── search_service.py
│   ├── recommendation_service.py
│   └── analytics_service.py
│
├── storage/
│   └── json_storage.py
│
├── utils/
│   └── validators.py
│
├── exceptions/
│   └── custom_exceptions.py
│
├── tests/
│   ├── test_validators.py
│   ├── test_perfume.py
│   ├── test_perfume_catalog.py
│   ├── test_search_service.py
│   ├── test_recommendation_service.py
│   ├── test_analytics_service.py
│   └── test_json_storage.py
│
├── data/
│   └── perfumes.json
│
└── .gitignore
```

## Technologies Used

- Python
- Object-Oriented Programming
- JSON
- pytest
- Git
- GitHub

## Core Concepts Applied

- Python Fundamentals
- Data Structures
- Functions
- Modules and Packages
- File Handling
- Exception Handling
- Object-Oriented Programming
- Clean Code
- Debugging
- Automated Testing
- Data Structures and Algorithms
- Searching and Sorting
- Hashing
- Basic Analytics
- Rule-Based Recommendation Logic

## How to Run

Clone the repository:

```bash
git clone https://github.com/ahmed-omar-dev/perfume-intelligence.git
```

Move into the project directory:

```bash
cd perfume-intelligence
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Run the application:

```bash
python main.py
```

## Running Tests

Install pytest:

```bash
pip install pytest
```

Run the test suite:

```bash
pytest -v
```

For coverage:

```bash
pip install pytest-cov
```

```bash
pytest --cov=. --cov-report=term-missing
```

## Recommendation System

The project includes a simple rule-based recommendation engine.

Perfumes receive scores based on user preferences such as:

- Budget
- Preferred notes
- Preferred seasons
- Preferred occasions
- Minimum longevity
- Minimum sillage

The perfumes are then ranked according to their recommendation score.

## Analytics

The analytics module can provide information such as:

- Average perfume price
- Average perfume rating
- Highest rated perfume
- Lowest priced perfume
- Highest priced perfume
- Perfume count by brand
- Perfume count by fragrance family
- Top-rated perfumes
- Low-stock count

## Purpose of This Project

This project was built as a practical Phase 1 learning project to connect multiple programming concepts inside one complete application.

It is not intended to be the final flagship project of my roadmap.

Future projects will be larger and will include technologies such as:

- Web Development
- Backend Engineering
- Databases
- Data Science
- Machine Learning
- AI Engineering

## Author

Ahmed Omar

Computer Science Student  
Python Developer  
Software Engineering | AI & Data