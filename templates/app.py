from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def recommend_plan(name, age, weight, fat_percentage):
    # Define the training plans
    plans = [
        {
            "Plan ID": 1,
            "Plan Name": "Weight Loss",
            "Weight Range": (70, 100),
            "Fat % Range": (20, 30),
            "Daily Exercises": "Cardio, HIIT",
            "Duration (Days)": 30,
            "Focus Areas": "Fat Burning",
        },
        {
            "Plan ID": 2,
            "Plan Name": "Muscle Gain",
            "Weight Range": (60, 80),
            "Fat % Range": (10, 20),
            "Daily Exercises": "Strength Training",
            "Duration (Days)": 60,
            "Focus Areas": "Muscle Growth",
        },
        {
            "Plan ID": 3,
            "Plan Name": "General Fitness",
            "Weight Range": (50, 70),
            "Fat % Range": (5, 15),
            "Daily Exercises": "Yoga, Stretching",
            "Duration (Days)": 15,
            "Focus Areas": "Flexibility",
        },
        {
            "Plan ID": 4,
            "Plan Name": "Weight Loss",
            "Weight Range": (100, 150),
            "Fat % Range": (30, 50),
            "Daily Exercises": "Cardio, HIIT, Strength",
            "Duration (Days)": 90,
            "Focus Areas": "Fat Burning",
        },
    ]

    # Find a matching plan
    for plan in plans:
        if (plan["Weight Range"][0] <= weight <= plan["Weight Range"][1] and
            plan["Fat % Range"][0] <= fat_percentage <= plan["Fat % Range"][1]):
            return {
                "success": True,
                "message": f"Hello {name} (Age: {age}), based on your weight ({weight} kg) and fat percentage ({fat_percentage}%), "
                          f"you are recommended to follow the '{plan['Plan Name']}' plan.\n"
                          f"Daily Exercises: {plan['Daily Exercises']}\n"
                          f"Focus Areas: {plan['Focus Areas']}\n"
                          f"Duration: {plan['Duration (Days)']} days."
            }
   
    return {
        "success": False,
        "message": f"Sorry {name}, no plan matches your details. Please consult a fitness expert!"
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendation():
    try:
        data = request.json
        result = recommend_plan(
            data['name'],
            float(data['age']),
            float(data['weight']),
            float(data['fatPercentage'])
        )
        return jsonify(result)
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"An error occurred: {str(e)}"
        }), 400

if __name__ == '__main__':
    app.run(debug=True) 