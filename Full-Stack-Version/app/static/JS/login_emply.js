async function loginEmployee() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("/auth/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();

        if (response.ok) {
            alert("✅ Login successful!");
            console.log("Token:", data.access_token);

            // Save JWT token for future authenticated requests
            localStorage.setItem("token", data.access_token);

            // Redirect to employee dashboard page
            window.location.href = "/employee";
        } else {
            alert("❌ Login failed: " + data.detail);
        }
    } catch (err) {
        console.error("Error:", err);
        alert("⚠️ Something went wrong. Please try again.");
    }
}
