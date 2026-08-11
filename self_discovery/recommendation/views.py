import joblib
import os
from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(
    os.path.join(BASE_DIR, 'recommendation/ml_model/job_recommendation_model.pkl')
)
encoder = joblib.load(
    os.path.join(BASE_DIR, 'recommendation/ml_model/encoder.pkl')
)
vectorizer = joblib.load(
    os.path.join(BASE_DIR, 'recommendation/ml_model/vectorizer.pkl')
)


def home(request):
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')


def job_recommendation(request):
    return render(request, 'job-recommendation.html')


def admin_page(request):
    return render(request, 'admin.html')


def roadmap_page(request):
    return render(request, 'roadmap.html')

def resources_page(request):
    return render(request, 'resources.html')


def team_page(request):
    return render(request, 'team.html')


def contact_page(request):
    return render(request, 'contact.html')

def chatbot_page(request):
    return render(request, 'chatbot.html')



def predict_job(request):
    result = None
    job_key = None

    if request.method == 'POST':
        text = request.POST.get('text')

        if text:
            text_vec = vectorizer.transform([text]).toarray()
            prediction = model.predict(text_vec)

            try:
                result = encoder.inverse_transform(prediction)[0]
            except Exception:
                job_mapping = {
                    0: "Data Scientist",
                    1: "Machine Learning Engineer",
                    2: "Backend Developer",
                    3: "Frontend Developer"
                }
                result = job_mapping.get(prediction[0], "Unknown Job")

            job_key_mapping = {
                "Data Scientist": "data_scientist",
                "Machine Learning Engineer": "machine_learning_engineer",
                "Backend Developer": "backend_developer",
                "Frontend Developer": "frontend_developer",
                "Front-end Developer": "frontend_developer",
                "Software Engineer": "software_engineer",
                "UX Designer": "ux_designer",
                "AI Researcher": "ai_researcher",
                "Project Manager": "project_manager",
                "Embedded Systems Engineer": "embedded_systems_engineer",
                "Data Analyst": "data_analyst",
                "Digital Marketer": "digital_marketer",
                "NLP Engineer": "nlp_engineer",
                "Financial Analyst": "financial_analyst",
                "Research Scientist": "research_scientist",
                "Software Developer": "software_developer",
                "Marketing Manager": "marketing_manager",
                "Full Stack Developer": "full_stack_developer",
                "AI Specialist": "ai_specialist",
                "Cybersecurity Analyst": "cybersecurity_analyst",
                "Research Analyst": "research_analyst",
                "DevOps Engineer": "devops_engineer",
                "Graphic Designer": "graphic_designer",
                "Deep Learning Engineer": "deep_learning_engineer",
                "Business Analyst": "business_analyst",
                "Biostatistician": "biostatistician",
                "Data Engineer": "data_engineer",
                "Content Strategist": "content_strategist",
                "Automation Engineer": "automation_engineer",
                "Mobile Developer": "mobile_developer",
                "UX Researcher": "ux_researcher",
                "Cybersecurity Specialist": "cybersecurity_specialist",
                "Cloud Engineer": "cloud_engineer"
            }

            job_key = job_key_mapping.get(result, result.lower().replace(" ", "_"))

    return render(request, 'predict.html', {
        'result': result,
        'job_key': job_key
    })
import json
import os

from django.http import JsonResponse
from django.conf import settings

from difflib import SequenceMatcher


def chatbot_response(request):

    user_message = request.GET.get('message', '').lower().strip()

    file_path = os.path.join(
        settings.BASE_DIR,
        'career_app',
        'static',
        'chatbot_data.json'
    )

    with open(file_path, 'r', encoding='utf-8') as file:

        data = json.load(file)

    for item in data.values():

        for keyword in item['keywords']:

            if keyword in user_message:

                return JsonResponse({

                    'reply':
                    f"You mean {item['title']}?\n\n{item['answer']}"

                })

    all_keywords = []

    for item in data.values():

        all_keywords.extend(item['keywords'])

    best_match = None

    highest_ratio = 0

    for keyword in all_keywords:

        ratio = SequenceMatcher(
            None,
            user_message,
            keyword
        ).ratio()

        if ratio > highest_ratio:

            highest_ratio = ratio

            best_match = keyword

    if highest_ratio > 0.45:

        for item in data.values():

            if best_match in item['keywords']:

                return JsonResponse({

                    'reply':
                    f"Did you mean {item['title']}?\n\n{item['answer']}"

                })

    return JsonResponse({

        'reply':
        "Sorry, I couldn't understand your question."

    })