function loader() {
    window.scrollTo(0, 0);
    document.body.style = "overflow: hidden;";
    var loader = document.querySelector(".loader");
    loader.style.opacity = 1;
    loader.style.display = "flex";
    setTimeout(() => {
      $(".loader-span").fadeOut(2000);
    }, 1100);
    setTimeout(() => {
      $(".loader").fadeOut(1000);
      document.body.style = "overflow-y: scroll;";
    }, 1800);
}

window.addEventListener("load", () => {
    loader();
});