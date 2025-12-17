document.addEventListener("DOMContentLoaded", () => {
  const links = document.querySelectorAll(".nav-link");
  const sections = document.querySelectorAll(".section");

  links.forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();

      // retire 'active' de tous les liens
      links.forEach(l => l.classList.remove("active"));
      link.classList.add("active");

      const target = link.getAttribute("data-section");

      // masque toutes les sections
      sections.forEach(sec => sec.classList.add("d-none"));
      // affiche la section ciblée
      document.getElementById(target).classList.remove("d-none");
    });
  });
});
