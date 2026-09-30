async function generateComic() {
    const prompt = document.getElementById("prompt").value.trim();
    const result = document.getElementById("result");

    if (!prompt) {
        result.innerHTML = "<p>Please enter a story idea.</p>";
        return;
    }

    result.innerHTML = "<h2>Creating Comic...</h2>";

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({prompt})
        });

        const data = await response.json();

        result.innerHTML = `
            <h2>${data.title}</h2>
            <div class="panels">
                ${data.panels.map((panel, i) => `
                    <div class="panel">
                        <span>Panel ${i + 1}</span>
                        <p>${panel}</p>
                    </div>
                `).join("")}
            </div>
        `;
    } catch (error) {
        result.innerHTML = "<p>Something went wrong.</p>";
    }
}
