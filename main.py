from risk_rules import analyze_text

def read_text_from_file(file_path):
    """
    Reads text from a file and returns it as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return ""


def main():
    print("AI Legal Risk Analyzer")
    print("----------------------")
    print("This tool performs a basic legal risk check.\n")

    choice = input("Do you want to analyze a sample text file? (yes/no): ").lower()

    if choice == "yes":
        text = read_text_from_file("sample_texts/privacy_policy.txt")
        if not text:
            print("No text found.")
            return
    else:
        text = input("\nPaste the legal text you want to analyze:\n\n")

    risks = analyze_text(text)

    if not risks:
        print("\nNo major legal risks were detected.")
        print("This does NOT mean the text is legally compliant.")
    else:
        print("\nPotential legal risks found:\n")
        for risk in risks:
            print(f"- {risk}")


if __name__ == "__main__":
    main()
