# SkillLens: AI-Powered Personalized Learning Path Generator
A smart web app that analyzes student performance data and recommends YouTube videos for weak math skills using AI.

## Features
- Input student ID to analyze performance
- Recommends skill-wise YouTube tutorials
- Uses real data from `cleaned_skill_builder_data.csv`
- Displays student scores and weak skills
- Responsive UI using Bootstrap
- API key secured via `.env` file

## Tech Stack
- Python (Flask)
- Pandas
- Google YouTube Data API v3
- Bootstrap (for UI)
- dotenv for environment variable handling

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Shreyabhelekar/SkillLens.git
cd SkillLens
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Set Up the Environment
Create a .env file in the root folder and add your API key:
```bash
YOUTUBE_API_KEY=your_youtube_data_api_key
```
### 4. Run the Application
```bash
python app.py
```

## Sample Use Case
A student enters their ID.

The app analyzes scores from cleaned_skill_builder_data.csv.

Low-score skills are identified (score < 0.6).

A curated YouTube tutorial is fetched for each weak skill.

Student sees:

List of weak skills

Their scores

Tutorial links to improve

## Dataset
https://sites.google.com/site/assistmentsdata/home/2009-2010-assistment-data/skill-builder-data-2009-2010

## Security Notes
This app uses a .env file to keep your API key safe.

The .gitignore ensures that .env is never pushed to GitHub.

API key restrictions (refer to Google Cloud) are highly recommended.

## Contributing
Pull requests are welcome. If you find a bug or want to suggest a feature, feel free to open an issue.

## License
This project is licensed under the MIT License.
