/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./src/**/*.{html,js}", // Archivos en la carpeta src
        "./templates/**/*.html", // Archivos de plantilla de Django
        "./**/templates/**/*.html", // Archivos de plantilla en subdirectorios
        "./static/js/**/*.js", // Archivos JavaScript en la carpeta static
    ],
    theme: {
      extend: {},
    },
    plugins: [],
}