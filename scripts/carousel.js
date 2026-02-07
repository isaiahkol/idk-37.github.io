(function () {
  function setupCarousel(root) {
    const items = Array.from(root.querySelectorAll(".window img, .window video"));
    const prev = root.querySelector("[data-prev]");
    const next = root.querySelector("[data-next]");
    const counter = root.querySelector("[data-counter]");

    if (!items.length) return;

    let index = items.findIndex(el => el.classList.contains("active"));
    if (index < 0) index = 0;

    function stopVideo(el) {
      if (el && el.tagName === "VIDEO") {
        el.pause();
        el.currentTime = 0;
      }
    }

    function show(i) {
      // wrap
      if (i < 0) i = items.length - 1;
      if (i >= items.length) i = 0;

      // hide old
      stopVideo(items[index]);
      items[index].classList.remove("active");

      // show new
      index = i;
      items[index].classList.add("active");

      if (counter) counter.textContent = `${index + 1} / ${items.length}`;
    }

    prev?.addEventListener("click", () => show(index - 1));
    next?.addEventListener("click", () => show(index + 1));

    // init counter
    if (counter) counter.textContent = `${index + 1} / ${items.length}`;
  }

  window.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-carousel]").forEach(setupCarousel);
  });
})();
