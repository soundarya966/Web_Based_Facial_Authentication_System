window.onload = () => {
    const video = document.getElementById("video");

    if (!video) {
        console.error("Video element not found");
        return;
    }

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(err => {
            console.error("Camera error:", err);
        });
};

function capture() {
    const video = document.getElementById("video");
    const canvas = document.createElement("canvas");

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    canvas.getContext("2d").drawImage(video, 0, 0);

    fetch("/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ image: canvas.toDataURL("image/jpeg") })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.status;
    });
}
