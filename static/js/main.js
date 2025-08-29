// Navegación de secciones (mostrar/ocultar)
document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".navbtn");
  const sections = document.querySelectorAll(".section");

  function showSection(id) {
    sections.forEach(s => s.classList.remove("visible"));
    document.getElementById(id).classList.add("visible");

    buttons.forEach(b => b.classList.remove("active"));
    const btn = document.querySelector(`.navbtn[data-section="${id}"]`);
    if (btn) btn.classList.add("active");
    history.replaceState({}, "", `#${id}`); // opcional: actualiza hash
  }

  // click handlers
  buttons.forEach(b => {
    b.addEventListener("click", () => showSection(b.dataset.section));
  });

  // sección inicial (por hash o inicio)
  const initial = location.hash?.replace("#", "") || "inicio";
  showSection(initial);
});
