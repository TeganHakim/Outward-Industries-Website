function loader() {
    window.scrollTo(0, 0);
    document.body.style = "overflow: hidden;";
    var loader = document.querySelector(".loader");
    loader.style.opacity = 1;
    loader.style.display = "flex";
    setTimeout(() => {
      $(".loader").fadeOut(1500);
      $(".loader-span").fadeOut(1400);
      document.body.style = "overflow-y: scroll;";
    }, 1100);
}

window.addEventListener("load", () => {
    loader();
});