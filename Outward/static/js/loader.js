function loader() {
  window.scrollTo(0, 0);
  if (window.innerWidth < 768) {
  document.documentElement.style = "overflow-y: hidden !important;";
  setTimeout(() => {
      $(".loader-span").fadeOut(1700);
  }, 1000);
  setTimeout(() => {
      $(".loader").fadeOut(1000);
      document.documentElement.style = "overflow-y: scroll !important;";
  }, 1600);
  } else {
      document.documentElement.style = "overflow-y: hidden !important;";
      var loader = document.querySelector(".loader");
      loader.style.opacity = 1;
      loader.style.display = "flex";
      setTimeout(() => {
        $(".loader-span").fadeOut(2000);
      }, 1100);
      setTimeout(() => {
        $(".loader").fadeOut(1000);
        document.documentElement.style = "overflow-y: scroll !important;";
      }, 1800);
  }
}

window.addEventListener("load", () => {
    loader();
});