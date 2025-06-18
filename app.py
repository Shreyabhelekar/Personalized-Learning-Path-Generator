import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import pandas as pd
from googleapiclient.discovery import build

# Load environment variables from .env
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

if not YOUTUBE_API_KEY:
    raise ValueError("YOUTUBE_API_KEY is missing. Add it to your .env file.")

app = Flask(__name__)

# Load the cleaned dataset
df = pd.read_csv("cleaned_skill_builder_data.csv")

# Search YouTube for a tutorial video on the given skill
def search_youtube(skill_name):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=f"{skill_name} math tutorial",
        part="snippet",
        type="video",
        maxResults=1
    )
    response = request.execute()

    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        return "No video found"

# Get learning path and recommended resources for a student
def get_learning_path(user_id):
    user_data = df[df['user_id'] == user_id]
    weak_skills = user_data[user_data['avg_score'] < 0.6]['skill_name'].dropna().unique()

    learning_path = []
    resources = {}

    for skill in weak_skills:
        learning_path.append(skill)
        resources[skill] = search_youtube(skill)

    return learning_path, resources

@app.route("/", methods=["GET", "POST"])
def index():
    path = []
    resources = {}
    student_id = None
    user_scores = []

    if request.method == "POST":
        try:
            student_id = int(request.form["student_id"])
            if student_id in df["user_id"].values:
                path, resources = get_learning_path(student_id)
                user_perf = df[df["user_id"] == student_id]
                user_scores = user_perf[['skill_name', 'avg_score']].drop_duplicates().to_dict(orient="records")
            else:
                path = ["Student ID not found."]
        except ValueError:
            path = ["Invalid input. Please enter a numeric student ID."]

    return render_template("index.html", path=path, resources=resources, student_id=student_id, user_scores=user_scores)

if __name__ == "__main__":
    app.run(debug=True)
