document.querySelectorAll(".atl-categories").forEach((categories) => {

    const items = categories.querySelectorAll(
        ".atl-categories__item"
    );

    const touchDevice = window.matchMedia(
        "(hover: none) and (pointer: coarse)"
    );


    items.forEach((item) => {

        /* =================================================
           PC
           ================================================= */

        item.addEventListener("mouseenter", () => {

            if (touchDevice.matches) {
                return;
            }

            categories.style.backgroundColor =
                item.dataset.color;
        });


        item.addEventListener("mouseleave", () => {

            if (touchDevice.matches) {
                return;
            }

            categories.style.backgroundColor = "";
        });


        /* =================================================
           TOUCH
           ================================================= */

        item.addEventListener("pointerdown", () => {

            if (!touchDevice.matches) {
                return;
            }

            categories.style.backgroundColor =
                item.dataset.color;
        });


        item.addEventListener("pointerup", () => {

            if (!touchDevice.matches) {
                return;
            }

            categories.style.backgroundColor = "";
        });


        item.addEventListener("pointercancel", () => {

            if (!touchDevice.matches) {
                return;
            }

            categories.style.backgroundColor = "";
        });


        item.addEventListener("pointerleave", () => {

            if (!touchDevice.matches) {
                return;
            }

            categories.style.backgroundColor = "";
        });

    });

});