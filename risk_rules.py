def analyze_text(text):
    """
    This function performs a very simple rule-based analysis.
    It does not replace legal review and only highlights potential risks.
    """

    risks = []
    text = text.lower()

    if "personal data" in text or "personal information" in text:
        risks.append(
            "GDPR Risk: The text refers to personal data. "
            "A lawful basis for processing should be clearly stated."
        )

    if "ai system" in text or "automated decision" in text:
        risks.append(
            "AI Act Risk: Automated decision-making detected. "
            "Transparency and human oversight may be required."
        )

    if "third party" in text or "third-party" in text:
        risks.append(
            "Compliance Risk: Data sharing with third parties is mentioned. "
            "Data transfer conditions should be reviewed."
        )

    if "consent" not in text:
        risks.append(
            "GDPR Warning: No clear reference to user consent was found."
        )

    return risks
