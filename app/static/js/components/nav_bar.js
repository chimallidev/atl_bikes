function initNavBar() {
    const navBar = document.querySelector(".nav-bar");

    if (!navBar) {
        return;
    }


    const menuButton = navBar.querySelector(
        ".nav-bar__menu-button"
    );

    const mobileMenu = navBar.querySelector(
        ".nav-bar__mobile-menu"
    );

    const mainLevel = navBar.querySelector(
        ".nav-bar__mobile-level--main"
    );

    const subLevels = navBar.querySelectorAll(
        ".nav-bar__mobile-level--sub"
    );

    const targetButtons = navBar.querySelectorAll(
        "[data-nav-target]"
    );

    const backButtons = navBar.querySelectorAll(
        ".nav-bar__mobile-back"
    );


    /* ========================================
       SCROLL
       ======================================== */

    let lastScrollPosition = window.scrollY;

    let accumulatedScroll = 0;

    const scrollThreshold = 50;


    function handleScroll() {
        const currentScrollPosition = window.scrollY;

        const scrollDifference =
            currentScrollPosition - lastScrollPosition;


        /* ----------------------------------------
           TOP OF PAGE
           ---------------------------------------- */

        if (currentScrollPosition <= 0) {

            navBar.classList.remove("is-hidden");

            accumulatedScroll = 0;

            lastScrollPosition = currentScrollPosition;

            return;
        }


        /* ----------------------------------------
           SCROLL DOWN
           ---------------------------------------- */

        if (scrollDifference > 0) {

            accumulatedScroll += scrollDifference;


            if (accumulatedScroll >= scrollThreshold) {

                navBar.classList.add("is-hidden");

                accumulatedScroll = 0;
            }
        }


        /* ----------------------------------------
           SCROLL UP
           ---------------------------------------- */

        else if (scrollDifference < 0) {

            accumulatedScroll += Math.abs(
                scrollDifference
            );


            if (accumulatedScroll >= scrollThreshold) {

                navBar.classList.remove("is-hidden");

                accumulatedScroll = 0;
            }
        }


        lastScrollPosition = currentScrollPosition;
    }


    window.addEventListener(
        "scroll",
        handleScroll,
        {
            passive: true
        }
    );


    /* ========================================
       OPEN / CLOSE MAIN MENU
       ======================================== */

    function openMenu() {

        /*
         * La navbar siempre debe permanecer
         * visible mientras el menú está abierto.
         */

        navBar.classList.remove("is-hidden");

        navBar.classList.add("is-open");

        mobileMenu.classList.add("is-open");

        mobileMenu.setAttribute(
            "aria-hidden",
            "false"
        );

        menuButton.setAttribute(
            "aria-expanded",
            "true"
        );

        menuButton.setAttribute(
            "aria-label",
            "Cerrar menú"
        );

        resetLevels();
    }


    function closeMenu() {

        /*
         * Todos los niveles secundarios
         * desaparecen inmediatamente.
         */

        resetLevels();

        navBar.classList.remove("is-open");

        mobileMenu.classList.remove("is-open");

        mobileMenu.setAttribute(
            "aria-hidden",
            "true"
        );

        menuButton.setAttribute(
            "aria-expanded",
            "false"
        );

        menuButton.setAttribute(
            "aria-label",
            "Abrir menú"
        );
    }


    function toggleMenu() {

        const isOpen =
            navBar.classList.contains("is-open");


        if (isOpen) {

            closeMenu();

        } else {

            openMenu();
        }
    }


    /* ========================================
       RESET LEVELS
       ======================================== */

    function resetLevels() {

        mainLevel.classList.remove(
            "is-previous"
        );


        subLevels.forEach((level) => {

            level.classList.remove(
                "is-active"
            );

            level.classList.remove(
                "is-previous"
            );
        });
    }


    /* ========================================
       OPEN SUBMENU
       ======================================== */

    function openSubmenu(targetName) {

        const targetLevel = navBar.querySelector(
            `[data-nav-level="${targetName}"]`
        );


        if (!targetLevel) {
            return;
        }


        mainLevel.classList.add(
            "is-previous"
        );


        targetLevel.classList.add(
            "is-active"
        );
    }


    /* ========================================
       CLOSE SUBMENU
       ======================================== */

    function closeSubmenu(button) {

        const currentLevel = button.closest(
            ".nav-bar__mobile-level"
        );


        if (!currentLevel) {
            return;
        }


        currentLevel.classList.remove(
            "is-active"
        );


        mainLevel.classList.remove(
            "is-previous"
        );
    }


    /* ========================================
       MENU BUTTON
       ======================================== */

    menuButton.addEventListener(
        "click",
        toggleMenu
    );


    /* ========================================
       SUBMENU BUTTONS
       ======================================== */

    targetButtons.forEach((button) => {

        button.addEventListener(
            "click",
            () => {

                const target =
                    button.dataset.navTarget;

                openSubmenu(target);
            }
        );
    });


    /* ========================================
       BACK BUTTONS
       ======================================== */

    backButtons.forEach((button) => {

        button.addEventListener(
            "click",
            () => {

                closeSubmenu(button);
            }
        );
    });


    /* ========================================
       ESC
       ======================================== */

    document.addEventListener(
        "keydown",
        (event) => {

            if (event.key !== "Escape") {
                return;
            }


            if (
                navBar.classList.contains(
                    "is-open"
                )
            ) {

                closeMenu();
            }
        }
    );


    /* ========================================
       RESIZE
       ======================================== */

    window.addEventListener(
        "resize",
        () => {

            if (window.innerWidth > 1024) {

                closeMenu();
            }
        }
    );
}


export {
    initNavBar
};