from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/productionplan', methods=['POST'])
def production_plan():
    try:
        # Parse the input JSON payload
        data = request.get_json()

        load = data['load']
        fuels = data['fuels']
        powerplants = data['powerplants']

        # Calculate the production plan (your algorithm here)
        plan = calculate_production_plan(load, fuels, powerplants)

        return jsonify(plan), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

def calculate_production_plan(load, fuels, powerplants):
    # Implement the algorithm to calculate the production plan here
    # This will involve sorting the powerplants by cost and calculating the power distribution
    pass

if __name__ == '__main__':
    app.run(port=8888)
