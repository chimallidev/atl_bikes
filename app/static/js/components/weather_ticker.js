 /* ==========================================================
    WEATHER TICKER
 ========================================================== */

 export function initWeatherTicker() {

     const tickers = document.querySelectorAll(
         "[data-weather-ticker]"
     );


     tickers.forEach((viewport) => {

         const track =
             viewport.querySelector(
                 ".weather-ticker__track"
             );


         const animation =
             viewport.querySelector(
                 ".weather-ticker__animation"
             );


         if (
             !track ||
             !animation
         ) {
             return;
         }


         const autoplay =
             viewport.dataset.autoplay === "true";


         const DRAG_THRESHOLD = 8;


         let isPointerDown = false;
         let isDragging = false;


         let startX = 0;
         let startTrackX = 0;


         let currentTrackX = 0;


         let lastTimestamp = null;


         /* ======================================================
            DIMENSIONS
         ====================================================== */

         const getDimensions = () => {

             return {

                 viewportWidth:
                     viewport.clientWidth,

                 contentWidth:
                     track.getBoundingClientRect().width

             };

         };


         /* ======================================================
            SPEED
         ====================================================== */

         const getSpeed = () => {

             const speed =
                 parseFloat(
                     getComputedStyle(
                         viewport
                     ).getPropertyValue(
                         "--weather-ticker-speed"
                     )
                 );


             if (
                 !Number.isFinite(speed) ||
                 speed <= 0
             ) {

                 return 40;

             }


             return speed;

         };


         /* ======================================================
            SET POSITION
         ====================================================== */

         const setTrackPosition = (position) => {

             currentTrackX =
                 position;


             track.style.transform =
                 `translate3d(
                     ${currentTrackX}px,
                     0,
                     0
                 )`;

         };


         /* ======================================================
            RESET TO RIGHT
         ====================================================== */

         const resetToRight = () => {

             const {
                 viewportWidth
             } = getDimensions();


             setTrackPosition(
                 viewportWidth
             );

         };


         /* ======================================================
            AUTOPLAY
         ====================================================== */

         const animate = (timestamp) => {

             if (
                 lastTimestamp === null
             ) {

                 lastTimestamp =
                     timestamp;

             }


             const deltaTime =
                 timestamp -
                 lastTimestamp;


             lastTimestamp =
                 timestamp;


             if (
                 autoplay &&
                 !isPointerDown
             ) {

                 const {
                     viewportWidth,
                     contentWidth
                 } = getDimensions();


                 if (
                     viewportWidth > 0 &&
                     contentWidth > 0
                 ) {

                     /*
                      * speed = píxeles por segundo.
                      *
                      * Por ejemplo:
                      *
                      * 40 = 40 px/s
                      */

                     const pixelsPerSecond =
                         getSpeed();


                     currentTrackX -=
                         pixelsPerSecond *
                         deltaTime /
                         1000;


                     /*
                      * Cuando el mensaje ya salió
                      * completamente por la izquierda,
                      * vuelve inmediatamente a la derecha.
                      */

                     if (
                         currentTrackX <=
                         -contentWidth
                     ) {

                         currentTrackX =
                             viewportWidth;

                     }


                     track.style.transform =
                         `translate3d(
                             ${currentTrackX}px,
                             0,
                             0
                         )`;

                 }

             }


             requestAnimationFrame(
                 animate
             );

         };


         /* ======================================================
            POINTER DOWN
         ====================================================== */

         viewport.addEventListener(
             "pointerdown",
             (event) => {

                 if (
                     event.pointerType === "mouse" &&
                     event.button !== 0
                 ) {

                     return;

                 }


                 isPointerDown =
                     true;

                 isDragging =
                     false;


                 startX =
                     event.clientX;


                 startTrackX =
                     currentTrackX;


                 lastTimestamp =
                     null;


                 viewport.setPointerCapture(
                     event.pointerId
                 );

             }
         );


         /* ======================================================
            POINTER MOVE
         ====================================================== */

         viewport.addEventListener(
             "pointermove",
             (event) => {

                 if (!isPointerDown) {
                     return;
                 }


                 const deltaX =
                     event.clientX -
                     startX;


                 /* ==================================================
                    DRAG THRESHOLD
                 ================================================== */

                 if (!isDragging) {

                     if (
                         Math.abs(deltaX) <
                         DRAG_THRESHOLD
                     ) {

                         return;

                     }


                     isDragging =
                         true;

                 }


                 /* ==================================================
                    DRAG MOVEMENT
                 ================================================== */

                 currentTrackX =
                     startTrackX +
                     deltaX;


                 track.style.transform =
                     `translate3d(
                         ${currentTrackX}px,
                         0,
                         0
                     )`;


                 if (
                     event.pointerType === "touch"
                 ) {

                     event.preventDefault();

                 }

             },
             {
                 passive: false
             }
         );


         /* ======================================================
            POINTER UP
         ====================================================== */

         viewport.addEventListener(
             "pointerup",
             (event) => {

                 if (!isPointerDown) {
                     return;
                 }


                 isPointerDown =
                     false;


                 isDragging =
                     false;


                 lastTimestamp =
                     null;


                 if (
                     viewport.hasPointerCapture(
                         event.pointerId
                     )
                 ) {

                     viewport.releasePointerCapture(
                         event.pointerId
                     );

                 }

             }
         );


         /* ======================================================
            POINTER CANCEL
         ====================================================== */

         viewport.addEventListener(
             "pointercancel",
             (event) => {

                 if (!isPointerDown) {
                     return;
                 }


                 isPointerDown =
                     false;

                 isDragging =
                     false;


                 lastTimestamp =
                     null;


                 if (
                     viewport.hasPointerCapture(
                         event.pointerId
                     )
                 ) {

                     viewport.releasePointerCapture(
                         event.pointerId
                     );

                 }

             }
         );


         /* ======================================================
            LOST POINTER CAPTURE
         ====================================================== */

         viewport.addEventListener(
             "lostpointercapture",
             () => {

                 if (!isPointerDown) {
                     return;
                 }


                 isPointerDown =
                     false;

                 isDragging =
                     false;


                 lastTimestamp =
                     null;

             }
         );


         /* ======================================================
            INITIAL POSITION
         ====================================================== */

         resetToRight();


         /* ======================================================
            START AUTOPLAY
         ====================================================== */

         requestAnimationFrame(
             animate
         );

     });

 }


 const WEATHER_ICON_MAP = {
    clear: "icon-weather-clear",
    partly_cloudy: "icon-weather-partly-cloudy",
    cloudy: "icon-weather-cloudy",
    rain: "icon-weather-rain",
    storm: "icon-weather-storm",
    snow: "icon-weather-snow",
    fog: "icon-weather-fog",
};

