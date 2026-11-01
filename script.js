const menuButton = document.getElementById("menuButton");
const navMenu = document.getElementById("navMenu");

menuButton.addEventListener("click", () => {
  const isOpen = navMenu.classList.toggle("open");
  menuButton.setAttribute("aria-expanded", isOpen);
  menuButton.textContent = isOpen ? "Tutup" : "☰";
});

navMenu.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    navMenu.classList.remove("open");
    menuButton.setAttribute("aria-expanded", "false");
    menuButton.textContent = "☰";
  });
});

document.getElementById("year").textContent = new Date().getFullYear();
