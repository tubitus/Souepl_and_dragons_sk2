const questions = [
    {
      question: "Jaké je hlavní město České republiky?",
      answers: [
        { text: "Praha", correct: true },
        { text: "Brno", correct: false },
        { text: "Ostrava", correct: false },
        { text: "Plzeň", correct: false },
      ],
    },
    {
      question: "Kolik nohou má pavouk?",
      answers: [
        { text: "6", correct: false },
        { text: "8", correct: true },
        { text: "10", correct: false },
        { text: "12", correct: false },
      ],
    },
    {
      question: "Jaké je největší zvíře na světě?",
      answers: [
        { text: "Slon", correct: false },
        { text: "Modrá velryba", correct: true },
        { text: "Žirafa", correct: false },
        { text: "Medvěd", correct: false },
      ],
    },
  ];
  
  const questionText = document.getElementById("question-text");
  const answerButtons = document.getElementById("answer-buttons");
  const nextButton = document.getElementById("next-btn");
  
  let currentQuestionIndex = 0;
  let score = 0;
  
  function startQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    nextButton.innerText = "Další";
    showQuestion();
  }
  
  function showQuestion() {
    resetState();
    const currentQuestion = questions[currentQuestionIndex];
    questionText.innerText = currentQuestion.question;
  
    currentQuestion.answers.forEach((answer) => {
      const button = document.createElement("button");
      button.innerText = answer.text;
      button.classList.add("btn");
      if (answer.correct) {
        button.dataset.correct = answer.correct;
      }
      button.addEventListener("click", selectAnswer);
      answerButtons.appendChild(button);
    });
  }
  
  function resetState() {
    nextButton.style.display = "none";
    while (answerButtons.firstChild) {
      answerButtons.removeChild(answerButtons.firstChild);
    }
  }
  
  function selectAnswer(e) {
    const selectedButton = e.target;
    const correct = selectedButton.dataset.correct === "true";
    if (correct) score++;
    Array.from(answerButtons.children).forEach((button) => {
      setStatusClass(button, button.dataset.correct === "true");
    });
    nextButton.style.display = "block";
  }
  
  function setStatusClass(element, correct) {
    clearStatusClass(element);
    if (correct) {
      element.classList.add("correct");
    } else {
      element.classList.add("wrong");
    }
  }
  
  function clearStatusClass(element) {
    element.classList.remove("correct");
    element.classList.remove("wrong");
  }
  
  function showScore() {
    resetState();
    questionText.innerText = `Kvíz dokončen! Tvůj skóre je ${score} z ${questions.length}.`;
    nextButton.innerText = "Restartovat";
    nextButton.style.display = "block";
  }
  
  function handleNextButton() {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
      showQuestion();
    } else {
      showScore();
    }
  }
  
  nextButton.addEventListener("click", () => {
    if (currentQuestionIndex < questions.length) {
      handleNextButton();
    } else {
      startQuiz();
    }
  });
  
  startQuiz();
  