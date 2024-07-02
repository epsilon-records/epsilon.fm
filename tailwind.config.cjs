const colors = require('tailwindcss/colors');
const svelte_ux = require('svelte-ux/plugins/tailwind.cjs');

/** @type {import('tailwindcss').Config}*/
const config = {
	content: ['./src/**/*.{html,svelte}', './node_modules/svelte-ux/**/*.{svelte,js}'],
	theme: {
		extend: {}
	},
	ux: {
		themes: {
			light: {
				'color-scheme': 'light',
				primary: 'hsl(340.8799 100% 69.8833%)',
				secondary: 'hsl(185.3347 100% 50%)',
				accent: 'hsl(278.9515 100% 72.6993%)',
				neutral: 'hsl(227.154 55.502% 14.9159%)',
				'surface-100': 'hsl(55.763 100% 64.174%)'
			},
			dark: {
				'color-scheme': 'dark',
				primary: 'hsl(234.8208 100% 72.6713%)',
				secondary: 'hsl(313.3209 100% 66.1653%)',
				accent: 'hsl(173.7346 100% 40.1728%)',
				neutral: 'hsl(213.3333 17.6471% 20%)',
				'surface-100': 'hsl(212.3077 18.3099% 13.9216%)',
				'surface-200': 'hsl(212.7273 18.0328% 11.9608%)',
				'surface-300': 'hsl(213.3333 17.6471% 10%)'
			}
		}
	},
	variants: {
		extend: {}
	},
	plugins: [svelte_ux]
};

module.exports = config;
