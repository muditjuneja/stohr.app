/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{njk,md}"],
  theme: {
    extend: {},
  },
  plugins: [require('@tailwindcss/forms'),],
  corePlugins: {
    textColor: true,
  }
}

