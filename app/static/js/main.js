import {
    initWeatherTicker,
    updateWeatherTicker,
    setWeatherTickerLoading,
    setWeatherTickerError,
} from "./components/weather_ticker.js";

import { initWeather } from "./components/weather.js";
import { initAtlBrandsCard } from "./components/atl_brands_card.js";




const initializeApp = async () => {

    initWeatherTicker();

    setWeatherTickerLoading();

    initAtlBrandsCard();

    try {

        const weather = await initWeather();

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