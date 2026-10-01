import {
    initWeatherTicker,
    updateWeatherTicker,
    setWeatherTickerLoading,
    setWeatherTickerError,
} from "./components/weather_ticker.js";

import { initWeather } from "./components/weather.js";




const initializeApp = async () => {

    initWeatherTicker();

    setWeatherTickerLoading();

    try {

        const weather = await initWeather1();

        updateWeatherTicker(weather);

    }
    catch (error) {

        console.error(
            "No se pudo obtener el clima:",
            error,
        );

        setWeatherTickerError();

    }

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