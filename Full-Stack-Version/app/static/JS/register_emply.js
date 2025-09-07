async function registerEmployee() {
    const fname = document.getElementById("fname").value;
    const lname = document.getElementById("lname").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm_password").value;

    // Optional extra fields
    const bday = document.getElementById("bday").value;
    const phone_number = document.getElementById("phone_number").value;
    const occupation = document.getElementById("occupation").value;
    const experience = document.getElementById("experience").value;

    if (password !== confirmPassword) {
        alert("❌ Passwords do not match!");
        return;
    }

    try {
        const response = await fetch("/users/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name: `${fname} ${lname}`,
                email,
                password,
                bday,
                phone_number,
                occupation,
                experience
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert("✅ Registration successful! Please login.");
            console.log("New user:", data);

            // Redirect to login page
            window.location.href = "/employee_login";
        } else {
            alert("❌ Registration failed: " + data.detail);
        }
    } catch (err) {
        console.error("Error:", err);
        alert("⚠️ Something went wrong. Please try again.");
    }
}
