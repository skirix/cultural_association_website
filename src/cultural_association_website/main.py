#!/usr/bin/env python
# src/cultural_association_website/main.py
import sys
from cultural_association_website.crew import CulturalAssociationWebsiteCrew

def run():
    """
    Run the cultural association website development crew.
    """
    inputs = {
        'association_name': 'Cultural Heritage Society',
        'association_purpose': 'Preserving and promoting local cultural heritage through events, education, and community engagement',
        'target_audience': 'Community members, cultural enthusiasts, tourists, educators, and students',
        'key_features': 'Event calendar, membership management, gallery/media section, blog/news, contact form, about us page'
    }
    CulturalAssociationWebsiteCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()