# Her Story
#### Video Demo:  <https://youtu.be/92fNFrMRrXU>
#### Description: The project is a questionnaire inspired by the Korean novel Kim Ji-young, Born 1982.
This project aims to create an interactive web-based questionnaire inspired by the themes of gender inequality presented in the Korean novel Kim Ji-young, Born 1982. The questionnaire will allow users to explore societal issues related to gender roles and gender inequality, as depicted in the novel, by answering a series of questions. The goal is to raise awareness about gender-related challenges and provoke thought on how these issues impact individuals in everyday life.

## Folder Structure

The project is organized into four main components: three folders (`instance`, `static`, `templates`) and one file (`app.py`). Each of these components serves a specific purpose in the development and functioning of the application.

### 1. `intance` folder
- `question_bank_answers.csv`: A CSV file that contains the answers of the questionnaire. This file includes the id and question text for each question.
- `question_bank_questions.csv`: A CSV file that contains the questions of the questionnaire. This file includes metadata for each answer: answer id, question id, answer text, and the correction of the answer (true/false).
- `questionbank.db`: A database stores the CSV files above, which will be used for generating the questionnaire.

### 2. `static` folder
- `images` folder: This folder stores all images used in the project, which include the visual elements used in the layout page and infographics related to gender inequality.
- `style.css`: A CSS file that defines the styling for all the webpages. The stylesheet will handle layout, typography, color scheme, etc.

### 3. `templates` folder

- `layout.html`: The base template for all the web pages, which includes the header element, the footer element, and the title and subtitle elements.

- `index.html`: The landing page of the questionnaire. This page introduces the user to the questionnaire, provides an overview of the purpose, and includes a "Start" button that navigates to `question.html` to begin the survey.

- `question.html`: The main page where users answer the questions.
    - *Bootstrap*
        - *carousel*: The carousel allows users to navigate between questions via left and right controls.
        - *form-check radio button*: For each question, a set of radio buttons will be used for users to select their answers, ensuring a consistent interface.
    - *Jinja*: Loop through questions and display them dynamically, along with the selections.
    - *JavaScript*: Control the behavior of the "Previous" and "Next" buttons. Specifically, the "Previous" button will be hidden on the first slide, and the "Next" button will be hidden on the last slide. The "Submit" button will only appear on the last slide, and once you click the button, the form will be submitted and move to `result.html`.

- `result.html`:
    - Graph of Sex Ratio at Birth: A graph illustrating the sex ratio at birth (male births per female births) will be displayed, as a visual representation of gender inequality. The figure and figcaption HTML tags will be used to present the graph with a description for context.
    - The user's answers: Compared with a "correct" answer list. The comparison results will be categorized into:
        - The correct selected selection.
        - The correct unselected selection.
        - The incorrectly selected selection.
        - The incorrect unselected selection.
    - Radio Button Disabled Attribute: To ensure that no further changes can be made to the answers after submission, the radio buttons will be disabled using the disabled attribute.

- `apology.html`: If the user tries to submit the questionnaire without answering all the questions, they will be redirected to this page. This page will apologize for the incomplete submission and inform the user that they need to complete the questionnaire. It will also include a "Back to Question" button that redirects the user to the `question.html` to finish answering the questions.

### 4. `app.py`
This Python file will be the backend of the application, handling routing, database interaction, and form processing.
- Route `/`: Renders the `index.html`, which introduces the questionnaire and allows users to start the survey.
- Route `question`: Get the question text and selections from the `questionbank.db` using SQL queries. The data is passed to the question.html template to dynamically generate the `question.html`.
- Route `result`: This route processes the user’s responses once they submit the questionnaire.
    - Get the question text and selections from the database.
    - Get the user's answers from the submitted form.
        - If the user’s answers are incomplete (less than 7 questions answered), they are redirected to `apology.html`.
    - Create a list of correct answers per question, which will be used at `result.html` to compare with the user's selection.
    - Pass the question text, selections, variables, user's selections, and correct answers to `result.html`.

## Technologies Used:
Frontend:
- HTML5: For structuring the content of the questionnaire and result pages.
- CSS: For styling the pages with a responsive design.
- JavaScript: For interactive elements such as button visibility and form submission.
- Bootstrap: For responsive design, carousel layout, and other UI components.
- Jinja: For rendering dynamic content from the database.

Backend:
- Flask: For routing, form handling, and rendering HTML pages.
- SQL: For storing the questionnaire data, `questionbank.db`.
