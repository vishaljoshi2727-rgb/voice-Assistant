const startBtn = document.getElementById("startBtn");

startBtn.onclick = () => {

    if (!assistantRunning) {

        assistantRunning = true;

        recognition.start();

        startBtn.innerText = "Assistant Running";
    }
};
const chat = document.getElementById("chat");

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.continuous = false;
recognition.interimResults = false;
recognition.lang = "en-US";

let assistantRunning = false;

recognition.onresult = async (event) => {

    const text = event.results[0][0].transcript;

    console.log("User:", text);

    const response = await fetch("/command", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text
        })
    });

    const data = await response.json();

    speak(data.response);
};

recognition.onend = () => {

    if (assistantRunning) {

        setTimeout(() => {

            recognition.start();

        }, 500);
    }
};

recognition.onerror = (event) => {

    console.log("Speech Error:", event.error);

    if (assistantRunning) {

        setTimeout(() => {

            recognition.start();

        }, 1000);
    }
};


function addMessage(text,type){

    let div =
    document.createElement("div");

    div.classList.add("message");
    div.classList.add(type);

    div.innerText=text;

    chat.appendChild(div);

    chat.scrollTop=chat.scrollHeight;
}


function speak(text) {

    const speech = new SpeechSynthesisUtterance(text);

    speech.rate = 1;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech);
}