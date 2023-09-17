const onLoad = () => {
  const darkImage = document.querySelector("#hero-image-dark");
  const lightImage = document.querySelector("#hero-image-light");

  if ($darkmode.currentMode === "dark") lightImage.classList.add("hidden");
  else darkImage.classList.add("hidden");
};

window.addEventListener("app:mounted", onLoad, { once: true });
