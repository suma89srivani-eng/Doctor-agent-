def get_triage_level(user_input: str):
    """
    Determines urgency level based on symptoms.
    """
    symptoms = user_input.lower()

    urgent_keywords = ["chest pain", "difficulty breathing", "severe bleeding", "unconscious"]
    moderate_keywords = ["fever", "persistent cough", "vomiting", "dizziness"]

    if any(word in symptoms for word in urgent_keywords):
        return "🔴 Urgent: Seek immediate medical attention"

    if any(word in symptoms for word in moderate_keywords):
        return "🟠 Early Consultation Recommended"

    return "🟢 Routine Care / Monitor Symptoms"
