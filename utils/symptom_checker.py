def analyze_symptoms(user_input: str):
    """
    Basic symptom keyword extraction and possible condition matching.
    Replace this with your AI/LLM logic if needed.
    """
    symptoms = user_input.lower()

    possible_conditions = []

    if "fever" in symptoms and "cough" in symptoms:
        possible_conditions.append("Flu or viral infection")

    if "headache" in symptoms and "nausea" in symptoms:
        possible_conditions.append("Migraine")

    if "chest pain" in symptoms:
        possible_conditions.append("Cardiac or respiratory concern")

    if not possible_conditions:
        possible_conditions.append("General medical evaluation recommended")

    return possible_conditions
