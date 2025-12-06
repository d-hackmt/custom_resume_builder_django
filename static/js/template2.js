let dayNight = document.querySelector(".dayNight");
let banner = document.querySelector(".banner");

dayNight.addEventListener("click", () => {
  banner.classList.toggle("night");
});
let typingEffect = new Typed("#text", {
  strings: expertFields,
  loop: true,
  typeSpeed: 100,
  backSpeed: 100,
  backDelay: 1000,
});
