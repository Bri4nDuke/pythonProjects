#Lab Assignment -  Tuples Lab
#By: Brian Duke
#Date: 4/09/2025
#This program - This system will allow the user to add student scores, calculate average scores, and find the highest score.

def add_score(scores):
    name = input("Enter Student's Name: ")
    score = int(input("Enter Student's Score: "))
    scores.append((name, score))
    print("Score Added Successfully!")
    
def calculate_average(scores):
    if not scores:
        print("No Scores Available")
        return
    total_score = sum(score for _, score in scores)
    average_score = total_score / len(scores)
    print(f"Average Score: {average_score:.2f}")
    
def find_highest_score(scores):
    if not scores:
        print("No Scores Available")
        return
    highest_score = max(scores, key=lambda x: x[1])
    print(f"Highest Score: {highest_score[1]} by {highest_score[0]}")

def main():
    scores = []
    while True:
        print("\n--------- Menu: ---------")
        print("1. Add Score")
        print("2. Calculate Average Score")
        print("3. Find Highest Score")
        print("4. Exit")
        print("-------------------------")

        choice = input("Enter 1-4: ")
        
        if choice == '1':
            add_score(scores)
        elif choice == '2':
            calculate_average(scores)
        elif choice == '3':
            find_highest_score(scores)
        elif choice == '4':
            print("Have a Good Day!")
            break
        else:
            print("ERROR: PLEASE ONLY PUT 1-4")
            
if __name__ == "__main__":
    main()