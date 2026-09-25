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