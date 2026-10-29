document.addEventListener("DOMContentLoaded", () => {

const body = document.body;

const loader = document.getElementById("pageLoader");

const navbar = document.getElementById("navbar");

const menuToggle = document.getElementById("menuToggle");

const navigation = document.getElementById("navigation");

const skillBars = document.querySelectorAll(".skill-progress");


/* =====================================================
   PAGE LOADER
====================================================== */

window.addEventListener("load", () => {

    setTimeout(() => {

        if (loader) {
            loader.classList.add("loaded");
        }

    }, 450);

});


/* =====================================================
   NAVBAR SCROLL
====================================================== */

const handleScroll = () => {

    if (!navbar) return;

    if (window.scrollY > 40) {

        navbar.classList.add("scrolled");

    } else {

        navbar.classList.remove("scrolled");

    }

};

window.addEventListener(
    "scroll",
    handleScroll,
    { passive: true }
);

handleScroll();


/* =====================================================
   MOBILE MENU
====================================================== */

if (menuToggle && navigation) {

    menuToggle.addEventListener("click", () => {

        const isOpen =
            navigation.classList.toggle("open");

        menuToggle.classList.toggle(
            "active",
            isOpen
        );

        menuToggle.setAttribute(
            "aria-expanded",
            isOpen
        );

    });


    navigation
        .querySelectorAll("a")
        .forEach(link => {

            link.addEventListener(
                "click",
                () => {

                    navigation.classList.remove(
                        "open"
                    );

                    menuToggle.classList.remove(
                        "active"
                    );

                    menuToggle.setAttribute(
                        "aria-expanded",
                        "false"
                    );

                }
            );

        });

}


/* =====================================================
   SKILL BARS
====================================================== */

if ("IntersectionObserver" in window) {

    const observer =
        new IntersectionObserver(
            entries => {

                entries.forEach(entry => {

                    if (!entry.isIntersecting) {
                        return;
                    }

                    const bar =
                        entry.target;

                    const level =
                        bar.dataset.level || 0;

                    bar.style.width =
                        `${level}%`;

                    observer.unobserve(bar);

                });

            },
            {
                threshold: 0.3
            }
        );


    skillBars.forEach(bar => {

        observer.observe(bar);

    });

} else {

    skillBars.forEach(bar => {

        const level =
            bar.dataset.level || 0;

        bar.style.width =
            `${level}%`;

    });

}


/* =====================================================
   ACTIVE NAVIGATION
====================================================== */

const sections =
    document.querySelectorAll(
        "section[id]"
    );

const navLinks =
    document.querySelectorAll(
        ".navigation a"
    );


if (
    sections.length &&
    navLinks.length &&
    "IntersectionObserver" in window
) {

    const sectionObserver =
        new IntersectionObserver(
            entries => {

                entries.forEach(entry => {

                    if (!entry.isIntersecting) {
                        return;
                    }

                    const id =
                        entry.target.id;

                    navLinks.forEach(link => {

                        link.classList.remove(
                            "active"
                        );

                        if (
                            link.getAttribute(
                                "href"
                            ) === `#${id}` ||
                            link.getAttribute(
                                "href"
                            )?.endsWith(
                                `#${id}`
                            )
                        ) {

                            link.classList.add(
                                "active"
                            );

                        }

                    });

                });

            },
            {
                rootMargin:
                    "-35% 0px -55% 0px"
            }
        );


    sections.forEach(section => {

        sectionObserver.observe(section);

    });

}


/* =====================================================
   SMOOTH ANCHORS
====================================================== */

document
    .querySelectorAll('a[href^="#"]')
    .forEach(link => {

        link.addEventListener(
            "click",
            event => {

                const targetId =
                    link.getAttribute("href");

                if (
                    !targetId ||
                    targetId === "#"
                ) {
                    return;
                }

                const target =
                    document.querySelector(
                        targetId
                    );

                if (!target) {
                    return;
                }

                event.preventDefault();

                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

            }
        );

    });


/* =====================================================
   HERO MOUSE MOVEMENT
====================================================== */

const heroVisual =
    document.querySelector(
        ".hero-visual"
    );

const imageFrame =
    document.querySelector(
        ".image-frame"
    );


if (
    heroVisual &&
    imageFrame &&
    window.matchMedia(
        "(pointer: fine)"
    ).matches
) {

    heroVisual.addEventListener(
        "mousemove",
        event => {

            const rect =
                heroVisual.getBoundingClientRect();

            const x =
                event.clientX - rect.left;

            const y =
                event.clientY - rect.top;

            const centerX =
                rect.width / 2;

            const centerY =
                rect.height / 2;

            const rotateX =
                ((y - centerY) /
                    centerY) * -3;

            const rotateY =
                ((x - centerX) /
                    centerX) * 3;


            imageFrame.style.transform =
                `rotateX(${rotateX}deg)
                 rotateY(${rotateY}deg)
                 rotateZ(1deg)`;

        }
    );


    heroVisual.addEventListener(
        "mouseleave",
        () => {

            imageFrame.style.transform =
                "rotateZ(2deg)";

        }
    );

}


/* =====================================================
   SCROLL REVEAL
====================================================== */

const revealElements =
    document.querySelectorAll(
        ".section-intro, .about-grid, .skill-card, .service-card, .project-card, .experience-item, .contact-grid"
    );


revealElements.forEach(element => {

    element.style.opacity = "0";

    element.style.transform =
        "translateY(25px)";

    element.style.transition =
        "opacity 0.8s cubic-bezier(0.16,1,0.3,1), transform 0.8s cubic-bezier(0.16,1,0.3,1)";

});


if ("IntersectionObserver" in window) {

    const revealObserver =
        new IntersectionObserver(
            entries => {

                entries.forEach(entry => {

                    if (!entry.isIntersecting) {
                        return;
                    }

                    entry.target.style.opacity =
                        "1";

                    entry.target.style.transform =
                        "translateY(0)";

                    revealObserver.unobserve(
                        entry.target
                    );

                });

            },
            {
                threshold: 0.12
            }
        );


    revealElements.forEach(element => {

        revealObserver.observe(element);

    });

}


/* =====================================================
   BODY READY
====================================================== */

body.classList.add("ready");

});