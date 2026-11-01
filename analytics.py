"""
Portfolio Analytics Helper Script
Language: Python 3
Purpose: Process portfolio metrics and tech stack summary for dynamic loading.
"""

from typing import Dict, List

def calculate_portfolio_metrics() -> Dict[str, str]:
    metrics = {
        "education": "Universitas Muhammadiyah Malang",
        "major": "S1 Teknik Informatika",
        "gpa": "3.94 / 4.00",
        "experience": "Front-End Developer Internship at PT Lanius Inovasi Indonesia"
    }
    return metrics

def get_tech_stack() -> List[str]:
    return ["HTML5", "CSS3", "JavaScript", "React.js", "Node.js", "Python", "SQL", "Figma"]

if __name__ == "__main__":
    print("=== KEYSA AMANDA PORTFOLIO METRICS ===")
    for key, value in calculate_portfolio_metrics().items():
        print(f"{key.capitalize()}: {value}")
    print("\nTech Stack:", ", ".join(get_tech_stack()))