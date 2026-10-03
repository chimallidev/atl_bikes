/**
 * Inicializa las animaciones de los logos
 * de las tarjetas de marcas ATL.
 */
export function initAtlBrandsCard() {

    const brandLogos = document.querySelectorAll(
        ".atl-brands-card__logo"
    );


    if (!brandLogos.length) {
        return;
    }


    const observer = new IntersectionObserver(
        (entries, observer) => {

            entries.forEach((entry) => {

                if (!entry.isIntersecting) {
                    return;
                }


                entry.target.classList.add("is-visible");


                observer.unobserve(entry.target);

            });

        },
        {
            threshold: 0.2
        }
    );


    brandLogos.forEach((logo) => {
        observer.observe(logo);
    });

}