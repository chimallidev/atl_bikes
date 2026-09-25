import { initWeatherTicker } from "./components/weather_ticker.js";


const initializeApp = () => {

    initWeatherTicker();

};


if (document.readyState === "loading") {

    document.addEventListener(
        "DOMContentLoaded",
        initializeApp,
        { once: true }
    );

}
else {

    initializeApp();

}