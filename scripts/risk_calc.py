"""
Simple Risk Assessment Calculator for Security Architecture
Formula: Risk = Impact * Probability
"""

def calculate_risk(name, impact, probability):
    score = impact * probability
    if score >= 6:
        status = "HIGH - Urgent Mitigation Required"
    elif score >= 3:
        status = "MEDIUM - Mitigation Planned"
    else:
        status = "LOW - Accept/Monitor"
    
    print(f"[{name}] Score: {score} | Level: {status}")

# Assessment based on STRIDE Analysis
calculate_risk("PHI Disclosure", 3, 3)  # High impact, high probability
calculate_risk("Appointment Tampering", 3, 2) # High impact, medium probability
calculate_risk("Service DoS", 2, 2) # Medium impact, medium probability
