function clearSurvey() {
    const surveyForm = document.getElementById('surveyForm');
    surveyForm.reset();
    const questionsContainer = document.getElementById('questionsContainer');
    questionsContainer.innerHTML = '';
    addQuestionField();
}

document.getElementById('surveyForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // Hier könnte eine Validierung oder ein anderer vor dem Absenden nötiger Code hinzugefügt werden.
    alert('Umfrage erfolgreich gesendet!'); // Nur ein Platzhalter für Feedback
});
