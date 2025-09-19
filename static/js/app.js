// Punto de entrada JS (sin lógica aún)
document.addEventListener("DOMContentLoaded", () => {
  // Placeholder: setear año en el footer
  const y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  // Hooks de ejemplo (sin implementar):
  // const addBtn = document.querySelector('[data-action="add-to-cart"]');
  // addBtn?.addEventListener("click", (e) => {
  //   e.preventDefault();
  //   // TODO: lógica de carrito (fetch, localStorage, etc.)
  // });
});
