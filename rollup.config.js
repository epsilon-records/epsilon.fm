import svelte from 'rollup-plugin-svelte';
import resolve from '@rollup/plugin-node-resolve';
import sveld from 'sveld';

export default {
	input: 'src/index.js',
	output: {
		format: 'es',
		file: 'lib/index.mjs'
	},
	plugins: [svelte(), resolve(), sveld()]
};
