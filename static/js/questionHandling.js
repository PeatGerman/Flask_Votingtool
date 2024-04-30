function addQuestionField() {
    const questionContainer = document.getElementById('questionsContainer');
    const numQuestions = questionContainer.children.length + 1;

    const questionField = document.createElement('div');
    questionField.className = 'form-group question-field';
    questionField.id = 'questionField' + numQuestions;

    const card = document.createElement('div');
    card.className = 'card mb-3';

    const cardBody = document.createElement('div');
    cardBody.className = 'card-body';

    const cardTitle = document.createElement('h5');
    cardTitle.className = 'card-title';
    cardTitle.textContent = 'Frage';
    cardBody.appendChild(cardTitle);

    const questionInput = document.createElement('input');
    questionInput.type = 'text';
    questionInput.className = 'form-control mb-2';
    questionInput.id = 'question' + numQuestions;
    questionInput.name = `questions[${numQuestions}]`;
    questionInput.placeholder = 'Frage eingeben...';
    questionInput.required = true;
    cardBody.appendChild(questionInput);

    // Der Rest der Frageerstellungsfunktion hier...
    questionContainer.appendChild(questionField);
}

function removeQuestionField(questionIndex) {
    const questionToRemove = document.getElementById('questionField' + questionIndex);
    questionToRemove.remove();
}

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('addQuestion').addEventListener('click', addQuestionField);
});
