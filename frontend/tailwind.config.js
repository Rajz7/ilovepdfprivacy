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
        'surface': '#f8fafc',
        'ink': '#0f172a',
      },
      fontFamily: {
        'sans': ['SF Pro Text', 'SF Pro Display', '-apple-system', 'BlinkMacSystemFont', 'Helvetica Neue', 'Segoe UI', 'sans-serif'],
        'display': ['SF Pro Display', 'SF Pro Text', '-apple-system', 'BlinkMacSystemFont', 'Helvetica Neue', 'Segoe UI', 'sans-serif'],
        'formula': ['SF Pro Display', 'SF Pro Text', '-apple-system', 'BlinkMacSystemFont', 'Helvetica Neue', 'Segoe UI', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
