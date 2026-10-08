export async function initWeather() {

    const timezone = Intl.DateTimeFormat()
        .resolvedOptions()
        .timeZone;

    const weatherElement = document.querySelector(
        "[data-weather-ticker]"
    );

    if (!weatherElement) {
        throw new Error(
            "No se encontró el elemento del componente del clima."
        );
    }

    const weatherUrl = weatherElement.dataset.weatherUrl;

    if (!weatherUrl) {
        throw new Error(
            "No se encontró la URL del endpoint del clima."
        );
    }

    const url = new URL(weatherUrl);

    url.searchParams.set("timezone", timezone);

    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(
            `Error al obtener el clima: ${response.status}`
        );
    }

    const weather = await response.json();

    return weather;
}