const form = document.getElementById("newsForm");
const resultDiv = document.getElementById("result");
const resultText = document.getElementById("resultText");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const newsInput = document.getElementById("newsInput").value;

  // Display loading state
  resultDiv.classList.remove("hidden");
  resultText.textContent = "Checking...";

  // Call the API
  const response = await fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `news=${encodeURIComponent(newsInput)}`,
  });

  const data = await response.json();

  // Display the result
  resultText.textContent = `This news is: ${data.result}`;
});
