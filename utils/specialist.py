def suggest_specialist(user_input: str):
    """
    Suggests the most relevant medical specialist.
    """
    symptoms = user_input.lower()

    if "skin" in symptoms or "rash" in symptoms:
        return "Dermatologist"

    if "chest pain" in symptoms or "heart" in symptoms:
        return "Cardiologist"

    if "headache" in symptoms or "migraine" in symptoms:
        return "Neurologist"

    if "stomach" in symptoms or "abdominal pain" in symptoms:
        return "Gastroenterologist"

    if "fever" in symptoms or "cough" in symptoms:
        return "General Physician"

    return "General Physician"
