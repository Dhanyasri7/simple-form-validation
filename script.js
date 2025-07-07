function validateForm() {
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();

  if (name === "" || email === "") {
    alert("❌ Error: All fields must be filled!");
    return false;
  }

  if (!email.includes("@")) {
    alert("❌ Error: Email must contain '@'!");
    return false;
  }

  return true; // allow form submission
}
