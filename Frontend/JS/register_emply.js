document.getElementById("registerForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:8000/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            name: name,
            email: email,
            password: password,
            role: "freelancer" // fixed for employee
        })
    });

    const data = await response.json();
    console.log(data);

    if (response.ok) {
        alert("Registration successful!");
        window.location.href = "login_emply.html";
    } else {
        alert("Error: " + data.detail);
    }
});