export function updateWeatherTicker(weather) {

    const group = getWeatherTickerGroup();

    if (!group) {
        return;
    }

    const iconId = WEATHER_ICON_MAP[weather.weather_type];

    if (!iconId) {
        setWeatherTickerError();
        return;
    }

    group.replaceChildren();

    group.appendChild(
        createWeatherIcon(iconId)
    );

    const text = document.createElement("span");

    text.textContent = (
        `${weather.city} · ` +
        `${weather.temperature}°C · ` +
        `${weather.description}`
    );

    group.appendChild(text);
}


export function setWeatherTickerLoading() {

    const group = getWeatherTickerGroup();

    if (!group) {
        return;
    }

    group.replaceChildren();

    group.appendChild(
        createWeatherIcon("icon-weather-loading")
    );

    const text = document.createElement("span");

    text.textContent = "Obteniendo información del clima...";

    group.appendChild(text);
}

export function setWeatherTickerError() {

    const group = getWeatherTickerGroup();

    if (!group) {
        return;
    }

    group.replaceChildren();

    group.appendChild(
        createWeatherIcon("icon-weather-unavailable")
    );

    const text = document.createElement("span");

    text.textContent = "No se pudo obtener el clima.";

    group.appendChild(text);
}

function getWeatherTickerGroup() {

    const ticker = document.querySelector(
        "[data-weather-ticker]"
    );

    if (!ticker) {
        return null;
    }

    return ticker.querySelector(
        ".weather-ticker__group"
    );
}

function createWeatherIcon(iconId) {

    const svg = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "svg",
    );

    svg.classList.add("weather-ticker__icon");

    const use = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "use",
    );

    use.setAttribute(
        "href",
        `#${iconId}`,
    );

    svg.appendChild(use);

    return svg;
}