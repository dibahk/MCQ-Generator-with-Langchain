# **MCQ Generator using LangChain, GPT-3.5 Turbo, and Streamlit**

A tool for generating multiple-choice questions from uploaded PDF or .txt files. Users can customize the difficulty level, number of questions, and subject area.

---

## **Features**
- **Upload File**: Accepts PDF or .txt files as input.
- **Customizable Options**: 
  - Choose the difficulty level (Easy, Medium, Hard).
  - Set the number of questions to generate.
  - Specify the subject area for the questions.
- **Interactive UI**: Built with Streamlit for a seamless user experience.
- **Powered by AI**: Utilizes LangChain and GPT-3.5 Turbo for question generation.

---

## **Installation**

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/username/repo-name.git](https://github.com/dibahk/MCQ-Generator-with-Langchain.git)

2. Set environment variables:
  ```bash
export OPENAI_API_KEY='your_openAI_key'
``` 
3. Navigate to the project directory:
  ```bash
  cd MCQ-Generator-with-Langchain
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Run the Streamlit application:
```bash
streamlit run app.py
```
## **Usage**

1. Launch the app using the command:
   `streamlit run app.py`
2. Upload a `.pdf` or `.txt` file via the upload button.
3. Select your preferences:
   - **Difficulty level** (Easy, Medium, Hard)
   - **Number of questions**
   - **Subject of the questions**
4. View and download the generated multiple-choice questions.

---

## **Tech Stack**

- **LangChain**: For orchestrating prompts and managing the question-generation workflow.
- **GPT-3.5 Turbo**: The AI model for generating high-quality multiple-choice questions.
- **Streamlit**: Provides an interactive and user-friendly web application interface.

---

## **Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   `git checkout -b feature-name`
3. Make your changes and commit:
   `git commit -m "Add feature"`
4. Push to your fork:
   `git push origin feature-name`
5. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Acknowledgments**

- [OpenAI GPT-3.5 Turbo](https://platform.openai.com/)
- [LangChain](https://langchain.com/)
- [Streamlit](https://streamlit.io/)
