import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            # Use PdfReader instead of PdfFileReader due to deprecation
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                # Ensure extract_text is called correctly
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text

        except Exception as e:
            print(f"Error: {e}")
            raise Exception("Error reading the PDF file")

    elif file.name.endswith(".txt"):
        try:
            # Handling text files
            return file.read().decode("utf-8")
        except Exception as e:
            print(f"Error: {e}")
            raise Exception("Error reading the text file")

    else:
        raise Exception("Unsupported file format. Only PDF and text files are supported.")


def get_table_data(quiz_str):
    try:
        # convert the quiz from a str to dict
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        # iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq = value.get("mcq", "No Question Found")
            options = " || ".join(
                [
                    f"{option}-> {option_value}" 
                    for option, option_value in value.get("options", {}).items()
                ]
            )

            correct = value.get("correct", "No Correct Answer")
            quiz_table_data.append({
                "MCQ": mcq,
                "Choices": options,
                "Correct": correct
            })

        return quiz_table_data

    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
    except Exception as e:
        print(f"General Error: {e}")
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
