document.getElementById("colorPicker").addEventListener("input", function () {
  document.querySelector(".left-side").style.backgroundColor = this.value;
});

document
  .getElementById("leftSidePicker")
  .addEventListener("input", function () {
    let elements = document.querySelectorAll("p, h2, h3, h4, h5, span, li");
    elements.forEach((el) => {
      el.style.color = this.value;
    });
  });

function saveResume() {
  const element = document.querySelector(".container"); // Capture the entire resume container

  html2canvas(element, {
    scale: 2, // Increases resolution
    width: element.scrollWidth, // Ensures proper width
    height: element.scrollHeight, // Ensures full height
  }).then((canvas) => {
    const link = document.createElement("a");
    link.download = "resumes.png";
    link.href = canvas.toDataURL("image/png");
    link.click();
  });
}
