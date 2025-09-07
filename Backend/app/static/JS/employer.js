// Count total inputs dynamically
  function updateInputCount() {
    const form = document.getElementById("jobForm");
    const inputs = form.querySelectorAll("input, select, textarea");
    document.getElementById("inputCount").textContent =
      "Total input fields: " + inputs.length;
  }

  // Run on load and whenever form changes
  document.addEventListener("DOMContentLoaded", updateInputCount);
  document.getElementById("jobForm").addEventListener("input", updateInputCount);

  document.addEventListener("DOMContentLoaded", () => {
    const addBtn = document.querySelector(".btn-success"); // "Add Member" button
    const memberTableBody = document.querySelector("#memberTable tbody");
    const totalMembersEl = document.getElementById("totalMembers");
    const totalPriceEl = document.getElementById("totalPrice");

    let memberCount = 0;
    let totalPrice = 0;

    addBtn.addEventListener("click", () => {
        const occupation = document.getElementById("Occup").value;
        const price = parseFloat(document.getElementById("price").value);
        const qty = parseInt(document.getElementById("Qty").value);

        if (!occupation || occupation === "Select Occupation") {
            alert("Please select an occupation");
            return;
        }
        if (isNaN(price) || price <= 0) {
            alert("Please enter a valid price");
            return;
        }
        if (isNaN(qty) || qty <= 0) {
            alert("Please enter a valid quantity");
            return;
        }

        const rowTotal = price * qty;
        memberCount += qty;
        totalPrice += rowTotal;

        // Add row to table
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${memberTableBody.children.length + 1}</td>
            <td>${occupation}</td>
            <td>₹${price}</td>
            <td>${qty}</td>
            <td>₹${rowTotal}</td>
        `;
        memberTableBody.appendChild(row);

        // Update summary
        totalMembersEl.textContent = memberCount;
        totalPriceEl.textContent = totalPrice;

        // Clear inputs
        document.getElementById("Occup").selectedIndex = 0;
        document.getElementById("price").value = "";
        document.getElementById("Qty").value = "";
    });
});
