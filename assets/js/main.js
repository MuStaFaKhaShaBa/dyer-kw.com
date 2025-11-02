(function () {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector("body");
    const selectHeader = document.querySelector("#header");
    if (
      !selectHeader.classList.contains("scroll-up-sticky") &&
      !selectHeader.classList.contains("sticky-top") &&
      !selectHeader.classList.contains("fixed-top")
    )
      return;
    window.scrollY > 100
      ? selectBody.classList.add("scrolled")
      : selectBody.classList.remove("scrolled");
  }

  document.addEventListener("scroll", toggleScrolled);
  window.addEventListener("load", toggleScrolled);

  /**a
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector(".mobile-nav-toggle");

  function mobileNavToogle() {
    document.querySelector("body").classList.toggle("mobile-nav-active");
    mobileNavToggleBtn.classList.toggle("bi-list");
    mobileNavToggleBtn.classList.toggle("bi-x");
  }
  mobileNavToggleBtn.addEventListener("click", mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll("#navmenu a").forEach((navmenu) => {
    navmenu.addEventListener("click", () => {
      if (document.querySelector(".mobile-nav-active")) {
        mobileNavToogle();
      }
    });
  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll(".navmenu .toggle-dropdown").forEach((navmenu) => {
    navmenu.addEventListener("click", function (e) {
      e.preventDefault();
      this.parentNode.classList.toggle("active");
      this.parentNode.nextElementSibling.classList.toggle("dropdown-active");
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector("#preloader");
  if (preloader) {
    window.addEventListener("load", () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector(".scroll-top");

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100
        ? scrollTop.classList.add("active")
        : scrollTop.classList.remove("active");
    }
  }
  scrollTop.addEventListener("click", (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  });

  window.addEventListener("load", toggleScrollTop);
  document.addEventListener("scroll", toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: "ease-in-out",
      once: true,
      mirror: false,
    });
  }
  window.addEventListener("load", aosInit);

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function (swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);
})();


const words = [
  "صباغ محترف",
  "أعمال صبغ متكاملة",
  "مقاولات عامة",
  "صباغ الكويت",
  "صبغ جوتن عالي الجودة",
  "دهان بدون ريحة",
  "تركيب ورق جدران",
  "تصاميم عصرية",
  "أصباغ داخلية وخارجية",
  "رقم صباغ: 99201288",
  "اتصل الآن",
  "صباغ أبو عبدالله",
  "تشطيب فاخر للمنازل",
  "أسعار مناسبة وجودة عالية",
  "ألوان مودرن وهادئة",
];

// تدرجات لونية مختلفة بنفس ترتيب الكلمات
const gradients = [
  "linear-gradient(270deg, #ff6a00, #ee0979, #ff6a00)",
  "linear-gradient(270deg, #00c6ff, #0072ff)",
  "linear-gradient(270deg, #43cea2, #185a9d)",
  "linear-gradient(270deg, #f7971e, #ffd200)",
  "linear-gradient(270deg, #8360c3, #2ebf91)",
  "linear-gradient(270deg, #ff512f, #dd2476)",
  "linear-gradient(270deg, #4568dc, #b06ab3)",
  "linear-gradient(270deg, #6a11cb, #2575fc)",
  "linear-gradient(270deg, #00b09b, #96c93d)",
  "linear-gradient(270deg, #f12711, #f5af19)",
  "linear-gradient(270deg, #f953c6, #b91d73)",
  "linear-gradient(270deg, #e65c00, #F9D423)",
  "linear-gradient(270deg, #00c3ff, #ffff1c)",
  "linear-gradient(270deg, #654ea3, #eaafc8)",
  "linear-gradient(270deg, #dce35b, #45b649)",
];

let currentWord = 0;
const textWrapper = document.querySelector(".ml1 .letters");

function animateWord(word) {
  // غيّر النص
  textWrapper.textContent = word;

  // غيّر التدرج حسب ترتيب الكلمة
  const gradient = gradients[currentWord % gradients.length];
  textWrapper.style.background = gradient;

  anime.timeline()
    .add({
      targets: ".ml1 .letters",
      scale: [0.8, 1],
      opacity: [0, 1],
      translateZ: 0,
      easing: "easeOutExpo",
      duration: 600,
    })
    .add({
      targets: ".ml1 .line",
      scaleX: [0, 1],
      opacity: [0.5, 1],
      easing: "easeOutExpo",
      duration: 700,
      offset: "-=400",
    })
    .add({
      targets: ".ml1",
      opacity: 0,
      duration: 1000,
      easing: "easeOutExpo",
      delay: 1000,
      complete: () => {
        currentWord = (currentWord + 1) % words.length;
        textWrapper.parentElement.parentElement.style.opacity = 1;
        animateWord(words[currentWord]);
      },
    });
}

animateWord(words[currentWord]);
