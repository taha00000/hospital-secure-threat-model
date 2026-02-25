"""
Simple Risk Assessment Calculator for Security Architecture
Formula: Risk = Impact * Probability
"""

def calculate_risk_level(impact, probability):
    # Scale of 1 to 3 (1=Low, 2=Medium, 3=High)
    score = impact * probability
    
    if score >= 6:
        return "HIGH - Urgent Mitigation Required"
    elif score >= 3:
        return "MEDIUM - Mitigation Planned"
    else:
        return "LOW - Accept/Monitor"

# Example Scenario: Information Disclosure of PHI
impact_val = 3 # High
prob_val = 2   # Medium
print(f"Risk Assessment for PHI Leak: {calculate_risk_level(impact_val, prob_val)}")
