import { initWeatherTicker } from "./components/weather_ticker.js";
import { initWeather } from "./components/weather.js";




const initializeApp = async () => {


    initWeatherTicker();

    await initWeather();


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