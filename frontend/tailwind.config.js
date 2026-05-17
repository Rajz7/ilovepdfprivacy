/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'accent-pink': '#F5C0C0',
        'accent-dark': '#31263B',
      },
      fontFamily: {
        'formula': ['PP-Formula-ExtraBold', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
