from datetime import date

name = "Rahul Pandey"
today = date.today()
oracle_skills = ["Performance tuning", "PL/SQL", "RAC administration"]

print(f"Name: {name}")
print(f"Date: {today}")
print(f"Top Oracle skills: {', '.join(oracle_skills)}")
