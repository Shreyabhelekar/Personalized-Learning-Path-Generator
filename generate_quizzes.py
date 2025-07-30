import random
import math
import mysql.connector

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="123456789", 
    database="learning_path" 
)
cursor = db.cursor()

# Function to insert quiz into MySQL with random options
def insert_quiz(skill, question, correct_answer, wrong1, wrong2, difficulty):
    options = [correct_answer, wrong1, wrong2]
    random.shuffle(options)

    correct_index = options.index(correct_answer)
    correct_option = ["A", "B", "C"][correct_index]

    query = """
    INSERT INTO quizzes (skill_name, question, option_a, option_b, option_c, correct, difficulty)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (skill, question, options[0], options[1], options[2], correct_option, difficulty))
    db.commit()

# Weak skills
skills = [
    "Fractions", "Percent Discount", "Quadratic Equation Solving", "Pythagorean Theorem",
    "Area Circle", "Ratio", "Mean", "Surface Area Rectangular Prism",
    "Probability Compound", "Unit Conversion","Median", "Percent Of", "Table"
]

# Generate quizzes
for skill in skills:
    
    # ================= EASY QUESTIONS =================
    if skill == "Fractions":
        insert_quiz(skill, "What is 1/2 + 1/3?", "5/6", "2/5", "3/4", "Easy")
    elif skill == "Percent Discount":
        insert_quiz(skill, "A product costs $100 with 20% discount. Final price?", "$80", "$70", "$85", "Easy")
    elif skill == "Quadratic Equation Solving":
        insert_quiz(skill, "Solve x² - 3x + 2 = 0", "x=1 or x=2", "x=2 or x=3", "x=3 or x=4", "Easy")
    elif skill == "Pythagorean Theorem":
        insert_quiz(skill, "Triangle sides are 3 and 4. Hypotenuse?", "5", "6", "7", "Easy")
    elif skill == "Area Circle":
        insert_quiz(skill, "Area of circle radius=7 (π=3.14)?", "153.86", "144", "160", "Easy")
    elif skill == "Ratio":
        insert_quiz(skill, "Simplify ratio 6:9", "2:3", "3:4", "4:5", "Easy")
    elif skill == "Mean":
        insert_quiz(skill, "Mean of 10, 20, 30?", "20", "15", "25", "Easy")
    elif skill == "Surface Area Rectangular Prism":
        insert_quiz(skill, "Surface area of prism l=2,w=3,h=4?", "52", "48", "60", "Easy")
    elif skill == "Probability Compound":
        insert_quiz(skill, "Two coins tossed. Probability of 2 heads?", "1/4", "1/2", "1/3", "Easy")
    elif skill == "Unit Conversion":
        insert_quiz(skill, "Convert 1 meter to cm", "100 cm", "10 cm", "1000 cm", "Easy")
    elif skill == "Median":
        insert_quiz(skill, "What is the median of 5, 7, 9?", "7", "5", "9", "Easy")
    elif skill == "Percent Of":
        insert_quiz(skill, "What is 50% of 200?", "100", "80", "90", "Easy")
    elif skill == "Table":
        insert_quiz(skill, "Which table shows multiplication of 5?", "5,10,15,20", "6,12,18,24", "4,8,12,16", "Easy")
    
    # ================= MEDIUM QUESTIONS =================
    if skill == "Fractions":
        insert_quiz(skill, "What is 3/4 - 2/5?", "7/20", "5/20", "1/2", "Medium")
    elif skill == "Percent Discount":
        insert_quiz(skill, "Laptop is $500 with 30% discount. Price?", "$350", "$300", "$370", "Medium")
    elif skill == "Quadratic Equation Solving":
        insert_quiz(skill, "Solve x² - 5x + 6 = 0", "x=2 or x=3", "x=1 or x=6", "x=3 or x=4", "Medium")
    elif skill == "Pythagorean Theorem":
        insert_quiz(skill, "Triangle sides are 5 and 12. Hypotenuse?", "13", "14", "12", "Medium")
    elif skill == "Area Circle":
        insert_quiz(skill, "Area of circle radius=10 (π=3.14)?", "314", "300", "320", "Medium")
    elif skill == "Ratio":
        insert_quiz(skill, "Simplify ratio 15:35", "3:7", "5:7", "4:5", "Medium")
    elif skill == "Mean":
        insert_quiz(skill, "Mean of 5, 10, 15, 20?", "12.5", "15", "10", "Medium")
    elif skill == "Surface Area Rectangular Prism":
        insert_quiz(skill, "Surface area prism l=5,w=4,h=3?", "94", "88", "100", "Medium")
    elif skill == "Probability Compound":
        insert_quiz(skill, "Rolling two dice. Probability sum=7?", "6/36", "5/36", "4/36", "Medium")
    elif skill == "Unit Conversion":
        insert_quiz(skill, "Convert 5 km to meters", "5000 m", "50 m", "500 m", "Medium")
    elif skill == "Median":
        insert_quiz(skill, "Find median of 3, 8, 12, 20, 25", "12", "10", "15", "Medium")
    elif skill == "Percent Of":
        insert_quiz(skill, "What is 30% of 250?", "75", "65", "80", "Medium")
    elif skill == "Table":
        insert_quiz(skill, "In a data table, the row represents?", "Records", "Columns", "Values", "Medium")
    
    # ================= HARD QUESTIONS =================
    if skill == "Fractions":
        insert_quiz(skill, "What is (5/6 ÷ 2/3) + 1/2?", "1.75", "2", "1.5", "Hard")
    elif skill == "Percent Discount":
        insert_quiz(skill, "Item price $800, 20% discount, then 10% discount. Final price?", "$576", "$600", "$640", "Hard")
    elif skill == "Quadratic Equation Solving":
        insert_quiz(skill, "Solve 2x² - 7x + 3 = 0", "x=3, x=0.5", "x=2, x=1", "x=1, x=3", "Hard")
    elif skill == "Pythagorean Theorem":
        insert_quiz(skill, "Triangle sides 8 and 15. Hypotenuse?", "17", "18", "16", "Hard")
    elif skill == "Area Circle":
        insert_quiz(skill, "Area of circle diameter=14cm (π=3.14)?", "153.86", "160", "140", "Hard")
    elif skill == "Ratio":
        insert_quiz(skill, "Simplify ratio 84:126", "2:3", "3:5", "4:5", "Hard")
    elif skill == "Mean":
        insert_quiz(skill, "Mean of 12, 15, 18, 21, 24?", "18", "20", "16", "Hard")
    elif skill == "Surface Area Rectangular Prism":
        insert_quiz(skill, "Surface area prism l=10,w=5,h=3?", "190", "180", "200", "Hard")
    elif skill == "Probability Compound":
        insert_quiz(skill, "Probability of drawing 2 red balls from 3 red, 5 blue?", "3/28", "2/28", "5/28", "Hard")
    elif skill == "Unit Conversion":
        insert_quiz(skill, "Convert 2.5 km to cm", "250000 cm", "25000 cm", "2500 cm", "Hard")
    elif skill == "Median":
        insert_quiz(skill, "Median of 2, 4, 8, 10, 14, 18?", "9", "10", "8", "Hard")
    elif skill == "Percent Of":
        insert_quiz(skill, "What is 12.5% of 640?", "80", "85", "75", "Hard")
    elif skill == "Table":
        insert_quiz(skill, "Which table correctly represents frequency of test scores?", "Frequency table", "Multiplication table", "Truth table", "Hard")

print("✅ Quizzes with randomized options inserted successfully!")
