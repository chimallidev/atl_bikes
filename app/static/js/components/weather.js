export async function initWeather() {

    const timezone = Intl.DateTimeFormat()
        .resolvedOptions()
        .timeZone;

    const response = await fetch(
        `/api/weather?timezone=${encodeURIComponent(timezone)}`
    );

    if (!response.ok) {
        throw new Error(
            `Error al obtener el clima: ${response.status}`
        );
    }

    const weather = await response.json();


    return weather;
}