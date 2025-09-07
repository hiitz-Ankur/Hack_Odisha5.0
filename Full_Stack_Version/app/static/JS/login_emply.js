document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            email: email,
            password: password
        })
    });

    const data = await response.json();
    console.log(data);

    if (response.ok) {
        localStorage.setItem("token", data.access_token); // save JWT
        alert("Login successful!");
        window.location.href = "employee.html";  // redirect after login
    } else {
        alert("Error: " + data.detail);
    }
});
