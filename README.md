# CareerIgnite - AI Career Recommendation System

## Project Overview

CareerIgnite is an AI-powered web application that helps users discover suitable career paths based on their education, skills, and interests. The project uses Machine Learning to provide personalized career recommendations through a Django web application, along with self-discovery, career roadmaps, resources, and an interactive chatbot.

## Features

- AI-powered career recommendations
- Personalized career suggestions
- Self-discovery section
- Career roadmap
- Interactive chatbot
- Career resources
- Machine Learning-based prediction
- Django web application

## Technologies Used

• Python  
• Django  
• Pandas  
• NumPy  
• Scikit-learn  
• Joblib  
• HTML  
• CSS  
• JavaScript  
• Git & GitHub

## Machine Learning

The CareerIgnite recommendation system uses a trained Machine Learning model to recommend a suitable career based on user information.

Input Features:

• Education  
• Skills  
• Interests

The Machine Learning pipeline includes:

• Data preprocessing  
• Text vectorization using TF-IDF  
• Feature encoding  
• Trained Machine Learning model  
• Career prediction

The trained Machine Learning files are stored in the `recommendation/ml_model/` folder:

• `job_recommendation_model.pkl`  
• `vectorizer.pkl`  
• `encoder.pkl`

## Application Structure

The project is built using Django and contains:

• `recommendation/` → Main Django application  
• `templates/` → HTML pages  
• `static/` → CSS, JavaScript, images, and JSON files  
• `ml_model/` → Trained Machine Learning components  
• `views.py` → Application logic and prediction handling  
• `urls.py` → Application URL configuration  
• `settings.py` → Django project configuration

## Project Structure

CareerIgnite/  
│  
├── .gitignore  
│  
└── self_discovery/  
&nbsp;&nbsp;&nbsp;&nbsp;├── manage.py  
&nbsp;&nbsp;&nbsp;&nbsp;├── settings.py  
&nbsp;&nbsp;&nbsp;&nbsp;├── urls.py  
&nbsp;&nbsp;&nbsp;&nbsp;├── asgi.py  
&nbsp;&nbsp;&nbsp;&nbsp;├── wsgi.py  
&nbsp;&nbsp;&nbsp;&nbsp;│  
&nbsp;&nbsp;&nbsp;&nbsp;├── recommendation/  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── admin.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── apps.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── models.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── urls.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── views.py  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── ml_model/  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── encoder.pkl  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── vectorizer.pkl  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── job_recommendation_model.pkl  
&nbsp;&nbsp;&nbsp;&nbsp;│  
&nbsp;&nbsp;&nbsp;&nbsp;├── static/  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── css/  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── site.js  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── chatbot_data.json  
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;└── roadmap.json  
&nbsp;&nbsp;&nbsp;&nbsp;│  
&nbsp;&nbsp;&nbsp;&nbsp;└── templates/

## How to Run

1. Clone the repository

git clone https://github.com/shahdashraf-it/CareerIgnite.git

2. Move to the project folder

cd CareerIgnite

3. Install the required libraries

pip install django pandas numpy scikit-learn joblib

4. Move to the Django project

cd self_discovery

5. Run the application

python manage.py runserver

6. Open the application in your browser:

http://127.0.0.1:8000/

## Results

- The Machine Learning model was successfully integrated into the Django web application.
- The system can analyze user education, skills, and interests to generate career recommendations.
- The trained model, vectorizer, and encoder were successfully saved and integrated into the application.
- The project provides additional career guidance features including self-discovery, career roadmaps, resources, and an interactive chatbot.

## Future Improvements

- Improve the Machine Learning recommendation performance.
- Add more career categories and training data.
- Improve the chatbot and career guidance features.
- Add user authentication and profiles.
- Store users' recommendation history.
- Deploy the application online using a cloud platform.

## Author

**Shahd Ashraf**  
Information Technology Student  
Faculty of Industrial Technology and Energy  
Machine Learning & AI

GitHub: https://github.com/shahdashraf-it  
LinkedIn: https://linkedin.com/in/shahd-ashraf-277707344
