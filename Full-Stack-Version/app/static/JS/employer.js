document.addEventListener("DOMContentLoaded", () => {
    const jobForm = document.getElementById("jobForm");

    jobForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const token = localStorage.getItem("token");  // Employer must be logged in

        if (!token) {
            alert("⚠️ Please login first.");
            window.location.href = "/employer_login";
            return;
        }

        // Collect form values
        const jobData = {
            description: document.getElementById("descrip").value,
            location: document.getElementById("location").value,
            pincode: document.getElementById("pincode").value,
            requirement: document.getElementById("requirement").value,
            occupation: document.getElementById("Occup").value,
            price: document.getElementById("price").value,
            quantity: document.getElementById("Qty").value,
            from_date: document.getElementById("fdate").value,
            from_time: document.getElementById("ftime").value,
            to_date: document.getElementById("tdate").value,
            to_time: document.getElementById("ttime").value
        };

        try {
            const response = await fetch("/jobs", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${token}` // ✅ secure
                },
                body: JSON.stringify(jobData)
            });

            const data = await response.json();

            if (response.ok) {
                alert("✅ Job posted successfully!");
                console.log("Job created:", data);
                jobForm.reset();
            } else {
                alert("❌ Failed to post job: " + (data.detail || "Unknown error"));
            }
        } catch (err) {
            console.error("Error:", err);
            alert("⚠️ Something went wrong while posting job.");
        }
    });
});
