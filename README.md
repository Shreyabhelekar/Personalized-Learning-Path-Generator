# Personalized Learning Path Generator
 An AI-driven web application that analyzes student performance, identifies weak math skills, and generates a **personalized learning path**.  
The app recommends **YouTube tutorials**, **Khan Academy links**, **MathIsFun resources**, and provides **custom quizzes** to help students master their weak topics.  

--

## Features
- **Student Performance Analysis** – Enter a Student ID to analyze skill-level performance from real dataset.  
- **Weak Skill Detection** – Automatically detects skills with **average score < 0.6**.  
- **AI-Powered YouTube Recommendations** – Fetches best tutorials for weak skills using YouTube Data API v3.  
- **Additional Learning Resources** – Links to Khan Academy and MathIsFun, with Google Search fallback.  
- **Mini Quiz Generator** –  
  - Auto-generates quizzes for each weak skill (Easy → Medium → Hard).  
  - Randomized options to avoid memorization.  
  - Results show **Mastered / In Progress** status based on score.  
- **Student Progress Tracking** – Stores quiz results in MySQL (`student_progress` table).  
- **Responsive UI** – Clean Bootstrap design for desktop & mobile.  
- **Secure API Key Management** – API keys stored in `.env` file and ignored in Git.  

---

## Tech Stack
- **Backend:** Python (Flask)  
- **Database:** MySQL (for quizzes & student progress)  
- **Data Processing:** Pandas (Student skill analysis)  
- **API Integration:** Google YouTube Data API v3  
- **Frontend:** HTML, CSS, Bootstrap (Responsive UI)  
- **Configuration:** dotenv (.env for API key security)  

---

## How to Run the Project

### 1️. Clone the Repository
```bash
git clone https://github.com/Shreyabhelekar/Personalized-Learning-Path-Generator.git
cd Personalized-Learning-Path-Generator
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

### 5. Configure Database
Create a MySQL database:
```bash
CREATE DATABASE learning_path;
```
Create tables :
```bash
CREATE TABLE quizzes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill_name VARCHAR(255),
    question TEXT,
    option_a VARCHAR(255),
    option_b VARCHAR(255),
    option_c VARCHAR(255),
    correct CHAR(1),
    difficulty ENUM('Easy', 'Medium', 'Hard')
);

CREATE TABLE student_progress (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    skill_name VARCHAR(255),
    score INT,
    status VARCHAR(50),
    UNIQUE(user_id, skill_name)
);

```

## Sample Use Case
1. A student enters their ID.

2. App checks cleaned_skill_builder_data.csv for performance.

3. Weak skills identified (score < 0.6).

4. For each weak skill:
   - YouTube tutorial link is fetched.
   - Additional resources (Khan Academy, MathIsFun) provided.
   - Student can take quizzes to check mastery.

5. Quiz results update student_progress table.

6. Student sees updated status: Mastered / In Progress.

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
