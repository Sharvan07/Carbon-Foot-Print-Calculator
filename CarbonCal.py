from flask import Flask, render_template, request

app = Flask(__name__)

ELECTRICITY_EMISSION_FACTOR = 0.4  # Genetal Units Used In Entire World = kg CO2/kWh
TRANSPORT_EMISSION_FACTOR = 2.3  # Genetal Units Used In Entire World = kg CO2 per mile
MANUFACTURING_EMISSION_FACTOR = 5  # Genetal Units Used In Entire World = kg CO2 per unit
CONSTRUCTION_EMISSION_FACTOR = 10  # Genetal Units Used In Entire World = kg CO2 per ton of materials
AGRICULTURE_EMISSION_FACTOR = 2  # Genetal Units Used In Entire World = kg CO2 per ton of crops

CRITERIA = {
    'Electricity': 100,
    'Transport': 50,
    'Manufacturing': 200,
    'Construction': 100,
    'Agriculture': 50
}

def calculate_electricity_footprint(energy_consumed):
    return energy_consumed * ELECTRICITY_EMISSION_FACTOR

def calculate_transport_footprint(miles_driven, fuel_efficiency):
    if fuel_efficiency == 0:
        return 0
    return miles_driven / fuel_efficiency * TRANSPORT_EMISSION_FACTOR

def calculate_manufacturing_footprint(products_produced):
    return products_produced * MANUFACTURING_EMISSION_FACTOR

def calculate_construction_footprint(materials_used):
    return materials_used * CONSTRUCTION_EMISSION_FACTOR

def calculate_agriculture_footprint(crops_grown):
    return crops_grown * AGRICULTURE_EMISSION_FACTOR

def get_suggestions(footprint, category):
    suggestions = []
    if footprint < CRITERIA.get(category, float('inf')):
        suggestions.append(f"Great job! Your {category} practices have a sustainable carbon footprint.")
    else:
        if category == 'Electricity':
            suggestions.append("Consider using energy-efficient appliances and switch to renewable energy sources.")
        elif category == 'Transport':
            suggestions.append("Explore alternative transportation methods like cycling or public transportation.")
        elif category == 'Manufacturing':
            suggestions.append("Optimize manufacturing processes to reduce waste and energy consumption.")
        elif category == 'Construction':
            suggestions.append("Prioritize sustainable and recycled materials in construction projects.")
        elif category == 'Agriculture':
            suggestions.append("Implement sustainable farming practices and reduce the use of synthetic fertilizers.")
    return suggestions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/electricity', methods=['GET', 'POST'])
def electricity():
    if request.method == 'POST':
        energy_consumed = float(request.form['user_input'])
        result = calculate_electricity_footprint(energy_consumed)
        suggestions = get_suggestions(result, 'Electricity')
        return render_template('result.html', category='Electricity', result=result, suggestions=suggestions)
    return render_template('electricity.html')

@app.route('/transport', methods=['GET', 'POST'])
def transport():
    if request.method == 'POST':
        miles_driven = float(request.form['user_input_1'])
        fuel_efficiency = float(request.form['user_input_2'])
        result = calculate_transport_footprint(miles_driven, fuel_efficiency)
        suggestions = get_suggestions(result, 'Transport')
        return render_template('result.html', category='Transport', result=result, suggestions=suggestions)
    return render_template('transport.html')

@app.route('/manufacturing', methods=['GET', 'POST'])
def manufacturing():
    if request.method == 'POST':
        products_produced = float(request.form['user_input'])
        result = calculate_manufacturing_footprint(products_produced)
        suggestions = get_suggestions(result, 'Manufacturing')
        return render_template('result.html', category='Manufacturing', result=result, suggestions=suggestions)
    return render_template('manufacturing.html')

@app.route('/construction', methods=['GET', 'POST'])
def construction():
    if request.method == 'POST':
        materials_used = float(request.form['user_input'])
        result = calculate_construction_footprint(materials_used)
        suggestions = get_suggestions(result, 'Construction')
        return render_template('result.html', category='Construction', result=result, suggestions=suggestions)
    return render_template('construction.html')

@app.route('/agriculture', methods=['GET', 'POST'])
def agriculture():
    if request.method == 'POST':
        crops_grown = float(request.form['user_input'])
        result = calculate_agriculture_footprint(crops_grown)
        suggestions = get_suggestions(result, 'Agriculture')
        return render_template('result.html', category='Agriculture', result=result, suggestions=suggestions)
    return render_template('agriculture.html')

if __name__ == '__main__':
    app.run(debug=True)
